# BUSINESS INTEL OUTPUT WORKFLOW

## PURPOSE

This document defines how the Business Intelligence Agent creates, stores, links, indexes, and maintains outputs inside the MORFRAC Obsidian vault.

Business Intelligence outputs are template-driven.

No active Python Strategic Opportunities generator was found in:

```
C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Business_Intel

```

All future Business Intelligence outputs must follow:

```
C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\OBSIDIAN_REPORT_STANDARD.md

```

The objective is to ensure:

* consistent report structure
* valid Obsidian graph relationships
* repeatable report generation
* reduced report fragmentation
* traceable strategic reasoning
* proper knowledge graph growth

***

# REQUIRED OUTPUT STANDARD

Every generated Business Intelligence output must:

* be Markdown
* include valid YAML frontmatter
* include a Related Links section
* comply with OBSIDIAN\_REPORT\_STANDARD.md
* be saved directly into the MORFRAC vault
* remain accessible after execution

Never save reports exclusively in temporary workspaces.

Always write final outputs directly into the vault.

***

# REQUIRED YAML FRONTMATTER

Every generated report must include:

```
---
type:
source_agent: Business_Intel
created:
related_findings:
related_concepts:
related_projects:
related_reports:
---

```

Populate relationship fields whenever valid relationships exist.

Do not leave fields empty when supporting evidence exists.

***

# RELATED LINKS REQUIREMENT

Every generated report must end with exactly one visible section:

```
## Related Links

### Related Findings

### Related Concepts

### Related Reports

```

Populate using Obsidian wiki-links whenever valid relationships exist.

***

# OBSIDIAN LINKING RULES

Use Obsidian wiki-links only for structured entities that already exist or are intentionally being created as part of the output.

Valid links include:

* finding IDs
* finding note names
* report note names
* convergence files
* taxonomy nodes
* concept notes
* project notes
* agent notes

Examples:

```
[[MORAAAAA-89]]
[[RETROFIT_COMPLEXITY]]
[[ENGINEERING_UNCERTAINTY]]
[[USABILITY_FRICTION]]
[[POWERFURL]]
[[Business Intelligence Agent]]

```

Do not automatically link generic words such as:

* engineering
* retrofit
* hardware
* serviceability
* analysis
* marketing
* SEO
* project
* opportunity
* validation

Only link structured entities.

***

# CROSS-AGENT CONVERGENCE MAPPING

Business Intelligence reports should function as bridge nodes between:

* B2B findings
* B2C findings
* convergence concepts
* projects
* strategic opportunities

Before finalizing any report:

Review:

* related findings
* related reports
* B2B convergence files
* B2C convergence files

Populate:

* related\_findings
* related\_concepts
* related\_projects
* related\_reports

whenever valid relationships exist.

Business Intelligence outputs should never become orphan notes.

***

# STRATEGIC OPPORTUNITY REPORTS

Create Strategic Opportunity reports from:

```
outputs\Strategic_Opportunities\Strategic_Opportunity_Template.md

```

Use:

```
type: strategic_opportunity
source_agent: Business_Intel

```

Populate relationships from evidence used directly within the report.

Examples:

```
related_findings:
  - MORAAAAA-86
  - MORAAAAA-88

related_concepts:
  - RETROFIT_COMPLEXITY
  - ENGINEERING_UNCERTAINTY

related_projects:
  - K8

related_reports:
  - 2026-05-24_MORAAAAA-89_Convergence_Retrofit_Serviceability_Strategic_Assessment

```

Only include relationships that materially influenced the report.

***

# WEEKLY REPORTS

Create weekly synthesis reports from:

```
outputs\Weekly_Reports\Weekly_Report_Template.md

```

Use:

```
type: business_intel_weekly_report
source_agent: Business_Intel

```

Weekly reports should:

* summarize strategic developments
* summarize opportunity evolution
* identify convergence growth
* identify emerging risks
* identify validation priorities

***

# RAW FINDINGS

Create raw findings from:

```
outputs\Raw_Findings\Raw_Finding_Template.md

```

Use:

```
type: business_intel_raw_finding
source_agent: Business_Intel

```

Raw findings should only be created when:

* new strategic evidence is identified
* meaningful intelligence is discovered
* a strategic signal cannot be incorporated into an existing finding

Avoid unnecessary finding proliferation.

***

# OPPORTUNITY STATUS TRACKING

Every strategic opportunity must be assigned one status:

* DISCOVERY
* VALIDATION\_REQUIRED
* VALIDATING
* STRATEGIC\_OPPORTUNITY
* COMMERCIAL\_OPPORTUNITY
* DEFERRED
* REJECTED

Provide rationale.

Status progression must be evidence-based.

Example:

```
Opportunity:
Retrofit Validation Package

Status:
VALIDATION_REQUIRED

Reason:
Strong recurring evidence.
Commercial willingness-to-pay remains unvalidated.

```

***

# DUPLICATE OPPORTUNITY CONTROL

Before creating a new strategic opportunity:

Search:

* MASTER\_INDEX.md
* Strategic Opportunities
* Weekly Reports
* Convergence Reviews
* Commercial Opportunity Reports

Determine whether the opportunity already exists.

If the opportunity already exists:

* update the existing opportunity

or

* append additional validation evidence

Do not create duplicate opportunities describing the same underlying commercial opportunity.

Prioritize convergence over opportunity count.

***

# INDEX MANAGEMENT

After completing any report:

Save:

* reports
* strategic assessments
* opportunity reviews

Then run:

```
py C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\scripts\update_business_intel_index.py

```

Report:

* created reports
* modified reports
* updated files
* updated MASTER\_INDEX.md path

Do not manually maintain MASTER\_INDEX.md.

MASTER\_INDEX.md is maintained exclusively through system scripts.

***

# EXISTING OUTPUT MIGRATION PLAN

Existing Business Intelligence reports should be migrated using:

* shared Obsidian helper
  or
* migration scripts

Do not manually rewrite reports.

***

## MIGRATION SCOPE

Migrate:

```
outputs\Strategic_Opportunities\*.md
outputs\Weekly_Reports\*.md

```

and:

```
05_BUSINESS\

```

when Business Intelligence copies are the canonical vault-facing versions.

***

## MIGRATION REQUIREMENTS

Preserve:

* filenames
* report content
* report dates
* report structure

Add:

* YAML frontmatter
* structured relationships
* Related Links section

Populate relationships only when explicitly supported by evidence.

Do not invent relationships.

***

## VALIDATION REQUIREMENTS

After migration verify:

* YAML is valid
* wiki-links are valid
* relationships resolve correctly
* only one Related Links section exists
* report body content remains unchanged

***

# OUTPUT QUALITY CONTROL

Before finalizing any Business Intelligence output verify:

* report follows template
* YAML is valid
* relationships are populated
* convergence links are valid
* confidence level is justified
* evidence supports conclusions
* opportunity status is assigned
* no duplicate opportunity already exists

If validation fails:

* revise output
* do not finalize

***

# LONG-TERM OBJECTIVE

Business Intelligence outputs should create a connected strategic knowledge graph that links:

* findings
* convergence themes
* projects
* opportunities
* validation activities
* strategic recommendations

The objective is not report generation.

The objective is a continuously improving strategic intelligence system for MORFRAC.