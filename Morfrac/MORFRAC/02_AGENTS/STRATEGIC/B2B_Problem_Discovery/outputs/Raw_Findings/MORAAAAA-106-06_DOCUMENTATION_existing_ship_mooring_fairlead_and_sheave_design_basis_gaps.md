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
  - MORAAAAA-106_REPORT_industrial_block_market_scope_correction
---

# MORAAAAA-106-06 Existing-ship mooring fairlead and sheave design-basis gaps

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| DNV | https://www.dnv.com/news/2023/towing-and-mooring-equipment-update-january-2024-preparation-for-solas-regulation-ii-1-3-8-248367/ | 2023-11-16 | Regulatory implementation note | HIGH |
| Lloyd's Register | https://www.lr.org/en/knowledge/class-news/15-23/ | 2023-08-09 | Classification implementation guidance | HIGH |
| ABS | https://ww2.eagle.org/content/dam/eagle/rules-and-guides/archives/offshore/292-position-mooring-systems/292-position-mooring-reqts-july22.pdf | 2022-07-01 | Classification-rule technical requirement | HIGH |
| STAG | https://portalcip.org/wp-content/uploads/2020/04/Static-Towing-Assembly-Guidelines-2020.pdf | 2020-01-01 | Towing-industry inspection guidance | HIGH |

---

# INDUSTRY_SEGMENT

OEM_BUILDERS

---

# PROBLEM_TYPE

DOCUMENTATION

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Industrial marine operators are facing a recurring fairlead and sheave problem that is partly regulatory and partly physical: many existing ships and towing assets must now prove that their mooring and towing equipment remains suitable, but they do not have complete original design-basis records, safe working load markings, or maintenance documentation. Evidence suggests the resulting value is in reconstructing design intent, validating load paths, and defining inspection and replacement logic for legacy arrangements.

---

# EVIDENCE

## Directly observed evidence

- DNV's note on SOLAS II-1/3-8 states that from 1 January 2024 the scope of towing and mooring requirements extends to new and existing ships, including new inspection and maintenance obligations.
- DNV states the new framework includes guidance on inspection and maintenance of mooring equipment including lines, and is relevant to shipowners, managers, designers, shipyards, and suppliers.
- Lloyd's Register states owners should have procedures, periodic inspections, manufacturer replacement criteria, and records of the original design concept, equipment, arrangements, and specifications available onboard.
- LR then identifies a specific legacy-vessel problem: ships with keel laid before 1 January 2007 may not have the original design concept needed to support the new maintenance and inspection requirements.
- LR further states that if a vessel has neither mooring documentation nor safe working load markings on fittings, owners are advised to check the strength of the mooring equipment and supporting hull structure, determine design loads from actual capacity onboard, and submit calculations for appraisal.
- ABS states that fairleads and sheaves must be designed to prevent excessive bending and wear, that attachments to the hull or structure must withstand rated breaking strength, and that the most unfavorable line direction must be included in the strength analysis.
- ABS also specifies large sheave-to-rope diameter ratios to reduce tension-bending fatigue and requires corrosion allowance or protection for underwater fairleads, showing that these are geometry- and environment-sensitive components rather than passive fittings.
- The `Static Towing Assembly Guidelines` identifies deck fairleads and pedestal rollers as explicit wear zones that should be inspected, alongside winch anchor points, drum cross-over zones, and rope terminations.

## Repeated pattern

- The recurring pattern is documentation deficit converting into engineering work. Legacy marine assets often still operate with serviceable hardware, but without a usable design basis for inspection, discard, or upgrade decisions.
- Fairleads and sheaves repeatedly sit at the intersection of rope wear, structural capacity, bending fatigue, and procedural compliance.
- Operators are pushed toward calculations, line identification systems, and formal maintenance logic because the original vessel documentation is incomplete or absent.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Missing original design concept for mooring and towing arrangements
- Missing or unreliable load markings on fairleads and fittings
- Need to calculate capacity and supporting-structure strength after the fact
- Increased inspection and maintenance burden under the post-2024 regime

## Likely root operational causes

- Many older ships were built before current documentation and procedural expectations were imposed.
- Mooring and towing fittings were historically treated as installed equipment rather than as assets requiring lifecycle traceability and explicit design-basis retention.
- Fairleads and sheaves concentrate wear, bending, and support-structure stresses, so a missing design basis creates disproportionate uncertainty at exactly the most fatigue-sensitive interfaces.
- Replacement and inspection decisions now require engineering reconstruction of load paths and actual onboard capacity.

---

# OPERATIONAL IMPACT

- Owners and managers may need engineering appraisal before they can demonstrate compliance or plan upgrades.
- Shipyards and retrofit teams can inherit scope expansion when missing load data forces supporting-structure checks and documentation reconstruction.
- Maintenance systems become harder to standardize across fleets when identical-looking fittings have unknown design margins or undocumented changes.
- Legacy assets face increased downtime risk if appraisal, marking, or documentation work is deferred until survey or failure pressure.

---

# STRATEGIC SCORES

## Severity Score:
4

## Frequency Score:
4

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

Observed evidence supports a bounded legacy-arrangement validation service for industrial marine fairleads, sheaves, and associated load-bearing fittings: reconstructing design basis, reviewing supporting-structure capacity, defining marking and documentation packs, and creating inspection/replacement logic for older vessels and mixed-fleet assets.

This is an interpretation from repeated technical and regulatory friction, not validated demand.

---

# CONFIDENCE_LEVEL

HIGH

---

# NOTES

- This is currently the strongest industrial-market signal because it combines repeated cross-source evidence, clear operational burden, and a bounded engineering scope.
- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]`, `[[MECHANICAL_INTEGRATION_COMPLEXITY]]`, and `[[RETROFIT_COMPLEXITY]]`.
- The value appears to come from engineering interpretation and retrofit planning support rather than from another undifferentiated hardware catalog.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_scope_correction]]
