# Workflow - Direct CAD Request

## Trigger

A direct human Paperclip task asks to create, convert, review or update 2D/3D CAD or a Fusion 360 model from written dimensions, a sketch/drawing, an image/PDF or a supported 2D/3D CAD file.

## Fast path

1. Read the assigned task and its attachment list.
2. Confirm the wording clearly requests CAD, Fusion, drawing, sketch or model work.
3. A fully dimensioned written instruction needs no attachment. Preserve supported PDF, PNG/JPEG/WEBP, DXF, SVG, STEP/STP, IGES/IGS, SAT, SMT, F3D, STL, OBJ and 3MF attachments on the same issue.
4. Do not request project, client, NDA, budget, schedule, material, finish, manufacturing process, acceptance plan or release details unless the user states that those items control the CAD output.
5. Check out the task and call `route_cad_task`. This transfers the same issue and supported attachments to the Drafting & Fusion 360 CAD Agent.
6. Report `ROUTED_TO_DRAFTING`. Do not claim the model has been created.

## Drafting defaults

- Standalone CAD ID: use the Paperclip issue identifier until the human supplies another ID.
- Units: use explicit instruction/source units; if absent and scale cannot be established, Drafting asks one consolidated question.
- 3D output: default internal reference formats are native Fusion `.f3d` plus STEP where supported.
- 2D output: include a reference DXF/profile when supported; production drawings remain separately reviewed.
- Material, finish and tolerances may remain `not specified` for geometry-only reference models.

## Boundaries

The direct assigned task authorises routing and one first internal reference draft through the controlled Fusion bridge. It does not authorise invention of material geometry, overwrite, production drawing release, manufacturing, external sending or design release.
