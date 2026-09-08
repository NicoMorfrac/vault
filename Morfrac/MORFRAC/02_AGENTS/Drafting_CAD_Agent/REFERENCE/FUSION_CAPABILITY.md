# MORFRAC Fusion 360 Capability

## Purpose

This file defines the currently supported Fusion 360 execution capability available to the Drafting/CAD Agent.

It is a live capability reference.

Update this file when:

- the Fusion bridge version changes;
- supported declarative operations change;
- import formats change;
- output formats change;
- execution semantics change;
- drawing automation becomes validated;
- connector capabilities change.

General CAD methodology belongs in:

`REFERENCE/CAD_STANDARD.md`

Operational rules and authority boundaries belong in:

`AGENTS.md`

---

# Current Capability

Fusion 360 is available through the controlled MORFRAC Fusion Bridge.

Current validated bridge version:

`0.4.0`

Paperclip exposes these controlled Drafting tools:

- `fusion_status`
- `build_fusion_reference`
- `fusion_receipt`

The bridge supports controlled internal reference-model creation.

It does not provide:

- arbitrary Fusion API access;
- arbitrary Python execution;
- shell access;
- arbitrary filesystem access;
- unrestricted macros;
- CAM execution;
- FEA execution;
- machine control;
- design release;
- manufacturing release;
- external sending.

---

# Execution Architecture

The Fusion bridge uses a controlled queue and Fusion add-in.

The bridge:

- accepts schema-validated declarative jobs;
- uses a fixed controlled queue;
- does not accept arbitrary generated code;
- does not accept arbitrary output paths;
- executes Fusion modelling on Fusion's main thread through the controlled add-in;
- creates new outputs only;
- does not overwrite existing outputs;
- emits execution receipts;
- emits output hashes;
- preserves failed/uncertain attempts for review.

A queued job is not proof that Fusion executed successfully.

Successful execution exists only when the corresponding receipt confirms the result and required outputs.

---

# Readiness Check

Before attempting Fusion execution:

1. call `fusion_status`;
2. verify that the bridge is ready;
3. require a current Fusion heartbeat;
4. verify that the requested operation is currently supported.

If the bridge is unavailable or stale, report:

`FUSION_BRIDGE_NOT_READY`

Do not fabricate execution.

---

# Supported Reference Operations

Current declarative operations are:

## create_cylinder_v1

Creates a cylindrical reference body.

Required geometry includes:

- diameter;
- height.

---

## create_box_v1

Creates a rectangular reference body.

Required geometry includes:

- length;
- width;
- height.

---

## create_tube_v1

Creates a tubular reference body.

Required geometry includes:

- outer diameter;
- inner diameter;
- height.

---

## create_extruded_profile_v1

Creates a reference extrusion from an ordered 2D polygon profile.

Supports:

- ordered `[x,y]` profile points;
- extrusion distance;
- optional circular holes.

Use explicit millimetres for generated geometry.

Do not force geometry into this operation when the actual shape requires unsupported feature logic.

---

## import_reference_v1

Imports an assigned reference file through the controlled attachment route.

Supported source formats currently include:

- DXF
- SVG
- STEP
- STP
- IGES
- IGS
- SAT
- SMT
- F3D
- STL
- OBJ
- 3MF

Mesh-unit information must be supplied where relevant.

The imported file remains reference geometry unless separately reviewed and approved for a different use.

---

## create_reference_bracket_v1

Creates only the currently validated ORF12 reference-bracket family.

Do not use this family for unrelated bracket geometry.

---

# Unsupported Geometry

The bridge does not currently provide unrestricted arbitrary CAD reconstruction.

If the requested geometry exceeds the supported declarative operations:

- identify the exact missing capability;
- ask one consolidated geometry question where clarification could make the task fit an existing operation;
- otherwise prepare a human-build specification or propose a reviewed new declarative feature family.

Do not force unrelated geometry into an existing operation merely to obtain an executable job.

---

# Source Attachments

Only attachments belonging to the assigned Paperclip issue may be used for Fusion reference execution.

For supported CAD/import files:

- use the assigned attachment ID;
- preserve the expected SHA-256;
- verify the copied source against the hash before import.

Do not accept arbitrary filesystem paths.

---

# Images and PDFs

Images and PDFs are geometry evidence, not direct CAD imports through the bridge.

The Drafting/CAD Agent may:

1. inspect the assigned image/PDF;
2. extract visible geometry and dimensions;
3. distinguish source dimensions from assumptions;
4. translate the geometry into a supported declarative operation if possible.

Do not claim that an image or PDF itself was imported as authoritative CAD geometry.

---

# Assumptions

For reference-only work, bounded assumptions may be used where needed.

Every assumption must be:

- explicit;
- listed in the build request;
- clearly distinguishable from source geometry.

Outputs containing assumptions remain:

`REFERENCE ONLY`

`UNVERIFIED`

`NOT FOR MANUFACTURE`

unless subsequently reviewed under the applicable engineering process.

---

# First Internal Reference Build

A direct assigned Paperclip CAD task, or an authorised project handoff, is sufficient authority for one new internal reference draft when:

- the geometry baseline is sufficiently defined;
- the selected operation is supported;
- no consequential design decision is being invented;
- no overwrite is required.

Do not request a redundant second approval merely to execute the first supported internal reference build.

This authority does not approve:

- design assumptions;
- technical design release;
- manufacturing;
- analysis;
- master modification;
- overwrite;
- external handoff.

---

# Build Execution

For a supported task:

1. verify bridge readiness;
2. freeze the source geometry/parameters;
3. select the narrowest valid operation;
4. identify assumptions;
5. define a new output basename;
6. include the assigned source attachment where applicable;
7. call `build_fusion_reference` once.

Do not automatically retry a durable attempt.

---

# Failed or Uncertain Execution

A queued or durable attempt that fails or becomes uncertain is not automatically retryable.

After such an attempt:

1. inspect the available receipt/status;
2. preserve the failed attempt;
3. identify the cause;
4. correct the input or capability issue;
5. use a new revision for a subsequent approved attempt.

Do not submit the same uncertain mutation repeatedly.

---

# Receipt Verification

Use:

`fusion_receipt`

to verify execution.

Check as applicable:

- receipt status;
- operation;
- source attachment/hash;
- generated geometry;
- body count;
- feature count;
- parameter count;
- output files;
- output hashes;
- warnings/errors.

Do not report:

`FUSION EXECUTED`

or equivalent unless the receipt confirms execution.

A queued job is not sufficient.

---

# Output Behaviour

The controlled reference bridge may produce supported internal outputs such as:

- native Fusion `.f3d`;
- STEP;
- reference DXF;
- preview image;

according to the selected operation.

Outputs are created as new files.

Existing output files are not overwritten automatically.

Output identity and hashes should be verified through the receipt.

---

# Output Status

Bridge-generated outputs are internal reference outputs unless a separate process establishes a higher maturity.

Use labels such as:

- `REFERENCE ONLY`
- `UNVERIFIED`
- `INTERNAL ONLY`
- `NOT FOR MANUFACTURE`
- `NOT RELEASED`

Creation by Fusion does not mean:

- design approved;
- drawing released;
- manufacturing approved;
- FEA validated;
- product conforming.

---

# 2D Drawing Capability

Automated Fusion production-drawing creation is not currently treated as a validated production workflow.

Fusion's drawing API capability may exist, but MORFRAC has not established the automated path as authoritative production-drawing execution.

Therefore:

- automated drawing generation must not be represented as released production drawing capability;
- production-oriented drawings require supervised creation/review;
- drawing content must still comply with `REFERENCE/CAD_STANDARD.md`;
- human technical review remains required.

When a validated MORFRAC automated drawing workflow is established, update this file before allowing autonomous production-drawing execution.

---

# Import and Export Limitations

Imports and exports may lose information.

Examples:

- neutral BREP may lose parametric feature history;
- mesh formats may lose analytic surfaces and manufacturing precision;
- DXF may contain only a 2D representation;
- imported F3D/reference geometry may not establish design authority.

The bridge confirms file generation/import behaviour.

It does not establish engineering correctness.

---

# No-Overwrite Rule

The bridge must not overwrite an existing CAD/output revision automatically.

For changes:

- create a new revision/output identity;
- preserve prior outputs;
- maintain traceability.

This applies to:

- F3D;
- STEP;
- DXF;
- previews;
- imported/reference outputs.

---

# Capability vs Release

The bridge may establish that Fusion successfully created geometry.

It does not establish that the geometry is:

- correct engineering design;
- suitable for manufacture;
- structurally adequate;
- inspected;
- conforming;
- released.

Those decisions remain with the relevant accountable roles.

---

# Explicitly Unsupported Actions

The current Fusion capability does not authorise the Drafting/CAD Agent to:

- run arbitrary generated Python;
- execute arbitrary Fusion scripts;
- access arbitrary paths;
- modify uncontrolled existing masters;
- overwrite prior revisions;
- run CAM;
- generate production NC;
- perform FEA;
- operate machinery;
- save to uncontrolled cloud locations;
- send files externally;
- release design;
- approve manufacturing.

---

# Capability Verification Rule

Never rely solely on this document to prove that Fusion is currently executable.

At runtime, actual capability is established by:

`fusion_status`

This file describes what the connector is intended and validated to support.

The live connector status determines whether execution is available now.

---

# Historical Validation Notes

The MORFRAC Fusion Bridge validation established controlled reference generation including:

- F3D output;
- STEP output;
- reference DXF output;
- preview output;
- no-overwrite behaviour;
- execution receipts;
- output hashes;
- fixed-queue execution;
- Fusion main-thread modelling;
- hash-verified assigned reference imports.

These validation results support the controlled reference workflow described here.

They do not constitute unrestricted Fusion automation approval.