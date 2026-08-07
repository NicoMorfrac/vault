---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-08-07
related_findings:
  - MORAAAAA-106-07_SERVICING_underdetected_sheave_bearing_and_pin_degradation_in_lifting_blocks
  - MORAAAAA-106-08_QUALITY_CONTROL_sheave_design_change_and_retrofit_validation_gaps
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - SERVICEABILITY_COMPLEXITY
related_projects: []
related_reports:
  - MORAAAAA-106_REPORT_industrial_block_market_stage_3_maintainer_workflow
---

# MORAAAAA-106-09 Inspection-disassembly burden in crane blocks and sheaves

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| BSEE Accident Investigation Report | https://www.bsee.gov/sites/bsee.gov/files/2025-12/WD%20152%20Renaissance%2027-Aug-2025.pdf | 2025-12-11 | Incident investigation and inspection-method critique | HIGH |
| BSEE Accident Investigation Report | https://www.bsee.gov/sites/bsee.gov/files/2025-11/ST%20229%20W%26T%2009-May-2025.pdf | 2025-11-13 | Incident investigation and corrective-action evidence | HIGH |
| Crosby Split-Nut brochure | https://www.thecrosbygroup.com/wp-content/uploads/catalog/2016/en-US/379.pdf | 2019 catalog page | OEM serviceability feature justification | HIGH |
| Crosby Easy Reeve crane blocks catalog | https://www.thecrosbygroup.com/wp-content/uploads/2014/07/9991013.pdf | 2014 | OEM reeving/access feature justification | HIGH |
| Crosby Tackle Block and Sheave Assembly Warning | https://www.thecrosbygroup.com/wp-content/uploads/2014/02/375_382.pdf | 2013 | OEM teardown/reassembly maintenance guidance | HIGH |
| OSHA 1926.1413 | https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1413 | current standard accessed 2026-08-07 | Regulatory inspection requirement | HIGH |

---

# INDUSTRY_SEGMENT

OEM_BUILDERS

---

# PROBLEM_TYPE

SERVICING

---

# OPPORTUNITY_TYPE

DESIGN_OPTIMIZATION

---

# SUMMARY

Recurring industrial evidence suggests that effective inspection of crane blocks and sheaves is often limited by the amount of disassembly required to access the real wear surfaces. The symptom is a block or sheave that appears acceptable under routine checks but later fails at the pin, bearing, or retention interface. The deeper operational problem is service architecture: many assemblies are still inspected through low-disruption routines even when meaningful condition validation requires pin removal, teardown, reassembly control, and reliable restoration of locking features.

---

# EVIDENCE

## Directly observed evidence

- In BSEE's August 27, 2025 Renaissance report, the annual inspection performed a few days before the incident found the bridle sheaves in good condition after free rotation and greasing, but the inspector did not remove the sheave pin. BSEE states that because the pins were not removed during past annual inspections, there is no definitive conclusion on when the pin wear became critical, and explicitly recommends future pin removal for a more thorough examination.
- The same Renaissance report states the third-party crane inspection guide did not require removal of the bridle sheave pin and instead relied on tilt and alignment checks as wear indicators. This shows that the accepted workflow was shaped by what could be checked without deeper disassembly.
- In BSEE's May 9, 2025 W&T report, investigators concluded debris restricted the lubrication passage to the load-block sheave pin and bearing. Corrective action required revised inspection forms and a mandate to flush and verify all lubrication pathways, showing that apparent greasing was not enough without more invasive service confirmation.
- Crosby's Split-Nut literature states conventional threaded nuts create problems during required crane-block inspections and presents the product benefit as allowing hook disassembly and inspection in a fraction of the time. That is direct commercial evidence that inspection access is a recognized service bottleneck.
- Crosby's Easy Reeve crane-block catalog states removable pull-pins allow block reeving without removing wedge sockets, again showing that field labor and disassembly burden are recurring enough to be a design selling point.
- Crosby's block-and-sheave warning document requires checking sheave pin nut positioning, snap-ring security, and proper locking methods after teardown inspection, which indicates that inspection itself creates reassembly risk and procedure sensitivity.
- OSHA 1926.1413 requires a competent person to begin visual wire-rope inspection before each shift, but also explicitly states untwisting wire rope or booming down is not required as part of that inspection. This reinforces the gap between frequent compliance checks and deeper mechanical verification.

## Repeated pattern

- The recurring pattern is that inspection quality is constrained by service access. If meaningful inspection requires teardown, organizations tend to default toward quicker external checks until an event or anomaly forces deeper intervention.
- OEMs are already commercializing easier-inspection features, which suggests the burden is not theoretical but operationally significant.
- Disassembly is not a neutral step: once a block is opened, correct locking, end-play restoration, and reassembly integrity become their own failure-control problem.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Serious internal wear discovered only after an incident
- Inspection programs that document acceptable condition shortly before failure
- Heavy dependence on grease points, free rotation, or tilt checks
- Long service windows before pins, bearings, or internal lock features are directly inspected

## Likely root operational causes

- Internal condition is expensive and disruptive to verify, especially when pin removal or block disassembly is required.
- Existing maintenance procedures are often optimized around uptime and routine compliance, not around direct access to the highest-consequence wear interfaces.
- Many block architectures make inspection harder than it needs to be, so service organizations rationally avoid teardown until symptoms appear.
- Reassembly risk discourages frequent disassembly unless the assembly is explicitly designed for repeated inspection access.

---

# OPERATIONAL IMPACT

- Maintainers and inspection contractors can sign off equipment that still contains hidden bearing or pin degradation.
- Operators inherit latent failure risk because deeper inspection is deferred by labor, access, and reassembly burden.
- Maintenance events expand in scope once teardown starts, because wear limits, lock features, and end-play settings must all be restored correctly.
- Downtime and service cost become less predictable when inspection quality depends on whether the assembly can be opened efficiently.

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
4

---

# POTENTIAL OPPORTUNITY

Observed evidence supports a bounded serviceability-focused offer for industrial crane blocks and sheaves: inspection-access redesign, teardown-threshold logic, reassembly control documentation, and retrofit concepts that reduce the labor and ambiguity of pin, bearing, and locking-feature inspection.

This is an interpretation from repeated technical pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- This finding is narrower than a general crane-maintenance market claim. The evidence supports a specific recurring workflow burden around getting to the real wear surfaces without creating excessive downtime or reassembly risk.
- Convergence is strongest with `[[SERVICEABILITY_COMPLEXITY]]` and `[[ENGINEERING_UNCERTAINTY]]`.
- The strongest strategic angle may be making deep inspection easier and more repeatable, not adding another undifferentiated block SKU.

## Related Links

- [[MORAAAAA-106-07_SERVICING_underdetected_sheave_bearing_and_pin_degradation_in_lifting_blocks]]
- [[MORAAAAA-106-08_QUALITY_CONTROL_sheave_design_change_and_retrofit_validation_gaps]]
- [[ENGINEERING_UNCERTAINTY]]
- [[SERVICEABILITY_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_stage_3_maintainer_workflow]]
