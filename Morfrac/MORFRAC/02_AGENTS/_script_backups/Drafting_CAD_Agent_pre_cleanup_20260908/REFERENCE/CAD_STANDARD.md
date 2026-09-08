# MORFRAC CAD and Drafting Standard

## Purpose

This document defines MORFRAC's technical methodology for controlled CAD modelling, drafting, configuration management, verification and engineering handoff.

It applies to:

- 3D part modelling;
- assemblies and components;
- parametric geometry;
- surfaces;
- reference models;
- 2D sketches;
- manufacturing drawings;
- drawing review;
- parameter management;
- configuration/revision control;
- CAD verification;
- neutral/native exports;
- CAD handoffs to Engineering, FEA, CNC, Quality and Product Documentation.

Live Fusion execution capability, supported bridge operations and connector limitations are defined separately in:

`REFERENCE/FUSION_CAPABILITY.md`

Runtime, Paperclip coordination, persistence and release authority belong in `AGENTS.md`.

---

# 1. Fundamental Principle

Drafting/CAD represents approved design intent.

It does not create engineering authority.

The controlled chain is:

`source requirement → parameter baseline → CAD representation → verification → reviewed export/drawing → downstream handoff`

Always distinguish:

- source geometry;
- derived geometry;
- assumptions;
- proposed changes;
- approved design;
- reference-only geometry;
- released geometry.

A model that rebuilds correctly is not automatically an approved design.

---

# 2. Responsibility Boundary

Drafting/CAD owns:

- representation of approved geometry;
- model structure;
- sketch/feature organisation;
- parameterisation;
- drawing completeness;
- configuration/revision traceability;
- export traceability;
- CAD verification.

Engineering owns:

- design intent;
- loads;
- material;
- structural requirements;
- safety factors;
- engineering tolerances;
- acceptance criteria;
- design changes;
- technical release.

CNC owns:

- stock;
- workholding;
- manufacturing setups;
- tooling;
- cutting data;
- CAM;
- NC code;
- prove-out.

FEA owns:

- analysis idealisation;
- loads/boundary conditions used in FEA;
- mesh/solver methodology;
- analysis results.

Quality/Metrology owns:

- inspection method;
- measurement;
- conformity;
- nonconformance disposition.

Project Manager owns project structure and coordination.

Product Documentation owns released product documentation.

---

# 3. Proportional Intake

Request only the information needed for the requested CAD result.

A simple geometry-only task does not automatically require:

- project administration;
- client information;
- budget;
- schedule;
- material;
- finish;
- manufacturing method;
- release authority.

Example:

A fully dimensioned cylinder with known units is sufficient for a reference-model task.

Do not manufacture administrative blockers.

More information is required when the requested output depends on:

- manufacturing;
- fit/interface;
- tolerance;
- analysis;
- formal drawing;
- controlled project use;
- design release;
- external release.

---

# 4. Minimum CAD Task Intake

Capture as applicable:

- Paperclip issue;
- CAD ID;
- requested revision;
- project relationship;
- requester;
- decision owner;
- requested 3D output;
- requested 2D output;
- requested export formats;
- source files/instructions;
- source revision/hash/reference;
- units;
- origin;
- axis convention;
- material where representation requires it;
- manufacturing context where relevant;
- Engineering authority;
- drawing reviewer;
- release authority;
- capability state;
- missing inputs;
- conflicts.

For standalone work, the issue ID may serve as the provisional CAD ID.

---

# 5. Source Hierarchy

Prefer:

1. approved current Engineering requirements;
2. controlled drawing/CAD/BOM/configuration;
3. explicit human design decisions recorded in the task;
4. traceable supplied sketches/files;
5. verified dimensions in supplied technical evidence;
6. derived geometry from controlled source values;
7. bounded assumptions for reference-only work;
8. visual measurements or generic inference only as low-confidence aids.

Never replace a source dimension with an estimated screen measurement when a controlling value exists.

---

# 6. Source Evidence

For important source inputs record as applicable:

- source identifier;
- file/document;
- revision;
- hash;
- date;
- configuration;
- page/view;
- dimension/feature reference;
- owner;
- status.

A screenshot, neutral export, mesh or printed drawing is evidence of a representation.

It is not automatically the authoritative parametric source.

---

# 7. Units

Units must be explicit.

Record:

- source units;
- model units;
- drawing units;
- export units.

Do not silently convert units.

When conversion is required:

- retain original source value;
- show conversion method;
- verify the result;
- preserve the relationship in the parameter record.

---

# 8. Coordinate and Reference System

Establish where relevant:

- origin;
- X/Y/Z axes;
- reference planes;
- centreplanes;
- symmetry;
- principal directions;
- interfaces;
- envelopes;
- assembly references.

Coordinate decisions that affect downstream manufacturing, FEA or interfaces must be explicit.

---

# 9. Parameter Register

Important geometry should be parameterised where practical.

For each controlling parameter record:

- name;
- symbol;
- value or formula;
- unit;
- tolerance where applicable;
- configuration;
- source;
- source revision;
- owner;
- status;
- notes.

Recommended statuses:

- `source`
- `derived`
- `proposed`
- `approved`
- `superseded`
- `conflict`
- `unknown`

Do not mix these states.

---

# 10. Derived Parameters

A derived parameter should show its relationship to authoritative inputs.

Examples:

- half-width;
- pitch spacing;
- derived radius;
- geometric offset;
- calculated pattern spacing.

A derived value is not a new design requirement unless Engineering approves it as such.

---

# 11. Assumptions

For internal reference modelling, bounded assumptions may be used when necessary to complete non-critical visual geometry.

Every assumption must be:

- explicit;
- identifiable;
- limited in scope;
- distinguishable from source geometry.

Outputs containing unresolved assumptions must remain labelled as appropriate:

`REFERENCE ONLY`

`UNVERIFIED`

`NOT FOR MANUFACTURE`

Do not silently convert an assumption into approved geometry.

---

# 12. Source Conflicts

When sources disagree, use:

`CAD_SOURCE_CONFLICT`

or, where appropriate:

`CAD_INPUT_BASELINE_REQUIRED`

Identify:

- conflicting sources;
- exact affected dimension/feature;
- revision/configuration;
- effect on the requested output;
- authority required to resolve it.

Do not choose the easier geometry.

---

# 13. Design Intent

CAD structure should communicate design intent.

Prefer:

- named parameters;
- constrained sketches;
- stable construction geometry;
- symmetry;
- patterns;
- deliberate feature dependencies;
- controlled component references.

Avoid unnecessary dependence on fragile:

- face IDs;
- edge IDs;
- incidental topology;
- imported geometry details likely to change.

---

# 14. Feature Tree

Keep modelling deterministic and understandable.

Name important:

- sketches;
- planes;
- parameters;
- bodies;
- components;
- features;
- patterns;
- exports.

Record feature order and dependencies where they matter.

Avoid unnecessary complexity.

Do not change approved geometry merely to make the feature tree easier.

---

# 15. 3D Part Modelling

For a 3D part define as applicable:

- model purpose;
- body/component structure;
- origin/reference system;
- controlling sketches;
- parameters;
- feature order;
- extrusion/revolution/sweep/loft logic;
- patterns;
- symmetry;
- draft;
- fillets;
- chamfers;
- holes;
- interfaces;
- envelopes;
- manufacturing allowances only when approved.

---

# 16. Assemblies

Before assembly changes establish:

- component identity;
- component revision;
- grounded/reference components;
- interfaces;
- joints;
- constraints;
- motion intent;
- clearances;
- configurations.

Do not modify component geometry merely to force an assembly to fit unless the design authority approves the change.

---

# 17. Configurations

Where multiple variants exist, identify:

- common geometry;
- variant-specific parameters;
- configuration identifier;
- source requirements;
- revision relationships.

Do not mix geometry from different configurations in one output without explicit identification.

---

# 18. Interfaces and Envelopes

For interface-critical geometry record as applicable:

- mating component;
- locating geometry;
- hole patterns;
- shafts/pins;
- bearing surfaces;
- clearance;
- interference;
- envelope;
- movement range.

Interface dimensions should trace to approved sources.

---

# 19. Manufacturing Awareness

Drafting/CAD should consider manufacturability but does not own the machining process.

It may identify:

- inaccessible features;
- impossible geometry;
- excessively fragile detail;
- ambiguous datums;
- tolerance conflicts;
- manufacturing complexity;
- tool-access concerns;
- split-line or setup implications.

Route manufacturing-process decisions to CNC.

Do not alter design intent without Engineering approval.

---

# 20. FEA Handoff Geometry

For FEA handoff identify:

- exact configuration;
- revision;
- units;
- geometry simplifications;
- removed features;
- retained interfaces;
- idealised features;
- analysis-specific variant identity.

A simplified FEA model is not automatically the design master.

Keep analysis geometry distinguishable from production geometry.

---

# 21. 2D Drawing Purpose

Before preparing a drawing establish its purpose.

Examples:

- manufacturing;
- inspection;
- assembly;
- installation;
- reference;
- customer/general arrangement.

Drawing content should match its intended use.

---

# 22. Drawing Identity

Every controlled drawing should identify as applicable:

- source model;
- configuration;
- revision;
- drawing ID;
- units;
- projection standard;
- sheet size;
- template;
- title block;
- revision state;
- intended purpose.

---

# 23. Views

Plan views required to communicate geometry clearly.

Possible views include:

- base;
- projected;
- section;
- detail;
- auxiliary;
- isometric.

Define:

- orientation;
- scale;
- hidden-line policy;
- tangent-edge policy;
- section location;
- detail boundary.

Do not use a visually convenient view that obscures the controlling geometry.

---

# 24. Dimensioning

Dimensions must trace to approved design information.

Distinguish:

- driving dimensions;
- inspection dimensions;
- reference dimensions.

Reference dimensions should be marked as such.

Check for:

- duplicate dimensions;
- contradictory dimensions;
- over-dimensioning;
- missing controlling dimensions;
- ambiguity;
- unreadable layout.

Do not create tolerances by inference.

---

# 25. Datums and GD&T

Include:

- datums;
- geometric tolerances;
- datum reference frames;
- critical characteristics;

only when sourced or approved by the accountable Engineering/Quality authority.

Drafting represents the requirement.

It does not invent the engineering tolerance scheme.

---

# 26. Notes and Process Requirements

Include only source-backed or approved:

- material;
- heat treatment;
- coating;
- surface finish;
- welding notes;
- process notes;
- deburring;
- edge treatment;
- inspection notes;
- marking;
- cleanliness.

Do not populate drawings with generic shop assumptions.

---

# 27. Parts Lists and Balloons

For applicable assemblies verify:

- item identity;
- component revision;
- quantity;
- BOM consistency;
- balloon correspondence;
- omitted/duplicate items.

The drawing parts list must remain consistent with the authoritative BOM/configuration.

---

# 28. Drawing Verification

Review:

- source model/configuration/revision;
- projection;
- units;
- sheet/template/title block;
- view completeness;
- sections/details;
- dimensions;
- tolerances;
- datums;
- GD&T;
- notes;
- finish/process requirements;
- parts list;
- balloons;
- revision table;
- readability;
- broken references;
- conflicting dimensions.

A drawing can be geometrically correct but still incomplete for manufacturing.

---

# 29. Automated Drawing Boundary

Automated or preview-generated drawings are not automatically production drawings.

A production-oriented drawing requires:

- correct source model;
- complete requirements;
- suitable layout;
- drawing verification;
- human technical review.

Automated generation capability and design release are separate matters.

---

# 30. Model Verification

For a 3D model verify as applicable:

- identity;
- configuration;
- revision;
- units;
- parameters;
- constraints;
- feature health;
- body/component structure;
- joints;
- interfaces;
- envelopes;
- clearances/interferences;
- material representation status;
- export identity.

Do not confuse visual similarity with verified geometry.

---

# 31. Mass Properties

Mass properties require suitable prerequisites.

Verify as applicable:

- correct geometry;
- correct body state;
- correct material/density;
- correct included components.

If material/density is not authoritative, mass properties must remain qualified.

---

# 32. Export Planning

For each export define:

- source model/drawing;
- configuration;
- revision;
- format;
- units;
- filename;
- intended purpose;
- information-loss considerations.

Possible formats include:

- native CAD;
- STEP;
- IGES;
- SAT;
- DXF;
- SVG;
- STL;
- OBJ;
- 3MF;
- PDF;

where supported by the applicable workflow/capability.

---

# 33. Export Traceability

An export should remain traceable to:

- source CAD ID;
- configuration;
- revision;
- export version;
- unit system;
- generation source;
- hash where controlled.

Where possible verify the exported file by:

- reopening;
- importing;
- geometry comparison;
- dimensional check;
- hash/receipt.

---

# 34. Neutral and Mesh Formats

Recognise information loss.

A neutral BREP export may lose:

- parametric history;
- feature intent;
- native constraints.

A mesh may additionally lose:

- analytic surfaces;
- exact topology;
- parameter structure;
- manufacturing precision.

Do not treat a mesh as equivalent to an authoritative parametric model unless explicitly intended.

---

# 35. Revision Control

A topology- or requirement-affecting change requires controlled revision handling.

Typical triggers include:

- changed dimensions;
- changed formulas;
- changed hole pattern;
- changed interface;
- changed material representation affecting downstream use;
- changed configuration;
- changed drawing requirement;
- changed export basis.

Preserve prior revisions.

Do not overwrite historical evidence automatically.

---

# 36. Change Record

For an important CAD change record:

- requester;
- reason;
- prior revision;
- new revision;
- affected parameters;
- affected features;
- affected views;
- affected interfaces;
- downstream consumers;
- required re-review.

Possible downstream reviewers include:

- Engineering;
- CNC;
- FEA;
- Quality;
- Product Documentation.

---

# 37. Downstream Impact

A CAD change may invalidate:

- FEA geometry;
- manufacturing process;
- NC/CAM work;
- inspection plans;
- drawings;
- manuals;
- installation documentation;
- costing.

Identify affected consumers rather than assuming the change is local.

---

# 38. Handoff to Engineering

Provide:

- exact CAD ID;
- configuration;
- revision;
- source baseline;
- assumptions;
- unresolved design questions;
- model/drawing verification state.

Engineering owns the design decision.

---

# 39. Handoff to CNC

Provide only the approved geometry and manufacturing-relevant requirements needed.

Include:

- part/configuration;
- revision;
- units;
- datums;
- tolerances;
- interfaces;
- relevant export identity.

CNC owns manufacturing strategy.

---

# 40. Handoff to FEA

Provide:

- exact geometry/configuration;
- revision;
- units;
- analysis-specific simplifications;
- interface references;
- source identity.

FEA owns analysis methodology and results.

---

# 41. Handoff to Quality

Provide:

- drawing/configuration/revision;
- critical characteristics;
- approved tolerances/datums;
- inspection-relevant geometry.

Quality owns conformity evidence.

---

# 42. Handoff to Product Documentation

Provide only approved/released visual or geometry information intended for documentation use.

Draft/reference CAD must not silently become released product documentation.

---

# 43. Handoff to Project Costing

Drafting/CAD may provide technical effort/resource information such as:

- estimated drafting hours;
- model complexity;
- drawing count;
- export requirements;
- revision effort.

Project Costing owns commercial rates, margins, prices and supplier-commercial data.

---

# 44. Vault Information Architecture

Obsidian is appropriate for durable textual/traceability records such as:

- requirements;
- parameter registers;
- source manifests;
- CAD review reports;
- verification findings;
- change records;
- execution receipts;
- links to authoritative CAD.

Authoritative native CAD may live in the approved CAD/Fusion/project repository selected by the responsible human/project owner.

Do not assume Obsidian is the authoritative binary CAD store.

---

# 45. Project Structure

Drafting/CAD does not create project folders.

Project Manager owns project structure.

When project-specific storage is required, use the exact existing authorised project destination.

Do not invent a CAD discipline folder merely because one would be convenient.

---

# 46. Internal Review Records

Controlled internal CAD review records may contain:

- source identity;
- parameter baseline;
- assumptions;
- verification;
- change impact;
- execution receipt references;
- unresolved issues.

An internal review record is not design release.

---

# 47. Confidentiality

Treat as need-to-know:

- unreleased CAD;
- drawings;
- interfaces;
- tolerances;
- customer geometry;
- design concepts;
- supplier geometry;
- manufacturing-sensitive details.

Do not expose unrelated project geometry merely because it exists in the vault.

Credentials, tokens and unrestricted connector configuration do not belong in CAD records.

---

# 48. Minimum Parameter Register

For each important parameter:

| Field | Required content |
|---|---|
| Parameter | Descriptive name |
| Symbol | CAD/engineering symbol |
| Value/formula | Controlled value or expression |
| Unit | Explicit unit |
| Tolerance | If authoritative/applicable |
| Configuration | Applicable variant |
| Source/revision | Traceable source |
| Owner | Authority for the value |
| Status | source/derived/proposed/approved/etc. |
| Notes | Assumptions or dependencies |

Also define:

- origin;
- axes;
- reference planes;
- symmetry;
- interfaces;
- envelopes;
- display precision where relevant;
- unit-conversion method;
- revision/supersession.

---

# 49. Minimum 3D Build Definition

Record as applicable:

- CAD ID/revision;
- model purpose;
- source baseline;
- units;
- component/body structure;
- parameters;
- sketches;
- constraints;
- feature sequence;
- construction geometry;
- patterns;
- symmetry;
- fillets/chamfers/draft;
- interfaces;
- joints;
- clearances;
- configurations;
- assumptions;
- expected verification.

---

# 50. Minimum Drawing Definition

Record:

- drawing ID/revision;
- source model/configuration/revision;
- purpose;
- units;
- projection;
- sheet/template/title block;
- base view;
- projected views;
- sections;
- details;
- scales;
- dimensions;
- tolerances;
- datums;
- GD&T;
- material/process notes;
- parts list;
- balloons;
- revision information;
- required reviewers.

---

# 51. Minimum Model / Drawing Verification Record

## Identity

- CAD/model/drawing ID;
- configuration;
- revision;
- source baseline;
- execution/source receipt where applicable;
- reviewer.

## 3D

- units;
- parameters;
- feature health;
- bodies/components;
- joints;
- interfaces;
- envelopes;
- clearance/interference;
- material representation;
- downstream handoff state.

## 2D

- source model;
- projection;
- sheet/template/title block;
- views;
- sections/details;
- dimensions;
- tolerances;
- datums/GD&T;
- notes;
- parts list;
- balloons;
- revision table;
- readability;
- reference health.

## Release Boundary

- save state;
- export state;
- Engineering review;
- Quality/manufacturing review;
- external-release state;
- open issues.

---

# 52. Minimum Export Manifest

Record:

- CAD ID;
- configuration;
- source revision;
- export version;
- format;
- units;
- options/tessellation where relevant;
- filename;
- intended recipient/use;
- information-loss limitations;
- resulting file identity/hash;
- verification method;
- release status.

---

# 53. Verification Language

Use precise maturity labels.

Examples:

- `REFERENCE ONLY`
- `UNVERIFIED`
- `ENGINEERING REVIEW REQUIRED`
- `DRAWING VERIFICATION REQUIRED`
- `INTERNAL ONLY`
- `NOT RELEASED`
- `NOT FOR MANUFACTURE`

Do not use `approved`, `released`, `production-ready` or equivalent unless the applicable authority actually established that state.

---

# 54. Quality Rules

Always:

- preserve source geometry;
- preserve units;
- identify configuration;
- maintain parameter traceability;
- distinguish source/derived/proposed values;
- expose assumptions;
- maintain revision history;
- verify model health;
- verify drawing completeness;
- identify downstream impact;
- preserve export traceability;
- separate reference CAD from released CAD.

Never:

- invent engineering requirements;
- invent tolerances;
- silently resolve source conflicts;
- silently convert visual estimates into approved geometry;
- change design intent merely to simplify modelling;
- overwrite a prior revision automatically;
- treat a mesh/screenshot as equivalent to a parametric master;
- treat an automated drawing as released by default;
- declare manufacturing suitability from CAD alone;
- release or externally send CAD without the governing authority.

The objective is a traceable CAD representation of controlled design intent, not merely geometry that looks correct.