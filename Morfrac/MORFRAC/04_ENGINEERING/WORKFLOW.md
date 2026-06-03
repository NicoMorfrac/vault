# Engineering Output Workflow

Engineering outputs are template-driven. No active Python Engineering report generator was found in the vault.

All future Engineering Markdown outputs must follow:

- `00_SYSTEM/OBSIDIAN_REPORT_STANDARD.md`
- `00_SYSTEM/ENGINEERING_RULES.md`
- `99_TEMPLATES/Engineering_Analysis_Template.md`

## Required Output Standard

Every generated Engineering report must include YAML frontmatter with:

- `type`
- `source_agent`
- `created`
- `related_findings`
- `related_concepts`
- `related_projects`
- `related_reports`

Every generated Engineering report must include exactly one visible section:

## Related Links

Use Obsidian wiki links only for structured entities that already exist or are intentionally being created as part of the output:

- finding IDs or finding note names
- taxonomy/concept note names
- project note names
- report note names
- agent names

Do not auto-link generic terms such as engineering, retrofit, hardware, serviceability, analysis, marketing, SEO, or project.

## Output Locations

- Blocked or incomplete task reports: `04_ENGINEERING/logs/`
- Completed calculations: `04_ENGINEERING/Calculations/`
- Bearing analyses: `04_ENGINEERING/Calculations/Bearings/`
- Sheave analyses: `04_ENGINEERING/Calculations/Sheaves/`
- Rig load analyses: `04_ENGINEERING/Calculations/Rig_Loads/`
- Dyneema loop analyses: `04_ENGINEERING/Calculations/Dyneema/`
- Material evaluations: `04_ENGINEERING/Materials/`
- Trade studies and R&D: `04_ENGINEERING/R&D/`

## Relationship Rules

Populate relationships only from explicit source material:

- `related_findings`: source finding IDs or finding note names directly used
- `related_concepts`: taxonomy/concept nodes directly used
- `related_projects`: project note names directly tied to the analysis
- `related_reports`: prior report note names directly referenced

If no structured relationships are identified, keep the related fields as empty lists and use:

`No structured related links identified.`
