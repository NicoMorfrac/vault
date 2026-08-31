---
type: decision_register
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

# Owner decisions and standing constraints

These decisions are taken from the owner's setup conversation and checked against the current configuration where possible. The record date is 2026-08-31; it is not an invented original approval timestamp. “Approved” below means the stated setup scope only, never approval of a client project or financial transaction.

| ID | Decision / constraint | Current meaning |
| --- | --- | --- |
| DEC-01 | Review the organisation before configuration; later authorise configuration and cleanup. | Current structure is recorded in the authoritative organisation guide. |
| DEC-02 | Nico is the personal/project intake agent; check and use the existing PM. | Reuse existing ownership rather than invent duplicate managers. |
| DEC-03 | Raffa is an employee interface, not a company-wide specialist; do not configure or assign specifics. | Raffa remains unchanged. No new access, responsibilities, assignment or certification is implied. |
| DEC-04 | Wait for Fusion installation. | CAD drafting integration is still deferred; software absence cannot be concealed by generated instructions. |
| DEC-05 | Gather parameters incrementally, retaining MORFRAC prices/discounts and external suppliers. | Preserve original uploads. Costing reviews sourced candidates and needs separate approval for actual master changes. Unknown values remain unknown. |
| DEC-06 | Grants/tenders may eventually run every 15 days; set schedules later. | No biweekly or other recurring schedule has been enabled. |
| DEC-07 | Add Accounting with Odoo access; it may write only after human approval. | Prepared corrections are limited to reference/invoice/due dates on one existing draft invoice/bill. Posting/payments/reconciliation/deletion and other unsupported writes stay blocked. |
| DEC-08 | Odoo is at https://odoo.morfrac.com; configure later. | Address is owner-provided, not a verified integration. Connection settings and read/write activation remain unchanged and disabled. |
| DEC-09 | Tighten handoffs and run a dummy project. | HandoffCompletion-v2 was implemented and the isolated seven-task workflow passed. This is not a live client-project pass. |
| DEC-10 | Save all relevant information for future analysis in Obsidian. | This indexed setup archive and shared retention procedure preserve durable knowledge; existing business/save/access approval gates remain. |

## Approval distinctions to retain in every analysis

- APPROVE BRIEF <Project> <Revision>: only the frozen Nico brief and its exact handoff payloads.
- APPROVE WORKPLAN <Issue-ID> <Revision>: only the reviewed leadership work packages.
- APPROVE <Project>: only the operation in the current applicable plan, such as a PM folder or cost-report save. It is not an umbrella project approval.
- APPROVE RECORD SAVE <Issue-ID> <Version>: the exact internal record paths/bytes/evidence.
- APPROVE COSTING MASTER <Issue-ID>: the exact eligible master changes, not a purchase, quotation or supplier appointment.
- APPROVE PROPOSAL SAVE <Project> <Version> and APPROVE PROPOSAL RELEASE <Proposal-ID> <Version>: distinct storage and human-release-readiness decisions.
- APPROVE ACCOUNTING CHANGE <Issue-ID> <Version>: only the exact supported Odoo change, with a reviewed enabled executor.

Saving a document is not approval of its technical, legal, commercial or accounting conclusions. An agent-authored, quoted, stale or generic “ok” is not a substitute for a required direct human approval.

## Related Links

- [[00_SYSTEM/ORGANISATION]]
- [[00_SYSTEM/GENERAL_AGENT_RULES]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Operating_Baseline|Operating baseline]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Outstanding work]]

