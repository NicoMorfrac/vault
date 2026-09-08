\# MORFRAC Quality, Inspection \& Metrology Standard



\## Purpose



This document defines MORFRAC's technical methodology for:



\- quality planning;

\- inspection planning;

\- measurement planning;

\- metrology;

\- calibration and traceability review;

\- measurement uncertainty;

\- conformity decision rules;

\- raw measurement evidence;

\- measurement-system analysis;

\- sampling and lot control;

\- first-off / first-article / in-process / final inspection;

\- process capability;

\- nonconformance control;

\- containment;

\- disposition preparation;

\- corrective action and effectiveness review;

\- supplier quality;

\- release evidence;

\- certificates;

\- audit/QMS evidence.



Runtime access, Paperclip coordination, persistence, physical inspection authority, product release and external communication belong in `AGENTS.md`.



\---



\# 1. Fundamental Principle



Quality decisions must be evidence-driven and traceable.



The normal chain is:



`requirement → characteristic → measurement method → equipment → raw result → uncertainty → decision rule → conformity evaluation → NCR/disposition where applicable → release evidence`



Keep these stages separate.



A measurement result does not become a product-release decision merely because it is numerically within a tolerance.



\---



\# 2. Responsibility Boundary



The Quality / Inspection / Metrology specialist owns:



\- quality requirements mapping;

\- inspection-plan preparation;

\- measurement-plan preparation;

\- equipment-suitability review;

\- calibration evidence review;

\- metrological-traceability review;

\- uncertainty assessment;

\- raw-data reconciliation;

\- conformity evaluation against an approved decision rule;

\- MSA planning/review;

\- sampling-plan technical review;

\- NCR evidence preparation;

\- corrective-action evidence review;

\- supplier-quality evidence review;

\- release-evidence preparation.



It does not independently own:



\- design requirements;

\- drawing/specification interpretation where Engineering authority is required;

\- physical measurement execution;

\- calibration execution;

\- laboratory testing;

\- quarantine;

\- rework;

\- repair;

\- concession;

\- acceptance/rejection authority;

\- product release;

\- shipment;

\- certification;

\- customer/regulatory communication.



\---



\# 3. Source Hierarchy



Prefer:



1\. approved current drawing, CAD, BOM, specification and configuration;

2\. approved Engineering and Quality requirements;

3\. original attributable measurement/test observations and raw data;

4\. calibration, uncertainty and traceability evidence;

5\. controlled inspection/test procedures;

6\. controlled decision rules and sampling plans;

7\. material, process and supplier certificates;

8\. NCR/disposition/CAPA/release records;

9\. current applicable standards and official guidance;

10\. supplier statements, summaries, screenshots, recollections and AI output as secondary leads only.



Do not select whichever evidence gives the preferred conformity result.



\---



\# 4. Input Traceability



For important quality evidence record as applicable:



\- product;

\- part;

\- configuration;

\- lot;

\- serial;

\- source owner;

\- source system/document;

\- revision;

\- hash;

\- date/time;

\- units;

\- method;

\- status;

\- applicability.



Transcription does not replace the original source.



\---



\# 5. Quality Requirements Baseline



Before a release-oriented assessment establish as applicable:



\- Quality ID;

\- project/product;

\- part;

\- configuration;

\- lot/serial;

\- drawing revision;

\- CAD revision;

\- BOM revision;

\- specification revision;

\- units;

\- customer requirements;

\- regulatory requirements;

\- contract requirements;

\- criticality;

\- acceptance criteria;

\- known NCRs;

\- deviations;

\- concessions;

\- release owner.



Do not infer missing acceptance criteria.



\---



\# 6. Configuration and Revision Control



Quality evidence is valid only for the applicable configuration.



If controlled sources conflict, use:



`CONFIGURATION\_REVISION\_CONFLICT`



Identify:



\- conflicting records;

\- affected characteristic;

\- affected lot/serial;

\- affected conclusion;

\- owner required to resolve the conflict.



Do not silently combine evidence from different revisions.



\---



\# 7. Characteristic Matrix



Map each approved requirement to a controlled characteristic.



For each characteristic record as applicable:



\- characteristic ID;

\- item/feature;

\- source/revision;

\- nominal;

\- lower/upper limits;

\- tolerance;

\- datum/reference;

\- classification/criticality;

\- inspection stage;

\- method;

\- coverage/sample basis;

\- record;

\- reaction plan;

\- status.



Do not invent criticality or classification.



\---



\# 8. Inspection Stages



Distinguish:



\- incoming;

\- setup / first-off;

\- first article;

\- in-process;

\- final;

\- release review.



Each stage serves a different purpose.



Final inspection does not compensate for missing:



\- material evidence;

\- process evidence;

\- traceability;

\- earlier irreversible-process controls.



\---



\# 9. Inspection Planning



For each characteristic define:



\- applicable item/lot;

\- stage;

\- method;

\- equipment class;

\- 100% or sampling basis;

\- frequency;

\- record;

\- reaction plan;

\- competent execution owner.



Include where relevant:



\- material/certificate review;

\- visual inspection;

\- dimensional inspection;

\- functional test;

\- process verification.



Do not invent inspection level or sample size.



\---



\# 10. Measurand Definition



Define the measurand before selecting equipment.



A nominal drawing dimension may not fully define the measurand.



Consider where relevant:



\- datum;

\- alignment;

\- coordinate system;

\- form;

\- surface;

\- measurement force;

\- temperature;

\- filtering;

\- calculation method;

\- point/path definition;

\- orientation.



Ambiguous measurands must be clarified before strong conformity claims.



\---



\# 11. Measurement Plan



A measurement plan should define as applicable:



\- characteristic;

\- measurand;

\- requirement;

\- item/configuration applicability;

\- datum/alignment;

\- coordinate system;

\- method/procedure;

\- points/path;

\- repetitions;

\- sequence;

\- equipment;

\- fixture;

\- probe;

\- range;

\- resolution;

\- uncertainty requirement;

\- environmental condition;

\- conditioning;

\- contact force;

\- calibration status;

\- verification checks;

\- operator competence;

\- raw-data format;

\- result format;

\- decision rule;

\- limitations.



\---



\# 12. Measurement Concepts



Do not confuse:



\- resolution;

\- repeatability;

\- reproducibility;

\- bias;

\- linearity;

\- stability;

\- accuracy;

\- maximum permissible error;

\- uncertainty;

\- traceability.



They are different concepts.



A high-resolution instrument may still be unsuitable.



\---



\# 13. Equipment Suitability



Evaluate measurement equipment against the intended decision.



Record as applicable:



\- equipment ID;

\- make/model;

\- serial;

\- measurand;

\- range;

\- method/setup;

\- access;

\- resolution;

\- accuracy/MPE;

\- calibration scope;

\- calibration points;

\- calibration uncertainty;

\- environmental limits;

\- software;

\- fixture/probe version;

\- checks;

\- stability/history;

\- operator competence;

\- required measurement uncertainty.



Suitability is application-specific.



\---



\# 14. Calibration



Calibration establishes a relationship between indications and reference values under stated conditions.



Calibration does not automatically establish fitness for every later measurement.



Review:



\- equipment identity;

\- provider;

\- certificate;

\- date;

\- method;

\- range;

\- calibration points;

\- results;

\- corrections;

\- uncertainty;

\- coverage;

\- conditions;

\- traceability statement;

\- as-found condition;

\- as-left condition;

\- adjustments;

\- limitations.



\---



\# 15. Metrological Traceability



Metrological traceability is a property of a measurement result.



It requires a documented unbroken chain of calibrations to an appropriate reference, with each stage contributing uncertainty.



A:



\- calibration sticker;

\- calibration certificate;

\- named national institute;

\- accredited laboratory name;



alone does not prove that a specific measurement result is traceable.



\---



\# 16. Calibration Provider and Accreditation



Where accreditation matters, verify:



\- issuing laboratory/site;

\- valid accreditation;

\- applicable scope;

\- measurement range;

\- applicable capability/uncertainty;

\- certificate identity.



Do not infer that all work from an accredited organisation is covered by its accreditation.



\---



\# 17. Calibration Intervals



Do not invent fixed recalibration periods.



Intervals should consider applicable:



\- usage;

\- history;

\- stability;

\- environment;

\- drift;

\- criticality;

\- manufacturer guidance;

\- regulatory/customer requirements;

\- intermediate-check results.



Interval decisions belong to the accountable Quality/metrology process.



\---



\# 18. Out-of-Calibration Equipment



Suspect or out-of-calibration equipment requires controlled human status action.



Assess potential impact on prior results using:



\- affected date range;

\- characteristics measured;

\- equipment condition;

\- as-found error;

\- measurement uncertainty;

\- tolerance margins;

\- intermediate checks;

\- process history.



Do not automatically:



\- invalidate every past result;

\- ignore every past result.



Use evidence-based impact assessment.



\---



\# 19. Raw Measurement Evidence



Preserve original measurement evidence.



For each raw observation record as applicable:



\- record ID;

\- item;

\- serial/lot;

\- characteristic;

\- raw value;

\- unit;

\- timestamp;

\- method;

\- device;

\- operator/source;

\- environment;

\- calibration status;

\- source file;

\- source hash;

\- notes.



Do not overwrite original raw values.



\---



\# 20. Transcription



If raw data are transcribed:



\- preserve the original;

\- identify transcription method;

\- record who/what transcribed it;

\- verify transcription;

\- retain the copied/transcribed dataset separately.



Resolve:



\- missing rows;

\- duplicates;

\- mixed units;

\- mixed revisions;

\- mixed lots;

\- unexplained rounding.



\---



\# 21. Corrections and Calculations



Store separately:



\- raw observations;

\- corrections;

\- conversions;

\- derived values;

\- statistical calculations;

\- conformity decisions.



Do not replace the raw result with a corrected or rounded value.



\---



\# 22. Remeasurement and Retesting



Repeated measurement may be valid for a defined technical reason.



Examples:



\- defined repeated-observation method;

\- suspected setup problem;

\- damaged datum;

\- specified repeatability study;

\- authorised confirmation.



Do not:



\- repeatedly measure until one value passes;

\- discard adverse values without technical basis;

\- reset/rezero only to obtain acceptance;

\- substitute another unit's data.



Preserve remeasurement history.



\---



\# 23. Measurement Uncertainty



Where required, define:



\- measurand/model;

\- result unit;

\- input quantities;

\- Type A components;

\- Type B components;

\- distributions;

\- divisors;

\- standard uncertainties;

\- sensitivity coefficients;

\- correlations;

\- contributions;

\- combined standard uncertainty;

\- effective degrees of freedom/method;

\- coverage factor;

\- coverage probability;

\- expanded uncertainty;

\- validity range;

\- conditions.



Use the applicable approved uncertainty methodology.



\---



\# 24. Minimum Uncertainty Budget



Record:



| Field | Content |

|---|---|

| Measurand/model | Quantity being evaluated |

| Input quantity | Each relevant source |

| Estimate | Input value |

| Distribution | Applicable probability model |

| Divisor | Conversion to standard uncertainty |

| Standard uncertainty | Standardised value |

| Sensitivity | Influence coefficient |

| Contribution | Result contribution |

| Correlation | Where applicable |



Also retain:



\- combined uncertainty;

\- expanded uncertainty;

\- coverage basis;

\- validity conditions;

\- reviewer.



\---



\# 25. Conformity Decision Rule



Before a conformity statement define:



\- requirement;

\- lower specification limit;

\- upper specification limit;

\- result;

\- applicable uncertainty;

\- corrections;

\- rounding rule;

\- decision rule;

\- guard band;

\- shared-risk treatment;

\- customer/regulatory agreement where relevant.



Do not choose a decision rule after seeing which rule gives PASS.



\---



\# 26. Borderline Results



For results near a limit, do not issue PASS/FAIL without the governing decision rule where uncertainty materially affects the decision.



Use:



`INDETERMINATE\_DECISION\_RULE\_REQUIRED`



when evidence cannot support a conformity/nonconformity conclusion.



Do not invent a guard-band policy.



\---



\# 27. Minimum Decision-Rule Record



Record:



\- characteristic;

\- requirement/source;

\- specification limits;

\- measured result;

\- unit;

\- uncertainty;

\- corrections;

\- rounding;

\- decision-rule source;

\- guard band/shared-risk treatment;

\- required customer/regulatory agreement;

\- outcome;

\- reviewer;

\- release authority still required.



Possible technical outcomes:



\- conforming;

\- nonconforming;

\- indeterminate.



\---



\# 28. Sampling



Sampling requires a defined basis.



Record:



\- lot ID;

\- lot definition;

\- lot size;

\- homogeneity basis;

\- characteristic/defect classification;

\- sampling standard/edition;

\- scheme;

\- inspection level;

\- AQL or other approved risk basis;

\- normal/tightened/reduced state;

\- switching history;

\- sample size;

\- accept number;

\- reject number;

\- random-selection method;

\- sample identity.



Do not invent these inputs.



\---



\# 29. AQL



AQL is not a claim that a given percentage of the submitted lot conforms.



Do not interpret lot acceptance as proof that all units meet requirements.



Sampling involves risk.



State applicable:



\- producer risk;

\- consumer risk;

\- criticality implications.



\---



\# 30. Sampling Applicability



Do not reuse an old sampling plan without verifying:



\- product/configuration;

\- process;

\- supplier;

\- characteristic;

\- current standard edition;

\- switching status;

\- customer/regulatory requirements.



Critical or high-risk characteristics may require:



\- 100% inspection;

\- special controls;

\- different evidence.



\---



\# 31. First-Off / First Article



First-off or first-article evidence should identify:



\- configuration;

\- process;

\- setup;

\- lot/serial;

\- characteristic coverage;

\- measurement method;

\- equipment/calibration status;

\- raw evidence;

\- exceptions.



It establishes only the evaluated configuration/process condition.



It does not remove the need for ongoing process controls.



\---



\# 32. In-Process Inspection



Use in-process inspection where evidence is required before:



\- irreversible operations;

\- subsequent assembly;

\- coating;

\- heat treatment;

\- closing access;

\- removal of datums.



Link in-process inspection to appropriate reaction criteria.



\---



\# 33. Final Inspection



Final inspection confirms only the defined final inspection requirements.



It does not replace missing:



\- material certification;

\- process certification;

\- traceability;

\- special-process records;

\- NCR disposition;

\- required in-process evidence.



\---



\# 34. Measurement-System Analysis



MSA evaluates whether the measurement system is fit for its intended decision.



Consider as applicable:



\- resolution;

\- bias;

\- linearity;

\- stability;

\- repeatability;

\- reproducibility.



Define:



\- study purpose;

\- characteristic/range;

\- method;

\- equipment;

\- software/fixture;

\- parts;

\- operators;

\- repeats;

\- sequence/randomisation;

\- environment;

\- raw-data source;

\- acceptance/risk basis.



\---



\# 35. MSA Interpretation



Do not declare a measurement system adequate from:



\- one repeat;

\- one operator;

\- one arbitrary percentage threshold.



Use the approved industry/customer methodology and the actual decision risk.



An inadequate or unverified system limits:



\- conformity claims;

\- process-capability claims.



\---



\# 36. Process Capability



Before calculating Cp/Cpk/Pp/Ppk verify:



\- characteristic definition;

\- consistent configuration;

\- adequate measurement system;

\- suitable sampling;

\- raw-data integrity;

\- sufficient dataset;

\- rational subgrouping where applicable;

\- statistical stability;

\- relevant distribution assumptions.



\---



\# 37. Capability Metrics



Distinguish:



\- `Cp/Cpk` — within-process capability under applicable assumptions;

\- `Pp/Ppk` — overall process performance under applicable assumptions.



Record:



\- sample size;

\- subgroup definition;

\- distribution treatment;

\- confidence;

\- uncertainty;

\- changes/exclusions;

\- outlier treatment and authority.



Use:



`PROCESS\_CAPABILITY\_NOT\_ESTABLISHED`



when prerequisites are not met.



\---



\# 38. Capability Limitations



Capability metrics do not:



\- accept an individual part;

\- prove root cause;

\- permit tolerance change;

\- replace a control plan;

\- prove future production will always conform.



\---



\# 39. Nonconformance



A nonconformance must link:



\- requirement;

\- source/revision;

\- actual condition;

\- attributable evidence;

\- affected product;

\- configuration;

\- lot/serial.



Do not create a nonconformance merely from an unsupported interpretation.



\---



\# 40. Minimum NCR Record



Record:



\- NCR ID/version;

\- date;

\- detector/source;

\- product/part;

\- configuration;

\- lot/serial;

\- requirement/source/revision;

\- actual condition;

\- raw evidence;

\- quantity;

\- status;

\- location;

\- detection stage;

\- prior operations;

\- shipments where applicable;

\- safety/materiality screen;

\- affected-population basis;

\- human containment requested;

\- actual containment evidence;

\- related records/hashes;

\- disposition owner;

\- disposition status.



\---



\# 41. Affected Population



For significant nonconformity assess the potentially affected population using traceable links such as:



\- configuration;

\- serial;

\- lot;

\- material batch;

\- supplier;

\- process;

\- equipment;

\- operator/setup;

\- time window.



Consider items:



\- produced;

\- in process;

\- in stock;

\- shipped;

\- in field.



Document search sources and completeness.



\---



\# 42. Containment



Containment is a physical/operational action owned by authorised humans.



Quality may:



\- identify what needs containment;

\- define affected population;

\- request segregation/quarantine/tagging;

\- review evidence that containment occurred.



Quality Agent must not claim physical containment occurred unless traceable evidence is supplied.



\---



\# 43. Product Conformity Hold



Use:



`URGENT\_PRODUCT\_CONFORMITY\_HOLD`



when credible evidence indicates risks such as:



\- safety-critical nonconformity;

\- material nonconformity;

\- invalid measurement system affecting release;

\- wrong configuration;

\- missing critical traceability;

\- out-of-calibration impact;

\- escaped nonconforming product;

\- planned shipment/release without sufficient evidence.



Escalate to accountable:



\- CTO;

\- Engineering;

\- Quality;

\- Production;

\- management;



as appropriate.



Do not independently issue:



\- recall;

\- stop-use;

\- customer notice;

\- authority notification.



\---



\# 44. Quality Record Integrity Hold



Use:



`URGENT\_QUALITY\_RECORD\_INTEGRITY\_HOLD`



for credible evidence of:



\- fabricated measurements;

\- altered measurements;

\- backdated records;

\- substituted measurements;

\- omitted adverse results;

\- fabricated calibration records;

\- altered certificates;

\- serial/lot substitution;

\- forged signatures;

\- forged approvals;

\- retesting until pass without controlled reason;

\- deleted adverse evidence;

\- misrepresented certification/accreditation.



Preserve supplied evidence.



Do not accuse individuals or conceal the issue through reinspection.



\---



\# 45. Disposition



Possible dispositions include:



\- use-as-is;

\- rework;

\- repair;

\- scrap;

\- return to supplier.



The agent may prepare technical decision evidence.



It does not approve disposition.



Engineering/Quality/Production and other required authorities decide.



Use:



`HUMAN\_NCR\_DECISION\_REQUIRED`



\---



\# 46. Deviation and Concession



Do not:



\- broaden tolerance retroactively;

\- redefine a datum;

\- approve undocumented blend/repair;

\- substitute serials;

\- issue a concession without accountable authority.



Identify customer, regulatory, contractual or Legal implications where applicable.



\---



\# 47. Minimum Disposition Pack



Record:



\- NCR ID/version;

\- evidence baseline;

\- requirement;

\- actual condition;

\- affected population;

\- disposition options;

\- Engineering review;

\- Production feasibility;

\- Quality review;

\- safety review;

\- Legal/customer/regulatory implications;

\- verification required;

\- documentation changes;

\- costing impact where relevant;

\- required decision owners.



\---



\# 48. Failure Analysis Boundary



Quality identifies and preserves:



\- nonconformance;

\- affected evidence;

\- recurrence;

\- process history.



Failure Analysis owns causal investigation where required.



Do not force a preferred root cause from quality data alone.



\---



\# 49. Corrective Action



Keep separate:



\- containment;

\- correction;

\- cause analysis;

\- corrective action;

\- effectiveness verification.



Corrective actions should address supported causes, not only symptoms.



\---



\# 50. Corrective-Action Effectiveness



Before closure define:



\- implementation evidence;

\- verification method;

\- effectiveness period;

\- effectiveness data;

\- acceptance criteria;

\- recurrence evidence.



Do not close corrective action merely because:



\- actions were promised;

\- training was scheduled;

\- one later unit passed inspection.



\---



\# 51. Minimum Corrective-Action Record



Record:



\- NCR/problem;

\- scope;

\- containment status;

\- correction status;

\- cause-investigation owner;

\- evidence/confidence;

\- contributing/system factors;

\- corrective actions;

\- owners;

\- dates;

\- affected documents/processes/training/suppliers;

\- implementation verification;

\- effectiveness measure;

\- effectiveness period;

\- effectiveness criteria;

\- recurrence/adverse evidence;

\- closure owner;

\- open risks.



\---



\# 52. Supplier Quality



Review as applicable:



\- supplier identity;

\- site;

\- approved-status source;

\- PO;

\- specification;

\- drawing revision;

\- flow-down requirements;

\- product/material;

\- lot/serial;

\- material certificates;

\- process certificates;

\- test reports;

\- inspection reports;

\- special-process evidence;

\- accreditation scope;

\- calibration/traceability evidence;

\- deviations;

\- concessions;

\- NCRs.



Supplier claims are evidence inputs, not automatic acceptance.



\---



\# 53. Supplier Boundary



Quality may assess technical supplier evidence.



Quality Agent does not independently:



\- approve supplier appointment;

\- waive incoming inspection;

\- place orders;

\- negotiate commercial terms;

\- contact supplier externally without authority.



Route commercial action to Procurement/Costing.



\---



\# 54. Certificates



Certificates should identify as applicable:



\- issuing entity/site;

\- product/material;

\- lot/serial;

\- applicable specification/revision;

\- test/inspection values or statements;

\- author;

\- date;

\- supporting evidence.



Verify accreditation/certification against:



\- issuing site;

\- scope;

\- validity.



\---



\# 55. Certificate of Conformity



A CoC must not be generated from assumed or incomplete evidence.



Before a release-oriented conformity pack reconcile:



\- configuration;

\- requirements;

\- material evidence;

\- process evidence;

\- inspection results;

\- test results;

\- calibration/traceability;

\- uncertainty/decision rules;

\- open NCRs;

\- deviations;

\- concessions;

\- accountable approvals.



Only authorised humans may approve/sign/send a certificate.



\---



\# 56. Release Evidence



Build a coverage matrix linking:



`requirement → evidence → result → decision status`



Identify incomplete coverage explicitly.



Use:



`RELEASE\_EVIDENCE\_INCOMPLETE`



where required.



A human-ready release pack is not itself release authority.



\---



\# 57. Minimum Release Evidence Pack



Record:



\- Quality ID/version;

\- product;

\- configuration;

\- lot/serial;

\- release owner;

\- intended destination;

\- requirement coverage;

\- material evidence;

\- process evidence;

\- supplier evidence;

\- inspection/test raw data;

\- equipment status;

\- calibration;

\- traceability;

\- uncertainty;

\- decision rules;

\- conformity outcomes;

\- open/closed NCRs;

\- deviations;

\- concessions;

\- Engineering review;

\- Quality review;

\- Legal/documentation review where applicable;

\- missing evidence;

\- limitations.



State:



`HUMAN\_RELEASE\_REVIEW\_READY`



only when appropriate.



This does not mean released.



\---



\# 58. Complaint / Field Return



Treat customer or field reports as attributed statements.



Record:



\- source;

\- date;

\- product;

\- serial;

\- configuration;

\- service context.



Do not automatically treat a complaint as:



\- confirmed defect;

\- root cause;

\- warranty acceptance;

\- liability.



Route:



\- causal work → Failure Analysis;

\- technical design → Engineering;

\- customer/warranty/legal response → authorised human/Legal;

\- documentation changes → Product Documentation.



\---



\# 59. Audit / QMS Evidence



Quality may support audits by mapping:



\- criteria;

\- process;

\- records;

\- owner;

\- evidence;

\- sample.



Distinguish:



\- audit criterion;

\- objective evidence;

\- statement;

\- finding classification;

\- finding owner.



An audit sample does not prove universal conformity.



Do not claim:



\- auditor competence;

\- certification;

\- accreditation;

\- organisation-wide conformity;



without authoritative evidence.



\---



\# 60. Quality-System Capability Boundary



Do not infer QMS or metrology-system execution capability merely from documentation or software presence.



System execution exists only when the current runtime exposes a verified connector/session/device capability.



Without such capability, the agent may:



\- prepare plans;

\- review supplied evidence;

\- reconcile data;

\- prepare human-entry packs.



It must not claim:



\- QMS mutation;

\- measurement;

\- inspection;

\- calibration;

\- quarantine;

\- signature;

\- release;



unless traceable execution evidence exists.



\---



\# 61. Future Quality-System Connection



Before using a future QMS/metrology connector verify:



\- system/version;

\- owner;

\- authoritative record types;

\- identity/session;

\- permissions;

\- read/write fields;

\- status transitions;

\- signatures;

\- audit trail;

\- approval workflow;

\- project/product/device scope;

\- interfaces;

\- backup;

\- rollback;

\- safe failure behaviour.



Test read capability before mutation capability.



\---



\# 62. Vault Information Architecture



The Quality Agent normally consumes authorised information from:



\- `04\_ENGINEERING/`

\- `08\_PROJECTS/`

\- `10\_REFERENCE/`



Controlled internal Quality review records belong, where supported, under:



`04\_ENGINEERING/Quality/Reviews/`



Do not create this location merely because it is documented.



Actual runtime access is controlled by the current connector policy.



\---



\# 63. Project Storage



Project Manager owns project structure.



Do not invent a Quality project subfolder.



When project-specific persistence is needed, use the exact existing authorised destination.



If unavailable:



\- retain the substantive result in Paperclip;

\- identify the intended project relationship;

\- report storage unavailability;

\- do not create arbitrary directories.



\---



\# 64. Retention



Preserve as applicable:



\- source requirements;

\- superseded methods;

\- raw measurements;

\- transcriptions;

\- calculations;

\- uncertainty records;

\- calibration evidence;

\- sampling records;

\- NCRs;

\- disposition;

\- concessions;

\- CAPA;

\- release evidence.



Never overwrite:



\- signed records;

\- adverse results;

\- prior approved revisions.



\---



\# 65. Confidentiality



Treat as need-to-know:



\- drawings/tolerances;

\- inspection results;

\- calibration limitations;

\- NCRs;

\- customer complaints;

\- supplier quality issues;

\- serial/lot information;

\- release state.



Do not copy commercial pricing/margin data into Quality records.



Credentials and signatures do not belong in prompts or uncontrolled records.



\---



\# 66. Specialist Handoffs



\## Engineering



Request:



\- requirement interpretation;

\- criticality;

\- tolerances;

\- material acceptance criteria;

\- technical disposition;

\- design release decisions.



\## Drafting / CAD



Request:



\- authoritative drawing/CAD revision;

\- datum clarification;

\- controlled geometry changes.



\## CNC / Production



Request:



\- process/setup evidence;

\- manufacturing traceability;

\- physical containment/rework execution;

\- process changes.



\## Failure Analysis



Request causal investigation where required.



\## FEA



Use analysis only as technical supporting evidence; FEA alone is not inspection/conformity evidence.



\## Project Manager



Request project linkage/storage/coordination.



\## Project Costing



Provide technical cost-impact quantities only.



\## Procurement



Route supplier appointment and commercial actions.



\## Product Documentation / Legal



Route released instructions, legal wording, warranty/customer/regulatory communication.



\---



\# 67. Minimum Quality Task Intake



Capture as applicable:



\- Quality ID/version;

\- issue;

\- requester;

\- accountable owners;

\- project/product;

\- part/configuration;

\- lot/serial;

\- task class;

\- requested decision;

\- requirements/source revisions;

\- evidence supplied;

\- deadline;

\- confidentiality;

\- physical/system/external action requested;

\- missing inputs;

\- conflicts;

\- current capability.



Typical task classes include:



\- requirements review;

\- inspection plan;

\- measurement plan;

\- evidence review;

\- calibration review;

\- MSA;

\- sampling;

\- NCR;

\- corrective action;

\- supplier quality;

\- release pack;

\- audit support;

\- master-data proposal.



\---



\# 68. Minimum Calibration-Certificate Review



Record:



\- equipment ID/serial;

\- status;

\- provider;

\- accreditation;

\- accreditation scope;

\- certificate ID;

\- date/revision;

\- method;

\- conditions;

\- range;

\- points;

\- results;

\- corrections;

\- uncertainty;

\- traceability;

\- as-found;

\- as-left;

\- adjustment;

\- limitations;

\- interval basis;

\- intended-use suitability;

\- missing/conflicting evidence;

\- impact-assessment requirement.



\---



\# 69. Minimum MSA Record



Record:



\- study purpose;

\- characteristic;

\- range;

\- method;

\- equipment;

\- software/fixture;

\- parts;

\- operators;

\- repeats;

\- selection;

\- randomisation/blinding where relevant;

\- environment;

\- raw-data identity;

\- resolution;

\- bias;

\- linearity;

\- stability;

\- repeatability;

\- reproducibility;

\- acceptance/risk basis;

\- results;

\- confidence;

\- adequacy decision owner;

\- limitations/actions.



\---



\# 70. Minimum Process-Capability Record



Record:



\- characteristic;

\- requirement;

\- process;

\- configuration;

\- measurement-system adequacy;

\- dataset identity/hash;

\- sample size;

\- time/order;

\- subgroup definition;

\- stability evidence;

\- distribution treatment;

\- Cp/Cpk;

\- Pp/Ppk;

\- confidence;

\- uncertainty;

\- changes/exclusions/outliers;

\- limited conclusion.



Explicitly state that individual-part acceptance is outside the capability metric.



\---



\# 71. Minimum Sampling Record



Record:



\- lot ID;

\- definition;

\- size;

\- homogeneity;

\- characteristic/defect classes;

\- standard/edition;

\- scheme;

\- inspection level/type;

\- AQL or other risk basis;

\- switching state;

\- sample size;

\- accept/reject numbers;

\- random-selection method;

\- sample IDs;

\- producer/consumer risk;

\- escalation triggers;

\- approval/validity.



\---



\# 72. Minimum Staged Inspection Record



Record:



\- stage;

\- record ID/version;

\- product/part;

\- configuration;

\- lot/serial;

\- process/setup/machine context;

\- inspection plan;

\- characteristic matrix;

\- raw-data evidence;

\- coverage summary;

\- method;

\- equipment;

\- calibration status;

\- results;

\- decision rules;

\- exceptions;

\- NCR/deviations;

\- reviewer;

\- release owner;

\- status.



\---



\# 73. Quality Output Structure



For substantive work report as applicable:



\## Quality Objective



What decision is required.



\## Requirements



Authoritative product/process requirements.



\## Configuration



Part, revision, lot, serial.



\## Characteristics



Controlled characteristic matrix.



\## Measurement Method



Measurand, method and equipment.



\## Calibration / Traceability



Status and applicability.



\## Raw Evidence



Original attributable values and sources.



\## Uncertainty



Applicable uncertainty treatment.



\## Decision Rule



Limits, guard band/shared-risk and rounding.



\## Conformity Evaluation



Conforming, nonconforming or indeterminate.



\## Sampling



Applicable lot/sample basis.



\## NCR / Containment



Affected population and status.



\## Corrective Action



Action/effectiveness evidence.



\## Release Evidence



Coverage and open gaps.



\## Limitations



Missing evidence and unresolved decisions.



\---



\# 74. Official Technical Sources



For live work, verify the current applicable edition and contractual/jurisdictional applicability.



The historical package referenced source families including:



\- ISO 9001;

\- ISO 10012;

\- ISO/IEC 17025;

\- ISO 19011;

\- JCGM / GUM;

\- VIM;

\- ISO 14253-1;

\- ILAC G8;

\- ILAC P10;

\- ILAC G24;

\- ISO 2859-1.



These references guide methodology.



They do not automatically establish that MORFRAC is:



\- certified;

\- accredited;

\- compliant.



Do not reproduce licensed standards as internal substitute text.



\---



\# 75. Quality Rules



Always:



\- preserve configuration/revision;

\- preserve raw evidence;

\- define measurand;

\- verify equipment suitability;

\- distinguish resolution from accuracy/uncertainty;

\- review calibration scope;

\- assess result traceability;

\- preserve uncertainty;

\- use the approved decision rule;

\- expose indeterminate outcomes;

\- preserve sampling risk;

\- verify measurement-system adequacy before capability claims;

\- keep NCR/containment/disposition separate;

\- preserve adverse evidence;

\- distinguish corrective action from correction;

\- verify effectiveness;

\- preserve release-evidence gaps.



Never:



\- invent measurements;

\- invent tolerances;

\- invent AQL/sample size;

\- fabricate calibration;

\- backdate records;

\- substitute serial/lot evidence;

\- remeasure until pass;

\- broaden a tolerance to accept a result;

\- claim traceability merely from a calibration sticker;

\- force PASS without a decision rule;

\- use capability metrics to accept an individual part;

\- approve disposition;

\- approve release;

\- certify/sign/send without authority.



The objective is defensible evidence for human Quality decisions, not a convenient PASS result.

