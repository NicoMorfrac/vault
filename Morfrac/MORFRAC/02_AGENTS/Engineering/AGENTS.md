# FILE ROUTING RULES

- Keep 02_AGENTS/Engineering only for agent configuration, memory, task patterns, skills and logs.
- Do not save engineering calculations or technical analyses in 02_AGENTS/Engineering root.
- Save blocked or incomplete task reports under:
  04_ENGINEERING/logs/
- Save completed engineering calculations under:
  04_ENGINEERING/Calculations/
- Save bearing analyses under:
  04_ENGINEERING/Calculations/Bearings/
- Save sheave analyses under:
  04_ENGINEERING/Calculations/Sheaves/
- Save rig load analyses under:
  04_ENGINEERING/Calculations/Rig_Loads/
- Save Dyneema loop analyses under:
  04_ENGINEERING/Calculations/Dyneema/
- Save material evaluations under:
  04_ENGINEERING/Materials/
- - Save trade studies and cost-benefit analyses under:
  04_ENGINEERING/R&D/
- If unsure where to save a file, ask before writing it.

# OBSIDIAN REPORT STANDARD

All future Engineering Markdown outputs must comply with:

- 00_SYSTEM/OBSIDIAN_REPORT_STANDARD.md
- 99_TEMPLATES/Engineering_Analysis_Template.md

Every generated engineering output must include YAML frontmatter with:

- type
- source_agent
- created
- related_findings
- related_concepts
- related_projects
- related_reports

Every generated engineering output must include exactly one visible section:

## Related Links

Use Obsidian wiki links only for structured entities:

- finding IDs
- taxonomy or concept note names
- project note names
- report note names
- agent note names

Do not auto-link generic words such as engineering, retrofit, hardware, serviceability, analysis, or project.
