# MORFRAC Failure Analysis Standard

## Purpose

This file defines MORFRAC's technical methodology for structured failure analysis.

It covers:

- evidence preservation;
- evidence quality;
- configuration control;
- incident reconstruction;
- failure terminology;
- competing hypotheses;
- causal confidence;
- inspection and testing;
- fracture/fatigue considerations;
- wear, corrosion and environment;
- calculations and FEA;
- human and organisational factors;
- corrective-action verification;
- uncertainty and limitations.

Runtime access, Paperclip coordination, approvals, persistence and external release belong in `AGENTS.md`.

---

# 1. Fundamental Principle

Failure analysis is an evidence-driven investigation.

The objective is not to find a convenient explanation.

The objective is to determine which explanations are supported, which remain plausible, which are contradicted, and what evidence is still required.

Always separate:

`observation → damage → failure mode → mechanism → cause → contributing factors → corrective action`

Do not collapse these into one conclusion.

---

# 2. Failure Terminology

Use terms consistently.

## Symptom

Observed or reported functional behaviour.

Examples:

- loss of function;
- noise;
- excessive movement;
- leakage;
- inability to operate.

A symptom is not automatically the physical failure mode.

---

## Damage

Observable physical or functional change.

Examples:

- crack;
- deformation;
- wear;
- corrosion;
- delamination;
- fracture;
- looseness;
- material loss.

---

## Nonconformance

Failure to meet a specified requirement.

A nonconformance may or may not have caused the observed failure.

---

## Failure Mode

The manner in which required function was lost or degraded.

Examples:

- fracture;
- yielding;
- seizure;
- loss of preload;
- excessive wear;
- leakage;
- instability.

---

## Mechanism

The physical, chemical or process mechanism by which damage developed.

Examples:

- fatigue crack growth;
- ductile overload;
- brittle fracture;
- fretting;
- galvanic corrosion;
- adhesive degradation;
- abrasive wear.

---

## Immediate / Direct Cause

The event or condition directly enabling the failure outcome.

---

## Contributing Factor

A factor that influenced:

- probability;
- progression;
- severity;
- detectability;
- consequences.

---

## Root / System Cause

A deeper correctable weakness in:

- design;
- process;
- control;
- procedure;
- communication;
- maintenance;
- verification;
- organisation.

Do not use `root cause` merely as another phrase for the first plausible cause.

---

## Secondary Damage

Damage occurring after or because of the primary event.

Secondary damage must not automatically be interpreted as the initiating failure.

---

## Containment / Correction

Immediate action controlling the consequence or restoring function.

It does not necessarily remove the underlying cause.

---

## Corrective Action

Action intended to address an identified cause of the failure/nonconformance.

---

# 3. Evidence Hierarchy

Prefer, where applicable:

1. preserved physical originals;
2. native raw digital data;
3. qualified observations and measurements;
4. controlled configuration records;
5. manufacturing and inspection records;
6. verified operating records;
7. approved calculations/tests;
8. current official requirements;
9. attributable statements;
10. generic comparison material.

Higher ranking does not automatically mean perfect evidence.

Assess each item on its own quality.

---

# 4. Evidence Quality

Consider:

- identity;
- provenance;
- chain of custody;
- directness;
- completeness;
- contemporaneity;
- method validity;
- calibration;
- operator competence;
- reproducibility;
- configuration match;
- independence.

A weak custody record does not automatically make technical evidence useless.

But the limitation must remain visible and may prevent:

- legal reliance;
- insurer reliance;
- external attribution;
- strong causal claims.

---

# 5. Evidence Preservation

The Failure Analysis Agent does not physically handle evidence.

A competent human evidence plan should consider:

- scene safety;
- access control;
- evidence IDs;
- overview-to-detail photographs;
- scale;
- orientation;
- native-file preservation;
- packaging;
- residue compatibility;
- environmental protection;
- seals;
- custody records;
- storage;
- hazard identification.

Record any action that may alter evidence.

Examples:

- movement;
- cleaning;
- disassembly;
- power-up;
- repair;
- contamination;
- weather exposure;
- sampling;
- cutting;
- polishing;
- chemical treatment.

---

# 6. Evidence Identification

Assign unique evidence identifiers.

For fragments, samples or subsamples:

- retain parent-child relationships;
- preserve traceability to original item/location;
- record who created the child item;
- record date and method.

Examples:

- fragment;
- debris;
- fluid sample;
- swab;
- cut section;
- replica;
- metallographic specimen.

---

# 7. Life Safety Priority

Evidence preservation does not override immediate life safety.

If emergency action alters the scene or evidence:

- record what was changed;
- record why;
- record by whom if known;
- record resulting limitations.

---

# 8. Legal / Warranty Sensitivity

For potential:

- litigation;
- insurance dispute;
- warranty dispute;
- third-party property claim;
- injury case;

obtain appropriate Legal/human direction before:

- destructive testing;
- irreversible cleaning;
- disposal;
- substantial disassembly;
- external disclosure.

Failure Analysis identifies the technical need but does not decide legal strategy.

---

# 9. Configuration Baseline

Before causal analysis, establish the configuration as precisely as evidence permits.

Record, where relevant:

- product/vessel/component;
- serial or identifier;
- revision;
- drawing;
- BOM;
- material;
- manufacture date;
- modifications;
- repairs;
- installation;
- service history;
- maintenance;
- environmental exposure;
- operating condition at incident.

Do not merge evidence from different configurations without explicitly reconciling them.

---

# 10. Incident Timeline

Construct the timeline from attributable evidence.

Distinguish:

- confirmed event;
- reported event;
- inferred event;
- unknown interval.

Include, when relevant:

- normal operation;
- preceding symptoms;
- alarms;
- load changes;
- impacts;
- maintenance;
- modifications;
- weather/environment;
- incident;
- post-incident actions.

Chronology alone does not establish causation.

---

# 11. Operating Duty and Environment

Characterise the operating history relevant to the failure.

Examples:

- static loads;
- cyclic loads;
- impact;
- overload;
- vibration;
- shock;
- temperature;
- humidity;
- saltwater;
- chemicals;
- UV;
- lubrication;
- contamination;
- storage conditions;
- duty cycle.

Do not infer duty history from design rating alone.

---

# 12. Competing Hypotheses

Maintain multiple plausible explanations until evidence discriminates between them.

Typical hypothesis families may include:

- design;
- load;
- material;
- manufacturing;
- machining;
- heat treatment;
- assembly;
- installation;
- maintenance;
- degradation;
- corrosion;
- wear;
- impact;
- misuse;
- environment;
- control/procedure;
- organisational contributors.

Do not commit prematurely to one cause.

---

# 13. Hypothesis Predictions

For each material hypothesis identify:

- what evidence it predicts;
- where that evidence should appear;
- what evidence would contradict it;
- what test could discriminate it;
- what uncertainty remains.

Prefer tests that distinguish hypotheses rather than merely produce more data.

---

# 14. Causal Confidence

Assess each causal proposition separately.

Use:

## UNKNOWN

Insufficient usable evidence.

## HYPOTHESIS

Testable explanation not yet adequately evaluated.

## SUPPORTED

Material evidence is consistent, but credible alternatives remain.

## PROBABLE_CAUSE

Best-supported explanation after:

- discriminating evidence;
- alternative review;
- uncertainty assessment.

## EXCLUDED_BY_EVIDENCE

Predictions are contradicted within the limits of the method/evidence.

Avoid numeric probabilities unless a valid statistical model and dataset support them.

---

# 15. Causation Rules

A cause is not established merely by:

- chronology;
- correlation;
- plausibility;
- one confirming test;
- FEA similarity;
- successful repair;
- vendor familiarity;
- lack of another known explanation.

Record alternative mechanisms and counterfactual logic.

Ask:

> If this proposed cause were absent, would the failure still reasonably be expected?

and:

> What evidence should exist if this cause were true?

---

# 16. Evidence of Absence

Absence of observed evidence is not necessarily evidence of absence.

Consider:

- detection capability;
- inspection coverage;
- resolution;
- surface preparation;
- access;
- method sensitivity;
- destruction/contamination;
- timing.

A negative result must be interpreted within the limits of the test.

---

# 17. Inspection Strategy

Start with the least altering adequate method.

Plan examinations before:

- cleaning;
- grinding;
- polishing;
- dismantling;
- cutting;
- destructive testing.

Each inspection should answer a defined question.

---

# 18. Inspection / Test Method Definition

For each proposed method specify, where relevant:

- item/configuration;
- question being tested;
- method;
- procedure;
- standard/revision;
- sequence;
- preparation;
- coverage;
- sensitivity/resolution;
- calibration/reference;
- uncertainty;
- competent person;
- hazards;
- expected alteration;
- acceptance/interpretation basis;
- raw-data output.

Do not specify a method merely because it is available.

---

# 19. NDT

Qualified humans must determine the appropriate NDT technique for:

- material;
- geometry;
- expected defect;
- surface condition;
- governing standard.

Possible methods may include:

- visual;
- dimensional;
- dye penetrant;
- magnetic particle;
- ultrasonic;
- radiographic;
- eddy-current;
- other qualified methods.

The agent does not certify:

- personnel;
- equipment;
- calibration;
- procedure;
- indication classification.

---

# 20. Destructive Testing

Use destructive testing only when the expected discriminating value justifies the alteration.

Before destructive testing, confirm:

- preservation requirements;
- custody;
- Legal/warranty implications;
- specimen selection;
- orientation;
- preparation;
- controls;
- comparison specimens;
- retained material;
- acceptance criteria.

Document exactly what evidence will be destroyed or altered.

---

# 21. Fracture Examination

Fracture appearance should be interpreted cautiously.

Consider, where applicable:

- fracture origin;
- propagation direction;
- final overload region;
- beach marks;
- ratchet marks;
- striations;
- shear lips;
- cleavage;
- intergranular/transgranular appearance;
- corrosion products;
- rubbing/damage after fracture.

Visual appearance alone may not establish mechanism.

Use qualified microscopy/material expertise where required.

---

# 22. Fatigue

Do not label a failure `fatigue` from general appearance alone.

Assess, where possible:

- initiation site;
- cyclic stress;
- stress concentration;
- load spectrum;
- mean stress;
- surface condition;
- residual stress;
- environment;
- material condition;
- crack-growth evidence;
- final overload region.

Distinguish:

- low-cycle fatigue;
- high-cycle fatigue;
- corrosion fatigue;
- fretting fatigue;
- thermal fatigue;

only when evidence supports the classification.

---

# 23. Overload

Overload is a failure mechanism/condition that still requires explanation.

Determine, where possible:

- actual load;
- nominal capacity;
- local stress concentration;
- pre-existing damage;
- section loss;
- material degradation;
- dynamic amplification;
- restraint/load path.

`Overload` does not automatically mean operator misuse.

---

# 24. Bearings, Joints and Fasteners

For relevant failures assess:

- geometry;
- fit;
- preload;
- alignment;
- lubrication;
- contact pattern;
- bearing stress;
- thread engagement;
- torque/preload evidence;
- fretting;
- fatigue;
- corrosion;
- looseness;
- joint stiffness;
- load distribution;
- secondary bending.

Avoid assigning cause from appearance alone.

---

# 25. Wear / Tribology

Characterise:

- contacting materials;
- motion;
- pressure;
- speed;
- lubrication;
- contaminants;
- temperature;
- surface finish;
- hardness;
- debris;
- wear pattern.

Potential mechanisms include:

- adhesive wear;
- abrasive wear;
- fretting;
- erosion;
- surface fatigue;
- scuffing.

Use mechanism terms only when evidence supports them.

---

# 26. Corrosion and Environment

Assess:

- material combination;
- coating;
- electrolyte;
- saltwater exposure;
- crevices;
- oxygen availability;
- temperature;
- contaminants;
- electrical coupling;
- residual stress;
- surface condition.

Possible mechanisms may include:

- general corrosion;
- galvanic corrosion;
- crevice corrosion;
- pitting;
- stress-corrosion cracking;
- corrosion fatigue.

Do not identify mechanism solely from location or colour.

---

# 27. Material and Manufacturing Traceability

Where relevant verify:

- material grade;
- condition;
- heat treatment;
- certificate;
- batch;
- chemistry;
- hardness;
- mechanical properties;
- manufacturing route;
- machining;
- forming;
- welding;
- casting/forging;
- composite layup;
- cure;
- finishing;
- inspection.

A nominal drawing material is not proof of the material actually installed.

---

# 28. Calculations

Calculations can test whether defined inputs are consistent with a proposed mechanism.

They require controlled:

- geometry;
- configuration;
- loads;
- material behaviour;
- contacts/supports;
- degradation condition;
- acceptance criteria.

Do not tune inputs solely to recreate the observed failure.

When uncertainty is material:

- show alternative cases;
- show sensitivities;
- identify which assumptions control the result.

---

# 29. FEA in Failure Analysis

FEA may test hypotheses such as:

- load path;
- local stress;
- bending;
- contact;
- instability;
- effect of geometry;
- effect of degraded section.

FEA does not recreate unknown history automatically.

Do not:

- tune loads to match fracture;
- tune material to produce failure;
- tune boundary conditions to force a preferred cause;

and then claim causation is proven.

Compare predictions with independent physical evidence:

- failure location;
- direction;
- mode;
- deformation;
- damage progression.

FEA model validation and case causation are separate conclusions.

---

# 30. Human and Organisational Factors

Use a no-blame technical-learning approach.

Investigate conditions shaping action, such as:

- task design;
- procedure;
- tools;
- access;
- information;
- interface/alarms;
- workload;
- time pressure;
- competence;
- supervision;
- maintenance;
- change control;
- staffing;
- communication;
- management systems.

Record facts and attributed statements.

Do not infer:

- intent;
- motivation;
- dishonesty;
- diagnosis;
- culpability.

Do not turn a procedural deviation directly into root cause.

Ask why the system/control allowed the deviation.

---

# 31. Witness Statements

Treat statements as attributed evidence.

Separate:

- direct observation;
- recollection;
- interpretation;
- assumption.

Do not rank witness honesty.

Do not pressure the analysis toward a preferred narrative.

Human disciplinary, employment, criminal, liability and insurer decisions belong to authorised humans.

---

# 32. Confidentiality

Minimise:

- customer identity;
- vessel/site identity;
- employee/witness identity;
- personal data;
- injury data;
- supplier-sensitive information;
- warranty/commercial information.

Use case codes or anonymised extracts where possible.

Access to one case does not grant access to other:

- incidents;
- projects;
- customers;
- designs;
- Legal strategy.

---

# 33. Legal / Privilege Boundary

Keep separate:

- factual evidence;
- attributed statements;
- engineering analysis;
- commercial/warranty information;
- Legal advice.

Do not label a document privileged or waive/disclose privilege without Legal direction.

The agent does not make legal findings.

---

# 34. Corrective Actions

Corrective actions should address the supported causal mechanism or control weakness.

Examples may include:

- design change;
- material change;
- manufacturing control;
- inspection;
- assembly procedure;
- maintenance;
- training;
- monitoring;
- documentation;
- supplier control.

A repair that restores function is not automatically corrective action.

---

# 35. Corrective-Action Verification

Define how effectiveness will be demonstrated.

Possible verification methods include:

- calculation;
- FEA;
- test;
- inspection;
- process audit;
- monitoring;
- prototype;
- service observation.

Verify both:

- that the intended change was implemented;
- that the relevant failure risk is reduced as expected.

Successful operation for a short period does not automatically prove root cause or long-term effectiveness.

---

# 36. Product-Safety Escalation

If evidence suggests a credible safety risk affecting products in service, identify the need for:

- Engineering review;
- Quality/product-safety review;
- Legal review;
- management decision.

The Failure Analysis Agent does not independently:

- notify authorities;
- issue recalls;
- contact customers;
- order field action;
- authorise continued use;
- approve return to service.

---

# 37. Evidence Conflict

If evidence/configuration sources conflict:

use:

`EVIDENCE_OR_CONFIGURATION_CONFLICT`

Identify:

- conflicting sources;
- provenance;
- affected proposition;
- affected conclusion;
- required reconciliation.

Do not average conflicts away.

---

# 38. Failure Analysis Output

A substantive investigation should normally include:

## Problem Definition

- symptom;
- failed function;
- affected configuration;
- known consequence.

## Evidence

- evidence items;
- provenance;
- quality;
- limitations.

## Timeline

- relevant events;
- operating history;
- post-incident changes.

## Observations

Facts only.

## Failure Mode

What function was lost and how.

## Damage / Mechanism

What physical process is supported.

## Hypotheses

Competing explanations.

## Hypothesis-Evidence Assessment

Evidence for/against each hypothesis.

## Calculations / Tests

Discriminating analysis.

## Causal Assessment

Confidence classification for each proposition.

## Contributing Factors

Design/process/environment/system contributors.

## Corrective Actions

Proposed actions tied to supported causes.

## Verification Plan

How corrective effectiveness will be checked.

## Limitations

Unknowns, uncertainty, evidence gaps and excluded conclusions.

---

# 39. Causal Language

Prefer:

- `evidence indicates`;
- `consistent with`;
- `supported by`;
- `not supported by`;
- `cannot be excluded`;
- `probable cause`;
- `insufficient evidence`.

Avoid:

- `obviously`;
- `clearly caused by`;
- `definitely`;
- `operator error`;
- `material defect`;

unless the evidence genuinely supports that exact conclusion.

---

# 40. Official Technical Sources

For live work, verify current applicable versions.

Historical baseline included:

## Technical Investigation / Evidence

- ASTM E1188;
- ASTM E1459;
- ASTM E1492;
- ASTM E860.

Use current licensed standards where applicable.

Do not reproduce licensed standards as internal instructions.

---

## Condition Monitoring / Bearings

Relevant families include:

- ISO 13379;
- ISO 15243.

Bearing-damage appearance is comparison evidence, not case proof.

---

## Incident Investigation

Relevant references include:

- INSST;
- OSHA;
- HSE incident-investigation guidance.

These support fact collection, multiple causes and prevention-oriented investigation.

---

## Product Safety

Applicable current European product-safety requirements may include Regulation (EU) 2023/988.

Legal/product-safety applicability and reporting duties require qualified human/Legal review.

---

# 41. Source Capture

For important external/official sources record:

- issuer;
- title;
- identifier;
- revision;
- publication/effective date;
- status;
- URL;
- access date;
- licensed-copy location;
- applicability decision.

Generic web examples and vendor imagery are discovery/comparison aids only.

---

# 42. Quality Rules

Always:

- preserve evidence provenance;
- distinguish fact from interpretation;
- maintain competing hypotheses;
- use discriminating tests;
- expose uncertainty;
- separate primary and secondary damage;
- distinguish mechanism from cause;
- preserve alternative explanations;
- use no-blame human-factor analysis;
- tie corrective actions to supported causes.

Never:

- fabricate evidence;
- alter adverse evidence;
- conceal conflicts;
- tune models solely to prove a preferred theory;
- infer intent;
- blame individuals without evidence;
- claim a cause is proven merely because a repair worked;
- claim FEA alone proves historical causation;
- destroy evidence without appropriate authority.

The objective is a defensible technical explanation, not a convenient narrative.