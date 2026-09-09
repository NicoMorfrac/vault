---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-05-24
related_findings: []
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - MECHANICAL_INTEGRATION_COMPLEXITY
  - RETROFIT_COMPLEXITY
  - SERVICEABILITY_COMPLEXITY
related_projects: []
related_reports:
  - 2026-05-24_MORAAAAA-91_rigger_and_refit_yard_workflow_bottlenecks_summary
---

# MORAAAAA-91-01 Mast-handling access and staging dependencies in rigging/refit work

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| YBW Forum | https://forums.ybw.com/threads/unstepping-a-mast.408310/ | 2014-09-15 | Owner + yard access planning discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/howto-un-step-keel-stepped-mast-without-crane.233099/ | 2010-04-01 | Mast-handling and safety discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/unstepping-a-keel-stepped-mast.595197/ | 2023-04-15 | Technical unstepping discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/remove-furler-without-dropping-the-mast-while-afloat.451161/ | 2016-03-03 | Furling service-access discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/lazy-jacks-used-furler-install-mast-down-or-up.477913/ | 2017-05-02 | Retrofit installation discussion | MEDIUM |
| Cruisers Forum | https://www.cruisersforum.com/forums/f47/unstepping-the-mast-for-low-bridges-rod-rigging-inmast-furling-214010.html | 2019-02-14 | Yard logistics and mast transport discussion | MEDIUM |

---

# INDUSTRY_SEGMENT

REFIT_YARDS

---

# PROBLEM_TYPE

INSTALLATION

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Rigging and mechanical retrofit jobs repeatedly bottleneck on mast-handling logistics rather than on the hardware itself. The recurring problem is that access mode selection `mast up`, `mast down`, `afloat`, `ashore`, crane, bucket truck, temporary halyard support, mast shed, storage stands` drives safety, sequence, labor count, and whether adjacent rigging or furling work is economically viable in the same visit.

---

# EVIDENCE

## Directly observed evidence

- In `Unstepping a Mast`, the owner is replacing standing rigging and inspecting chainplates but the yard has no mast crane, relies on a bucket-truck contractor who normally does tree work, and has no mast racks. Replies shift quickly from rigging work to crane height, insurance, control of the lift, and whether a rigger should own the risk.
- In `Howto un/step keel-stepped mast without crane?`, multiple contributors argue that the real constraint is not theoretical lifting force but controlled vertical feed through the deck collar and onto the step. The thread explicitly raises injury risk, insurance limits, crane-height constraints, and the cost of bringing in tall enough lifting gear.
- In `Unstepping a keel stepped mast`, the technical advice centers on mast-foot monitoring, wiring control, deck-partner sealing, and protecting nearby bulkheads if the mast does not come out perfectly vertical. Even routine transport preparation requires live spotters and preplanned handling details.
- In `Remove furler without dropping the mast while afloat`, a top-bearing service question turns into a mast-support procedure using halyards, shroud slackening, boom removal, and model-specific decisions about whether the foil can stay in place. A service task becomes a rig-support operation.
- In `Lazy Jacks & Used Furler Install Mast Down or Up`, contributors disagree on the preferred install mode. Some prefer mast-down work because inspection and fitting are easier on trestles; others prefer mast-up for foil handling. The same thread notes that many systems need a new forestay and exact measurements, making access-mode decisions part of scope definition.
- In the Cruisers Forum `Unstepping the mast for low bridges` discussion, contributors describe yards offering unstep, storage, and re-step services, and highlight secondary logistics such as deck overhang, mast stands, tie-downs, and canal/transport handling after the lift itself.

## Repeated pattern

- Jobs that appear to be `standing rigging renewal`, `furler bearing service`, `forestay replacement`, or `inspection` repeatedly escalate into access planning, lift-equipment procurement, temporary support strategy, and mast storage/staging work.
- The bottleneck often appears before the mechanical work starts: yards lacking mast cranes, insufficient jib height, no mast racks, no standardized stands, or uncertainty over who carries lifting liability.
- Work-scope efficiency depends on batching. Once the mast is down, owners and installers try to combine chainplate inspection, wiring, sheaves, tangs, spreaders, and furling work into the same window because repeating the access event is costly.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Difficulty scheduling rigging/refit work
- Disagreement over mast-up versus mast-down execution
- Lift delays, extra labor, and scope expansion
- Safety and liability concern around crane or temporary-support methods

## Likely root operational causes

- Key components are distributed across masthead, forestay, foil, deck partners, and mast step rather than concentrated in one serviceable module.
- Access requirements are geometry-sensitive: tall spars, double spreaders, keel-stepped masts, and long foil extrusions impose handling constraints that ordinary yard equipment may not cover.
- Yards and riggers often inherit infrastructure variability: some have cranes, mast sheds, and racks; others improvise with hired equipment or external contractors.
- Because the lift event is expensive and risky, adjacent inspection and retrofit tasks get bundled, which increases coordination burden and quote instability.

---

# OPERATIONAL IMPACT

- Riggers and yards lose schedule flexibility because a single missing access asset can delay the whole job.
- Mechanical service tasks inherit crane, storage, or temporary-support costs that are disproportionate to the apparent component failure.
- Liability becomes ambiguous when lifting is performed by third-party crane operators, bucket-truck contractors, or owners attempting partial DIY methods.
- Jobs become serial and labor-dense because mast handling requires multiple people, sequencing discipline, and protection of wires, joinery, and foil sections.

---

# STRATEGIC SCORES

## Severity Score:
4

## Frequency Score:
3

## MORFRAC Fit Score:
4

## Commercial Potential Score:
4

## Repeatability Score:
4

## Technical Complexity Score:
3

---

# POTENTIAL OPPORTUNITY

Observed evidence supports a bounded pre-job access-planning and installation-support service for riggers and refit yards: mast-up versus mast-down decision support, lift/staging checklist, mast-stand specification, temporary-support method selection, bundled work sequencing, and liability-conscious install documentation for geometry-sensitive rigging and furling jobs.

This is an interpretation from repeated workflow pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- Convergence signals: `RETROFIT_COMPLEXITY`, `SERVICEABILITY_COMPLEXITY`, `MECHANICAL_INTEGRATION_COMPLEXITY`.
- The repeated value appears to come more from planning and risk reduction than from inventing new hardware.
- Liability remains material where the work touches primary rigging, mast handling, and temporary support of load-bearing systems.

## Related Links

### Concepts
- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[SERVICEABILITY_COMPLEXITY]]

### Reports
- [[2026-05-24_MORAAAAA-91_rigger_and_refit_yard_workflow_bottlenecks_summary]]
