from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

B2B_ROOT = ROOT / "02_AGENTS" / "STRATEGIC" / "B2B_PROBLEM_DISCOVERY"
OUTPUTS = B2B_ROOT / "outputs"

RAW_FINDINGS = OUTPUTS / "RAW_FINDINGS"
REPORTS = OUTPUTS / "WEEKLY_REPORTS"
MASTER_INDEX = OUTPUTS / "MASTER_INDEX.md"
CONVERGENCE = OUTPUTS / "PATTERN_CONVERGENCE"

CONVERGENCE_FILES = [
    "ENGINEERING_UNCERTAINTY",
    "RETROFIT_COMPLEXITY",
    "SERVICEABILITY_COMPLEXITY",
    "MECHANICAL_INTEGRATION_COMPLEXITY",
]

DEFAULT_STATUS = "UNREVIEWED"
DEFAULT_OPPORTUNITY_TYPE = "UNCLASSIFIED"


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


def extract_problem_type(text: str) -> str:
    return extract_first_valid_tokens_from_section(text, "PROBLEM_TYPE")


def extract_industry_segment(text: str) -> str:
    return extract_first_valid_tokens_from_section(text, "INDUSTRY_SEGMENT")


def extract_opportunity_type(text: str) -> str:
    section_value = extract_first_valid_tokens_from_section(text, "OPPORTUNITY_TYPE").upper()
    searchable = (section_value or text).upper().replace(" ", "_").replace("-", "_")

    valid_types = [
        "ENGINEERING_SERVICE",
        "B2B_SERVICE",
        "B2B_PRODUCT",
        "RETROFIT_SERVICE",
        "INSTALLATION_SUPPORT",
        "SERVICEABILITY_IMPROVEMENT",
        "PARTNERSHIP",
        "NO_ACTION",
    ]

    for opportunity_type in valid_types:
        if opportunity_type in searchable:
            return opportunity_type

    return DEFAULT_OPPORTUNITY_TYPE


def extract_opportunity_status(text: str) -> str:
    searchable = text.upper().replace(" ", "_").replace("-", "_")

    valid_statuses = [
        "COMMERCIAL_OPPORTUNITY",
        "STRATEGIC_OPPORTUNITY",
        "VALIDATION_REQUIRED",
        "VALIDATING",
        "DISCOVERY",
        "DEFERRED",
        "REJECTED",
        "NO_OPPORTUNITY",
        "NO_ACTION",
        "UNREVIEWED",
    ]

    for status in valid_statuses:
        if status in searchable:
            return status

    return DEFAULT_STATUS


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


def collect_markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []

    return sorted(
        path
        for path in folder.glob("*.md")
        if path.name.lower() != "master_index.md"
    )


def ensure_convergence_files() -> None:
    CONVERGENCE.mkdir(parents=True, exist_ok=True)

    for name in CONVERGENCE_FILES:
        path = CONVERGENCE / f"{name}.md"

        if path.exists():
            continue

        path.write_text(
            "\n".join(
                [
                    f"# {name}",
                    "",
                    "## DESCRIPTION",
                    "",
                    "Emerging B2B problem discovery convergence theme.",
                    "",
                    "## LINKED FINDINGS",
                    "",
                    "None yet.",
                    "",
                    "## CURRENT_CONFIDENCE_LEVEL",
                    "",
                    "LOW",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def build_index() -> str:
    findings = collect_markdown_files(RAW_FINDINGS)
    reports = collect_markdown_files(REPORTS)

    lines: list[str] = []

    lines.append("# B2B PROBLEM DISCOVERY MASTER INDEX")
    lines.append("")
    lines.append(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## ACTIVE CONVERGENCE FILES")
    lines.append("")
    for name in CONVERGENCE_FILES:
        lines.append(f"- [[{name}]]")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## FINDINGS")
    lines.append("")
    lines.append(
        "| Finding | Date | Problem Type | Industry Segment | Confidence | Opportunity Type | Status |"
    )
    lines.append("|---|---|---|---|---|---|---|")

    for path in findings:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        problem_type = extract_problem_type(text)
        industry_segment = extract_industry_segment(text)
        confidence = extract_confidence(text)
        opportunity_type = extract_opportunity_type(text)
        status = extract_opportunity_status(text)

        lines.append(
            f"| {wikilink(path)} | {date} | {problem_type} | "
            f"{industry_segment} | {confidence} | {opportunity_type} | {status} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## REPORTS")
    lines.append("")
    lines.append("| Report | Date | Topic | Opportunity Type | Status |")
    lines.append("|---|---|---|---|---|")

    for path in reports:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        topic = extract_heading(text, path.stem)
        opportunity_type = extract_opportunity_type(text)
        status = extract_opportunity_status(text)

        lines.append(
            f"| {wikilink(path)} | {date} | {topic} | {opportunity_type} | {status} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## HIGH PRIORITY OPPORTUNITIES")
    lines.append("")
    lines.append("Pending Business Intelligence Review")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## B2B SERVICE OPPORTUNITIES")
    lines.append("")
    lines.append("Pending Business Intelligence Review")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## B2B PRODUCT OPPORTUNITIES")
    lines.append("")
    lines.append("Pending Business Intelligence Review")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RETROFIT / MODERNIZATION OPPORTUNITIES")
    lines.append("")
    lines.append("Pending Business Intelligence Review")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED STRATEGIC AGENTS")
    lines.append("")
    lines.append("- [[B2B Problem Discovery Agent]]")
    lines.append("- [[Business Intelligence Agent]]")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED CONCEPTS")
    lines.append("")
    for name in CONVERGENCE_FILES:
        lines.append(f"- [[{name}]]")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    RAW_FINDINGS.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    ensure_convergence_files()

    content = build_index()
    MASTER_INDEX.write_text(content, encoding="utf-8")

    print(f"Updated: {MASTER_INDEX}")


if __name__ == "__main__":
    main()