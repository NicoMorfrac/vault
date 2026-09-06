---
type: implementation_evidence
status: achieved
decision_status: approved
source_agent: Drafting_CAD_Agent
created: 2026-09-06
audience: internal
related_findings: []
related_concepts:
  - controlled-cad-automation
  - fusion-360
  - paperclip-workflow
related_projects: []
related_reports:
  - MORAAAAA-188
---

# MORAAAAA-188 — General CAD intake and Fusion Bridge 0.4.0

## Outcome

The Drafting & Fusion 360 CAD Agent now accepts geometry from direct written instructions, sketches, technical drawings, PDF/images and supported 2D/3D CAD attachments. A simple fully dimensioned instruction no longer requires an attachment, project brief or repeated build approval. The assigned Paperclip task authorises one new internal reference draft; manufacturing, overwrite, production drawing, external transfer and release remain separately controlled.

MORAAAAA-188 completed automatically through Paperclip after its blocked state was returned to `todo`. No manual agent invocation was used.

## Root cause

Bridge 0.3.3 exposed only `create_reference_bracket_v1`. The Drafting connector required a PDF/image and a later exact build approval, so the valid instruction “cylinder, diameter 10 mm, height 60 mm” could only block.

## Implemented capability

- `create_cylinder_v1`: diameter and height;
- `create_box_v1`: length, width and height;
- `create_tube_v1`: outer diameter, inner diameter and height;
- `create_extruded_profile_v1`: ordered dimensioned polygon plus optional circular holes and one extrusion;
- `import_reference_v1`: DXF, SVG, STEP/STP, IGES/IGS, SAT, SMT, F3D, STL, OBJ and 3MF;
- retained validated `create_reference_bracket_v1` for the ORF12 family.

All jobs remain declarative and schema-validated. Generated Python, arbitrary paths and overwrite are rejected. Attached source files are copied into a controlled source directory and SHA-256 checked before Fusion imports them.

## Live proof — MORAAAAA-188

- Issue UUID: `9833383d-265c-459f-9fcd-8a1f06ae1c67`
- Final Paperclip state: `done`
- Fusion job: `f1e96a5e-db53-428d-9bb3-e8cd855f387c`
- Bridge: 0.4.0
- Fusion: 2704.1.53
- Geometry: single solid cylinder, diameter 10 mm, height 60 mm
- Parameters: 2
- Features: 1
- Receipt: `SUCCEEDED`; scratch document closed after export

Verified outputs:

- F3D: `facb6ecf493314d2bc089316a96010368ceaa0cbdc6f3efda42c178ad2be397b`
- STEP: `f713ae2ce4de4c589cb1f9121465e818636a0baa6c06aa73b07e6fd70b8f9ccc`
- reference DXF: `1e9d683f394d2d6a94a424c946f8a5a42dfd209e1b689cfa5fe6f2c168ea1fba`
- preview PNG: `770346ba6f06be06b0cbcd368ef37b9745f0e1aa1f37f9d8ebf1a547052d0847`

## Verification

- Full Node connector/workflow regression: 234 passed, 0 failed.
- Fusion shared validator tests: 5 passed, 0 failed.
- Python source compiled successfully.
- Live Bridge 0.4.0 heartbeat verified.
- Live Fusion job produced F3D, STEP, DXF and preview with receipt/hash verification.

## Limits retained

The bridge is not an unrestricted arbitrary-shape code generator. Common primitives, prismatic polygon profiles and reference imports are automated. Freeform surfaces, complex multi-feature assemblies and production drawing automation require additional reviewed declarative feature families or supervised CAD work. Outputs remain `REFERENCE ONLY / UNVERIFIED / NOT FOR MANUFACTURE` until qualified review and release.

## Related Links

- [[02_AGENTS/Drafting_CAD_Agent/AGENTS|Drafting & Fusion 360 CAD Agent]]
- [[02_AGENTS/Drafting_CAD_Agent/REFERENCE/FUSION_CAPABILITY|Fusion capability and limitations]]
- [[02_AGENTS/Nico_AI/WORKFLOWS/DIRECT_CAD_REQUEST|Nico direct CAD routing]]
- [Paperclip issue MORAAAAA-188](http://127.0.0.1:3100/MORAAAAA/issues/MORAAAAA-188)
