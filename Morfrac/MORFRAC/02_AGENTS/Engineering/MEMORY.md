\# Engineering Experience Memory



\## Purpose



This file preserves reusable engineering experience learned from completed MORFRAC work.



It is not a task tracker and is not an authoritative material database.



Paperclip remains the source for:



\- current tasks;

\- task status;

\- blockers;

\- assignments;

\- approvals;

\- handoffs.



Project reports and controlled Engineering records remain the source for the detailed calculations and evidence.



Use this memory to improve future engineering work by recalling:



\- validated findings;

\- useful design patterns;

\- observed failure modes;

\- assumptions that proved important;

\- practical engineering lessons;

\- approaches that worked well;

\- approaches that should not be repeated;

\- recurring checks that proved valuable.



\---



\# Memory Use Rules



Before relevant engineering work:



1\. Check this memory for applicable prior experience.

2\. Follow the referenced original issue/report where available.

3\. Verify that geometry, material, load case, environment and operating conditions are sufficiently comparable.

4\. Recalculate when the current case differs materially.

5\. Reverify material properties and external technical data against the current authoritative source.



Memory is supporting engineering experience, not proof.



Do not copy a historical result into a new design without checking applicability.



Do not treat historical values as current controlled master data.



\---



\# What Belongs Here



Add an entry when completed work produces a reusable lesson such as:



\- a design feature repeatedly governing stress;

\- a bearing limitation;

\- a useful sizing relationship;

\- a manufacturing constraint;

\- a failure mechanism;

\- a validated modelling approach;

\- a recurring source of error;

\- a successful verification method;

\- a useful conservative assumption;

\- a lesson from prototype, test or field experience.



Each entry should contain:



\- source issue/project;

\- original context;

\- observed result;

\- reusable lesson;

\- applicability;

\- limitations;

\- source/report reference when available.



\---



\# What Does Not Belong Here



Do not store:



\- active task status;

\- current blockers;

\- heartbeat information;

\- temporary todo lists;

\- repeated Paperclip comments;

\- approval state;

\- stale project status;

\- credentials;

\- raw logs;

\- entire reports;

\- unverified speculation presented as learned experience.



\---



\# Experience Records



\## ENG-MEM-001 — Titanium Cheek Structural Assessment



\### Source



\- Issue: MORAAAAA-13

\- Parent project/task: MORAAAAA-11

\- Date: 2026-04-29



\### Context



A titanium cheek structural assessment was performed for the evaluated sheave design and load case.



\### Observed Result



\- Peak reported stress: 38.0 MPa

\- Reported factor of safety: 23.2

\- Evaluated structural checks passed with a large margin.



\### Reusable Lesson



The evaluated cheek geometry was substantially over-strength for the analysed load case.



A significant weight-reduction opportunity was identified.



When a similar hardware component shows very high structural margin, optimisation for:



\- mass;

\- section thickness;

\- manufacturability;

\- material use;



should be considered rather than automatically retaining the oversized geometry.



\### Applicability



Reuse this lesson only as a design heuristic.



Do not reuse the reported stress or factor of safety unless the current:



\- geometry;

\- material;

\- load case;

\- constraints;

\- load introduction;



match the original analysis and the original calculation is verified.



\---



\## ENG-MEM-002 — Polymer Bearing PV Screening



\### Source



\- Issues: MORAAAAA-12 / MORAAAAA-11

\- Date: 2026-04-29



\### Context



iglidur X was considered for a sheave bearing application.



Historical project notes recorded:



\- PV reference: 1.32 MPa·m/s

\- project screening value: 0.66 MPa·m/s



\### Reusable Lesson



Polymer bearing selection must include explicit checks of:



1\. bearing pressure;

2\. sliding velocity;

3\. PV;

4\. environmental conditions;

5\. temperature;

6\. duty cycle;

7\. applicable safety margin.



Pressure and sliding velocity should be reviewed separately before evaluating PV.



A nominal material PV value alone is not sufficient to validate a bearing design.



\### Important Limitation



The original referenced material-data file is currently unavailable.



Therefore:



\- 1.32 MPa·m/s and 0.66 MPa·m/s are retained only as historical project values;

\- they are not current authoritative iglidur X properties;

\- current manufacturer data must be checked before using these values in a new calculation.



\---



\## ENG-MEM-003 — Input Sufficiency Before Calculation



\### Source



Repeated Engineering workflow experience.



\### Reusable Lesson



Before calculation, verify the critical inputs relevant to the analysis, particularly:



\- loads;

\- load direction;

\- geometry;

\- constraints/supports;

\- material;

\- units;

\- operating conditions;

\- required design criterion.



Do not silently invent missing critical inputs.



However, one missing input should not stop unrelated engineering work.



Use scoped blocking:



\- calculate what can be supported;

\- identify the affected unknown;

\- state its owner;

\- continue unaffected checks.



\### Applicability



General Engineering rule.



Also reflected in:



\- `TASK\_PATTERNS.md`

\- `SKILLS/bearing\_design.md`



\---



\# Adding New Experience



After a substantive completed project or engineering task, add a memory entry only when there is a useful lesson for future work.



Use:



\## ENG-MEM-NNN — Short Lesson Title



\### Source



\- Project:

\- Issue:

\- Report:

\- Date:



\### Context



What was being analysed or designed.



\### Observed Result



What was actually found.



\### Reusable Lesson



What future Engineering work should learn from this result.



\### Applicability



When this lesson is relevant.



\### Limitations



When it must not be reused without new verification.



\---



\# Memory Quality Rule



Prefer a small number of high-value lessons over a complete history of Engineering activity.



If an entry becomes obsolete:



\- do not silently rewrite history;

\- mark it superseded;

\- reference the newer evidence or lesson.



If a remembered lesson conflicts with current project evidence or an authoritative technical source, the current verified evidence governs.

