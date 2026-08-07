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
  - MORAAAAA-106_REPORT_general_industrial_block_market_scope_correction
---

# MORAAAAA-106-07 Underdetected sheave-bearing and pin degradation in lifting blocks

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| BSEE Accident Investigation Report | https://www.bsee.gov/sites/bsee.gov/files/2025-11/ST%20229%20W%26T%2009-May-2025.pdf | 2025-11-13 | Industrial incident investigation | HIGH |
| BSEE Accident Investigation Report | https://www.bsee.gov/sites/bsee.gov/files/2025-12/WD%20152%20Renaissance%2027-Aug-2025.pdf | 2025-12-11 | Industrial incident investigation | HIGH |
| BSEE Accident Investigation Report | https://www.bsee.gov/sites/bsee.gov/files/2026-04/BM%203%20Cantium%205-Aug-2025_0.pdf | 2026-04-01 | Industrial incident investigation | HIGH |
| OSHA Standard 1910.179 | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.179 | current standard accessed 2026-08-07 | Regulatory inspection standard | HIGH |
| Crosby General Catalog | https://www.thecrosbygroup.com/wp-content/uploads/catalog/2022/en/439.pdf | 2022 | OEM maintenance guidance | HIGH |

---

# INDUSTRY_SEGMENT

HIGH_PERFORMANCE_SYSTEMS

---

# PROBLEM_TYPE

SERVICING

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Recurring industrial evidence suggests that sheave-bearing and sheave-pin degradation in lifting blocks is often detected too late because prevailing inspection methods over-rely on unloaded free rotation, grease-at-zerk confirmation, or visible tilt rather than direct condition validation. The surface symptom is a sudden load-block or bridle-sheave event. The deeper operational problem is that service routines frequently do not expose internal wear progression, blocked lubrication paths, or pin loss until the damage has already propagated into the sheave, rope, and block structure.

---

# EVIDENCE

## Directly observed evidence

- In BSEE's May 9, 2025 W&T load-block investigation, the operator reported the block first showing a shake or wobble before the rope began paying out. BSEE concluded that a sheave bearing failed because debris restricted the sheave pin lubrication passage, which then generated enough rotational force to shear the dowel pin and let the pin and retainers dislodge from the block.
- The same BSEE report states that the operator, rigger, and crane contractor responded by revising inspection forms and requiring technicians to flush and verify all lubrication pathways during servicing, which indicates the pre-incident maintenance routine did not adequately validate internal grease passage condition.
- In BSEE's August 27, 2025 Renaissance bridle-sheave investigation, the failed bearing wore a 3-inch pin down to roughly 2.5 inches at the bearing location. The report states the annual inspection a few days earlier marked the bridle sheaves and boom cable as in good condition, and the inspector said he rotated the sheaves freely without cable tension and greased through the grease points but did not remove the pin.
- That same Renaissance report notes the third-party inspection guide relied on tilt and alignment checks as indicators of wear and did not include pulling the bridle sheave pin for inspection. This is strong evidence that accepted inspection practice can miss severe internal deterioration.
- In BSEE's Cantium report, a prior inspection note explicitly recorded that a sheave had bearing slop and recommended replacing the sheave and bearing, yet the later investigation still involved damage tied to sheave-bearing condition. This suggests recurring operational difficulty converting warning signs into timely corrective action.
- OSHA 1910.179 requires sheave grooves to remain smooth and defect-free, reflecting that rope path condition is safety-critical, but the incident reports show that compliance-grade visual checks do not necessarily catch internal pin or bearing degradation.
- Crosby's maintenance guidance notes that sheave pin nuts and end play should be checked and adjusted according to bearing type, which reinforces that correct block service involves more than external lubrication.

## Repeated pattern

- The recurring failure mode is not just bearing wear. The repeated pattern is latent degradation inside the load path: blocked lubrication passages, worn pins, end-play problems, or internal bearing collapse that remain hidden behind apparently normal unloaded movement.
- Inspection systems repeatedly appear to favor low-disassembly checks because full teardown is costly, time-consuming, or outside routine procedure.
- Once degradation escapes detection, the failure propagates across adjacent components: pin, sheave groove, rope, retainers, and block stability.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Load block wobble or shaking
- Jerky rope behavior, slack payout, or unstable block motion
- Unexpected sheave ejection, rope damage, or sheave-side cutting
- Inspection records showing acceptable condition shortly before failure

## Likely root operational causes

- Internal bearing and pin condition is difficult to verify with fast field inspections that avoid disassembly.
- Lubrication systems can appear functional while debris or restricted passages prevent lubricant from reaching the critical internal surfaces.
- Existing inspection guides may rely on tilt, alignment, or free rotation checks that are insufficient for advanced wear states.
- Maintenance escalation thresholds are not always clear, so early warning signs can remain advisory instead of triggering mandatory component removal.

---

# OPERATIONAL IMPACT

- Operators and service contractors face sudden out-of-service events, dropped-load risk, and collateral rope or block damage.
- Inspection burden increases because organizations respond after incidents by adding forms, grease-path verification, and stricter abnormality triggers.
- Maintenance cost rises when a missed internal defect destroys multiple components instead of one bearing or pin.
- Liability is significant because documented inspections may exist even when the inspection method itself was not capable of revealing the defect.

---

# STRATEGIC SCORES

## Severity Score:
5

## Frequency Score:
3

## MORFRAC Fit Score:
4

## Commercial Potential Score:
4

## Repeatability Score:
4

## Technical Complexity Score:
4

---

# POTENTIAL OPPORTUNITY

Evidence supports a bounded inspection-method and serviceability engineering offer for industrial block systems: teardown thresholds, grease-path validation protocols, pin/bearing wear decision trees, and retrofit-friendly block designs or service kits that make internal condition easier to verify before catastrophic propagation.

This is an interpretation from repeated technical pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- This finding is outside sailing scope and reflects the revised issue direction toward general industrial applications.
- The strongest signal is procedural and serviceability-related rather than product-aesthetic or brand-preference driven.
- Convergence is strongest with `[[SERVICEABILITY_COMPLEXITY]]` and `[[ENGINEERING_UNCERTAINTY]]`.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[SERVICEABILITY_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_general_industrial_block_market_scope_correction]]
