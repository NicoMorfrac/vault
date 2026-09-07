\# MORFRAC CNC Manufacturing Standard



\## Purpose



This document defines MORFRAC's technical methodology for CNC manufacturing planning, CAM preparation/review, cutting-data development, process verification and human prove-out preparation.



It applies to work including:



\- machinability assessment;

\- design-for-manufacture feedback;

\- manufacturing requirements;

\- stock and setup definition;

\- tooling;

\- workholding;

\- cutting data;

\- roughing;

\- rest machining;

\- semi-finishing;

\- finishing;

\- holemaking;

\- threading;

\- 3+2 and simultaneous multi-axis machining;

\- CAM specification and review;

\- simulation;

\- postprocessing;

\- NC-code review;

\- human prove-out preparation;

\- inspection/process planning;

\- cycle-time/resource estimation;

\- manufacturing change and deviation analysis.



This standard defines technical methodology.



Runtime access, Paperclip coordination, persistence, approval mechanics, project-folder control, physical machine authority and external release belong in `AGENTS.md`.



\---



\# 1. Fundamental Principle



CNC manufacturing is a controlled transformation from an authoritative design definition to an inspected physical component.



A plausible toolpath is not sufficient.



The chain must remain traceable:



`design requirements → manufacturing baseline → process strategy → setup/workholding → tooling → cutting data → CAM/toolpath → verification → post/NC → human prove-out → inspection → controlled production evidence`



At every stage distinguish:



\- authoritative requirements;

\- assumptions;

\- candidate process values;

\- CAM settings;

\- simulation results;

\- prove-out observations;

\- inspected production values;

\- approved master data.



Do not promote one category into another without evidence.



\---



\# 2. Responsibility Boundary



The CNC Manufacturing specialist owns manufacturing-process analysis and recommendations.



It does not own:



\- design requirements;

\- authoritative CAD geometry;

\- material specification;

\- engineering acceptance criteria;

\- design release;

\- physical machine operation;

\- machine safety approval;

\- inspection acceptance;

\- product release;

\- nonconformance disposition;

\- commercial pricing;

\- supplier appointment;

\- purchasing.



Engineering owns design intent and requirements.



Drafting/CAD owns authoritative geometry and drawing/BOM revision.



Production and authorised operators own physical machine setup and operation.



Quality/Metrology owns measurement acceptance and product conformity.



Project Costing owns commercial rates, prices, margins and supplier-commercial data.



\---



\# 3. Source Hierarchy



Use the strongest applicable evidence.



Preferred order:



1\. approved current drawing, CAD, BOM, configuration and Engineering manufacturing requirements;

2\. verified actual machine/controller documentation and measured machine capability;

3\. validated MORFRAC machine models, posts, workholding and tool-assembly records;

4\. current tool-manufacturer data for the exact cutter, grade, material and application;

5\. controlled MORFRAC prove-out and inspection evidence from a genuinely comparable process;

6\. approved specialist calculations and qualified supplier/application-engineer input;

7\. official CAM, controller and machine documentation;

8\. generic tables, old programs, public examples, screenshots, recollection and AI-generated suggestions.



Generic or historic data may generate a hypothesis or candidate.



They are not automatically approved manufacturing data.



For material inputs, record where relevant:



\- specification;

\- alloy/grade;

\- product form;

\- condition/temper;

\- heat treatment;

\- hardness;

\- certification/lot;

\- coating/scale/surface state.



Similar material names are not interchangeable.



\---



\# 4. Input Traceability



For every material process input, record as applicable:



\- value;

\- unit;

\- source;

\- source owner;

\- document/system;

\- revision or hash;

\- date;

\- configuration applicability;

\- maturity/status.



Do not select among conflicting values because one gives a preferred:



\- machining time;

\- tool life;

\- cost;

\- feed;

\- spindle speed;

\- outcome.



Resolve conflicts through the authority that owns the source field.



\---



\# 5. Manufacturing Requirements Baseline



Before a release-quality process plan, establish as applicable:



\- plan/part identifier;

\- project;

\- drawing revision;

\- CAD revision/configuration;

\- BOM revision;

\- units;

\- material specification;

\- material condition;

\- stock or near-net form;

\- quantity/lot;

\- critical features;

\- dimensional tolerances;

\- geometric tolerances;

\- datums;

\- surface finish;

\- edge condition;

\- deburring;

\- cleanliness;

\- marking;

\- inspection requirements;

\- traceability requirements;

\- delivery/process constraints;

\- acceptance criteria.



Distinguish:



\## Design Requirement



A requirement imposed by the authoritative design.



\## Manufacturing Choice



A process decision selected to satisfy the design requirement.



The manufacturing specialist may question design manufacturability but must not silently change a design requirement.



Missing material condition, design authority, critical tolerance or acceptance criterion may prevent a release-quality manufacturing plan while still allowing preliminary feasibility work.



\---



\# 6. CAD and Drawing Configuration



Verify:



\- model units;

\- model orientation;

\- configuration;

\- revision;

\- drawing-to-model agreement;

\- BOM agreement where applicable;

\- translated geometry integrity;

\- feature completeness.



Do not repair or redefine authoritative CAD silently.



If geometry is defective or conflicting, identify the exact issue and return it to Drafting/CAD or Engineering.



Manufacturing assumptions used temporarily for feasibility must remain explicit.



\---



\# 7. Stock Definition



Define:



\- stock material;

\- form;

\- nominal dimensions;

\- stock tolerance;

\- preparation condition;

\- certification/traceability;

\- machining allowance;

\- saw-cut/near-net condition;

\- surface/scale condition.



For each setup identify:



\- stock state before machining;

\- expected stock state afterward;

\- material intentionally retained;

\- sacrificial features;

\- transfer features;

\- material required for later clamping.



Rest-machining and subsequent operations must use a traceable prior stock state rather than assuming previous material removal.



\---



\# 8. Datums, WCS and Setup Planning



Explicitly distinguish:



\- design datums;

\- manufacturing datums;

\- setup datum;

\- workplane;

\- WCS;

\- origin;

\- axis directions;

\- machine offset convention.



For each setup define:



\- purpose;

\- part orientation;

\- locating scheme;

\- stock engagement;

\- clamping;

\- accessible features;

\- required transfer/reclamp;

\- tolerance consequences;

\- stock before;

\- stock after.



Review:



\- datum transfer;

\- tolerance stack;

\- re-clamp repeatability;

\- access;

\- stiffness;

\- distortion;

\- inspection opportunity.



Do not invent a WCS or stock datum when it materially affects the result.



\---



\# 9. Machine Capability



Manufacturing feasibility must consider the actual machine configuration.



Record where relevant:



\- machine ID;

\- manufacturer/model;

\- configuration;

\- travels;

\- working envelope;

\- number/type of axes;

\- kinematics;

\- rotary limits;

\- spindle interface;

\- spindle rpm range;

\- spindle power;

\- spindle torque curve;

\- feed limits;

\- rapid limits;

\- acceleration behaviour;

\- table capacity;

\- tool capacity;

\- tool-change restrictions;

\- coolant;

\- air;

\- probing;

\- precision/repeatability;

\- known limitations.



A machine model is useful only within its verified scope.



A similarly named machine is not automatically equivalent.



\---



\# 10. Controller



Record:



\- controller;

\- version;

\- installed options;

\- supported cycles;

\- coordinate behaviour;

\- rotary behaviour;

\- tool compensation capabilities;

\- probing capabilities;

\- supported codes/features;

\- known restrictions.



Do not infer controller syntax, cycles or behaviour from generic G-code knowledge where machine-specific behaviour matters.



\---



\# 11. Postprocessor Control



A production postprocessor is configuration-specific.



Record:



\- post name;

\- revision;

\- hash where controlled;

\- source;

\- machine;

\- controller;

\- machine configuration;

\- validated feature set;

\- excluded/unverified features;

\- output units;

\- workplane convention;

\- rotary convention;

\- program-number convention;

\- validation evidence.



A generic post, similarly named post or successful file generation is not production validation.



Do not hand-edit NC code to hide or work around a systematic postprocessor problem.



Correct the controlled source/process, repost and reverify.



\---



\# 12. CAM Capability



CAM execution capability exists only when the actual available runtime proves it.



Do not infer CAM capability merely because:



\- software is installed;

\- a file can be opened;

\- documentation exists;

\- screenshots exist;

\- a user describes how to click through the software.



Differentiate capability levels such as:



\- read/open;

\- edit;

\- calculate toolpath;

\- simulate;

\- machine-simulate;

\- postprocess;

\- save/export.



Before relying on executable CAM capability verify as applicable:



\- application;

\- version/build;

\- licence;

\- user/session;

\- access method;

\- API/UI/macro capability;

\- permitted paths;

\- machine models;

\- controllers;

\- validated posts;

\- tool libraries;

\- units/defaults;

\- logging;

\- backup;

\- rollback;

\- safe failure behaviour.



No CAM action should be claimed unless traceable evidence of that action exists.



\---



\# 13. Tool Assembly Definition



The tool is the complete assembly, not merely the cutter diameter.



For every operation identify as applicable:



\- tool number;

\- manufacturer;

\- product code;

\- cutter type;

\- cutting diameter at engagement;

\- corner/nose geometry;

\- insert or carbide grade;

\- coating;

\- effective tooth count;

\- flute/cutting length;

\- neck;

\- shank;

\- holder/arbor;

\- extension;

\- collet/chuck;

\- gauge length;

\- overhang/stick-out;

\- runout requirement;

\- balance requirement;

\- assembly operating limits.



Check:



\- flute exposure;

\- reach;

\- holder clearance;

\- shank clearance;

\- neck strength;

\- pullout/retention;

\- machine interface;

\- tool life/change criterion.



Tool-tip-only geometry is insufficient for collision analysis.



\---



\# 14. Cutting-Data Symbols



For metric milling:



\- `vc` = cutting speed, m/min

\- `D` = effective cutting diameter, mm

\- `n` = spindle speed, rev/min

\- `zc` = effective cutting teeth

\- `fz` = feed per tooth, mm/tooth

\- `fn` = feed per revolution, mm/rev

\- `vf` = table feed, mm/min

\- `ap` = axial depth of cut, mm

\- `ae` = radial width of cut, mm

\- `Q` = metal-removal rate, cm3/min



\---



\# 15. Basic Cutting-Data Equations



When the inputs are applicable and sourced:



Spindle speed:



`n = (vc × 1000) / (π × D)`



Table feed:



`vf = n × zc × fz`



Feed per revolution where applicable:



`fn = zc × fz`



Metal-removal rate for dimensions in mm:



`Q = (ap × ae × vf) / 1000`



Manufacturer-specific equations govern where geometry/application requires corrections.



Examples include:



\- effective cutting diameter;

\- chip-thinning correction;

\- entry-angle correction;

\- ball-nose effective diameter;

\- high-feed cutter geometry;

\- thread-milling centre-path correction.



Formulas convert valid process inputs.



They do not create safe starting data.



\---



\# 16. Cutting-Data Requirements



Before recommending production-oriented cutting data, establish as applicable:



\- exact material;

\- condition/temper;

\- hardness;

\- operation;

\- cutter;

\- cutter grade;

\- geometry;

\- effective diameter;

\- effective teeth;

\- `ap`;

\- `ae`;

\- coolant/lubrication;

\- chip evacuation;

\- machine;

\- holder;

\- overhang;

\- rigidity;

\- desired tool-life/result.



Prefer:



1\. current manufacturer application data;

2\. controlled MORFRAC comparable prove-out data.



Generic public data remain candidate data.



If essential information is missing, use:



`CUTTING\_DATA\_REQUIRED`



No number is preferable to an invented number.



\---



\# 17. Cutting-Data Verification



A calculated rpm/feed must be checked against:



\- cutter limits;

\- insert limits;

\- holder limits;

\- balance limits;

\- spindle rpm;

\- spindle torque;

\- spindle power;

\- machine feed;

\- acceleration;

\- rigidity;

\- workholding;

\- tool overhang;

\- runout;

\- expected deflection;

\- coolant;

\- chip evacuation;

\- re-cutting;

\- expected tool life;

\- surface/tolerance requirement.



Do not silently cap an impossible value to a machine maximum.



Show the conflict and reconsider the process strategy.



\---



\# 18. Cutting-Data Maturity



Label cutting values accurately.



Useful maturity categories include:



\- manufacturer start data;

\- MORFRAC technical master;

\- calculated candidate;

\- CAM input;

\- simulation input;

\- prove-out value;

\- observed production value.



A calculation is not proof of safe or capable machining.



Only controlled prove-out and inspection evidence can support promotion toward production data.



\---



\# 19. Workholding and Fixturing



Define:



\- fixture identity/revision;

\- locating scheme;

\- supports;

\- clamp locations;

\- clamp directions;

\- stock engagement;

\- tightening/preload basis;

\- cutting-force load path;

\- accessibility;

\- repeatability;

\- distortion risk;

\- thin-wall risk;

\- chip evacuation;

\- coolant access;

\- tool access;

\- collision geometry.



Review stock engagement and remaining material throughout the operation sequence.



Include in collision analysis as relevant:



\- fixture;

\- jaws;

\- clamps;

\- table;

\- machine components.



CAM verification does not prove:



\- fixture strength;

\- clamp adequacy;

\- safe operator practice.



Questionable ejection, collapse or workholding risk requires safety escalation.



\---



\# 20. Operation Sequence



Plan machining to preserve:



\- datum integrity;

\- stiffness;

\- access;

\- stock continuity;

\- inspection opportunity;

\- stability.



For each operation record:



\- sequence;

\- setup/WCS;

\- feature/surfaces;

\- purpose;

\- strategy;

\- tool;

\- stock state before;

\- allowance afterward;

\- requirement;

\- verification;

\- inspection stage;

\- status.



Explain operation dependencies and datum-transfer rationale.



Include where relevant:



\- deburring;

\- cleaning;

\- marking;

\- intermediate inspection.



\---



\# 21. Roughing



Define:



\- source stock state;

\- roughing strategy;

\- cut direction;

\- tool assembly;

\- stepdown;

\- stepover;

\- engagement;

\- entry method;

\- ramp;

\- leads;

\- links;

\- radial allowance;

\- axial allowance;

\- thin-wall controls;

\- island/slug controls;

\- chip evacuation;

\- coolant;

\- re-cutting control.



Check for:



\- unsupported plunges;

\- sudden engagement;

\- trapped slugs;

\- excessive engagement;

\- weak remaining walls;

\- chip recutting;

\- unreachable remnants.



Efficiency must not override tool, machine or workholding limits.



\---



\# 22. Rest Machining



Rest machining must reference a controlled prior material state.



Record:



\- prior toolpath/stock model;

\- revision/state;

\- threshold;

\- tool;

\- remaining-stock logic;

\- areas expected to remain.



Do not assume the previous operation removed the intended material.



\---



\# 23. Semi-Finishing



Semi-finishing may be used to:



\- regularise remaining stock;

\- reduce finishing load variation;

\- reduce deflection sensitivity;

\- stabilise surface condition;

\- prepare consistent finishing allowance.



State its purpose and remaining allowance explicitly.



\---



\# 24. Finishing



For each critical surface define:



\- requirement;

\- datum;

\- setup/WCS;

\- tool assembly;

\- strategy;

\- cutting direction;

\- prior allowance;

\- final allowance;

\- stepover;

\- stepdown;

\- cusp target where relevant;

\- compensation method;

\- deflection control;

\- runout control;

\- thermal considerations;

\- blending;

\- edge/deburr requirements;

\- inspection stage.



CAM tolerance and cusp settings are process inputs.



They are not dimensional or surface-conformity evidence.



\---



\# 25. Holemaking



For each hole verify:



\- feature reference;

\- diameter;

\- tolerance;

\- depth;

\- through/blind;

\- entry condition;

\- exit condition;

\- bottom clearance;

\- chamfer/countersink;

\- positional requirement;

\- datum;

\- material;

\- pilot/pre-drill requirement;

\- inspection method.



Possible operations include:



\- drilling;

\- reaming;

\- boring;

\- interpolation;

\- countersinking;

\- spot-facing.



Use peck/dwell strategies only when supported by the application, tooling and controller/post.



Consider:



\- chip evacuation;

\- coolant;

\- tool length;

\- breakthrough;

\- bottom clearance;

\- recovery strategy.



\---



\# 26. Threading



Record:



\- thread standard;

\- nominal size;

\- pitch;

\- class;

\- depth;

\- through/blind;

\- runout/bottom clearance;

\- positional requirement;

\- material;

\- tool;

\- process;

\- inspection/gauge.



Possible processes include:



\- tapping;

\- thread milling;

\- other controlled methods.



Do not infer machine canned-cycle syntax.



Thread-milling feed may require tool-centre-path correction according to the manufacturer/process method.



\---



\# 27. 3+2 and Multi-Axis Machining



Use multi-axis only when justified by:



\- access;

\- setup reduction;

\- surface requirement;

\- tool-length reduction;

\- process control.



Define:



\- tool-axis method;

\- orientation limits;

\- preferred configurations;

\- smoothing;

\- singularity/pole behaviour;

\- rotary limits;

\- unwind/retract strategy;

\- connection moves.



Verify:



\- full machine kinematics;

\- reachability;

\- head clearance;

\- table clearance;

\- fixture clearance;

\- stock clearance;

\- complete tool-assembly clearance;

\- rotary configuration;

\- post inverse-kinematic behaviour.



A collision-free cutter tip does not demonstrate multi-axis machine safety.



Unreachable positions, axis-limit events, configuration jumps or unverified rotary behaviour invalidate release-oriented posting/prove-out.



\---



\# 28. Toolpath Verification



Verify against authoritative geometry and the evolving stock state.



Review as applicable:



\- cutting motion;

\- leads;

\- links;

\- rapids;

\- tool changes;

\- gouges;

\- cutter collision;

\- shank collision;

\- holder collision;

\- fixture collision;

\- clamp collision;

\- table collision;

\- spindle/head collision;

\- machine self-collision;

\- axis limits;

\- reachability;

\- rotary configuration;

\- overtravel;

\- near misses;

\- engagement;

\- plunges;

\- remaining stock;

\- thin remnants;

\- unmachined regions.



Record:



\- software/version;

\- model revision;

\- stock state;

\- workplane;

\- machine model;

\- tool assemblies;

\- clearance values;

\- verification scope;

\- warnings;

\- unverified areas;

\- coverage limitations.



Never hide or delete an unsafe section merely to create a green verification state.



\---



\# 29. Simulation Limitations



Simulation is evidence within a defined model.



It is not proof of the physical machining system.



Accuracy depends on:



\- model correctness;

\- machine representation;

\- stock state;

\- fixture geometry;

\- tool assembly;

\- offsets;

\- configuration;

\- sampling;

\- software coverage.



Collision checks may operate at sampled positions and can have gaps between samples.



Tool-assembly checking may also depend on separately configured controls.



Record these limitations.



A green simulation does not prove:



\- actual machine offsets;

\- actual fixture;

\- correct tool loading;

\- guarding;

\- operator execution;

\- product conformity.



\---



\# 30. Postprocessing



Postprocessing requires:



\- exact verified toolpath set;

\- machine;

\- controller;

\- machine configuration;

\- validated post revision;

\- validation scope;

\- output workplane;

\- units;

\- program number;

\- operation sequence;

\- output plan.



Preserve the generated NC file and its identity/hash when controlled.



Post generation alone does not authorise machining.



\---



\# 31. NC-Code Review



Review generated NC as appropriate for the machine/post validation scope.



Check:



\- program/header identity;

\- units;

\- modal states;

\- WCS;

\- tool numbers;

\- tool changes;

\- length compensation;

\- radius compensation;

\- spindle commands;

\- coolant commands;

\- safe start;

\- restart behaviour;

\- canned cycles;

\- rotary motion;

\- coordinate transformations;

\- limits;

\- retracts;

\- home/end positions;

\- program end state;

\- post warnings.



Do not manually patch systemic post errors into production code.



Correct, repost and reverify.



\---



\# 32. Human Setup / Prove-Out Pack



The CNC specialist prepares a controlled pack for an authorised operator.



The pack should identify:



\- part/project/revision;

\- machine;

\- controller;

\- post;

\- NC/program hash;

\- stock;

\- fixture;

\- setup;

\- WCS/origin;

\- tool assemblies;

\- tool numbers;

\- gauge lengths;

\- offsets requiring human verification;

\- coolant;

\- probing;

\- inspection requirements;

\- CAM/NC verification summary;

\- open risks.



It should reference the actual:



\- machine manual;

\- site risk assessment;

\- local operating procedure.



Human-controlled checks should cover as applicable:



\- guards/interlocks;

\- workholding;

\- tool loading;

\- offsets;

\- machine graphics/simulation;

\- safe-run methods defined by the actual machine/site;

\- initial motion/clearance;

\- incremental inspection;

\- stop criteria.



Do not prescribe a universal:



\- override percentage;

\- clearance distance;

\- offset sequence;

\- machine prove-out sequence;



in place of the actual machine/site procedure.



\---



\# 33. Physical Machine Boundary



Only authorised trained humans may:



\- mount workpieces;

\- clamp fixtures;

\- load tools;

\- set offsets;

\- verify physical coordinates;

\- command motion;

\- perform dry/prove-out runs;

\- press Cycle Start;

\- alter controller settings;

\- inspect hazardous areas;

\- operate machinery.



The CNC specialist must never:



\- defeat guarding/interlocks;

\- command motion through unsupported means;

\- tell an untrained person to run machinery;

\- instruct someone to enter a hazardous zone.



\---



\# 34. Inspection and Process Control



Map critical characteristics to inspection.



Record:



\- characteristic;

\- drawing reference;

\- requirement;

\- datum;

\- process stage;

\- inspection method;

\- equipment;

\- resolution;

\- calibration status/owner;

\- sampling/frequency basis;

\- result location;

\- traceability;

\- reaction plan.



Possible stages include:



\- incoming;

\- in-process;

\- first-off;

\- final.



Quality/Metrology owns:



\- inspection-method approval;

\- calibrated measurement;

\- acceptance;

\- nonconformance disposition;

\- release.



CAM settings are not conformity evidence.



\---



\# 35. Compensation and Process Adjustment



Define the boundary between:



\- permitted process compensation;

\- controlled manufacturing adjustment;

\- design change.



Any geometry change that modifies authoritative design intent belongs to Engineering/CAD change control.



Do not silently compensate away an engineering nonconformance.



\---



\# 36. Process Capability



Do not claim process capability from:



\- one simulation;

\- one CAM setting;

\- one successful component;

\- theoretical toolpath tolerance.



Capability requires appropriate inspected evidence from the applicable:



\- machine;

\- process;

\- tooling;

\- workholding;

\- material;

\- setup.



Until sufficient evidence exists, state:



`PROCESS\_CAPABILITY\_NOT\_ESTABLISHED`



\---



\# 37. Change Control



A change to any of the following may invalidate downstream evidence:



\- CAD;

\- drawing/configuration;

\- material;

\- stock;

\- fixture;

\- machine;

\- controller;

\- post;

\- tool assembly;

\- cutting data;

\- operation order;

\- WCS;

\- tolerance;

\- inspection method;

\- NC code.



For each change record:



\- trigger;

\- prior revision/hash;

\- new state;

\- reason;

\- evidence;

\- affected operations;

\- safety effect;

\- quality effect;

\- cost/schedule effect;

\- required recalculation;

\- required reverification;

\- required reposting;

\- required re-prove-out.



Do not overwrite adverse evidence.



\---



\# 38. Deviations and Unexpected Results



Treat as controlled evidence:



\- scrap;

\- tool breakage;

\- unexpected wear;

\- excessive wear;

\- alarm;

\- collision;

\- near miss;

\- gouge;

\- unexpected machine behaviour;

\- out-of-tolerance result;

\- unexplained cycle-time deviation.



Preserve the before/after condition.



Do not silently change the program and erase the evidence trail.



Route as appropriate to:



\- Production;

\- Engineering;

\- Quality;

\- Failure Analysis.



Failure causation belongs to Failure Analysis where a causal investigation is required.



\---



\# 39. Machine Safety Hold



Use:



`URGENT\_MACHINE\_SAFETY\_HOLD`



when credible evidence indicates risk such as:



\- collision;

\- ejection;

\- workholding failure;

\- tool failure;

\- overspeed;

\- excessive reach/deflection;

\- unsafe rapid/link motion;

\- wrong coordinate/offset;

\- overtravel;

\- guarding/interlock bypass;

\- unsafe instruction to run machinery.



Stop affected release/prove-out work.



Preserve the technical evidence and escalate to the responsible human owners.



\---



\# 40. Process Integrity Hold



Use:



`URGENT\_CAM\_PROCESS\_INTEGRITY\_HOLD`



for credible evidence of:



\- fabricated CAM results;

\- fabricated simulation;

\- altered prove-out evidence;

\- altered inspection evidence;

\- hidden warnings;

\- hidden collisions;

\- relabelled CAD/tool/post revisions;

\- invented cutting data;

\- code alteration intended to conceal a problem;

\- deleted adverse trials;

\- forged technical approvals;

\- pressure to misrepresent capability;

\- pressure to misrepresent cycle time;

\- pressure to misrepresent conformity.



Preserve available evidence.



Do not alter source records or perform a concealed rerun merely to produce a preferred result.



\---



\# 41. Human Prove-Out Feedback



When authorised humans return prove-out evidence, capture:



\- actual machine;

\- actual setup;

\- actual tool assembly;

\- actual parameters;

\- alarms;

\- deviations;

\- observed wear;

\- machine time;

\- inspection results.



Do not silently promote a trial parameter into a technical master.



Use controlled evidence and review.



\---



\# 42. Cycle-Time Estimation



Separate:



\- CAM cutting-time estimate;

\- non-cutting movement estimate;

\- tool-change time;

\- setup;

\- programming;

\- prove-out;

\- inspection;

\- handling;

\- deburring;

\- cleaning;

\- expected tool consumption.



State:



\- source;

\- maturity;

\- assumptions;

\- uncertainty;

\- confidence/range.



CAM or simulation time is not observed production time.



Observed machine-cycle evidence should remain separately identified.



\---



\# 43. Project Costing Handoff



CNC may provide technical inputs such as:



\- machine requirement;

\- cutting-time estimate/range;

\- setup hours;

\- programming hours;

\- prove-out hours;

\- inspection hours;

\- handling/deburr hours;

\- tooling requirements;

\- fixture requirements;

\- consumables;

\- expected tool consumption;

\- quantity-related process effects;

\- uncertainty.



Project Costing owns:



\- labour rates;

\- machine rates;

\- price;

\- margin;

\- markup;

\- discounts;

\- commercial supplier records.



Do not mix confidential commercial data into CNC technical records unnecessarily.



\---



\# 44. Supplier Technical Inputs



Supplier or application-engineer information may be used as technical evidence when attributable.



Separate:



\- technical capability;

\- technical recommendation;

\- commercial quotation;

\- supplier selection.



CNC may assess technical suitability.



Procurement/commercial owners choose or appoint suppliers.



\---



\# 45. Technical Master Candidates



CNC technical master candidates may include:



\- machine capability;

\- machine model;

\- validated post identity;

\- tool assemblies;

\- fixture identity;

\- technical cutting-data application windows;

\- proven process controls;

\- manufacturing methods.



Each controlled master candidate should retain:



\- source;

\- evidence;

\- owner;

\- status;

\- effective date;

\- history;

\- applicability limits.



Do not mix into CNC masters:



\- prices;

\- discounts;

\- margins;

\- confidential supplier-commercial terms.



\---



\# 46. Confidentiality



Treat as need-to-know:



\- unreleased CAD;

\- drawings;

\- tolerances;

\- process strategy;

\- fixtures;

\- tooling;

\- machine configuration;

\- postprocessors;

\- NC code;

\- process results;

\- supplier technical information;

\- production know-how.



Credentials do not belong in:



\- instructions;

\- reports;

\- comments;

\- technical masters.



\---



\# 47. Handoff Quality



A specialist handoff should state:



\- originating issue;

\- plan/part/version;

\- exact question;

\- required decision/input;

\- source package;

\- confidentiality scope;

\- expected return.



A handoff is a dependency.



It is not completion.



\---



\# 48. Minimum CNC Task Intake



Capture as applicable:



\- task/plan ID;

\- version;

\- originating issue;

\- requester;

\- decision owner;

\- project relationship;

\- part/configuration;

\- quantity;

\- task class;

\- objective;

\- input revisions;

\- deliverables;

\- deadline;

\- confidentiality;

\- CAM action requested;

\- machine action requested;

\- missing inputs;

\- conflicts;

\- current capability.



Typical task classes:



\- feasibility;

\- process plan;

\- cutting-data proposal;

\- CAM build specification;

\- supplied-CAM review;

\- simulation review;

\- post/NC review;

\- prove-out review;

\- process change;

\- deviation review;

\- costing handoff.



\---



\# 49. Minimum Manufacturing Baseline Record



Record:



\- plan/part/configuration/version;

\- project;

\- owners;

\- drawing/CAD/BOM revisions and hashes where used;

\- units;

\- material specification;

\- condition;

\- certification;

\- quantity/lot;

\- critical characteristics;

\- tolerances;

\- datums;

\- surface requirements;

\- edge requirements;

\- cleanliness;

\- marking;

\- stock;

\- inspection requirements;

\- traceability requirements;

\- machine/CAM capability;

\- conflicts;

\- unknowns;

\- exclusions.



\---



\# 50. Minimum CAD / Stock / Setup Record



Record:



\- authoritative CAD/drawing;

\- units;

\- translation issues;

\- stock form;

\- stock dimensions;

\- stock tolerance;

\- stock source;

\- design datums;

\- manufacturing datums;

\- setup number;

\- setup purpose;

\- workplane/WCS;

\- origin;

\- axes;

\- offset convention;

\- stock before;

\- stock after;

\- re-clamp controls;

\- datum-transfer issues;

\- access issues;

\- tolerance-stack risks.



\---



\# 51. Minimum Machine / Controller / Post Record



Record:



\- machine ID/model/configuration;

\- envelope;

\- axes/kinematics;

\- spindle interface;

\- rpm;

\- power;

\- torque;

\- feed/rapid limits;

\- table;

\- coolant;

\- probing;

\- tool capacity;

\- controller/version/options;

\- machine-model revision;

\- post revision/hash where controlled;

\- post source;

\- validated features;

\- excluded features;

\- output units;

\- workplane convention;

\- evidence owner;

\- evidence status.



\---



\# 52. Minimum Tool Assembly Record



For each tool:



\- tool number;

\- operation;

\- cutter product;

\- cutter grade;

\- effective diameter;

\- effective teeth;

\- geometry;

\- flute/cutting length;

\- shank;

\- holder/arbor;

\- extensions;

\- gauge length;

\- overhang;

\- runout requirement;

\- balance requirement where relevant;

\- source;

\- revision;

\- status.



Also record:



\- machine-interface check;

\- reach/clearance check;

\- retention/pullout check;

\- life/change criterion;

\- missing information.



\---



\# 53. Minimum Workholding Record



Record:



\- fixture identity/revision;

\- locating scheme;

\- stock engagement;

\- datums;

\- supports;

\- clamps;

\- clamp direction;

\- tightening basis;

\- cutting-force/load basis;

\- distortion risk;

\- thin-wall risk;

\- tool access;

\- chip/coolant access;

\- collision geometry;

\- repeatability/check method;

\- unknowns.



\---



\# 54. Minimum Cutting-Data Record



For each operation/tool record:



\- material;

\- condition/hardness;

\- tool;

\- grade;

\- geometry;

\- source/revision/date;

\- `ap`;

\- `ae`;

\- coolant/lubrication;

\- chip evacuation;

\- source `vc`;

\- source `fz` or `fn`;

\- effective diameter;

\- effective teeth;

\- equations;

\- unit conversions;

\- calculated rpm;

\- calculated feed;

\- calculated MRR where relevant;

\- tool limits;

\- holder limits;

\- machine rpm limit;

\- feed limit;

\- power/torque constraints;

\- rigidity risk;

\- runout risk;

\- deflection risk;

\- maturity label;

\- prove-out monitoring.



\---



\# 55. Minimum Operation Sequence Record



For each operation identify:



\- sequence;

\- setup/WCS;

\- feature;

\- purpose;

\- strategy;

\- tool;

\- stock before;

\- allowance after;

\- requirement;

\- verification;

\- inspection;

\- status.



Also record:



\- sequence rationale;

\- datum-transfer controls;

\- deburring;

\- cleaning;

\- marking;

\- open decisions.



\---



\# 56. Minimum Roughing / Rest Record



Record:



\- setup;

\- stock-model state;

\- strategy;

\- direction;

\- complete tool assembly;

\- stepdown;

\- stepover;

\- engagement;

\- ramp/entry;

\- leads/links;

\- axial allowance;

\- radial allowance;

\- rest reference;

\- rest threshold;

\- thin-wall controls;

\- island/slug controls;

\- chip/coolant controls;

\- plunge checks;

\- engagement checks;

\- residual-stock checks;

\- remaining stock for next stage.



\---



\# 57. Minimum Finishing Record



Record:



\- surface/feature;

\- requirement;

\- datum;

\- setup/WCS;

\- complete tool assembly;

\- strategy;

\- direction;

\- prior allowance;

\- final allowance;

\- stepover/stepdown;

\- cusp target;

\- compensation;

\- deflection controls;

\- runout controls;

\- thermal controls;

\- blend/edge requirements;

\- deburring;

\- inspection stage;

\- capability evidence status.



\---



\# 58. Minimum Hole / Thread Record



Record:



\- feature reference;

\- diameter/thread;

\- standard;

\- class;

\- depth;

\- through/blind;

\- entry/exit condition;

\- bottom clearance;

\- positional/datum requirement;

\- material;

\- operation chain;

\- tools;

\- cycle/strategy;

\- post dependency;

\- cutting-data source;

\- coolant;

\- chip evacuation;

\- inspection/gauge;

\- risks;

\- recovery/change-control considerations.



\---



\# 59. Minimum Multi-Axis Record



Record:



\- reason for multi-axis use;

\- operation;

\- machine model/kinematics revision;

\- setup/model location;

\- output workplane;

\- tool-axis method;

\- orientation limits;

\- preferred configurations;

\- singularity/pole handling;

\- unwind behaviour;

\- connection/rapid/retract behaviour;

\- tool clearance;

\- holder clearance;

\- fixture clearance;

\- machine clearance;

\- axis/reach evidence;

\- post inverse-kinematic validation scope;

\- remaining prove-out risks.



\---



\# 60. Minimum Simulation / Verification Record



Record:



\- CAM project/toolpath/NC identifiers;

\- hashes where controlled;

\- software/version;

\- authoritative model;

\- stock states;

\- machine model;

\- workplane;

\- tool assemblies;

\- clearance values;

\- included cutting moves;

\- leads;

\- links;

\- rapids;

\- tool changes;

\- gouge findings;

\- collision findings;

\- near misses;

\- fixture findings;

\- table/machine findings;

\- axis/reach findings;

\- configuration findings;

\- engagement/plunge findings;

\- residual-stock findings;

\- limitations;

\- evidence files/logs;

\- disposition;

\- required recheck.



\---



\# 61. Minimum Post / NC Record



Record:



\- plan/NC version;

\- source CAM/toolpath identity;

\- machine/controller/configuration;

\- post revision/hash;

\- validation scope;

\- output workplane;

\- units;

\- program number;

\- operation sequence;

\- generated NC identity/hash;

\- post messages/warnings;

\- independent review result;

\- simulation status;

\- simulation gaps;

\- release status.



Saving or reviewing an NC program does not authorise machine transfer or machining.



\---



\# 62. Minimum Human Prove-Out Pack



Record:



\- pack ID/version;

\- machine/controller/post;

\- program identity/hash;

\- part;

\- stock;

\- fixture;

\- setup;

\- WCS;

\- tool assemblies;

\- offsets requiring human verification;

\- CAM/NC verification status;

\- actual machine/site procedure references;

\- guard/interlock prerequisites;

\- workholding prerequisites;

\- tool prerequisites;

\- inspection points;

\- stop/escalation criteria;

\- deviation capture;

\- alarm capture;

\- tool-wear capture;

\- cycle-time capture;

\- actions explicitly outside agent authority.



\---



\# 63. Minimum Inspection / Process-Control Record



Record:



\- characteristic;

\- drawing requirement;

\- datums;

\- stage;

\- method;

\- equipment;

\- resolution;

\- calibration/Quality owner;

\- sampling/frequency source;

\- compensation boundary;

\- nonconformance reaction;

\- capability evidence required;

\- result location;

\- traceability.



\---



\# 64. Minimum Cycle-Time / Resource Handoff



Record:



\- plan/part;

\- quantity;

\- maturity;

\- cutting-time estimate;

\- source;

\- non-cut estimate;

\- setup hours/range;

\- programming hours/range;

\- prove-out hours/range;

\- inspection hours/range;

\- handling/deburr hours/range;

\- tooling quantity;

\- fixture requirements;

\- consumables;

\- tool-life basis;

\- machine/resource needs;

\- uncertainty;

\- confidence;

\- exclusions;

\- observed production evidence if available.



Exclude commercial values owned by Costing.



\---



\# 65. Minimum Change / Deviation Record



Record:



\- record ID;

\- date;

\- owner;

\- trigger;

\- prior revisions/hashes;

\- new/observed state;

\- reason;

\- source evidence;

\- affected setups;

\- affected toolpaths;

\- affected NC;

\- affected fixtures/tools;

\- affected inspection;

\- safety impact;

\- quality impact;

\- cost/schedule impact;

\- evidence preserved;

\- recalculation required;

\- repost required;

\- re-prove-out required;

\- review/disposition.



\---



\# 66. Technical Output Quality



A substantive CNC result should make clear:



\## Requirements



What is authoritative.



\## Capability



What machine/CAM/post capability is verified or unavailable.



\## Manufacturing Strategy



How the component is proposed to be produced.



\## Setups



Stock, datums, WCS and workholding.



\## Tools



Complete assemblies.



\## Cutting Data



Source, equations, limits and maturity.



\## Operations



Sequence and allowances.



\## Verification



CAM/simulation checks and limitations.



\## Inspection



Where product/process evidence will be established.



\## Human Prove-Out



What remains for authorised physical execution.



\## Costing Inputs



Technical time/resource ranges where requested.



\## Risks / Open Questions



Anything preventing release-quality maturity.



\---



\# 67. Official Technical Sources



For live technical work, recheck current revision and applicability.



The historical package referenced official Autodesk PowerMill documentation for:



\- setups;

\- stock;

\- workplanes;

\- machine/model location;

\- collision/gouge verification;

\- machine simulation;

\- NC program configuration;

\- postprocessing;

\- stock models/rest machining.



It also referenced Sandvik Coromant milling formulas.



These are technical references.



They do not validate MORFRAC's specific:



\- machine;

\- postprocessor;

\- tooling;

\- fixture;

\- setup;

\- cutting parameters;

\- NC output.



For operator/machine safety, the actual machine manufacturer's documentation, MORFRAC/site risk assessment and applicable jurisdiction govern.



A manual from another machine manufacturer may be illustrative only.



\---



\# 68. Source Capture



For important external technical information record:



\- issuer;

\- product/application;

\- title;

\- revision;

\- publication/status date;

\- URL or controlled source;

\- access date;

\- exact applicability;

\- affected operation/tool/material.



For tool cutting data, record enough information to confirm that the recommendation actually applies to:



\- cutter family;

\- grade;

\- geometry;

\- material group;

\- condition;

\- operation;

\- engagement.



\---



\# 69. Quality Rules



Always:



\- preserve design/configuration traceability;

\- identify material condition;

\- distinguish manufacturing choice from design requirement;

\- use the complete tool assembly;

\- source cutting data;

\- show calculation inputs and units;

\- check machine/tool/workholding limits;

\- preserve stock-state continuity;

\- verify links/rapids as well as cutting moves;

\- preserve simulation limitations;

\- bind post to exact machine/controller/configuration;

\- review NC independently;

\- require human physical prove-out;

\- require inspected evidence for capability;

\- retain adverse results and deviations;

\- separate technical and commercial information.



Never:



\- invent cutting data;

\- hide collisions;

\- suppress post warnings;

\- invent CAM execution;

\- invent physical prove-out;

\- silently change geometry;

\- silently change WCS;

\- silently change a post;

\- hand-edit systemic post errors away;

\- equate green simulation with machine safety;

\- equate CAM tolerance with conformity;

\- declare a part released from CAM evidence;

\- command machine motion;

\- bypass guards/interlocks;

\- overwrite adverse manufacturing evidence.



The objective is a traceable and producible manufacturing process whose maturity is supported by evidence, not merely a CAM file that calculates successfully.

