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

The blocked Nico AI project-intake, Project Manager return path and five specialist-result closeouts were repaired without weakening human approval boundaries. Paperclip now revalidates completed child evidence, recovers interrupted closeouts, presents bounded history to the model, and creates a durable human-review interaction before an agent moves a task to `in_review`. MORAAAAA-171 has reached its intended R0.3 human approval gate.

## Defects corrected

- Archived-project inspection used `08_PROJECTS/Archived`; the canonical Obsidian location is `08_PROJECTS/Archive`.
- The brief revision validator rejected the documented dotted revision `R0.1`.
- Durable comment verification depended on an exact-comment read that returned HTTP 403. Verification now uses the scoped paginated issue-comment list and still verifies comment ID, issue, author and unchanged body.
- Paperclip normalised the literal `\n` inside the Windows path `C:\Users\nicol` into a newline when saving comments. The PM connector now recognises only that exact persisted representation while retaining the plan hash, direct local-board author, timestamp/order, unchanged-plan and no-prior-attempt checks.
- Nico's live connector configuration omitted the already-implemented `read_handoff_result` tool.
- The general handoff reader understood `RESULT_AVAILABLE` callbacks but not the Project Manager's narrower `ENGINEERING_RESUME` readiness callback. It now verifies a PM result against the immutable PM task, same parent, exact deterministic callback/hash and independently complete project structure.
- Agent-authored `blocked` updates used a board-owned unblock descriptor, which Paperclip 2026.831.1 rejects with HTTP 403. The bridge now records the authenticated agent as the unblock owner while preserving the named human resolution action.
- A completed child could contain a valid signed final result with `status: null` after an interrupted closeout. The reader now accepts that result only after the child is independently terminal `done`, its callback is exact, and its immutable task hash matches.
- The company child-list endpoint truncates descriptions at 1,200 characters. Result verification now re-fetches the exact child issue before checking the full task hash.
- Transient upstream reads can retry once after a bounded delay; mutations are never retried after dispatch.
- Nico's task read now performs one bounded control-plane revalidation when a prior result-gate failure is detected and returns compact verified result pointers. Model-visible history is bounded and signed payload wrappers are omitted from visible comment text.
- An agent's `in_review` status was rejected when it had no durable review owner, after which Paperclip entered its missing-disposition recovery loop. The bridge now creates an idempotent pending `request_confirmation` interaction before the status change, so the human owns the next action and acceptance/comment automatically resumes the assigned agent.

## Verification

- Complete connector and offline end-to-end workflow suite: 231 passed, 0 failed.
- PM recovery run: `ed3bd9b2-244e-4c44-858e-db5b2486bc76`, succeeded.
- Nico recovery run: `4531aa11-7ea9-4a0f-924d-db3d2a538096`, succeeded.
- PM task MORAAAAA-173: `done`; no active recovery action.
- PM callback receipt: `b8dc23ed-5acb-493f-9862-8c30f8ff4e53`.
- Nico successfully retrieved the completed PM result through the governed `read_handoff_result` route.
- MORAAAAA-171 has no unresolved `blockedBy` dependency or active recovery action.
- R0.2 frozen brief-plan comment: `a7240111-80f7-43ed-a9b1-383da2a8fa82`.
- Specialist tasks MORAAAAA-174 through MORAAAAA-178 are all `done`; their exact signed results and parent callbacks verify.
- Automatic Paperclip recovery run `408637d7-e440-4157-a818-ae1b444db93c` was dispatched with `invocationSource: automation` / `triggerDetail: system` and advanced the workflow to R0.3 review evidence.
- No agent wake endpoint was invoked manually during this repair. The old parent was returned to a recoverable state; Paperclip dispatched its own system runs.
- R0.3 frozen brief-plan comment: `008bca43-95d8-4e04-bcae-3d8f952457c0`.
- Pending human-review interaction: `b2d55962-93dd-48bb-b64e-09411a36eea4`.

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

MORAAAAA-171 is `in_review` with a real pending human-review interaction. The first-wave Marketing, Business Intel, Engineering, Quality/Inspection/Metrology and Legal tasks are complete. The verified R0.3 brief now controls the next two work packages.

The next direct local-board comment must contain only:

`APPROVE BRIEF MORFRAC-B2B-Engineering-to-Manufacturing R0.3`

This approves only the exact payloads frozen in R0.3. It does not approve file saves, publication, spending, release, sending, external commitments, or reactivation of competitor/external research that requires its own authorisation.

## Scope protection

- Raffa AI was not read, edited, activated or assigned.
- Existing human gates remain distinct for specialist work, vault saves, publication, technical release, legal reliance, spending and external actions.

## Related Links

- Paperclip issue: MORAAAAA-171
- Project Manager issue: MORAAAAA-173
- Connector: `tools/company-scoped/bridge.mjs`
- PM connector: `tools/pm-access/bridge.mjs`
- Runtime argument source: `paperclip-config/company-scoped-args.ps1`

## 2026-09-06 approval-streamlining follow-up

### Finding

After the R0.3 approval was supplied, Nico repeatedly returned MORAAAAA-171 to `in_review` for internal phase and management-pack confirmations. All current child work was already complete, so these reviews were administrative gates rather than risk controls. They interrupted the approved project before a first client-facing draft existed.

### Corrected approval model

1. Human approval of the initial project brief authorises the bounded project scope.
2. One separate human approval authorises the Project Manager to create the complete standard project folder structure, including proposal working folders.
3. Once both gates are verified, Paperclip may continue automatically through internal workplans, governed specialist delegation, same-project evidence exchange, internal analysis, versioned internal records, costing, and creation of the first proposal/client draft.
4. The next normal human gate is the first client-facing release.

Internal phase reviews, consolidated management packs, and strategy challenges remain useful milestones and evidence, but they no longer create new approval gates by themselves.

### Gates retained

Separate explicit approval remains mandatory for Odoo writes; price, discount, and supplier-master changes; external communication or publication; paid-ad activation; signing or legal acceptance; customs, grant, or tender submission; purchases, payments, or hiring; production CAD/CAM/FEA release; machine-code execution or manufacturing; destructive overwrite/deletion; and material changes to the approved project scope.

### Implementation and verification

- The company-scoped bridge now verifies inherited approved-project authority from the signed initial plan, direct human approval, dispatch receipt, completed PM folder child, and live project structure before permitting later internal work.
- Same-project completed sibling evidence can be consumed without another source-issue approval when both tasks inherit the same verified project authority and origin.
- Internal specialist records, cost reports, and the first proposal draft can be saved automatically under that authority; external release remains approval-gated.
- The PM's single folder approval now covers the complete standard folder tree, including proposal working directories.
- Review interactions are idempotent, preventing repeated duplicate pending approval prompts.
- Full connector and offline end-to-end workflow suite: **232 passed, 0 failed**.
- No wake endpoint or manual agent invocation was used.
- Raffa AI was not read, edited, activated, or assigned.

### Superseded text

The earlier `Current governed continuation` section records the historical R0.3 gate as it existed during the initial repair. That additional gate and the earlier statement that every specialist or internal vault save required its own approval are superseded by this dated follow-up. The retained high-risk gates above remain in force.

### Live continuation proof

- The obsolete pending Phase 1 review interaction `39f1c619-1b30-4d08-9164-adaac0007a50` was withdrawn; it was not accepted as a new project approval.
- MORAAAAA-171 was returned to the ordinary Paperclip queue. Paperclip—not a manual wake call—started run `8eb88b4d-ad31-48b0-835f-f7ae7eff17a4` with `invocationSource: automation` and `triggerDetail: system`.
- Nico automatically dispatched MORAAAAA-183, MORAAAAA-184, and MORAAAAA-185 under inherited approved-project authority. No approval interaction was created.
- The first Engineering run revealed a narrower source-routing defect: a governed child could not see its approved project origin, discover exact UUIDs for completed same-project siblings, or list its active-project subtree.
- The connector was tightened to expose only the verified approved project origin, verified completed siblings of that origin, and `08_PROJECTS/Active/<approved-project>`. It still does not expose arbitrary company history, other projects, archives, sensitive paths, external actions, or release authority.
- Engineering rerun `00eeef8b-9c7a-419b-8540-b88ee772c977` was started by Paperclip with `invocationSource: automation`, `triggerDetail: system`, and `wakeReason: issue_status_changed`; it consumed the originating objective, MORAAAAA-176, Quality and Legal sibling evidence, and the project index, then completed without requesting human approval.
- Parent continuation run `3edb0091-f97d-4ebf-ae2d-815630b2ee92` was started automatically after the child completion/unblock event.
- Nico then dispatched MORAAAAA-186, `FIRST COMPLETE INTERNAL DOSSIER DRAFT MORFRAC-B2B-Engineering-to-Manufacturing R0.5`, to Marketing. Its assignment run `b4b988b6-3ffa-4b58-aaaf-ad0adcc0456d` was system-triggered and created no approval interaction.
- Verification after the source-routing correction: **232/232 Node connector tests passed**, **3/3 extraction tests passed**, and **20/20 project-folder tests passed**.
