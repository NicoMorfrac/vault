---
type: repair_evidence
source_agent: Codex
created: 2026-09-05
status: achieved
related_findings: [MORAAAAA-171, MORAAAAA-173]
related_concepts: [Paperclip, Nico_AI, Project_Manager, project_intake, approval_workflow, handoff_completion]
related_projects: [MORFRAC-B2B-Engineering-to-Manufacturing]
related_reports: []
---

# MORAAAAA-171 workflow repair

## Outcome

The blocked Nico AI project-intake and Project Manager return path was repaired without weakening human approval boundaries. The project structure now exists, the PM task is complete, Nico retrieved its verified result, the stale dependency was reconciled, and the next specialist brief is frozen for human review.

## Defects corrected

- Archived-project inspection used `08_PROJECTS/Archived`; the canonical Obsidian location is `08_PROJECTS/Archive`.
- The brief revision validator rejected the documented dotted revision `R0.1`.
- Durable comment verification depended on an exact-comment read that returned HTTP 403. Verification now uses the scoped paginated issue-comment list and still verifies comment ID, issue, author and unchanged body.
- Paperclip normalised the literal `\n` inside the Windows path `C:\Users\nicol` into a newline when saving comments. The PM connector now recognises only that exact persisted representation while retaining the plan hash, direct local-board author, timestamp/order, unchanged-plan and no-prior-attempt checks.
- Nico's live connector configuration omitted the already-implemented `read_handoff_result` tool.
- The general handoff reader understood `RESULT_AVAILABLE` callbacks but not the Project Manager's narrower `ENGINEERING_RESUME` readiness callback. It now verifies a PM result against the immutable PM task, same parent, exact deterministic callback/hash and independently complete project structure.

## Verification

- Connector and offline end-to-end workflow suite: 113 passed, 0 failed.
- PM recovery run: `ed3bd9b2-244e-4c44-858e-db5b2486bc76`, succeeded.
- Nico recovery run: `4531aa11-7ea9-4a0f-924d-db3d2a538096`, succeeded.
- PM task MORAAAAA-173: `done`; no active recovery action.
- PM callback receipt: `b8dc23ed-5acb-493f-9862-8c30f8ff4e53`.
- Nico successfully retrieved the completed PM result through the governed `read_handoff_result` route.
- MORAAAAA-171 has no unresolved `blockedBy` dependency or active recovery action.
- R0.2 frozen brief-plan comment: `a7240111-80f7-43ed-a9b1-383da2a8fa82`.

## Created project structure

`08_PROJECTS/Active/MORFRAC-B2B-Engineering-to-Manufacturing`

- `00_Project_Index.md`
- `01_Structures`
- `02_Bearings`
- `03_Thermal`
- `04_Cost`
- `05_Decisions`

No optional proposal directories, specialist output, final dossier, publication, spend, external communication or recurring schedule was created by this repair.

## Current governed continuation

MORAAAAA-171 is `in_review` / ready for approval. R0.2 contains five first-wave packages: Marketing, Business Intel, Engineering, Quality/Inspection/Metrology and Legal. Strategy and final Marketing synthesis are deferred to R0.3 so that they can consume verified first-wave evidence.

The next direct local-board comment must contain only:

`APPROVE BRIEF MORFRAC-B2B-Engineering-to-Manufacturing R0.2`

This approves only the five exact payloads frozen in R0.2. It does not approve file saves, publication, Phase 2, spending, release, sending or external commitments.

## Scope protection

- Raffa AI was not read, edited, activated or assigned.
- Existing human gates remain distinct for specialist work, vault saves, publication, technical release, legal reliance, spending and external actions.

## Related Links

- Paperclip issue: MORAAAAA-171
- Project Manager issue: MORAAAAA-173
- Connector: `tools/company-scoped/bridge.mjs`
- PM connector: `tools/pm-access/bridge.mjs`
- Runtime argument source: `paperclip-config/company-scoped-args.ps1`
