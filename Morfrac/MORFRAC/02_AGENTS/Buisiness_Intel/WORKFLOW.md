# Business Intel Output Workflow

Business Intel outputs are template-driven. No active Python Strategic Opportunities generator was found in `02_AGENTS/Buisiness_Intel`.

All future Business Intel Markdown outputs must follow `00_SYSTEM/OBSIDIAN_REPORT_STANDARD.md`.

## Required Output Standard

Every generated report must include YAML frontmatter with:

- `type`
- `source_agent`
- `created`
- `related_findings`
- `related_concepts`
- `related_projects`
- `related_reports`

Every generated report must also end with one visible section:

## Related Links

Use Obsidian wiki links only for structured entities that already exist or are intentionally being created as part of the output:

- finding IDs or finding note names
- taxonomy/concept note names
- project note names
- report note names
- agent names

Do not auto-link generic terms such as engineering, retrofit, hardware, serviceability, analysis, marketing, SEO, or project.

## Strategic Opportunities

Create Strategic Opportunity reports from:

`outputs/Strategic_Opportunities/Strategic_Opportunity_Template.md`

Use `type: strategic_opportunity` and `source_agent: Business_Intel`.

Populate relationships from the evidence used in the report:

- `related_findings`: source finding IDs or finding note names used directly
- `related_concepts`: taxonomy/concept nodes such as `RETROFIT_COMPLEXITY`
- `related_projects`: project notes such as `K8`, only when directly relevant
- `related_reports`: previous report note names that materially informed the output

## Weekly Reports

Create weekly synthesis reports from:

`outputs/Weekly_Reports/Weekly_Report_Template.md`

Use `type: business_intel_weekly_report` and `source_agent: Business_Intel`.

## Raw Findings

Create raw findings from:

`outputs/Raw_Findings/Raw_Finding_Template.md`

Use `type: business_intel_raw_finding` and `source_agent: Business_Intel`.

## Existing Output Migration Plan

Existing Business Intel reports should be migrated with the shared Obsidian helper or migration script, not manually rewritten.

Migration scope:

- `outputs/Strategic_Opportunities/*.md`
- `outputs/Weekly_Reports/*.md`
- copied Business Intel reports in `05_BUSINESS` if they are canonical vault-facing copies

Migration requirements:

- preserve filenames and body content
- add frontmatter
- populate structured relationships from explicit evidence references only
- add exactly one `## Related Links` section
- do not link generic words
- validate YAML fields and wiki links after migration
