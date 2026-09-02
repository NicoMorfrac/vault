# Workflow - Direct CAD Request

## Trigger

A direct human Paperclip task asks to create, convert, review or update 2D/3D CAD or a Fusion 360 model from an attached technical PDF or supported image.

## Fast path

1. Read the assigned task and its attachment list.
2. Confirm the wording clearly requests CAD, Fusion, drawing, sketch or model work.
3. If no PDF/image is attached, ask only for the missing attachment and set the task to blocked with that exact action.
4. Do not request project, client, NDA, budget, schedule, material, finish, manufacturing process, acceptance plan or release details unless the user already states that those items control the CAD output.
5. Check out the task and call `route_cad_task`. This transfers the same issue, with its existing attachments, to the Drafting & Fusion 360 CAD Agent.
6. Report `ROUTED_TO_DRAFTING`. Do not claim the model has been created.

## Drafting defaults

- Standalone CAD ID: use the Paperclip issue identifier until the human supplies another ID.
- Units: use the drawing's stated units; if absent, the Drafting agent asks one question.
- 3D output: default requested internal formats are native Fusion `.f3d` plus STEP when execution/save becomes available.
- 2D output: add PDF/DXF only when requested or clearly implied.
- Material, finish and tolerances may remain `not specified` for geometry-only reference models; they become blockers only when the representation, verification or manufacturing purpose depends on them.

## Boundaries

The direct task authorises routing and technical intake, not invention of missing geometry, production release, external sending, manufacturing, or automatic Fusion write access. The Drafting agent may read the attachment and prepare the model/build plan. Actual Fusion execution and binary save/export require the validated execution path and applicable human gates.
