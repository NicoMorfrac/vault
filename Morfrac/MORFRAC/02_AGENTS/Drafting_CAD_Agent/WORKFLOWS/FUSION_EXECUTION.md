# Fusion execution workflow

1. Call `fusion_status`; stop at `FUSION_BRIDGE_NOT_READY` unless the heartbeat is current.
2. Establish geometry from the assigned written instruction and any same-issue source. Read PDF/image pages before modelling. Keep the verified attachment ID/hash when using DXF, SVG or a 3D CAD file.
3. Choose the narrowest operation:
   - `create_cylinder_v1`: `diameter`, `height`;
   - `create_box_v1`: `length`, `width`, `height`;
   - `create_tube_v1`: `outer_diameter`, `inner_diameter`, `height`;
   - `create_extruded_profile_v1`: ordered `[x,y]` profile points, optional circular holes and extrusion distance;
   - `import_reference_v1`: assigned DXF, SVG, STEP/STP, IGES/IGS, SAT, SMT, F3D, STL, OBJ or 3MF plus mesh units;
   - `create_reference_bracket_v1`: only the validated ORF12 family.
4. Separate source dimensions from bounded visual assumptions. Use millimetres explicitly for generated geometry and list all assumptions together.
5. Call `build_fusion_reference` once with revision, operation, parameters, assumptions, a new output basename and the optional source attachment ID. Do not request a second approval for the first internal reference draft.
6. Poll with `fusion_receipt`; do not infer success from a queued state and never retry an uncertain or failed attempt. Use a new revision after review.
7. Verify receipt status, source hash where present, body/feature/parameter counts and every output hash. Review the preview against the source.
8. Report `REFERENCE ONLY / UNVERIFIED / NOT FOR MANUFACTURE`. A production drawing, manufacturing release, external handoff or overwrite still needs its own human gate.

If a sketch/drawing defines geometry beyond these declarative operations, ask one consolidated geometry question or report the exact missing feature family. Do not force unrelated geometry into the wrong operation and never submit generated code.
