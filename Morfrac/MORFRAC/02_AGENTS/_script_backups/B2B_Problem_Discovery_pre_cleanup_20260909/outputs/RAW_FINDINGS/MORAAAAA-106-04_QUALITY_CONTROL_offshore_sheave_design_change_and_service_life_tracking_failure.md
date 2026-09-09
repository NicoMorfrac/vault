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
  - MORAAAAA-106_REPORT_industrial_block_market_scope_correction
---

# MORAAAAA-106-04 Offshore sheave design-change and service-life tracking failure

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| BSEE | https://www.bsee.gov/sites/bsee.gov/files/qc-fit-sheaves-final-report.pdf | 2016-12-01 | Offshore technical failure evaluation | HIGH |
| ABS | https://ww2.eagle.org/content/dam/eagle/rules-and-guides/archives/offshore/292-position-mooring-systems/292-position-mooring-reqts-july22.pdf | 2022-07-01 | Classification-rule technical requirement | HIGH |

---

# INDUSTRY_SEGMENT

MARINE_HARDWARE_BRANDS

---

# PROBLEM_TYPE

QUALITY_CONTROL

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Industrial marine sheave failures in offshore systems are not only a materials or welding problem. The deeper recurring issue is configuration control under service: design changes, manufacturing variation, interchangeable parts, and incomplete service-life traceability shift inspection and replacement burden onto operators. Evidence suggests the value sits in validation, traceability, and replacement-path engineering, not in generic sheave supply.

---

# EVIDENCE

## Directly observed evidence

- BSEE's `QC-FIT Evaluation of Sheave Failures` describes failures of 78-inch dual-web sheaves in crown mounted compensators on offshore drilling rigs. The report states the OEM identified ten rigs requiring sheave replacements, issued product bulletins, and recommended weekly inspections for cracks at the hub-web weld joint.
- The same BSEE report states the OEM stopped sourcing the affected dual-web sheaves from the existing manufacturer and moved to a different qualified manufacturer, indicating that supplier and manufacturing quality became part of the failure chain rather than a simple field-maintenance issue.
- BSEE's root-cause summary states that the dual-web design and hand-weld root pass created a gap that prevented full weld penetration, and that a hub-dimension design change increased load rating while pushing web-plate stresses beyond allowable compression limits.
- BSEE explicitly notes that because the sheaves were interchangeable across positions in the compensator assembly, tracking service life was difficult. It therefore recommended daily visual inspections by operators and inspectors.
- ABS `Requirements for Position Mooring Systems` states that fairleads and sheaves are to be designed to prevent excessive bending and wear, that hull/structure attachments must withstand rated breaking strength, and that quality-control details for individual mooring-system components are to be submitted, tested, marked, and documented.

## Repeated pattern

- The recurring pattern is not just fatigue cracking. It is uncertainty about whether the installed component is the right revision, made to the right process, and still within a defensible service window.
- Once industrial sheaves become interchangeable within a larger system, operators lose straightforward component-life traceability unless serialisation, inspection logic, and replacement discipline are strong.
- Offshore operators inherit ongoing inspection intensity when manufacturers or OEMs cannot bound failure risk through design robustness and configuration control alone.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Sheave cracking in service
- Urgent replacement campaigns across multiple rigs
- Elevated inspection frequency
- Difficulty tracking remaining life of interchangeable sheaves

## Likely root operational causes

- Design revisions were not fully revalidated against real stress concentrations and welding-process realities.
- Manufacturing quality and material traceability were insufficiently controlled for a fatigue-sensitive geometry.
- Interchangeable sheaves created a serviceability and traceability problem: once parts move between positions, life tracking and discard logic become weaker.
- Industrial operators rely on component documentation, markings, and test records that may not adequately support long-term in-service risk management.

---

# OPERATIONAL IMPACT

- Operators absorb inspection and downtime burden after design or manufacturing defects emerge in the field.
- Replacement campaigns can span multiple rigs or vessels when a sheave family is widely deployed.
- Safety-critical lifting or motion-compensation systems become dependent on frequent visual inspection because configuration and life status cannot be trusted passively.
- Procurement shifts from simple resupply to engineering-led replacement and validation.

---

# STRATEGIC SCORES

## Severity Score:
5

## Frequency Score:
2

## MORFRAC Fit Score:
4

## Commercial Potential Score:
3

## Repeatability Score:
3

## Technical Complexity Score:
5

---

# POTENTIAL OPPORTUNITY

Observed evidence supports a bounded engineering-validation offer for industrial sheaves and related block assemblies: design-review support, manufacturing and weld-detail audit, replacement-path qualification, service-life traceability frameworks, and retrofit documentation for operators managing mixed or legacy component populations.

This is an interpretation from observed technical failure patterns, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- This finding is industrially relevant but evidence is more concentrated than broad-based; confidence is therefore limited by recurrence visibility rather than by technical specificity.
- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]` and `[[SERVICEABILITY_COMPLEXITY]]`.
- Liability exposure is significant because these components sit inside safety-critical offshore load paths.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[SERVICEABILITY_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_scope_correction]]
