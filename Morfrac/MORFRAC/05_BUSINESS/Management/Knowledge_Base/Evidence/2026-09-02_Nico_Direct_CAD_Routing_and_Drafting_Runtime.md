---
type: implementation_evidence
source_agent: Codex
created: 2026-09-02
as_of: 2026-09-02
audience: internal
status: achieved
approval_status: owner_authorised_configuration
related_findings:
  - Nico routes simple human-authored CAD tasks with a PDF or image directly to Drafting on the same Paperclip issue
  - Direct CAD routing creates no project and asks only geometry questions that change the CAD output
  - MORAAAAA-143 retained its PDF and was analysed by the Drafting agent through org_scoped
  - Drafting runtime configuration was normalised and all Paperclip agents returned to idle
  - The controlled Fusion bridge produced and cryptographically verified a reference F3D, STEP, two DXFs and preview for MORAAAAA-143
  - Reference reconstruction remains unverified and not for manufacture when the source drawing omits controlling geometry
related_concepts:
  - Paperclip agent routing
  - Fusion 360 drafting
  - Scoped attachments
  - Human approval boundaries
related_projects: []
related_reports:
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
  - "[[005 - DASHBOARD LATEST REPORTS AND INFORMATION]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Fusion_360_and_Drafting_CAD_Agent]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair]]"
---

# Nico Direct CAD Routing and Drafting Runtime

## Outcome

Simple CAD orders no longer enter the full new-project questionnaire. A local-board request that explicitly asks for CAD, 2D/3D drawing, modelling or Fusion work and includes a PDF or image can be transferred by Nico directly to the Drafting & Fusion 360 CAD Agent on the same Paperclip issue. The attachment remains with the issue and no project is created.

This configuration is achieved for intake, routing, attachment reading, controlled CAD planning and bounded Fusion execution. Paperclip can now send an approved allowlisted reference-bracket job to the local Fusion add-in, which creates new outputs without overwrite and returns a receipt whose output sizes and SHA-256 hashes are independently verified by the Paperclip-side connector.

## Root causes repaired

- Nico classified every attached CAD request as `NEW_PROJECT`, so it asked for client, NDA, budget, schedule, material and other project data even when the order was a simple drawing.
- Drafting was absent from Nico's approved route map.
- Drafting was absent from the organisation-scoped role policy and its live adapter configuration contained repeated command, working-directory and argument values.
- Paperclip normalised newline escapes inside hidden verification JSON, corrupting multi-line `post_update` records and preventing the issue status from being verified.
- Two older Paperclip-managed Codex homes referenced OpenAI document plugins but lacked their installed cache.

## Configuration applied

- Added Nico workflow `DIRECT_CAD_REQUEST` and the scoped `route_cad_task` operation.
- Added Drafting as an approved company- and organisation-scoped role and recipient; Raffa AI remains excluded and unchanged.
- Direct route requires a human-authored current issue, explicit CAD intent, an attached PDF/image and an idle exact Drafting recipient.
- The route reassigns the same issue to Drafting, preserves the attachment and creates no child issue or project.
- Automatic `Review productivity for <issue>` children are ignored by this specific direct-route guard; real open work children still block transfer.
- Drafting adapter was normalised to CLI, model `gpt-5.6-sol`, a scalar working directory and 36 required arguments instead of 1,567 repeated entries.
- Multi-line verification payloads are now stored as newline-safe base64url with backward-compatible legacy reading.
- The missing OpenAI primary-runtime plugin cache was restored for the CEO and CTO Paperclip-managed Codex homes.
- Drafting alone now has `fusion_status`, `plan_fusion_reference`, `execute_fusion_reference` and `fusion_receipt`; no other agent, including Raffa AI, received those tools.
- The Fusion add-in accepts only the allowlisted `create_reference_bracket_v1` operation. It cannot execute supplied Python, select arbitrary paths, overwrite an output or release a design for manufacture.
- The bridge monitors an immutable local job queue, executes Fusion API work on Fusion's main thread and writes a durable receipt. The exported scratch document is closed after success or discarded after failure.
- Heartbeats remain disabled.

## Live proof — MORAAAAA-143

- Title: `drawing test`.
- Human request: create a native Fusion 360 geometry-only 3D model from `123.pdf`; no calculations or working-load analysis.
- The issue was transferred to Drafting with the same issue ID and its single PDF attachment retained.
- Drafting used `org_scoped`, read the issue, read the attachment and recorded a bounded CAD intake.
- Extracted visible parameters: overall length 36.66, width 12, height 22, main bore Ø12, mounting-centre spacing 25 and an M5 callout; units remain unconfirmed but are proposed as millimetres.
- Owner authorisation to continue with a reference-only reconstruction was recorded through this repair task.
- Final controlled job: `0c3ea19f-50be-491e-a845-8fa8fbf58441`, output basename `MORAAAAA-143_ORF12_reference_v06`.
- Fusion 360 2704.1.53 produced one solid body with five features and ten named user parameters.
- The reference controls the visible 36.66 × 12 × 22 mm envelope, Ø12 bore, 25 mm mounting-hole spacing and two nominal Ø5 mm through-all cuts.
- Output readback verified the F3D, STEP, top-reference DXF, front-reference DXF and PNG preview. The F3D SHA-256 is `42a65d2e14e662b738a21eeda078a425e0ae977c6d31803bd758960e1b6d0aee`; the STEP SHA-256 is `2c69f90f67f7868985bdf5ab5a360851bdc8edc73241f6f3d9311ff6f2b8ed78`.
- Paperclip state after lifecycle reconciliation: `in_review`, assigned to `local-board` for human engineering review, with no agent execution lock or active recovery action. Drafting and CTO are idle and there are no live runs.
- Superseded `MORAAAAA-141` and its automatic review `MORAAAAA-142` were cancelled. Automatic review `MORAAAAA-144` for the current issue was also cancelled after the direct route was recovered.

## Verification

- 119 JavaScript connector, organisation-policy and end-to-end workflow tests passed in the prior repair suite.
- The focused Fusion connector and organisation-policy suite passed 62 tests; the Fusion add-in validation suite passed 5 tests.
- 3 PDF extraction tests passed.
- Drafting, CTO and CEO each completed a direct `org_scoped` MCP initialization check.
- Paperclip readback after cleanup: 44 agents idle, 0 agents in error, and 0 enabled heartbeats.
- The v06 execution receipt reports `SUCCEEDED`, `SINGLE_BODY_REFERENCE`, five hash-verified outputs and `scratch_document_closed_after_export: true`.
- Visual QA compared the final preview to the supplied ORF12 sheet and accepted it as a reference reconstruction.
- Bridge 0.2.4 is the verified execution runtime. Bridge 0.2.5, which adds a short Fusion-startup event-loop grace period for pre-existing queued jobs, passed the same five validation tests and is installed for the next Fusion start.
- The supervised v06 repair was executed administratively after owner authorisation, not through an agent-authored Paperclip `fusion_job_plan`. A later automatic Drafting review therefore could not bind that historical receipt to an agent plan. The issue was reconciled to human review without rebuilding or changing any output. Future jobs must use Drafting's native plan → exact human approval → execute → receipt sequence.

## Remaining control

The v06 model is `REFERENCE_ONLY_UNVERIFIED_NOT_FOR_MANUFACTURE`. The source sheet does not control base thickness, boss outside diameter and centre, web profile, radii/fillets, M5 thread form or counterbore/countersink details. The bridge uses documented visual assumptions for those values. A qualified MORFRAC engineer must replace or approve the missing geometry before manufacturing, structural analysis or external release. Current automation is intentionally limited to the reference-bracket operation; new geometry families require their own implemented and tested allowlisted operation.

## Generated evidence and outputs

- Receipt: `C:\Users\nicol\Documents\paperclip 2\paperclip-config\drafting-cad-agent-20260901\fusion-bridge\receipts\0c3ea19f-50be-491e-a845-8fa8fbf58441.receipt.json`
- Fusion model: `C:\Users\nicol\Documents\paperclip 2\paperclip-config\drafting-cad-agent-20260901\fusion-bridge\output\MORAAAAA-143\MORAAAAA-143_ORF12_reference_v06.f3d`
- STEP: `C:\Users\nicol\Documents\paperclip 2\paperclip-config\drafting-cad-agent-20260901\fusion-bridge\output\MORAAAAA-143\MORAAAAA-143_ORF12_reference_v06.step`
- Top and front DXFs plus the preview are stored beside the model.

## Files and controls

- Canonical Nico instructions: [[02_AGENTS/Nico_AI/AGENTS]]
- Direct CAD workflow: [[02_AGENTS/Nico_AI/WORKFLOWS/DIRECT_CAD_REQUEST]]
- Canonical Drafting instructions: [[02_AGENTS/Drafting_CAD_Agent/AGENTS]]
- CAD task intake: [[02_AGENTS/Drafting_CAD_Agent/WORKFLOWS/CAD_TASK_INTAKE]]
- Organisation map: [[00_SYSTEM/ORGANISATION]]

No credentials or secret values are stored in this evidence note.
