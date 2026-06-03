from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Iterable


RELATED_KEYS = (
    "related_findings",
    "related_concepts",
    "related_projects",
    "related_reports",
)

GENERIC_TERMS = {
    "analysis",
    "business",
    "customer",
    "design",
    "engineering",
    "hardware",
    "manufacturing",
    "meeting",
    "project",
    "retrofit",
    "seo",
    "serviceability",
    "supplier",
}

FINDING_RE = re.compile(r"\bMORAAAAA-\d+(?:-\d+)?\b")
CONCEPT_RE = re.compile(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b")
PROJECT_RE = re.compile(r"\b(?:K\d+|SRW|GA4|Search Console)\b")
CLASSIFICATION_RE = re.compile(
    r"(?im)^\s*(?:Classification|Classifications|Taxonomy|Labels|Concepts)\s*:?\s*$"
)
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
RELATED_SECTION_RE = re.compile(
    r"(?ms)^## Related Links\s*\n.*?(?=^## |\Z)"
)


@dataclass
class ReportLinks:
    related_findings: list[str] = field(default_factory=list)
    related_concepts: list[str] = field(default_factory=list)
    related_projects: list[str] = field(default_factory=list)
    related_reports: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, list[str]]:
        return {
            "related_findings": self.related_findings,
            "related_concepts": self.related_concepts,
            "related_projects": self.related_projects,
            "related_reports": self.related_reports,
        }

    def has_links(self) -> bool:
        return any(self.as_dict().values())


def enrich_report(
    content: str,
    *,
    report_type: str,
    source_agent: str,
    created: str | None = None,
    related_findings: Iterable[str] | None = None,
    related_concepts: Iterable[str] | None = None,
    related_projects: Iterable[str] | None = None,
    related_reports: Iterable[str] | None = None,
    report_path: Path | str | None = None,
) -> str:
    """Return Markdown with merged frontmatter and one Related Links section."""
    created = created or date.today().isoformat()
    existing_frontmatter, body = split_frontmatter(content)

    extracted = extract_structured_links(body, report_path=report_path)
    links = ReportLinks(
        related_findings=normalize_values(
            list(related_findings or []) + extracted.related_findings
        ),
        related_concepts=normalize_values(
            list(related_concepts or []) + extracted.related_concepts
        ),
        related_projects=normalize_values(
            list(related_projects or []) + extracted.related_projects
        ),
        related_reports=normalize_values(
            list(related_reports or []) + extracted.related_reports
        ),
    )

    frontmatter = merge_frontmatter(
        existing_frontmatter,
        {
            "type": report_type,
            "source_agent": source_agent,
            "created": created,
            **links.as_dict(),
        },
    )

    body = remove_related_links_section(body).strip()
    related_section = render_related_links(links)
    return f"---\n{frontmatter}---\n\n{body}\n\n{related_section}\n"


def write_markdown_report(path: Path, content: str, **kwargs: object) -> None:
    enriched = enrich_report(content, report_path=path, **kwargs)
    path.write_text(enriched, encoding="utf-8")


def split_frontmatter(content: str) -> tuple[str, str]:
    match = FRONTMATTER_RE.match(content)
    if not match:
        return "", content
    return match.group(1), content[match.end() :]


def merge_frontmatter(existing: str, fields: dict[str, object]) -> str:
    parsed = parse_frontmatter(existing)
    parsed.update(fields)
    lines: list[str] = []
    for key, value in parsed.items():
        if isinstance(value, list):
            if value:
                lines.append(f"{key}:")
                lines.extend(f"  - {item}" for item in value)
            else:
                lines.append(f"{key}: []")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines) + "\n"


def parse_frontmatter(text: str) -> dict[str, object]:
    parsed: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            value = line[4:].strip()
            existing = parsed.setdefault(current_key, [])
            if isinstance(existing, list):
                existing.append(value)
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == "[]":
                parsed[key] = []
            elif value:
                parsed[key] = value
            else:
                parsed[key] = []
    return parsed


def extract_structured_links(content: str, report_path: Path | str | None = None) -> ReportLinks:
    scan_text = strip_code_blocks(strip_frontmatter_and_links(content))
    findings = FINDING_RE.findall(scan_text)
    concepts = extract_classification_values(scan_text)
    concepts.extend(CONCEPT_RE.findall(scan_text))
    projects = PROJECT_RE.findall(scan_text)
    reports = extract_report_references(scan_text, report_path=report_path)

    return ReportLinks(
        related_findings=normalize_values(findings),
        related_concepts=normalize_values(concepts),
        related_projects=normalize_values(projects),
        related_reports=normalize_values(reports),
    )


def extract_classification_values(content: str) -> list[str]:
    values: list[str] = []
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if not CLASSIFICATION_RE.match(line):
            continue
        for candidate in lines[index + 1 : index + 12]:
            stripped = candidate.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                break
            if not stripped.startswith(("-", "*")):
                break
            value = stripped[1:].strip()
            values.extend(CONCEPT_RE.findall(value))
    return values


def extract_report_references(
    content: str,
    report_path: Path | str | None = None,
) -> list[str]:
    values: list[str] = []
    for match in re.finditer(r"(?im)^\s*-\s+[^:\n]+:\s+`?([^`\n]+\.md)`?", content):
        value = Path(match.group(1).strip()).stem
        if value:
            values.append(value)
    for match in re.finditer(r"\b[\w -]+(?:Report|Review|Analysis|Plan)\.md\b", content):
        values.append(Path(match.group(0)).stem)
    if report_path:
        current = Path(report_path).stem
        values = [value for value in values if value != current]
    return values


def render_related_links(links: ReportLinks) -> str:
    if not links.has_links():
        return "## Related Links\n\nNo structured related links identified."

    sections = ["## Related Links"]
    section_map = (
        ("Findings", links.related_findings),
        ("Concepts", links.related_concepts),
        ("Projects", links.related_projects),
        ("Reports", links.related_reports),
    )
    for heading, values in section_map:
        if not values:
            continue
        sections.append(f"\n### {heading}")
        sections.extend(f"- [[{value}]]" for value in values)
    return "\n".join(sections)


def remove_related_links_section(content: str) -> str:
    return RELATED_SECTION_RE.sub("", content).strip()


def strip_frontmatter_and_links(content: str) -> str:
    _, body = split_frontmatter(content)
    body = RELATED_SECTION_RE.sub("", body)
    return re.sub(r"\[\[[^\]]+\]\]", "", body)


def strip_code_blocks(content: str) -> str:
    return re.sub(r"```.*?```", "", content, flags=re.DOTALL)


def normalize_values(values: Iterable[str]) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = normalize_value(value)
        if not clean or clean.lower() in GENERIC_TERMS or clean in seen:
            continue
        seen.add(clean)
        normalized.append(clean)
    return normalized


def normalize_value(value: object) -> str:
    clean = str(value).strip()
    clean = clean.strip("`[](){}.,;:")
    while clean.lower().endswith(".md"):
        clean = clean[:-3]
    clean = re.sub(r"\s+", " ", clean)
    return clean
