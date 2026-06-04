---
type: b2b_raw_finding
source_agent: B2B_Problem_Discovery
created: 2026-05-24
related_findings:
  - MORAAAAA-86_RETROFIT_rigging_deck_hardware_load_path_uncertainty
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - MECHANICAL_INTEGRATION_COMPLEXITY
  - RETROFIT_COMPLEXITY
  - SERVICEABILITY_COMPLEXITY
related_projects: []
related_reports:
  - 2026-05-24_MORAAAAA-91_rigger_and_refit_yard_workflow_bottlenecks_summary
---

# MORAAAAA-91-02 Rig-specific measurement and sequencing uncertainty in rigging refits

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| YBW Forum | https://forums.ybw.com/threads/chainplates-on-a-cobra-850.453446/ | 2016-04-03 | Standing-rigging renewal and chainplate follow-on discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/new-rigging-shroud-length-question.601526/ | 2023-09-28 | Rigging replacement and adjustment discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/lazy-jacks-used-furler-install-mast-down-or-up.477913/ | 2017-05-02 | Furler retrofit measurement discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/finally-own-the-westerly-longbow.464974/ | 2016-09-21 | Refit planning and standing-rigging replacement discussion | MEDIUM |
| Cruisers Forum | https://www.cruisersforum.com/forums/f116/standing-rigging-replacement-concerns-258908-2.html | 2021-12-24 | Rigger and owner implementation discussion | HIGH |

---

# INDUSTRY_SEGMENT

RIGGERS

---

# PROBLEM_TYPE

DOCUMENTATION

---

# OPPORTUNITY_TYPE

ENGINEERING_SERVICE

---

# SUMMARY

Rigging refits repeatedly suffer from the same workflow failure: installers cannot rely on generic boat specs or nominal part replacement because each vessel carries its own accumulated geometry, adjustment state, chainplate condition, furler stack-up, and sequencing constraints. The visible symptom is incorrect stay length, bottomed-out turnbuckles, extra toggles/spacers, or missed inspection windows. The root problem is the absence of a trusted, rig-specific intake and measurement standard before fabrication and installation work begins.

---

# EVIDENCE

## Directly observed evidence

- In `Chainplates on a Cobra 850`, the owner reports that standing rigging was renewed before the chainplates were examined because `the rigger had a slot and me not being ready`. The inspection dependency surfaced after fabrication timing was already committed, showing how sequencing pressure can outrun structural verification.
- In `New rigging - shroud length question`, the owner worries the new stays were cut materially too long, with the forestay nearly bottomed out before proper tension. Replies discuss mast rake, pre-bend, chainplate position, mast-step packing, re-swaging, short-body rigging screws, and responsibility for who measured the job.
- In `Lazy Jacks & Used Furler Install Mast Down or Up`, contributors note that many furler retrofits require a new forestay and that exact measurement is critical because there may be no turnbuckle available inside the system. Access choice and measurement choice are coupled.
- In `Finally Own the Westerly Longbow`, owners recommend keeping the old rigging to verify lengths, warn that doing one stay at a time is inefficient, and note that furler conversion may require on-site cut-to-length terminals if mast dropping is avoided. The discussion frames mast-down batching as a way to reduce measurement uncertainty and repeated labor.
- In the Cruisers Forum `standing rigging replacement concerns` thread, a working rigger states that duplicating old wire eye-to-eye still leaves variables from mast compression, deck fittings, and chainplates, and that on-site compensation with extra fittings or turnbuckles is often required. The same discussion warns that drop-shipped rigging increases the error window, especially when a headstay was measured incorrectly during a furler install.

## Repeated pattern

- Fabrication errors are rarely pure shop mistakes; they often come from ambiguous intake conditions such as unknown turnbuckle adjustment range, mixed old/new hardware, changed furler stack height, or chainplate geometry that differs from nominal drawings.
- Sequencing matters as much as measurement. Owners and installers repeatedly discover that chainplate inspection, mast access, forestay replacement, furler retrofit, and final rig tune cannot be safely treated as independent tasks.
- When intake is weak, installers compensate late with toggles, spacers, mast-step packing, re-swaging, or repeat visits, increasing labor and reducing confidence.

---

# ROOT CAUSE ANALYSIS

## Symptom

- New stays arrive too long or too short
- Turnbuckles have poor adjustment margin
- Forestay/furler combinations force rework
- Important inspections happen after fabrication windows are booked

## Likely root operational causes

- Real boats drift away from nominal geometry through prior repairs, mast-step changes, chainplate movement, deck compression, and mixed-brand retrofits.
- Many legacy installations do not preserve reliable as-built measurement records, adjustment positions, or part-stack documentation.
- Riggers are pushed to fabricate before all upstream checks are complete because lift slots, seasonal yard windows, and customer availability compress sequencing.
- Furlers, fixed-length stays, and swaged terminals reduce post-fabrication adjustment room, so small intake errors produce expensive rework.

---

# OPERATIONAL IMPACT

- Fabrication and installation loops become iterative instead of right-first-time.
- Yard slots are consumed by avoidable re-measurement, re-swaging, extra fittings, and delayed tuning.
- Responsibility disputes emerge over whether the fault belongs to the measurer, the fabricator, the yard, or the owner-supplied hardware.
- Installers inherit higher callback risk because a rig that can be assembled is not necessarily a rig with adequate future adjustment margin.

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

Observed evidence supports a rig-specific retrofit intake and geometry-validation service: pre-fabrication measurement protocol, turnbuckle-range capture, furler stack-up verification, chainplate/attachment dependency checklist, and install-sequence planning that reduces late-stage compensation and ownership disputes for riggers and refit yards.

This is an interpretation from repeated technical friction, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- Convergence signals: `ENGINEERING_UNCERTAINTY`, `RETROFIT_COMPLEXITY`, `MECHANICAL_INTEGRATION_COMPLEXITY`.
- This finding is adjacent to `MORAAAAA-86`, but the dominant problem here is workflow-grade measurement and sequencing uncertainty rather than load-path uncertainty itself.
- The recurring value appears to be diagnosis, intake normalization, and fabrication readiness, not a commodity rigging product.

## Related Links

### Findings
- [[MORAAAAA-86_RETROFIT_rigging_deck_hardware_load_path_uncertainty]]

### Concepts
- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[SERVICEABILITY_COMPLEXITY]]

### Reports
- [[2026-05-24_MORAAAAA-91_rigger_and_refit_yard_workflow_bottlenecks_summary]]
