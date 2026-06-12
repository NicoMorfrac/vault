from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re


ROOT = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")
INCUBATION_ROOT = ROOT / "02_AGENTS" / "STRATEGIC" / "PRODUCT_INCUBATION"
OUTPUTS = INCUBATION_ROOT / "outputs"

PRODUCT_CONCEPTS = OUTPUTS / "PRODUCT_CONCEPTS"
FEASIBILITY_REPORTS = OUTPUTS / "FEASIBILITY_REPORTS"
VALIDATION_REPORTS = OUTPUTS / "VALIDATION_REPORTS"
DEVELOPMENT_ROADMAPS = OUTPUTS / "DEVELOPMENT_ROADMAPS"
MASTER_INDEX = OUTPUTS / "MASTER_INDEX.md"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def clean_cell(value: str) -> str:
    value = value.replace("\r", " ").replace("\n", " ")
    value = re.sub(r"\\|", "/", value)
    value = re.sub(r"\\s+", " ", value)
    return value.strip(" -|:;,.")


def wikilink(path: Path) -> str:
    return f"[[{path.stem}]]"


def extract_heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\\s+(.+)$", text, re.MULTILINE)
    return clean_cell(match.group(1)) if match else fallback


def extract_section(text: str, section: str) -> str:
    pattern = rf"^#\\s+{re.escape(section)}\\s*$([\\s\\S]*?)(?=^#\\s+|\\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    return clean_cell(match.group(1)) if match else ""


def extract_date(path: Path, text: str) -> str:
    match = re.search(r"created:\\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"Date:\\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", path.name)
    if match:
        return match.group(1)
    return ""


def extract_decision(text: str) -> str:
    searchable = text.upper().replace(" ", "_").replace("-", "_")
    for decision in ["GO_AFTER_VALIDATION", "GO", "HOLD", "REJECT"]:
        if decision in searchable:
            return decision
    return "UNREVIEWED"


def extract_confidence(text: str) -> str:
    searchable = text.upper()
    for level in ["HIGH", "MEDIUM", "LOW"]:
        if level in searchable:
            return level
    return ""


def collect(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(p for p in folder.glob("*.md") if p.name.lower() != "master_index.md")


def build_index() -> str:
    lines = []
    lines.append("# PRODUCT INCUBATION MASTER INDEX")
    lines.append("")
    lines.append(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    sections = [
        ("PRODUCT CONCEPTS", PRODUCT_CONCEPTS),
        ("FEASIBILITY REPORTS", FEASIBILITY_REPORTS),
        ("VALIDATION REPORTS", VALIDATION_REPORTS),
        ("DEVELOPMENT ROADMAPS", DEVELOPMENT_ROADMAPS),
    ]

    for title, folder in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| File | Date | Decision | Confidence |")
        lines.append("|---|---|---|---|")
        for path in collect(folder):
            text = read_text(path)
            lines.append(
                f"| {wikilink(path)} | {extract_date(path, text)} | {extract_decision(text)} | {extract_confidence(text)} |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## RELATED STRATEGIC AGENTS")
    lines.append("")
    lines.append("- [[Product Incubation Agent]]")
    lines.append("- [[Business Intelligence Agent]]")
    lines.append("- [[Engineering Agent]]")
    lines.append("- [[B2B Problem Discovery Agent]]")
    lines.append("- [[B2C Product Discovery Agent]]")
    lines.append("")

    return "\\n".join(lines)


def main() -> None:
    for folder in [OUTPUTS, PRODUCT_CONCEPTS, FEASIBILITY_REPORTS, VALIDATION_REPORTS, DEVELOPMENT_ROADMAPS]:
        folder.mkdir(parents=True, exist_ok=True)

    MASTER_INDEX.write_text(build_index(), encoding="utf-8")
    print(f"Updated: {MASTER_INDEX}")


if __name__ == "__main__":
    main()
