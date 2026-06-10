from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

BUSINESS_INTEL_ROOT = ROOT / "02_AGENTS" / "Buisiness_Intel"
OUTPUTS = BUSINESS_INTEL_ROOT / "outputs"

STRATEGIC_OPPORTUNITIES = OUTPUTS / "Strategic_Opportunities"
WEEKLY_REPORTS = OUTPUTS / "Weekly_Reports"
RAW_FINDINGS = OUTPUTS / "Raw_Findings"
MASTER_INDEX = OUTPUTS / "MASTER_INDEX.md"

RELATED_BUSINESS_FOLDERS = [
    ROOT / "05_BUSINESS" / "Strategic_Intelligence",
    ROOT / "05_BUSINESS" / "Commercial_Opportunities",
    ROOT / "05_BUSINESS" / "Competitor_Analysis",
]

DEFAULT_STATUS = "UNREVIEWED"
DEFAULT_CLASSIFICATION = "UNCLASSIFIED"


def wikilink(path: Path) -> str:
    return f"[[{path.stem}]]"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def clean_cell(value: str) -> str:
    if not value:
        return ""

    value = value.replace("\r", " ").replace("\n", " ")
    value = re.sub(r"\*+", "", value)
    value = re.sub(r"`+", "", value)
    value = re.sub(r"\[\[|\]\]", "", value)
    value = re.sub(r"\|", "/", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -|:;,.")


def extract_heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return clean_cell(match.group(1)) if match else fallback


def extract_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    frontmatter: dict[str, str] = {}

    for line in match.group(1).splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()

    return frontmatter


def extract_section_block(text: str, section: str) -> str:
    pattern = rf"^#\s+{re.escape(section)}\s*$([\s\S]*?)(?=^#\s+|\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_first_valid_tokens_from_section(text: str, section: str) -> str:
    block = extract_section_block(text, section)
    if not block:
        return ""

    lines: list[str] = []

    for raw_line in block.splitlines():
        line = clean_cell(raw_line)

        if not line:
            continue

        if line.upper() in {"EXAMPLES", "EXAMPLE"}:
            continue

        if line.lower().startswith("examples"):
            continue

        if line.startswith("---"):
            continue

        lines.append(line)

    return " / ".join(lines)


def extract_date_from_text_or_name(path: Path, text: str) -> str:
    frontmatter = extract_frontmatter(text)
    created = frontmatter.get("created", "")

    match = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", created)
    if match:
        return match.group(1)

    match = re.search(r"created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.IGNORECASE)
    if match:
        return match.group(1)

    match = re.search(r"Date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.IGNORECASE)
    if match:
        return match.group(1)

    match = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", path.name)
    if match:
        return match.group(1)

    return ""


def extract_confidence(text: str) -> str:
    block = extract_section_block(text, "CONFIDENCE_LEVEL").upper()

    for level in ["HIGH", "MEDIUM", "LOW"]:
        if re.search(rf"\b{level}\b", block):
            return level

    searchable = text.upper()

    for level in ["HIGH", "MEDIUM", "LOW"]:
        if re.search(rf"\bCONFIDENCE\b[\s\S]{{0,100}}\b{level}\b", searchable):
            return level

    return ""


def extract_opportunity_classification(text: str) -> str:
    section_value = extract_first_valid_tokens_from_section(
        text, "Opportunity Classification"
    ).upper()

    searchable = (section_value or text).upper().replace(" ", "_").replace("-", "_")

    classifications = [
        "B2B_SERVICE_OPPORTUNITY",
        "B2B_PRODUCT_OPPORTUNITY",
        "B2C_PRODUCT_OPPORTUNITY",
        "PRODUCT_IMPROVEMENT_OPPORTUNITY",
        "RETROFIT_KIT_OPPORTUNITY",
        "STRATEGIC_PARTNERSHIP_OPPORTUNITY",
        "VALIDATION_REQUIRED",
        "NO_OPPORTUNITY",
    ]

    for classification in classifications:
        if classification in searchable:
            return classification

    return DEFAULT_CLASSIFICATION


def extract_opportunity_status(text: str) -> str:
    section_value = extract_first_valid_tokens_from_section(
        text, "Opportunity Status"
    ).upper()

    searchable = (section_value or text).upper().replace(" ", "_").replace("-", "_")

    statuses = [
        "COMMERCIAL_OPPORTUNITY",
        "STRATEGIC_OPPORTUNITY",
        "VALIDATION_REQUIRED",
        "VALIDATING",
        "DISCOVERY",
        "DEFERRED",
        "REJECTED",
        "NO_OPPORTUNITY",
        "UNREVIEWED",
    ]

    for status in statuses:
        if status in searchable:
            return status

    return DEFAULT_STATUS


def collect_markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []

    return sorted(
        path
        for path in folder.glob("*.md")
        if path.name.lower() != "master_index.md"
    )


def build_index() -> str:
    strategic_opportunities = collect_markdown_files(STRATEGIC_OPPORTUNITIES)
    weekly_reports = collect_markdown_files(WEEKLY_REPORTS)
    raw_findings = collect_markdown_files(RAW_FINDINGS)

    related_business_reports: list[Path] = []
    for folder in RELATED_BUSINESS_FOLDERS:
        related_business_reports.extend(collect_markdown_files(folder))

    lines: list[str] = []

    lines.append("# BUSINESS INTEL MASTER INDEX")
    lines.append("")
    lines.append(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## STRATEGIC OPPORTUNITIES")
    lines.append("")
    lines.append("| Report | Date | Classification | Status | Confidence |")
    lines.append("|---|---|---|---|---|")

    for path in strategic_opportunities:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        classification = extract_opportunity_classification(text)
        status = extract_opportunity_status(text)
        confidence = extract_confidence(text)

        lines.append(
            f"| {wikilink(path)} | {date} | {classification} | {status} | {confidence} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## WEEKLY REPORTS")
    lines.append("")
    lines.append("| Report | Date | Topic | Status |")
    lines.append("|---|---|---|---|")

    for path in weekly_reports:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        topic = extract_heading(text, path.stem)
        status = extract_opportunity_status(text)

        lines.append(f"| {wikilink(path)} | {date} | {topic} | {status} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RAW FINDINGS")
    lines.append("")
    lines.append("| Finding | Date | Classification | Status | Confidence |")
    lines.append("|---|---|---|---|---|")

    for path in raw_findings:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        classification = extract_opportunity_classification(text)
        status = extract_opportunity_status(text)
        confidence = extract_confidence(text)

        lines.append(
            f"| {wikilink(path)} | {date} | {classification} | {status} | {confidence} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## CANONICAL BUSINESS COPIES")
    lines.append("")
    lines.append("| Report | Folder | Date | Classification | Status |")
    lines.append("|---|---|---|---|---|")

    for path in sorted(related_business_reports):
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        classification = extract_opportunity_classification(text)
        status = extract_opportunity_status(text)

        folder_name = clean_cell(path.parent.name)

        lines.append(
            f"| {wikilink(path)} | {folder_name} | {date} | {classification} | {status} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED STRATEGIC AGENTS")
    lines.append("")
    lines.append("- [[Business Intelligence Agent]]")
    lines.append("- [[B2B Problem Discovery Agent]]")
    lines.append("- [[B2C Product Discovery Agent]]")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED B2B CONCEPTS")
    lines.append("")
    lines.append("- [[ENGINEERING_UNCERTAINTY]]")
    lines.append("- [[RETROFIT_COMPLEXITY]]")
    lines.append("- [[SERVICEABILITY_COMPLEXITY]]")
    lines.append("- [[MECHANICAL_INTEGRATION_COMPLEXITY]]")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED B2C CONCEPTS")
    lines.append("")
    lines.append("- [[USABILITY_FRICTION]]")
    lines.append("- [[WORKFLOW_INEFFICIENCY]]")
    lines.append("- [[PRODUCT_COMPLEXITY]]")
    lines.append("- [[INSTALLATION_COMPLEXITY]]")
    lines.append("- [[MAINTENANCE_AVOIDANCE]]")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    STRATEGIC_OPPORTUNITIES.mkdir(parents=True, exist_ok=True)
    WEEKLY_REPORTS.mkdir(parents=True, exist_ok=True)
    RAW_FINDINGS.mkdir(parents=True, exist_ok=True)

    content = build_index()
    MASTER_INDEX.write_text(content, encoding="utf-8")

    print(f"Updated: {MASTER_INDEX}")


if __name__ == "__main__":
    main()