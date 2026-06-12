# PRODUCT INCUBATION WORKFLOW

## PURPOSE

This document defines how the Product Incubation Agent creates, stores, links, indexes and maintains outputs inside the MORFRAC Obsidian vault.

The Product Incubation workflow connects:

Business Intelligence
→ Product Incubation
→ Engineering
→ Prototype
→ Validation
→ Production Decision

---

# OUTPUT STANDARD

All outputs must follow:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\OBSIDIAN_REPORT_STANDARD.md

Every output must include YAML frontmatter with:

- type
- source_agent
- created
- related_findings
- related_concepts
- related_projects
- related_reports

Every output must end with exactly one visible:

## Related Links

section.

---

# OUTPUT FOLDERS

Root:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\PRODUCT_INCUBATION\

Outputs:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\PRODUCT_INCUBATION\outputs\

Subfolders:

- outputs\PRODUCT_CONCEPTS\
- outputs\FEASIBILITY_REPORTS\
- outputs\VALIDATION_REPORTS\
- outputs\DEVELOPMENT_ROADMAPS\

Index:

- outputs\MASTER_INDEX.md

---

# PRODUCT CONCEPT OUTPUTS

Create Product Concept reports from:

PRODUCT_INCUBATION_TEMPLATE.md

Use:

type: product_concept
source_agent: Product_Incubation

---

# FEASIBILITY REPORTS

Create feasibility reports from:

REPORT_TEMPLATE.md

Use:

type: product_feasibility_report
source_agent: Product_Incubation

---

# VALIDATION REPORTS

Use:

type: product_validation_report
source_agent: Product_Incubation

---

# DEVELOPMENT ROADMAPS

Use:

type: product_development_roadmap
source_agent: Product_Incubation

---

# LINKING RULES

Use Obsidian wiki-links only for structured entities.

Valid links include:

- finding IDs
- finding note names
- Business Intelligence report names
- convergence files
- project notes
- existing MORFRAC product notes
- agent notes

Do not link generic words.

---

# REQUIRED RELATIONSHIPS

Every output should link to:

- source Business Intelligence report
- source B2B/B2C findings
- relevant convergence files
- relevant MORFRAC products
- relevant project if applicable

---

# INDEX MANAGEMENT

After every execution run:

py C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\scripts\update_product_incubation_master_index.py

Report:

- created files
- modified files
- updated MASTER_INDEX.md

Do not manually maintain MASTER_INDEX.md.

---

# DUPLICATE CONTROL

Before creating a new product concept:

Search:

- PRODUCT_CONCEPTS
- FEASIBILITY_REPORTS
- VALIDATION_REPORTS
- DEVELOPMENT_ROADMAPS
- MASTER_INDEX.md

If concept already exists:

- update existing concept
or
- append new validation evidence

Do not create duplicates.

---

# MIGRATION PLAN

Existing incubation files should be migrated using script-based helpers.

Migration requirements:

- preserve filename
- preserve body content
- add valid frontmatter
- add one Related Links section
- populate relationships only from explicit evidence

---

# QUALITY CONTROL

Before finalizing verify:

- output follows template
- YAML is valid
- links are valid
- decision is present
- confidence level is present
- risks are documented
- index script has run

---

# LONG_TERM_OBJECTIVE

Create a connected Obsidian product-development knowledge graph linking:

- opportunities
- product concepts
- feasibility decisions
- validation results
- development roadmaps
- engineering projects
- production decisions
