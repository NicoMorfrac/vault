# Workflow - Direct CAD Request

## Trigger

Use this workflow when Nico directly requests creation, conversion, review or update of 2D/3D CAD or Fusion 360 geometry.

## Procedure

1. Read the task and available attachments.
2. Confirm the request is genuinely CAD/drawing/model work.
3. Route it directly to the Drafting & Fusion 360 CAD Agent using `route_cad_task`.
4. Preserve relevant supported attachments.
5. Do not turn a standalone CAD request into a full project unless project-level coordination is actually required.

## Defaults

* Use the Paperclip issue ID as the temporary CAD identifier if no other ID is supplied.
* Use explicit source units.
* If units or scale cannot be determined, ask one consolidated clarification.
* Geometry-only work does not require material, finish, manufacturing process, budget or release information unless those affect the requested geometry.
* Material, finish and tolerances may remain `not specified` for reference geometry.

## Boundaries

Routing a CAD request does not authorise:

* invented dimensions or geometry;
* production drawing release;
* design release;
* overwrite of controlled files;
* manufacturing;
* machine execution;
* external sending.

The Drafting/CAD agent remains responsible for its own technical workflow and output controls.
