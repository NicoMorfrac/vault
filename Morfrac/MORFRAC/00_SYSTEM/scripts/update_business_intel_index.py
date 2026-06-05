from pathlib import Path
import re
from datetime import datetime

ROOT = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")
B2C_ROOT = ROOT / "02_AGENTS" / "STRATEGIC" / "B2C_PRODUCT_DISCOVERY"
OUTPUTS = B2C_ROOT / "outputs"

RAW_FINDINGS = OUTPUTS / "RAW_FINDINGS"
REPORTS = OUTPUTS / "WEEKLY_REPORTS"
MASTER_INDEX = OUTPUTS / "MASTER_INDEX.md"
CONVERGENCE = B2C_ROOT / "PATTERN_CONVERGENCE"

CONVERGENCE_FILES = [
    "USABILITY_FRICTION",
    "WORKFLOW_INEFFICIENCY",
    "PRODUCT_COMPLEXITY",
    "INSTALLATION_COMPLEXITY",
    "MAINTENANCE_AVOIDANCE",
]


def wikilink(path: Path) -> str:
    return f"[[{path.stem}]]"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def extract_heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def extract_section_value(text: str, section: str) -> str:
    pattern = rf"^#\s+{re.escape(section)}\s*$([\s\S]*?)(?=^#\s+|\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    if not match:
        return ""
    value = match.group(1).strip()
    return re.sub(r"\s+", " ", value).strip()


def extract_confidence(text: str) -> str:
    section = extract_section_value(text, "CONFIDENCE_LEVEL")
    upper = section.upper()
    for level in ["HIGH", "MEDIUM", "LOW"]:
        if level in upper:
            return level
    return ""


def extract_problem_type(text: str) -> str:
    value = extract_section_value(text, "PROBLEM_TYPE")
    lines = [line.strip("- ").strip() for line in value.splitlines() if line.strip()]
    return lines[0] if lines else ""


def extract_user_segment(text: str) -> str:
    value = extract_section_value(text, "USER_SEGMENT")
    lines = [line.strip("- ").strip() for line in value.splitlines() if line.strip()]
    return lines[0] if lines else ""


def extract_date_from_text_or_name(path: Path, text: str) -> str:
    match = re.search(r"created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text)
    if match:
        return match.group(1)

    match = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", path.name)
    if match:
        return match.group(1)

    return ""


def collect_markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(folder.glob("*.md"))


def build_index() -> str:
    findings = collect_markdown_files(RAW_FINDINGS)
    reports = collect_markdown_files(REPORTS)

    lines = []
    lines.append("# B2C PRODUCT DISCOVERY MASTER INDEX")
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
    lines.append("| Finding | Date | Problem Type | User Segment | Confidence |")
    lines.append("|---|---|---|---|---|")

    for path in findings:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        problem_type = extract_problem_type(text)
        user_segment = extract_user_segment(text)
        confidence = extract_confidence(text)
        lines.append(
            f"| {wikilink(path)} | {date} | {problem_type} | {user_segment} | {confidence} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## REPORTS")
    lines.append("")
    lines.append("| Report | Date | Topic |")
    lines.append("|---|---|---|")

    for path in reports:
        text = read_text(path)
        date = extract_date_from_text_or_name(path, text)
        topic = extract_heading(text, path.stem)
        lines.append(f"| {wikilink(path)} | {date} | {topic} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## HIGH PRIORITY OPPORTUNITIES")
    lines.append("")
    lines.append("None yet.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## PRODUCT IMPROVEMENT OPPORTUNITIES")
    lines.append("")
    lines.append("None yet.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RETROFIT KIT OPPORTUNITIES")
    lines.append("")
    lines.append("None yet.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## NEW PRODUCT OPPORTUNITIES")
    lines.append("")
    lines.append("None yet.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## RELATED STRATEGIC AGENTS")
    lines.append("")
    lines.append("- [[B2C Product Discovery Agent]]")
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
    CONVERGENCE.mkdir(parents=True, exist_ok=True)

    content = build_index()
    MASTER_INDEX.write_text(content, encoding="utf-8")

    print(f"Updated: {MASTER_INDEX}")


if __name__ == "__main__":
    main()