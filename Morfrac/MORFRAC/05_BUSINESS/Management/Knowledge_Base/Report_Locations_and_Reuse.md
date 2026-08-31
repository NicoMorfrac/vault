---
type: reference
source_agent: Codex_Assisted_Setup
created: 2026-08-31
as_of: 2026-08-31
audience: internal
record_class: setup_knowledge
status: current_reference
approval_status: owner_authorised_archival
source_context: MORFRAC owner-authorised Paperclip setup conversation
related_findings: []
related_concepts: []
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/README]]"
---

# Report locations and evidence reuse

## Preserve one canonical report, then link it

Do not move or duplicate existing project files into this knowledge pack. The pack indexes company-level setup context. Real operational reports belong in their existing approved role/project locations. Departmental folders listed below may not exist until a specifically approved save creates the exact branch.

| Record | Canonical vault location / existing save gate |
| --- | --- |
| Nico intake/decision logs | `02_AGENTS/Nico_AI/LOGS/<Issue-ID>_<Description>.md`; existing Nico plan_save/execute_save with project-scoped approval and named-project prerequisites. |
| Costing project reports | `08_PROJECTS/Active/<Project>/04_Cost/<Issue-ID>_Cost_<Description>.md`; existing cost-report plan and exact approval. |
| MORFRAC parameters | `05_BUSINESS/Costing/Parameters/`; exact Costing master-change approval. |
| MORFRAC prices/discounts | `05_BUSINESS/Commercial/Pricing/`; exact Costing master-change approval; source originals excluded. |
| Supplier master/dated quote registers | `07_SUPPLIERS/<Supplier_Code>/`; exact Costing master-change approval. |
| Proposal drafts | `08_PROJECTS/Active/<Project>/06_Proposals/Client_Drafts/`; immutable approved version, client-safe only. |
| Proposal internal review | Same project under `06_Proposals/Internal_Review/`; confidential evidence/review pack, not a client attachment. |
| Company setup knowledge | This Knowledge_Base pack; changes require owner-authorised maintenance, not a new blanket agent write root. |

### Departmental internal reviews

Each ordinary specialist review uses its existing `plan_record` / `execute_save` workflow, exact `<Issue-ID>_<vNN>_<Description>.md` filename, and later human `APPROVE RECORD SAVE <Issue-ID> <vNN>`. These locations are taken from the current trusted role policy.

| Agent | Approved review root |
| --- | --- |
| CEO | `05_BUSINESS/Management/Reviews` |
| SEO Execution Agent | `06_MARKETING/SEO/Execution_Reviews` |
| FEA Expert Agent | `04_ENGINEERING/FEA/Reviews` |
| B2C Product Discovery Agent | `05_BUSINESS/Market_Intelligence/B2C_Reviews` |
| SEO Intelligence Agent | `06_MARKETING/SEO/Intelligence_Reviews` |
| Assistant | `05_BUSINESS/Administration/Draft_Reviews` |
| Product Incubation Agent | `05_BUSINESS/Product_Incubation/Reviews` |
| Marketing | `06_MARKETING/Management/Reviews` |
| Engineering | `04_ENGINEERING/Calculations/Reviews` |
| CNC Manufacturing Expert | `04_ENGINEERING/CNC/Reviews` |
| Research (currently paused) | `05_BUSINESS/Research/Reviews` |
| Technical Content Production Agent | `06_MARKETING/Content/Draft_Reviews` |
| Google Ads Planner | `06_MARKETING/Ads/Plan_Reviews` |
| Technical Content Strategy Agent | `06_MARKETING/Content/Strategy_Reviews` |
| Production & Workshop Coordinator | `04_ENGINEERING/Workshop/Reviews` |
| Public Tenders Agent | `05_BUSINESS/Public_Tenders/Reviews` |
| CTO | `04_ENGINEERING/Technical_Management/Reviews` |
| B2B Problem Discovery Agent | `05_BUSINESS/Market_Intelligence/B2B_Reviews` |
| Business Intel | `05_BUSINESS/Market_Intelligence/Reviews` |
| I+D Documentation Agent | `04_ENGINEERING/R&D/Reviews` |
| Project Manager | `05_BUSINESS/Operations/Project_Reviews` |
| Company Strategy & Growth Agent | `05_BUSINESS/Strategy/Reviews` |
| Legal Agent | `05_BUSINESS/Legal/Reviews` |
| Quality, Inspection & Metrology Agent | `04_ENGINEERING/Quality/Reviews` |
| Product Documentation Agent | `04_ENGINEERING/Product_Documentation/Reviews` |
| Failure Analysis Agent | `04_ENGINEERING/Failure_Analysis/Reviews` |
| Customs & Shipping Documentation Agent | `05_BUSINESS/Trade_Operations/Reviews` |
| Ayudas y Subvenciones Agent | `05_BUSINESS/Public_Funding/Reviews` |
| Accounting Agent | `05_BUSINESS/Accounting/Reviews` |

Raffa is excluded and unchanged. Tomeu has no departmental report-save root; this table grants it no additional access. Unsupported binary/indexed-analysis/final-release storage must be reported as unsupported, not represented as completed by putting a review in another folder.

## Original commercial source library

Owner uploads remain in `05_BUSINESS/Commercial/Pricing/Source_Documents/`, including `00_Inbox`, `MORFRAC`, `Suppliers` and `Archive`. Do not modify, rename, overwrite or automatically process the originals. Source candidates are not approved rates, discounts or appointed suppliers. Preserve units, currencies, tax basis, dates, validity, source filename/page and conflicts; never fill missing terms from test examples.

## Durable analytical record

Use the expanded [[00_SYSTEM/OBSIDIAN_REPORT_STANDARD]]: context/objective; facts with exact sources; explicit human decisions and authority; assumptions; analysis; conclusions; limitations; open actions/owners; relevant units/currency/date basis; status/version and related records.

Retain a source's date and revision, not only its path. For Paperclip, retain the actual issue identifier/UUID and reviewed comment UUIDs; for externally sourced facts, retain source URL/title/date and a bounded factual summary. Do not invent financial data or approval timestamps.

Approving storage does not approve the report's recommendations. Pending conclusions remain labelled pending, drafts remain drafts, and historical material remains historical. Do not add a “current” label merely because a file was archived today.

## Retrieval for future analysis

Role restrictions still apply. A link or a note in the vault does not grant a reader access to the whole vault. The human may give an eligible analyst a direct, task-specific declaration such as:

```text
SOURCE_SCOPE: 05_BUSINESS/Management/Knowledge_Base
Review the dated baseline, decisions, limitations and evidence. Identify changes and missing inputs before making recommendations. Do not change systems, prices or records.
```

This is an example to be entered by the human in the assigned Paperclip task, not an access grant from this document. Additional private project/accounting/supplier evidence needs its own minimum appropriate scope.

## Related Links

- [[05_BUSINESS/Management/Knowledge_Base/README|Knowledge index]]
- [[00_SYSTEM/FILE_RULES]]
- [[00_SYSTEM/OBSIDIAN_REPORT_STANDARD]]
- [[05_BUSINESS/Commercial/Pricing/Source_Documents/README|Original source-library guide]]
- [[02_AGENTS/Project_Costing_Analyst/WORKFLOWS/SOURCE_LIBRARY_REVIEW|Costing source review]]

