---
type: archived_setup_report
source_agent: Codex_Assisted_Setup
created: 2026-08-31
as_of: 2026-08-31
audience: internal
record_class: setup_knowledge
status: historical_evidence
approval_status: owner_authorised_archival
source_context: MORFRAC owner-authorised Paperclip setup conversation
related_findings: []
related_concepts: []
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/README]]"
source_original: "paperclip-config/organisation-cleanup/STATUS.md"
source_sha256: "F811372CF8ADDD096544B790BBB4503D7B13A187A8FBC1DA36E75F6BAC72665B"
---

# 2026-08-31 Organisation Cleanup

This is an archived deployment report, not current executable instructions or a fresh readiness certification. Its tests/holds describe the documented phase. Consult the operating baseline, current policy and readiness register before using it in future analysis. Original relative code/backup paths are relative to the source workspace, not permission to open or run them.

## Preserved report

# MORFRAC cleanup and Accounting — 2026-08-31

**Organisation cleanup deployed. Accounting Agent added with human-approved limited-write controls. Odoo connection is not yet configured.**

Follow-up completed: [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-08-31_Workflow_Closeout|workflow handoffs and closeout]]. HandoffCompletion-v2 adds exact origin references, result-before-close guards and a seven-task offline integration test. The combined suites now total 195 passing tests; six runtime guides were updated with a preserved before/after hash chain. The report below records the original cleanup and smoke tests.

## What changed

- MORFRAC now has **34 agents**. **33** use canonical external instruction entries in Obsidian and restricted tool configurations. Raffa AI is the explicit unchanged exception.
- SEO Execution and SEO Intelligence now report to Marketing; CTO retains technical-claim review. Existing content agents stay under SEO Execution. No duplicate content/CAD role was created.
- CEO/CTO and other legacy entries now refer to the current organisation, exact human approvals and the correct vault. CEO's autonomous agent-creation permission was removed.
- Corrected only the malformed `Model: gpt-5.5` identifiers on CTO and Product Incubation. Other model choices/reasoning settings were preserved.
- Nico, Costing and Proposal retain their original scoped workflows. PM and Workshop retain their original connectors, with organisation-scoped evidence/review/workplan tools added where appropriate.
- Scoped internal record plans and human-approved leadership work packages are available. Public research remains enabled for research-capable roles; Marketing/SEO have a fixed readonly analytics helper. Unsupported binary, final-release, arbitrary project-index and external-operation workflows are explicitly unavailable—not represented as working integrations.
- Deployed **69 instruction/policy files**. Existing business/project/price/supplier documents were not changed or moved. New departmental review folders are only created later through an individually approved save plan.
- Retired **18 historical installer entrypoints** with a fail-fast guard so they cannot accidentally restore old broad access or stale instructions. Original scripts and affected instructions are backed up; nothing was deleted. Do not rerun old installers. A future configuration change needs a fresh baseline and reviewed deployment plan; `-ResumeReviewed` is only for a specifically inspected partial deployment.

## Accounting

- Agent: **Accounting Agent**, ID `71aa0ff4-26ff-465a-9fe5-dfb77ffda787`, reports to CEO.
- Canonical instructions: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Accounting_Agent\AGENTS.md`.
- Owns financial evidence/actuals review, discrepancy identification, review checklists and correction proposals. Costing still owns estimates and price/discount/supplier masters. Strategy receives only human-approved minimum financial summaries.
- Reads are scoped to exact company/date/report declarations and allowlisted fields. Initial prepared changes are **reference, invoice date or due date on one existing draft invoice/bill**.
- Every supported write requires the latest frozen exact record/field plan and a later direct human comment in that same issue:

`APPROVE ACCOUNTING CHANGE <Issue-ID> <Version>`

- The tool rechecks approval, task, policies, connection and row state, persists one attempt before writing, and verifies readback. Stale/quoted/edited/agent-authored approvals, later human comments and uncertain attempts block execution.
- **Posting, payments, reconciliation, deletion, tax/amount/bank/account/access changes are not enabled.** Approval cannot unlock an unimplemented operation.
- **Both Odoo connections remain disabled. No Odoo business data was read or changed.** Required next: exact HTTPS URL, database, Odoo version/API availability, company IDs, dedicated read/write identities and securely provisioned credentials. Effective rights, deployment-specific side effects and concurrency controls need administrator review before enabling writes.
- Read-then-write is not atomic compare-and-swap; the connection review flag is not a technical lock. If a suitable exclusive-edit/server-side control cannot be provided, keep agent writes disabled and have the human accountant apply proposals.

## Verification

**169 automated checks pass:** 146 Node tests plus 3 extraction and 20 project-folder Python tests. External Odoo/Google operations in tests used mocks only. This includes exact approval gates, role/company restrictions, wrong-user rejection, fixed readonly analytics scopes, changed records/policies, immutable review files, and no retry after an uncertain Odoo write.

Four isolated live Paperclip smoke tests succeeded with substantive, saved/read-back-verified results. Logs were read through EOF; all used scoped tools and recorded **zero shell commands**. No business source read, Odoo/Google business request, handoff, file save, release or project creation occurred.

| Probe | Issue | Result comment | Observed scope |
| --- | --- | --- | --- |
| Accounting | MORAAAAA-137 | d10804ce-432b-4754-bc87-fc98a4cc8881 | Guidance, disconnected configuration status, approval boundary |
| CTO | MORAAAAA-138 | 47863806-4081-4c87-909b-dbcf7b0f321b | Organisation, technical-review ownership, held integrations |
| Marketing | MORAAAAA-139 | 70b2c4db-8782-419a-8a0a-f4770c52372b | SEO/content ownership and analytics-scope instructions |
| PM | MORAAAAA-140 | 3dcf9d40-6862-4060-b3f9-9b2e043a6bda | Both original PM and new organisation connectors available |

Smoke tests verify the observed connector/guidance paths, not professional competence or every workflow. PM's narrative reversed the order of its two initial task reads; the audit shows PM connector first, then organisation connector. Both were read-only and the actual logged sequence is retained in `evaluation-pm.json`.

Integrity verification passed after deployment and the live probes:

- One organisation root; no missing parent or cycle.
- All **135 pre-existing issues** retain their tracked title/description/status/assignment/project/parent state.
- All **33 pre-existing environment hashes** and all model reasoning settings preserved.
- Raffa's complete tracked configuration and original entry file unchanged.
- Existing `04_ENGINEERING`, `05_BUSINESS`, `06_MARKETING`, `07_SUPPLIERS` and `08_PROJECTS` contents unchanged; unrelated `00_SYSTEM`/`02_AGENTS` contents verified by reconstructing the baseline hashes with only the approved file changes removed.
- Research remains paused. Every scheduled heartbeat remains disabled. Fusion/CAD work remains deferred.

Deployment first stopped on a PowerShell comparison bug that interpreted wrapped path strings as property bags. The CEO values were independently compared and matched; the comparator was corrected, the partial state reviewed, and deployment resumed with the drift/protection checks retained.

## Remaining boundaries

Odoo and Google live authentication/schema are not verified. Fusion, SolidWorks FEA, CAM/NC, physical production, statutory filings, external communications and publishing are not activated. Some legacy specialist workflows can currently produce only an issue response or approved internal review record; their final/binary/dossier/master workflows need separately implemented scoped tools.

This is a model-tool restriction, not OS-level isolation against other processes/administrators sharing the Windows account. Raffa remains outside the cleanup and its legacy access is not certified safe for employee use. No safety/legal/accounting certification is claimed.

The **OpenAI Docs skill** guided the per-agent sandbox, disabled shell/patch/delegation and named MCP-tool controls using the official [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) and [MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). The integration discovery found no available Odoo connector; no plugin was installed. The prepared adapter follows the versioned official Odoo API references in the Accounting setup guide and still requires deployment-specific validation.

Primary entry points: `00_SYSTEM/ORGANISATION.md` in Obsidian, the Accounting agent package, `tools/organisation-scoped/README.md`, `verify.ps1`, `file-plan.json`, and `evaluation-*.json` here. Backups are retained under `backups/`.


## Related Links

- [[05_BUSINESS/Management/Knowledge_Base/README|Knowledge index]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Current readiness summary]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-08-31_Source_Manifest|Original source hashes]]

