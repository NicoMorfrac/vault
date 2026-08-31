---
type: operating_baseline
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

# MORFRAC AI operating baseline — 31 August 2026

## Verified structure

The company contains 34 Paperclip agents. There is one root and no missing reporting parent or cycle. Thirty-three have canonical instruction entries in Obsidian and scoped runtimes. Raffa remains the expressly unchanged exception. Research is paused. No recurring heartbeat schedule is enabled.

| Responsibility | Owner / boundary |
| --- | --- |
| Human decisions | The owner is final authority; an agent named CEO is not a human approver. |
| Intake | Nico AI gathers requirements and prepares the exact project brief and proposed routing. |
| Coordination | PM manages approved work packages, folders, progress, dependencies and escalation; it does not approve specialist conclusions. |
| Technical work | CTO coordinates Engineering, FEA, Failure Analysis, CNC, Workshop, Quality, I+D and Product Documentation. CAD/solver/CAM execution is not yet operational. |
| Estimates and commercial inputs | Costing owns project estimates, parameters and controlled price/discount/supplier registers. Proposal owns client drafts and a separate internal review pack. |
| Accounting and growth | Accounting reviews financial actuals and proposes narrowly supported corrections. Strategy uses only authorised financial summaries for growth scenarios. |
| Marketing | Marketing owns priorities; SEO Execution/Intelligence and Ads support it. Existing content strategy/production roles are reused, not duplicated. CTO reviews technical claims. |
| Market/compliance support | Business Intel leads B2B/B2C evidence work. Legal, Customs, Grants and Tenders retain their scoped duties and human review. |

Exact identities, routing and authoritative boundaries remain in [[00_SYSTEM/ORGANISATION]]; do not maintain a competing agent directory here.

## Operating sequence

Human -> Nico brief -> exact human approval -> PM coordination and accountable specialists -> reviewed results -> approved vault save -> result pointer to the origin -> verified closeout.

PM folder creation and general project coordination are different task types. Open delegated children prevent parent completion. A callback conveys a pointer, not private data, technical acceptance, commercial authority or file access.

Company/scoped completion tools verify the substantive saved Paperclip answer. The latest HandoffCompletion-v2 controls also check the origin callback and child status. **They do not universally enforce that every operational answer has a vault file.** KnowledgeRetention-v1 adds a mandatory reporting procedure in the shared instructions; existing approved saves verify their actual bytes. No new automatic archive tool was introduced in this retention change.

## Systems of record

- Canonical agent instructions and current policy: the existing Obsidian 00_SYSTEM and 02_AGENTS folders.
- Durable analysis and approved documents: the appropriate project or departmental vault location, not a copy in every department.
- Workflow execution and exact approvals: Paperclip task/comment history, referenced by UUID/identifier and date in retained reports.
- Commercial masters: Costing-controlled vault registers, based on actual evidence and explicit master-change approval.
- Accounting source: Odoo, once configured; no live connection or source data was validated by this setup.
- Implementation code, credential-free audit snapshots and recovery backups: the local paperclip 2 workspace. Do not copy credentials or raw runtime logs into the knowledge vault.

## Related Links

- [[00_SYSTEM/ORGANISATION]]
- [[00_SYSTEM/GENERAL_AGENT_RULES]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Readiness and next actions]]
- [[05_BUSINESS/Management/Knowledge_Base/Report_Locations_and_Reuse|Report destinations]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-08-31_Source_Manifest|Evidence sources]]

