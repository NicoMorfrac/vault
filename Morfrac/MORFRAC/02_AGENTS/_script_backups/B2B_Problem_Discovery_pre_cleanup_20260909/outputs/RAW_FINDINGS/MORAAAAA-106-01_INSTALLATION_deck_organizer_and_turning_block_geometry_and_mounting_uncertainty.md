---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-08-07
related_findings: []
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - MECHANICAL_INTEGRATION_COMPLEXITY
  - RETROFIT_COMPLEXITY
related_projects: []
related_reports:
  - MORAAAAA-106_REPORT_industrial_block_market_stage_1_summary
---

# MORAAAAA-106-01 Deck organizer and turning-block geometry and mounting uncertainty

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| YBW Forum | https://forums.ybw.com/threads/deck-organizers.575629/ | 2021-10-31 | Owner retrofit and sizing discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/low-friction-rings-high-load-thimbles.575583/ | 2021-11-19 | Owner line-routing retrofit discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/mainsheet-advice-needed-please.563070/ | 2021-04-03 | Owner geometry and block-orientation troubleshooting | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/difficulties-getting-it-up-mainsail-halyard-led-aft-high-friction.620150/ | 2025-06-29 | Owner troubleshooting discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/lead-angle.621948/ | 2025-08-26 | Owner deck-lead correction discussion | MEDIUM |
| Practical Sailor | https://www.practical-sailor.com/boat-maintenance/through-bolting-fiberglass-an-inquiry-into-failure-modes/ | 2016-06-28 | Technical hardware-mounting analysis | HIGH |
| Practical Sailor | https://www.practical-sailor.com/uncategorized/through-bolt-alternatives/ | 2023-09-21 | Technical fastening-access analysis | HIGH |
| Practical Sailor | https://www.practical-sailor.com/mailport-ps-advisor/are-you-ready-to-kludge-your-way-home/ | 2020-01-31 | Technical failure anecdote and recovery guidance | HIGH |

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

Recurring evidence suggests that organizer and turning-block retrofits are often treated as simple hardware additions when they are actually geometry-sensitive deck-routing projects. The repeated operational problem is not just friction; it is uncertainty transfer. Line angle, sheave orientation, rope construction, under-load behavior, and hidden mounting structure are often not validated together, so seemingly routine upgrades can create binding, inefficient sail handling, mounting risk, or field improvisation.

---

# EVIDENCE

## Directly observed evidence

- In the YBW `Deck organizers` thread, the owner tries to size a custom organizer installation on a 43-foot yacht and asks what sideways force the pulleys will see and whether brass bushes are acceptable or ball bearings are required. The same thread references an unusual coachroof recess and control-line tunnel, indicating that organizer selection is constrained by nonstandard deck geometry rather than catalog dimensions alone.
- In the YBW `Low Friction Rings, high load thimbles` thread, the owner wants to route halyards from the mast base around a deck step and back to the cockpit, explicitly considering a mix of horizontal pulleys, vertical pulleys, and low-friction rings. Replies note that low-friction rings are unsuitable for sharp, frequently used halyard turns and that custom flat sheaves are often preferable where line deflection and deck interaction matter.
- In the YBW `Mainsheet advice needed please!` thread, contributors identify the forward double block and induced line twist as the main cause of poor running, then recommend changing block arrangement and orientation so the load paths line up correctly. The problem is not lack of hardware but incorrect geometry between boom block, traveler block, and line lead.
- In the YBW `Difficulties getting it up` thread, the owner reports deck organizers that spin freely by hand but appear not to rotate under halyard load. A reply describes worn sheave holes becoming pear-shaped so the block works unloaded but binds when loaded, which is a clear example of under-load behavior diverging from superficial dockside inspection.
- In the YBW `Lead angle` thread, a deck organizer is used as a corrective measure because too many clutches on a small boat create a bad lead to the winch. This is another example of geometry correction being handled reactively after the deck layout has already become compromised.
- Practical Sailor's 2016 through-bolting analysis notes that rope clutches, turning blocks, and other highly loaded hardware require backing and topping plates sized to spread load without creating laminate stress risers, indicating that organizer and turning-block retrofits are structural as well as mechanical installations.
- Practical Sailor's 2023 fastening-access article states that turning blocks for windvane steering lines are among the installations most often complicated by lack of access to the reverse side of the mounting surface, reinforcing that hidden structure and fastening access are recurring blockers.
- Practical Sailor's 2020 emergency-repair article includes a failed deck organizer that prevented hoisting sails, with a temporary low-friction-ring workaround used until the correct turning hardware could be restored.

## Repeated pattern

- The recurring pattern is that routing changes are easy to visualize but hard to validate. Owners and installers repeatedly discover too late that line deflection, sheave type, and rope friction interact multiplicatively.
- The hardware frequently appears functional at rest but behaves differently under load, especially where wear, side load, or poor lead angle exists.
- Retrofit scope repeatedly expands from "add organizers" into structural fastening, backing-plate design, blind mounting, rope resizing, and block-orientation correction.

---

# ROOT CAUSE ANALYSIS

## Symptom

- High friction when leading lines aft
- Blocks or organizers that appear free-running but bind under load
- Poor lead angle into clutches or winches
- Unclear hardware selection between pulleys, deck organizers, and low-friction rings
- Mounting access and backing-plate difficulty

## Likely root operational causes

- Deck-routing retrofits combine line geometry, rope stiffness, sheave diameter, and hardware orientation into one coupled mechanical problem.
- Many boats have constrained or irregular coachroof geometry, recesses, liners, deck steps, or tunnels that break the assumptions behind standard hardware layouts.
- Under-load behavior is not well predicted by casual inspection; wear, side load, and deflection angle can convert a seemingly free-running part into a friction point.
- Mounting high-load turning hardware often requires structural judgment and fastening solutions where reverse-side access is limited or laminate behavior is uncertain.

---

# OPERATIONAL IMPACT

- Refit yards and riggers inherit diagnosis risk because poor sail-handling performance may come from geometry, wear, rope choice, or hidden mounting constraints rather than from one clearly failed part.
- Installation time expands when deck penetrations, backing plates, or blind-fastener strategies have to be developed after hardware selection.
- Boats can lose normal sail-handling functionality if an organizer or turning block fails or binds under load.
- Owners may overspecify or misapply hardware, increasing cost without resolving the root geometry problem.

---

# STRATEGIC SCORES

## Severity Score:
4

## Frequency Score:
3

## MORFRAC Fit Score:
5

## Commercial Potential Score:
4

## Repeatability Score:
4

## Technical Complexity Score:
4

---

# POTENTIAL OPPORTUNITY

Evidence supports a bounded retrofit-engineering offer focused on deck-routing validation for blocks, organizers, and related high-load control hardware: intake templates for line-path geometry, sheave and rope compatibility checks, mounting-structure review, backing-plate and fastening recommendations, and install drawings for riggers or yards.

This is an interpretation from repeated technical friction, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]`, `[[MECHANICAL_INTEGRATION_COMPLEXITY]]`, and `[[RETROFIT_COMPLEXITY]]`.
- Evidence quality is improved by the presence of technically specific failure descriptions, geometry corrections, and structural fastening guidance rather than generic owner dissatisfaction.
- Commercial validation remains limited. What is well supported is recurring installation-risk and troubleshooting burden around line-routing retrofits.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_stage_1_summary]]
