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

# MORAAAAA-106-05 Fishing-vessel lifting blocks inspection and continued-service uncertainty

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| GOV.UK MCA Safety Alert | https://assets.publishing.service.gov.uk/media/5a7c58a640f0b62dffde1814/safetyalert48.pdf | 2013-02-01 | Fishing-vessel technical failure alert | HIGH |
| IIMS / MCA bulletin summary | https://www.iims.org.uk/safety-bulletin-issued-by-mca-over-concerns-with-lifting-equipment-inspections-on-fishing-vessels/ | 2021-08-24 | Fishing-vessel inspection and maintenance bulletin | HIGH |
| GOV.UK MGN 332 | https://assets.publishing.service.gov.uk/media/5a80d69eed915d74e6230bcd/MGN_332.pdf | 2006-09-01 | Lifting-equipment regulation guidance | HIGH |
| Transport Canada TP 9912 | https://tc.canada.ca/en/marine-transportation/publications/tp-9912-standard-inspection-tackle-large-fishing-vessels | 2016-12-13 | Large-fishing-vessel tackle inspection standard | HIGH |

---

# INDUSTRY_SEGMENT

REFIT_YARDS

---

# PROBLEM_TYPE

SERVICING

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Evidence from fishing-vessel safety alerts and inspection guidance suggests a recurring industrial problem around blocks, pulleys, chains, and related lifting gear: continued-service decisions are difficult because the components operate in high-load, high-wear, high-impact conditions, but technical acceptance criteria, inspection methods, and intended-use boundaries are often fragmented across suppliers, competent persons, and vessel operators. The commercial pain is less about buying another block and more about defensible inspection, discard, and replacement logic.

---

# EVIDENCE

## Directly observed evidence

- The UK MCA `Failure of Swivel Block` safety alert states that a swivel block on a UK fishing vessel failed in a near-fatal incident even though it was marked with a 10-ton safe working load, and that it reportedly failed at a much lower load.
- The 2021 MCA bulletin, reproduced by IIMS, states that a number of near misses and accidents during lifting operations onboard UK fishing vessels triggered renewed concern over inspection regimes.
- That bulletin identifies fishing gear, lifting apparatus, chains, wires, and pulleys on beam trawlers and scallopers as typical high-load, high-wear, high-impact areas where inspection attention may need to increase.
- The same bulletin states it is the owner's responsibility to provide sufficient technical information to the competent person so the continued-service assessment and acceptance limits of each item can be judged, and notes that some cases may require inspection techniques beyond visual examination.
- MGN 332 states that lifting-equipment accidents are often caused by failure of lifting equipment or single-point failures, and that corrosion, metal fatigue, inappropriate repairs or modifications, and poor maintenance all reduce safety margins.
- MGN 332 also states employers must ensure lifting equipment is appropriate for its intended purpose and that regular preventative maintenance and annual examinations are carried out.
- Transport Canada's `TP 9912` states that on large fishing vessels the safe working load for a single-sheave block is derived from the resultant load on the head fitting, and sets proof-load expectations for single- and multi-sheave blocks. This indicates that correct continued-service assessment depends on understanding actual resultant loading, not relying on a simple label alone.

## Repeated pattern

- The recurring pattern is technical ambiguity at the maintenance boundary: operators may have hardware with a load label, but still lack enough context to know whether the block is appropriate, modified, degraded, or still safe in the actual service configuration.
- High-wear fishing applications create a cycle in which inspection burden rises fastest exactly where documentation, cleanliness, and access are weakest.
- Responsibility is fragmented: owners, skippers, competent inspectors, and suppliers each hold part of the safety case, but the system often lacks a clear engineering bridge between them.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Premature or unexpected block failure
- Repeated concern over inspection frequency
- Difficulty deciding whether gear can remain in service
- Reliance on annual inspection regimes that may be too coarse for high-wear applications

## Likely root operational causes

- Fishing-vessel lifting gear operates in high-impact, contamination-heavy environments that accelerate wear relative to generic lifting assumptions.
- Safe working load markings do not resolve resultant head-fit loads, shock loading, wear state, prior modification, or inspection adequacy.
- Vessel operators often need more technical guidance than suppliers provide to translate intended-use data into continued-service and discard criteria.
- Equipment is frequently inspected during operational windows where cleaning, access, or nondestructive examination are constrained.

---

# OPERATIONAL IMPACT

- Fishing operators and service providers face heightened liability when deciding whether loaded blocks and related gear remain fit for service.
- Maintenance windows can expand because inspection may require cleaning, disassembly, or more advanced techniques than visual checks.
- Unexpected failures carry severe safety consequences and can interrupt fishing operations during short seasonal windows.
- Yards and surveyors may inherit engineering-interpretation work that sits between generic supplier information and actual vessel duty cycle.

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

Observed evidence supports a bounded inspection-support and replacement-planning service for industrial fishing-vessel lifting gear: duty-cycle intake, configuration review, acceptance/discard criteria support, inspection-pack development, and replacement or reinforcement recommendations for high-wear block and sheave applications.

This is an interpretation from repeated technical pain, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- This is the strongest industrial fishing finding so far because the evidence explicitly identifies repeated near misses, high-wear applications, and technical-information gaps.
- Convergence is strongest with `[[ENGINEERING_UNCERTAINTY]]` and `[[SERVICEABILITY_COMPLEXITY]]`.
- Taxonomy fit is imperfect because the current industry-segment list has no direct commercial-fishing category; `REFIT_YARDS` is used here because remediation and continued-service decisions are likely to land in yard and inspection workflows.

## Related Links

- [[ENGINEERING_UNCERTAINTY]]
- [[SERVICEABILITY_COMPLEXITY]]
- [[MORAAAAA-106_REPORT_industrial_block_market_scope_correction]]
