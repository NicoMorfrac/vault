\# MORFRAC FEA Standard



\## Purpose



This file defines the technical methodology for finite-element analysis performed or reviewed by the MORFRAC FEA Expert Agent.



It covers:



\- analysis requirements;

\- model idealisation;

\- study selection;

\- material models;

\- loads and boundary conditions;

\- contacts and connectors;

\- mesh strategy;

\- convergence;

\- singularities;

\- solver checks;

\- equilibrium;

\- result interpretation;

\- failure criteria;

\- verification;

\- validation;

\- uncertainty;

\- source traceability.



Runtime access, Paperclip coordination, persistence, approvals and external release belong in `AGENTS.md`.



\---



\# 1. Fundamental Principle



A completed solver run is not evidence that the engineering model is correct.



FEA credibility depends on the complete chain:



`requirements → geometry → idealisation → materials → loads → constraints → interactions → mesh → solver → verification → interpretation → engineering criterion`



A numerical result is useful only to the extent that this chain is appropriate and traceable.



Do not use solver completion as proof of:



\- correct geometry;

\- correct materials;

\- correct loads;

\- correct boundary conditions;

\- correct contact;

\- adequate mesh;

\- suitable study type;

\- physical realism;

\- compliance;

\- safety;

\- acceptance.



\---



\# 2. Analysis Requirements



Before building or assessing a model, define the engineering question.



Identify:



\- component/system;

\- configuration/revision;

\- decision being supported;

\- quantities of interest;

\- applicable load cases;

\- acceptance criteria;

\- required accuracy/fidelity;

\- relevant failure modes;

\- assumptions;

\- exclusions;

\- expected output.



Examples of quantities of interest include:



\- displacement;

\- reaction;

\- stress;

\- strain;

\- contact pressure;

\- bearing load;

\- connector resultant;

\- buckling factor;

\- frequency;

\- temperature;

\- fatigue quantity.



Model fidelity should be chosen to answer the engineering question, not simply to maximise model complexity.



\---



\# 3. Input Source Hierarchy



Prefer controlled and attributable engineering inputs.



\## Geometry



Use, in order of relevance:



\- approved configuration;

\- approved drawing;

\- approved BOM;

\- current CAD revision;

\- CAD-owner confirmation.



Do not assume that the geometry currently open in software is the approved geometry.



\---



\## Loads and Criteria



Use Engineering-approved:



\- loads;

\- load combinations;

\- design criteria;

\- safety factors;

\- allowable basis.



Do not derive governing design loads from software defaults.



\---



\## Materials



Use the exact authorised material record where available.



For MORFRAC-controlled material data, use the appropriate record under:



`04\_ENGINEERING/Materials/`



Record, where relevant:



\- alloy/grade;

\- condition;

\- heat treatment;

\- temperature;

\- orientation;

\- batch;

\- statistical basis;

\- allowable basis;

\- constitutive model.



Software libraries, vendor libraries, handbooks, standards, supplier datasheets and web material values are not automatically MORFRAC-approved material properties.



\---



\## Manufacturing and As-Built Inputs



Use applicable:



\- Quality records;

\- CNC/manufacturing evidence;

\- inspection results;

\- measured dimensions;

\- tolerances;

\- assembly conditions.



Nominal CAD does not automatically represent the as-built product.



\---



\# 4. Conflicting Inputs



If current authoritative sources conflict:



\- expose the conflict;

\- identify the affected model inputs;

\- identify which conclusions are affected;

\- identify the accountable owner;

\- stop only the affected analysis or conclusion.



Do not choose the value that produces the preferred result.



Do not silently reconcile conflicting geometry, material or load data.



\---



\# 5. Study Selection



Choose the study type from the physics and engineering decision.



Do not choose a study merely because it is convenient or readily available.



\---



\## Linear Static



Linear static analysis generally assumes conditions compatible with:



\- linear elastic material behaviour;

\- small deformation;

\- small rotation;

\- stable load path;

\- boundary conditions compatible with linearisation;

\- contact/interactions that do not materially change state.



Review whether those assumptions are valid before relying on the result.



\---



\# 6. Nonlinearity Review



Explicitly consider whether the problem contains:



\## Geometric Nonlinearity



Examples:



\- large displacement;

\- large rotation;

\- geometric stiffness effects;

\- instability;

\- changing load path.



\## Material Nonlinearity



Examples:



\- plasticity;

\- hyperelasticity;

\- nonlinear material behaviour;

\- temperature-dependent constitutive response.



\## Contact Nonlinearity



Examples:



\- opening;

\- closing;

\- sliding;

\- friction;

\- separation;

\- changing contact area.



\## Other Nonlinear Effects



Examples:



\- preload;

\- clearance;

\- changing connector behaviour;

\- large strain;

\- nonlinear support stiffness.



If a neglected nonlinear effect could change the governing engineering conclusion, use:



\- sensitivity analysis;

\- a higher-fidelity method;

\- or an explicitly qualified limitation.



\---



\# 7. Other Study Families



Different study types answer different engineering questions.



Do not treat the results as interchangeable.



Examples include:



\- static;

\- nonlinear;

\- eigenvalue buckling;

\- modal;

\- dynamic;

\- thermal;

\- coupled;

\- fatigue.



For example:



\- an eigenvalue buckling result is not a nonlinear collapse load;

\- a modal frequency is not a dynamic response amplitude;

\- a static stress result is not automatically a fatigue assessment.



State the physical question answered by each study.



\---



\# 8. Model Idealisation



Every simplification must preserve the physics relevant to the requested quantities of interest.



Document significant idealisations such as:



\- omitted geometry;

\- symmetry;

\- rigid regions;

\- shell representation;

\- beam representation;

\- connector representation;

\- remote loads;

\- simplified fasteners;

\- simplified contact;

\- suppressed features;

\- idealised supports.



Assess whether each idealisation could materially affect:



\- stiffness;

\- load path;

\- local stress;

\- contact;

\- stability;

\- reaction distribution;

\- governing failure mode.



\---



\# 9. Boundary Conditions



Boundary conditions must represent the physical restraint realistically enough for the engineering question.



Avoid arbitrary rigid constraints merely to eliminate rigid-body motion.



Review:



\- constrained translations;

\- constrained rotations;

\- symmetry conditions;

\- remote constraints;

\- elastic supports;

\- fixture stiffness;

\- support location;

\- real load-transfer path.



Over-constraining can:



\- artificially increase stiffness;

\- redistribute load;

\- suppress deformation;

\- generate artificial local peaks.



Under-constraining can:



\- create rigid modes;

\- disconnect load paths;

\- make the model unstable.



\---



\# 10. Contacts and Interfaces



Inventory all significant interfaces.



For each interface define the intended physical behaviour.



Examples:



\- bonded;

\- no penetration;

\- frictional;

\- frictionless;

\- separation;

\- sliding;

\- connector;

\- bearing;

\- bolt;

\- spring;

\- rigid link.



Automatic or broad bonded contact can create false load paths.



Missing or inappropriate contact can disconnect components or transfer load incorrectly.



\---



\# 11. Contact Definition



Where relevant record:



\- initial gap;

\- interference;

\- contact offset;

\- friction coefficient;

\- stabilization;

\- preload;

\- contact stiffness assumptions;

\- expected contact state.



After solution, review:



\- active contact area;

\- contact opening;

\- slip;

\- penetration;

\- contact pressure;

\- resultant interface forces.



A converged contact solution is not sufficient by itself; the resulting contact state must be physically credible.



\---



\# 12. Connectors



For connectors such as:



\- bolts;

\- pins;

\- springs;

\- bearings;

\- rigid links;

\- remote connectors;



document, where relevant:



\- geometry;

\- stiffness;

\- preload;

\- degrees of freedom;

\- load-transfer assumption;

\- connector reference location;

\- expected resultants.



Review connector resultants as part of the overall equilibrium and load-path assessment.



\---



\# 13. Numerical Stabilisation



Numerical devices can have physical consequences.



Examples include:



\- soft springs;

\- inertia relief;

\- contact stabilisation;

\- artificial damping;

\- ignored clearance;

\- numerical stiffness.



Do not use them merely to force solution completion.



When used:



\- disclose them;

\- quantify their contribution where possible;

\- assess sensitivity;

\- confirm that they do not control the governing result.



\---



\# 14. Mesh Strategy



Mesh adequacy is specific to:



\- quantity of interest;

\- location;

\- geometry;

\- element formulation;

\- physics.



A mesh acceptable for global displacement may be inadequate for local stress or contact pressure.



Record:



\- element type;

\- formulation;

\- order;

\- global size;

\- local controls;

\- quality metrics;

\- node count;

\- element count;

\- DOF count.



Use local refinement where justified by:



\- geometry;

\- load introduction;

\- contact;

\- stress gradients;

\- quantity of interest.



\---



\# 15. Mesh Convergence



Use a planned refinement sequence or justified adaptive evidence.



When comparing refinements:



\- keep the same physical model;

\- keep the same boundary conditions;

\- keep the same loading;

\- keep the same extraction method.



Assess convergence of relevant quantities.



Examples:



\- global displacement;

\- reaction;

\- strain energy;

\- non-singular local stress;

\- contact resultants;

\- connector loads.



A small global error estimate does not guarantee accurate local stress.



\---



\# 16. Singularities



Possible sources of mathematical stress singularity include:



\- sharp re-entrant corners;

\- point loads;

\- edge loads;

\- perfectly rigid fixtures;

\- abrupt boundary-condition changes;

\- idealised bonded edges.



A stress value that diverges with mesh refinement may be singular rather than physical.



Do not report the highest singular node as a physical material stress.



Instead:



1\. identify the likely singularity;

2\. determine whether it represents real geometry or idealisation;

3\. improve the physical representation when appropriate;

4\. use an Engineering-approved assessment method.



Depending on the application, this may involve:



\- stress away from the singular region;

\- structural stress;

\- hot-spot stress;

\- linearised stress;

\- code-specific extraction;

\- revised geometry/load introduction.



The extraction method must match the engineering failure criterion.



\---



\# 17. Solver Controls



Retain and review:



\- solver errors;

\- warnings;

\- rigid modes;

\- iteration history;

\- convergence history;

\- stabilisation;

\- completed steps;

\- stale-result status.



Do not change:



\- tolerances;

\- iterations;

\- convergence controls;

\- stabilisation;



merely to obtain a completed run.



Changes to solver controls require a numerical and physical justification.



\---



\# 18. Equilibrium



Check global equilibrium where applicable.



Compare:



\- applied forces;

\- reacted forces;

\- applied moments;

\- reacted moments.



Also review:



\- contact resultants;

\- connector resultants;

\- expected load path;

\- expected rigid motion.



A significant unexplained imbalance requires investigation.



\---



\# 19. Energy and Work



Where appropriate to the formulation, review:



\- strain energy;

\- external work;

\- artificial/stabilisation energy;

\- kinetic energy;

\- contact work;

\- other applicable energy measures.



Unexpected energy behaviour may indicate:



\- numerical instability;

\- incorrect constraints;

\- inappropriate stabilisation;

\- contact problems;

\- dynamic effects;

\- modelling errors.



Energy checks supplement but do not replace equilibrium and physical review.



\---



\# 20. Deformed Shape



Always inspect the deformed shape.



Use it to assess:



\- load path;

\- deformation direction;

\- support behaviour;

\- interface behaviour;

\- unexpected rigid motion;

\- unrealistic stiffness;

\- unexpected penetration/separation.



Plot deformation scale must be disclosed.



A highly exaggerated plot must not be presented as physical deformation magnitude.



\---



\# 21. Result Definition



For governing results state:



\- physical quantity;

\- tensor component/invariant;

\- units;

\- coordinate system;

\- entity;

\- location;

\- nodal/element basis;

\- averaging;

\- deformation scale;

\- plot range;

\- extraction method.



Where important, retain numerical result extracts at:



\- governing points;

\- paths;

\- sections;

\- interfaces.



Do not rely solely on colour plots.



\---



\# 22. Stress Interpretation



Do not assume von Mises stress governs every material or failure mode.



Von Mises stress may be appropriate for ductile isotropic yielding.



It does not universally govern:



\- brittle fracture;

\- composites;

\- adhesives;

\- welds;

\- contact;

\- fatigue;

\- buckling;

\- serviceability;

\- bearing;

\- connector/fastener failure.



Select the criterion according to the material, structure and failure mode.



\---



\# 23. Failure Modes



Separate the relevant failure/acceptance modes.



Examples:



\- yield;

\- ultimate;

\- fatigue;

\- buckling/stability;

\- deflection/serviceability;

\- bearing;

\- contact;

\- fastener;

\- connector;

\- adhesive;

\- composite;

\- weld;

\- thermal.



Apply Engineering-approved:



\- material allowables;

\- design factors;

\- safety factors;

\- acceptance criteria;



consistently with the load basis.



\---



\# 24. PASS / FAIL Language



A FEA result may only be described as `PASS` for:



\- the supplied configuration;

\- the evaluated load cases;

\- the evaluated failure modes;

\- the applied criteria;

\- the stated assumptions.



Do not generalise a PASS beyond the analysed scope.



If a governing criterion is missing:



`PASS/FAIL NOT ASSESSED`



is preferable to inventing an allowable.



\---



\# 25. Verification



Verification asks whether the numerical problem was solved correctly.



Relevant checks can include:



\- unit checks;

\- dimensional checks;

\- hand calculations;

\- simplified analytical solutions;

\- benchmark problems;

\- mesh convergence;

\- iteration convergence;

\- equilibrium;

\- independent implementation review.



Code verification is primarily supported by:



\- software developer evidence;

\- recognised benchmarks;

\- independent benchmark testing.



A benchmark pass does not automatically validate a product model.



\---



\# 26. Validation



Validation asks whether the model sufficiently represents physical reality for its intended use.



Use independent physical evidence where available.



Examples:



\- component tests;

\- coupon tests;

\- prototype tests;

\- strain measurements;

\- displacement measurements;

\- load tests;

\- service evidence.



Calibration is not independent validation.



If parameters were fitted to test data, distinguish that calibration data from independent validation data.



\---



\# 27. Validation Domain



A validated model is only credible within the domain supported by the validation evidence.



Consider:



\- geometry;

\- material;

\- load;

\- boundary condition;

\- temperature;

\- manufacturing condition;

\- failure mode.



Do not claim validation outside the supported application domain.



\---



\# 28. Uncertainty



Track relevant uncertainty sources separately.



\## Input Uncertainty



Examples:



\- dimensions;

\- loads;

\- material properties;

\- friction;

\- preload.



\## Numerical Uncertainty



Examples:



\- mesh;

\- solver tolerance;

\- timestep;

\- iteration.



\## Model-Form Uncertainty



Examples:



\- idealisation;

\- contact simplification;

\- material law;

\- omitted physics.



\## Experimental Uncertainty



Examples:



\- measurement error;

\- fixture variation;

\- sample variation;

\- load uncertainty.



Do not collapse fundamentally different uncertainty sources into one unexplained factor.



\---



\# 29. Sensitivity



Use sensitivity analysis to identify assumptions that materially influence the decision.



Useful variables may include:



\- loads;

\- material properties;

\- contact friction;

\- support stiffness;

\- preload;

\- geometry;

\- mesh density;

\- clearances.



A model whose conclusion changes materially under plausible input variation requires that dependency to be clearly reported.



\---



\# 30. Software Capability Boundary



Software capability and installation status must be verified before relying on automated execution.



For any live solver workflow confirm, where applicable:



\- software;

\- version/service pack;

\- licence tier;

\- required study capability;

\- authorised user/session;

\- Simulation/add-in availability;

\- CAD reference resolution;

\- units/templates;

\- working-copy controls;

\- PDM/PLM behaviour;

\- result location;

\- compute resources;

\- crash/retry behaviour;

\- backup/rollback.



Do not assume capability based only on documentation.



Validate a new or changed execution environment with a non-production benchmark before relying on it for project work.



\---



\# 31. Software Defaults



Software defaults and automated advisers are not engineering decisions.



Review defaults affecting:



\- material;

\- contact;

\- fixtures;

\- mesh;

\- solver;

\- stabilisation;

\- large displacement;

\- convergence;

\- result averaging.



Record significant defaults that affect the model.



\---



\# 32. Official Technical Sources



For live analyses, re-open and verify current applicable sources.



Historical source baseline captured 2026-08-30 included:



\## SOLIDWORKS Simulation



\- fundamentals and study families;

\- study tree/input traceability;

\- static analysis;

\- adaptive h/p methods;

\- contact analysis;

\- contact stabilisation;

\- large-displacement solution;

\- stress hot-spot/singularity tools;

\- solver messages;

\- reporting.



Official SOLIDWORKS Help:



`https://help.solidworks.com/`



Documentation confirms software behaviour and capability.



It does not validate a MORFRAC model.



\---



\## Verification / Validation



Relevant reference families include:



\- ASME V\&V / VVUQ standards;

\- NAFEMS benchmark resources;

\- NASA FEMCI finite-element modelling/checking resources.



Engineering must select the applicable current standard or benchmark.



Do not reproduce or treat summaries as substitutes for licensed standards.



\---



\# 33. Source Capture



For important technical sources record:



\- issuer;

\- title;

\- version;

\- publication/status date;

\- URL or controlled location;

\- access date;

\- applicability;

\- relevant assumptions/defaults.



Vendor tutorials and screenshots are examples, not authoritative project inputs unless specifically accepted for that purpose.



\---



\# 34. Minimum FEA Output



A substantive FEA assessment should normally identify:



\## Problem



\- engineering question;

\- decision supported;

\- configuration.



\## Inputs



\- geometry/revision;

\- materials;

\- loads;

\- supports;

\- interfaces;

\- acceptance criteria.



\## Assumptions



\- idealisations;

\- omitted physics;

\- simplifications.



\## Model



\- study type;

\- element types;

\- contacts/connectors;

\- boundary conditions;

\- mesh;

\- solver.



\## Verification



\- equilibrium;

\- reactions;

\- convergence;

\- warnings;

\- singularities;

\- analytical checks where appropriate.



\## Results



\- governing quantities;

\- location;

\- extraction method;

\- values;

\- units.



\## Assessment



\- relevant failure modes;

\- allowable/criterion;

\- factor of safety or utilisation where applicable;

\- PASS/FAIL only for evaluated modes.



\## Limitations



\- missing inputs;

\- unsupported physics;

\- uncertainty;

\- validation status;

\- applicability limits.



\## Recommendation



\- design action;

\- additional analysis;

\- test;

\- review;

\- or evidence required.



\---



\# 35. FEA Quality Rules



Always:



\- state the engineering question;

\- preserve source traceability;

\- check model physics before interpreting plots;

\- review equilibrium;

\- check convergence for governing quantities;

\- identify singular results;

\- use appropriate failure criteria;

\- expose unsupported assumptions;

\- distinguish verification from validation;

\- report uncertainty and applicability.



Never:



\- fabricate solver results;

\- hide warnings;

\- suppress inconvenient results;

\- change model settings solely to obtain PASS;

\- report a singular peak as physical stress without justification;

\- claim validation from solver convergence alone;

\- claim certification from an FEA result;

\- generalise conclusions beyond the analysed configuration and load cases.



The objective is not to obtain a favourable numerical result.



The objective is to produce the most defensible engineering conclusion supported by the model and evidence.

