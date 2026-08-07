---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-08-07
related_findings: []
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - SERVICEABILITY_COMPLEXITY
related_projects: []
related_reports:
  - MORAAAAA-106_REPORT_industrial_block_market_stage_1_summary
---

# MORAAAAA-106-02 Block selection strength, friction, and serviceability tradeoffs

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| Cruisers Forum | https://www.cruisersforum.com/forums/f116/new-blocks-for-my-beneteau-411-which-ones-187313.html | 2017-07-05 | Owner and marine-service-provider replacement discussion | HIGH |
| Cruisers Forum | https://www.cruisersforum.com/forums/f116/servicing-blocks-and-cleaning-sheets-221195.html | 2019-07-20 | Maintenance and service discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/replacing-mainsheet-blocks-plain-or-ball-bearings.574297/ | 2021-10-22 | Owner bearing-type selection discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/freeing-a-seized-block.440521/ | 2015-09-17 | Owner block seizure discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/sheave-pin-replacement.625548/ | 2026-01-27 | Owner repair-method discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/mainsheet-system-westerly-storm.568352/ | 2021-08-02 | Replacement-selection and friction discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/replacing-mainsheet-block-and-cam-cleat.274641/ | 2011-05-26 | Performance improvement discussion | MEDIUM |

---

# INDUSTRY_SEGMENT

RIGGERS

---

# PROBLEM_TYPE

SERVICING

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Recurring evidence suggests that block replacement is constrained by a persistent tradeoff between static strength, running efficiency, and field serviceability. Legacy and OEM plain-bearing blocks are repeatedly described as strong but friction-heavy. Ball- or roller-bearing replacements improve handling but introduce their own wear modes, load-rating differences, and application limits. Service work is further complicated by seized pins, non-serviceable assemblies, and the need for improvised repair methods when replacement choices are unclear.

---

# EVIDENCE

## Directly observed evidence

- In the Cruisers Forum `New blocks for my Beneteau 411` thread, a marine service provider explains that HYE plain-bearing blocks are stronger than common roller or ball-bearing alternatives but much less efficient, and that friction becomes substantial in multi-block systems. The same thread includes an owner report of a replacement Harken lower mainsheet block exploding on passage and another service provider warning that published load figures are not directly comparable across brands and bearing types.
- In the Cruisers Forum `Servicing blocks and cleaning sheets` thread, contributors advise that pin-bearing blocks that do not turn freely need repair or replacement, and describe drilling out riveted pins and substituting clevis pins to make future sheave replacement possible. This indicates that ordinary servicing often becomes component re-engineering.
- In the YBW `Replacing mainsheet blocks: plain or ball bearings?` thread, contributors note that plain-bearing blocks generally offer higher safe working load, while ball-bearing blocks can suffer flat-spotting when left under long static load. This shows that the selection problem is not simply "better" versus "worse" hardware but application-specific duty-cycle tradeoffs.
- In the YBW `Freeing a seized block` thread, the owner asks how to free a seized kicker block rather than immediately replacing it, reflecting the reality that failure often first appears as maintenance burden and lost motion rather than catastrophic breakage.
- In the YBW `Sheave pin replacement` thread, contributors discuss destroying the original axle to replace worn sheaves and the need to maintain cheek compression so the rope does not force the cheeks apart and jam between cheek and sheave. The discussion highlights that even small repair decisions can alter load path and functional reliability.
- In the YBW `Mainsheet system - Westerly Storm` thread, the owner reports chipped and cracked blocks, oversized line creating excess friction, worn cam cleats, and difficulty finding the correct replacement kit without overbuying complexity or cost.
- In the YBW `Replacing mainsheet block and cam cleat` thread, an owner reports that moving from metal jaws and plain bearings to a ball-bearing unit transformed one-handed operation and light-air ease of use, indicating that friction losses are operationally meaningful, not theoretical.

## Repeated pattern

- Strength, efficiency, and maintainability are repeatedly in tension. Strong plain-bearing hardware can be operationally inefficient, while lower-friction hardware can be more sensitive to static loading, wear, or misapplication.
- Replacement is rarely a simple like-for-like purchase. Rope diameter, purchase count, duty cycle, static load exposure, and expected service access all affect the correct choice.
- Serviceability gaps recur because many blocks are riveted, difficult to inspect, or awkward to rebuild without custom methods.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Seized or rough-running blocks
- Excessive sheet or halyard friction
- Cracked or exploded replacement blocks
- Confusion about plain-bearing versus roller/ball-bearing selection
- Repair methods that require drilling out pins or modifying assemblies

## Likely root operational causes

- Block selection is often driven by headline load rating or price, while real performance depends on the interaction between duty cycle, deflection, rope size, and number of sheaves in the system.
- Multi-block purchases amplify friction losses, so a hardware choice that seems acceptable in isolation becomes operationally poor in a full system.
- Many legacy blocks are not designed for easy field disassembly, pushing service providers toward destructive removal or improvised pin solutions.
- Published load metrics are inconsistent across brands and product families, increasing specification uncertainty for replacement work.

---

# OPERATIONAL IMPACT

- Riggers and service providers absorb selection risk because a replacement that is strong enough on paper may still perform poorly in use.
- Owners defer maintenance or attempt improvised repairs when service paths are unclear or replacements are expensive.
- Friction-heavy or partly seized blocks increase crew effort, reduce one-handed handling quality, and can mask broader rigging inefficiencies.
- Failure or poor replacement choice can create follow-on damage, downtime, or repeat service visits.

---

# STRATEGIC SCORES

## Severity Score:
4

## Frequency Score:
3

## MORFRAC Fit Score:
4

## Commercial Potential Score:
3

## Repeatability Score:
3

## Technical Complexity Score:
4

---

# POTENTIAL OPPORTUNITY

Observed evidence supports a bounded specification-and-serviceability advisory offer for block replacement work: application-specific bearing selection guidance, purchase-system friction review, upgrade paths for legacy assemblies, and repairability assessments that help riggers choose when to rebuild, redesign, or replace.

This is an interpretation from repeated technical pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]` and `[[SERVICEABILITY_COMPLEXITY]]`.
- This finding appears commercially weaker than the geometry-sensitive routing finding because some burden may be absorbed by normal rigging trade practice rather than a standalone productizable offer.
- The recurring value may lie more in specification, diagnosis, and repairability guidance than in manufacturing a new generic block product.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[SERVICEABILITY_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_stage_1_summary]]
