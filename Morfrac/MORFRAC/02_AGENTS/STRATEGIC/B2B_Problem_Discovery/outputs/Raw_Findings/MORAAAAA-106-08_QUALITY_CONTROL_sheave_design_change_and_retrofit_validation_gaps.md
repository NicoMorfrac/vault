---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-08-07
related_findings:
  - MORAAAAA-106-07_SERVICING_underdetected_sheave_bearing_and_pin_degradation_in_lifting_blocks
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - MECHANICAL_INTEGRATION_COMPLEXITY
  - RETROFIT_COMPLEXITY
related_projects: []
related_reports:
  - MORAAAAA-106_REPORT_general_industrial_block_market_scope_correction
---

# MORAAAAA-106-08 Sheave design-change and retrofit validation gaps

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| BSEE QC-FIT Evaluation of Sheave Failures | https://www.bsee.gov/sites/bsee.gov/files/qc-fit-sheaves-final-report.pdf | 2017-07-01 | Engineering failure analysis | HIGH |
| HSE Offshore Cranes Safety Bulletin | https://www.hse.gov.uk/safetybulletins/offshore-cranes.htm | 2025-01-24 | Safety bulletin on rope/sheave behavior | HIGH |
| BSEE Crane Safety Assessment Findings | https://www.bsee.gov/sites/bsee.gov/files/2026-04/TAP%20729%20Crane%20Safety%20Awareness%20Final%20Research%20Report_%20508c.pdf | 2026-04-22 | Regulatory and audit framework | HIGH |
| Crosby Tackle Block and Sheave Assembly Warning | https://www.thecrosbygroup.com/wp-content/uploads/2014/02/375_382.pdf | 2013 | OEM application warning | HIGH |
| OSHA 1926.1413 | https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1413 | current standard accessed 2026-08-07 | Regulatory inspection standard | HIGH |

---

# INDUSTRY_SEGMENT

OEM_BUILDERS

---

# PROBLEM_TYPE

QUALITY_CONTROL

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Recurring industrial evidence suggests that block and sheave failures often emerge after configuration changes, replacement-path deviations, or operating-envelope shifts that were not fully revalidated. The deeper problem is bounded but serious: once a sheave design, weld method, material choice, rope path, retention geometry, or control logic changes, many organizations appear to rely on legacy assumptions and inspection routines even though the new stress state or rope behavior has materially changed.

---

# EVIDENCE

## Directly observed evidence

- In BSEE's QC-FIT sheave failure analysis, the hub dimension was reduced while web-plate thickness was unchanged, which increased the sheave load rating by about 11 percent and pushed compressive stress above allowable limits. BSEE states the impact of the design change was not fully evaluated and links the resulting crack initiation to the hub-web weld geometry and fatigue failure.
- The same BSEE report states that the dual-web design prevented welding on the inside of the hub-web joint, that a partial-penetration root condition created a stress riser, and that material test certificates were not available to the test laboratory during the metallurgical analysis. That combination indicates a quality-control and documentation gap, not just isolated wear.
- BSEE recommended finite element analysis on the replacement single-web sheave and verification of material certificates, which implies that the right response to the failure pattern is engineering revalidation rather than a simple like-for-like part swap.
- HSE's offshore crane bulletin describes rope coming off a sheave because slack rope, boom bounce, rope twist during installation, or fleet-angle effects can move the rope over the sheave rim and through the retention-bar gap. This shows that changes in operating method or rope-installation condition can defeat a sheave arrangement that appears acceptable in static design terms.
- BSEE's 2026 crane safety assessment emphasizes anti-two-block protection and documented inspection of devices intended to protect hoist ropes and structural components when load-block and boom-head sheave groups come into contact, reinforcing that block systems depend on control logic and protective devices, not only metal strength.
- Crosby's tackle-block warning explicitly states that incorrect sheave assembly material selection for the intended application can cause premature sheave, bearing, or wire-rope wear and eventual failure, which aligns with the incident evidence that application context matters as much as nominal rating.
- OSHA 1926.1413 requires observation of wire ropes and sheaves for deficiencies during use, but the incident and bulletin evidence shows that inspection alone does not close the gap created by changed geometry, altered loading, or replacement-path deviations.

## Repeated pattern

- Failures repeatedly cluster around changed conditions: altered sheave geometry, revised weld details, changed rope installation behavior, or system states where slack and contact occur unexpectedly.
- Documentation and validation frequently lag behind the change. Material certificates, FEA, updated inspection logic, or explicit installation constraints are added only after an incident or formal investigation.
- The real failure is often in the transfer of engineering assumptions from design to operation, maintenance, and retrofit execution.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Fatigue cracks in sheaves after design changes
- Rope climbing out of grooves or passing retention geometry
- Unexpected interaction between rope behavior and sheave/retention hardware
- Need for post-incident redesign, special bulletins, or new inspection requirements

## Likely root operational causes

- Configuration changes are treated as minor revisions even when they alter stress concentration, weld accessibility, rope tracking, or failure consequence.
- Replacement and retrofit work often inherits legacy standards that were validated for a prior geometry or operating envelope, not the current one.
- Quality documentation may be incomplete at the moment it is most needed, including material traceability or explicit revalidation of revised parts.
- Protective systems and inspection routines are sometimes assumed to compensate for design uncertainty even though they only mitigate parts of the risk.

---

# OPERATIONAL IMPACT

- Operators and OEMs face recurring risk of crack initiation, rope damage, or catastrophic lifting events after seemingly bounded design or replacement changes.
- Post-failure response often expands into fleetwide inspection campaigns, replacement programs, engineering reviews, and operational restrictions.
- Engineering responsibility becomes ambiguous when design change, maintenance practice, and operating behavior all contribute to the final failure mode.
- Downtime and retrofit cost increase because the corrective action typically requires validation work, not just parts procurement.

---

# STRATEGIC SCORES

## Severity Score:
5

## Frequency Score:
3

## MORFRAC Fit Score:
5

## Commercial Potential Score:
4

## Repeatability Score:
4

## Technical Complexity Score:
5

---

# POTENTIAL OPPORTUNITY

Evidence supports a bounded engineering-validation service for industrial block and sheave applications: design-change review, retrofit load-path verification, weld and material traceability checks, rope-path and retention-gap validation, and documentation packages for operators or OEMs making controlled modifications to lifting hardware systems.

This is an interpretation from repeated technical pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- This is the strongest non-sailing strategic pattern in the revised scope because it points toward recurring value in engineering validation rather than commodity supply.
- Liability exposure is high because the affected hardware is load-bearing and failure can be catastrophic.
- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]`, `[[MECHANICAL_INTEGRATION_COMPLEXITY]]`, and `[[RETROFIT_COMPLEXITY]]`.

## Related Links

- [[MORAAAAA-106-07_SERVICING_underdetected_sheave_bearing_and_pin_degradation_in_lifting_blocks]]
- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_general_industrial_block_market_scope_correction]]
