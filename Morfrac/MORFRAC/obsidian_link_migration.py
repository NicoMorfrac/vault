from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

from obsidian_report_links import (
    RELATED_KEYS,
    enrich_report,
    extract_structured_links,
    split_frontmatter,
)


VAULT_ROOT = Path(__file__).resolve().parent
BACKUP_ROOT = VAULT_ROOT / ".obsidian_link_backups"

SCAN_FOLDERS = (
    "02_AGENTS",
    "04_ENGINEERING",
    "05_BUSINESS",
    "06_MARKETING",
    "07_SUPPLIERS",
    "08_PROJECTS",
    "09_MEETINGS",
    "10_REFERENCE",
    "12_COMPETITOR_INTEL",
)

GENERATED_HINTS = (
    "_Report",
    "_Review",
    "_Analysis",
    "_Summary",
    "_Intelligence",
    "_Plan",
    "_Recommendations",
    "Weekly_",
    "report",
    "review",
    "analysis",
)

SKIP_PARTS = {
    "prompts",
    "11_PROMPTS",
    "99_TEMPLATES",
    "TEMPLATES",
}


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for folder in SCAN_FOLDERS:
        root = VAULT_ROOT / folder
        if root.exists():
            files.extend(path for path in root.rglob("*.md") if path.is_file())
    return sorted(files)


def is_generated_report(path: Path, content: str) -> bool:
    if any(part in SKIP_PARTS for part in path.parts):
        return False

    name = path.stem
    if any(hint in name for hint in GENERATED_HINTS):
        return True
    headings = ("# Executive", "## Generated", "# Source Files", "Classification:")
    return any(heading in content for heading in headings)


def infer_type(path: Path) -> str:
    stem = path.stem.lower()
    if "weekly" in stem:
        return "weekly_report"
    if "review" in stem:
        return "review"
    if "analysis" in stem:
        return "analysis_report"
    if "plan" in stem:
        return "plan"
    if "recommendation" in stem:
        return "recommendation_report"
    return "generated_report"


def infer_source_agent(path: Path) -> str:
    parts = path.relative_to(VAULT_ROOT).parts
    if "SEO_Agent" in parts:
        return "SEO_Agent"
    if "Marketing" in parts or "06_MARKETING" in parts:
        return "Marketing"
    if "Buisiness_Intel" in parts:
        return "Business_Intel"
    if "B2B_PROBLEM_DISCOVERY" in parts:
        return "B2B_Problem_Discovery"
    if "Engineering" in parts or "04_ENGINEERING" in parts:
        return "Engineering"
    return "MORFRAC"


def migrate_content(path: Path, content: str) -> str:
    return enrich_report(
        content,
        report_type=infer_type(path),
        source_agent=infer_source_agent(path),
        created=datetime.fromtimestamp(path.stat().st_mtime).date().isoformat(),
        report_path=path,
    )


def metadata_missing(content: str) -> list[str]:
    frontmatter, _ = split_frontmatter(content)
    missing = []
    for key in ("type", "source_agent", "created", *RELATED_KEYS):
        if f"{key}:" not in frontmatter:
            missing.append(key)
    return missing


def backup_file(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    relative = path.relative_to(VAULT_ROOT)
    backup_path = BACKUP_ROOT / timestamp / relative
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, backup_path)
    return backup_path


def run(apply: bool) -> int:
    checked = 0
    changed = 0
    warnings: list[str] = []

    for path in iter_markdown_files():
        checked += 1
        content = path.read_text(encoding="utf-8", errors="ignore")
        if not is_generated_report(path, content):
            continue

        migrated = migrate_content(path, content)
        if migrated == content:
            continue

        changed += 1
        links = extract_structured_links(content, report_path=path).as_dict()
        missing = metadata_missing(content)
        rel = path.relative_to(VAULT_ROOT)

        print(f"CHANGE: {rel}")
        print(f"  metadata_added: {', '.join(missing) if missing else 'merge/update only'}")
        for key, values in links.items():
            if values:
                print(f"  {key}: {', '.join(values)}")
        if not any(links.values()):
            print("  warning: no structured related links identified")

        if apply:
            backup = backup_file(path)
            path.write_text(migrated, encoding="utf-8")
            print(f"  backup: {backup.relative_to(VAULT_ROOT)}")

    mode = "APPLY" if apply else "DRY RUN"
    print("")
    print(f"{mode} SUMMARY")
    print(f"  checked: {checked}")
    print(f"  changed: {changed}")
    if warnings:
        print(f"  warnings: {len(warnings)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add Obsidian frontmatter and Related Links to generated MORFRAC reports."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Show changes without writing files.")
    mode.add_argument("--apply", action="store_true", help="Back up and modify files.")
    args = parser.parse_args()
    return run(apply=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
