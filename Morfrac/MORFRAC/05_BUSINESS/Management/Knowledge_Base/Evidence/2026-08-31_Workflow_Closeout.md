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
source_original: "paperclip-config/workflow-closeout/STATUS.md"
source_sha256: "920852DCCA0D3693593DC041718FA19497BB05FE43E9ECB66A216356FC74E3DC"
---

# 2026-08-31 Workflow Closeout

This is an archived deployment report, not current executable instructions or a fresh readiness certification. Its tests/holds describe the documented phase. Consult the operating baseline, current policy and readiness register before using it in future analysis. Original relative code/backup paths are relative to the source workspace, not permission to open or run them.

## Preserved report

# Workflow handoffs and closeout — 2026-08-31

HandoffCompletion-v2 is deployed in the scoped connector code and six canonical Obsidian runtime guides. The seven-task offline dummy project passed. Odoo configuration remains deferred and unchanged.

## Corrections

- New brief/workplan handoffs require one exact `originating_issue: <UUID>` line matching the actual parent. Embedded prose, missing/duplicate/malformed references, wrong parents and self-handoffs are rejected before dispatch. Old nonconforming approved plans require a new plan and human approval; existing tasks are not silently repaired.
- Exact human-approved shared input now receives a separate fixed origin header. The approved text stays unchanged, and cannot override its return destination. File/issue access still requires separate direct human scope; callbacks transfer no confidential results or approval.
- Costing and Proposal can return a fixed result pointer to Nico. This does not add Nico as an arbitrary handoff recipient or broaden business-source access.
- Linked closeout requires: save final substantive answer without status; verify notify_origin; repeat the identical answer with a new update_key and done. The current result, task, callback and open children are rechecked before the status change.
- Tasks cannot close with open child handoffs even when no dependency edge exists. Cancelled children are terminal, not successful results. Existing unresolved-dependency checks remain.
- Missing/edited pointers, changed tasks/results, closed/unavailable origins and uncertain callbacks block completion. An unresolved notification attempt cannot automatically retry across a restart or a new result.
- Nico can send a separately approved, exact `COORDINATE_PROJECT <Project> <Revision>` package to PM. This was needed to separate ongoing coordination from the existing fixed folder-creation request. PM workplans retain their own human approval.
- Exact PM_TASK folder operations use the original pm_scoped structure/readiness gates. General PM and Workshop operational completion uses org_scoped, preventing alternate-connector closeout bypasses. Existing read-and-report evaluation restrictions remain.

## Dummy workflow result

The integration harness completed all seven in-memory tasks:

1. Nico intake and approved PM folder request.
2. PM folder plan, simulated human approval, temporary folder creation, independent inspection and readiness callback.
3. Nico's separately approved PM coordination task and PM's approved Engineering, Costing and Proposal packages.
4. Engineering internal review plan/save, result callback and closeout.
5. Costing source access denied until a direct simulated human declaration, then estimate save and callback. No pricing master changes.
6. Proposal's separate PM storage request, approved temporary storage, explicitly scoped price evidence, separate draft-save approval and price/technical/schedule/legal/commercial review fixtures. Release produced only an issue manifest: no sending, signing or exports.
7. Proposal -> PM -> Nico results returned before closure. Premature parent completion was rejected. All child tasks closed and an unrelated fixture source remained byte-for-byte unchanged.

This used the **real connector guards and file-save code**, but an **in-memory Paperclip board, simulated human approvals, synthetic specialist answers and a fixture-only folder executor**. The production Python folder helper has separate regression tests. No live agent was asked to impersonate a human approval; no live company task, project, source file, supplier or price record was created. The temporary test fixtures were removed after testing; there is no dummy project in the live Obsidian vault.

This is an integration test of the control layer, not a live model-agent/domain acceptance test, engineering validation, legal/accounting certification or real client delivery.

## Verification

**195 tests passed: 172 Node tests (including the integration scenario), 3 extraction tests and 20 Python project-folder tests.**

- Negative cases cover malformed handoffs, unchanged legacy plans, exact PM coordination schema, edited/missing results and pointers, stale task state, employee destinations, premature parent completion and uncertain callback retries across restarts.
- Existing source, approval, costing/master, proposal save/release, PM, Workshop and Accounting/analytics mock tests still pass.
- Initial sandboxed filesystem tests encountered Windows EPERM on ancestor realpath inspection; all suites passed with approved host temporary-folder access. No production path check was weakened.
- Guide deployment preflight initially caught a PowerShell Split-Path parameter-set issue before any copy. It was corrected with the native path API, preflight rerun successfully, and all six deployed guide hashes verified.

Live integrity verification passed after deployment:

- **All 34 agent configuration/environment/entry hashes unchanged**, including Raffa. No model, authority, reporting-line or runtime/schedule settings were edited in this follow-up.
- **All 139 existing tasks unchanged** in the tracked title/description/status/assignment/project/parent fields; no new live task was created.
- Original structural baseline remains intact: one root, no reporting cycles/missing parents, 33 restricted canonical configurations, Research paused, heartbeats disabled.
- Existing engineering, business, marketing, supplier and project contents preserved. Original vault baseline verification now follows the exact six-file before/after hash chain, without rewriting the original baseline.
- Odoo connection file hash unchanged; both read and write flags disabled. No credentials accessed, no Odoo/analytics business requests and no live Paperclip API writes.

## Deployment and retained evidence

- `file-plan.json`: exact six guide predecessor/successor hashes and reviewed workspace code/test/Odoo hashes.
- `before.json`: redacted configuration hashes, vault tree hashes and existing task hashes. No credential values.
- `backups/`: original six guide files, retained for reviewed recovery. Nothing material was deleted or moved.
- `staged/`: deployed guide bytes.
- `verify.ps1`: repeatable read-only post-deployment audit. The older organisation-cleanup verifier also accepts only this exact reviewed successor hash chain.
- `deploy.ps1`: guarded one-time guide deployment. Do not rerun on deployed or partial state; a later change requires a fresh baseline and reviewed plan.
- `../../tools/company-scoped/workflow.integration.test.mjs`: reproducible offline scenario.

Connector changes load on subsequent agent runs; no shared backend restart or adapter-config rewrite was needed. All agents were idle or paused at deployment preflight.

## Still pending

Odoo will be configured later at the user's request. Live analytics authentication, Fusion/CAD, SolidWorks FEA, CAM/NC and other external operations remain outside this update. Recurring opportunity searches remain unscheduled. A supervised live project pilot is still needed before claiming all model-agent workflows operate successfully in production. Source access and business decisions continue to require the appropriate human input/approval; this update does not make them fully autonomous.

The guards are an application-level boundary, not atomic cross-service transactions or OS-level isolation against other processes using the same Windows account. Small concurrency windows remain. Raffa's legacy access remains untouched and outside the certified scope of these checks.


## Related Links

- [[05_BUSINESS/Management/Knowledge_Base/README|Knowledge index]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Current readiness summary]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-08-31_Source_Manifest|Original source hashes]]

