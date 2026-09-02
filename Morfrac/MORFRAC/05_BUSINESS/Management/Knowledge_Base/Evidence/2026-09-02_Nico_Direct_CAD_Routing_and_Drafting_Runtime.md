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
  - Fusion binary creation remains unavailable until a write-capable Fusion connector is validated
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

This configuration is achieved for intake, routing, attachment reading and CAD planning. It does not claim that Paperclip can yet create, save or export a native Fusion `.f3d` file.

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
- Heartbeats remain disabled.

## Live proof — MORAAAAA-143

- Title: `drawing test`.
- Human request: create a native Fusion 360 geometry-only 3D model from `123.pdf`; no calculations or working-load analysis.
- The issue was transferred to Drafting with the same issue ID and its single PDF attachment retained.
- Drafting used `org_scoped`, read the issue, read the attachment and recorded a bounded CAD intake.
- Extracted visible parameters: overall length 36.66, width 12, height 22, main bore Ø12, mounting-centre spacing 25 and an M5 callout; units remain unconfirmed but are proposed as millimetres.
- Current Paperclip state: `blocked`, assigned to Drafting, with one board-owned decision:
  - A — confirm millimetres and authorise a reference-only traced approximation, marked unverified and not for manufacture; or
  - B — confirm units and provide base thickness, bore-centre height, boss profile/diameter, side profile/radii, edge details and the two M5 feature definitions.
- Superseded `MORAAAAA-141` and its automatic review `MORAAAAA-142` were cancelled. Automatic review `MORAAAAA-144` for the current issue was also cancelled after the direct route was recovered.

## Verification

- 119 JavaScript connector, organisation-policy and end-to-end workflow tests passed.
- 3 PDF extraction tests passed.
- Drafting, CTO and CEO each completed a direct `org_scoped` MCP initialization check.
- Paperclip readback after cleanup: 44 agents idle, 0 agents in error, and 0 enabled heartbeats.
- Drafting readback: CLI engine, `gpt-5.6-sol`, current issue assigned and blocked with one concise unblock action.

## Remaining hold

Fusion 360 is installed, but the current Paperclip connector can only probe/read capability; it cannot yet execute modelling commands, save a binary `.f3d`, export STEP, or verify the resulting geometry. A write-capable Fusion add-in/API bridge and a supervised execution test are still required before agents may claim a native model was created.

## Files and controls

- Canonical Nico instructions: [[02_AGENTS/Nico_AI/AGENTS]]
- Direct CAD workflow: [[02_AGENTS/Nico_AI/WORKFLOWS/DIRECT_CAD_REQUEST]]
- Canonical Drafting instructions: [[02_AGENTS/Drafting_CAD_Agent/AGENTS]]
- CAD task intake: [[02_AGENTS/Drafting_CAD_Agent/WORKFLOWS/CAD_TASK_INTAKE]]
- Organisation map: [[00_SYSTEM/ORGANISATION]]

No credentials or secret values are stored in this evidence note.
