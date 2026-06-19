---
type: engineering_report
issue_id: MORAAAAA-99
project: LowFrictionSailHandlingSimplificationRetrofitKit
discipline: Decisions
created: 2026-06-19
status: FAIL
---

## Problem Statement
- Task: define preliminary engineering constraints for a low-friction sail-handling simplification retrofit kit.
- Source concept: low-friction sail-handling simplification retrofit kit from Product Incubation.
- Source feasibility report: MORAAAAA-97 feasibility report.
- Required decision: GO / HOLD recommendation for prototype development.
- Scope limit: no final dimensions produced.
- Scope limit: no CAD work performed.

## Inputs and Assumptions
- Input source: Product Incubation concept dated 2026-06-12.
- Input source: Product Incubation feasibility report dated 2026-06-12.
- Engineering assumption: first-release scope is limited to reefing path friction reduction, aft-led line separation, and line-tail stowage or clearance.
- Engineering assumption: headsail furling and in-mast furling optimization are excluded from first prototype scope.
- Engineering assumption: loads are treated as design loads when supplied.
- Engineering assumption: Required FoS = 2.0.
- Engineering assumption: no dynamic factor is applied.
- Engineering assumption: no final material selection is evaluated in this report.
- Engineering assumption: no final rope diameter is selected in this report.
- Engineering assumption: no load distribution is assumed.
- Engineering assumption: numerical likely line loads cannot be derived from the supplied documents without vessel, sail, rig, line, and reefing geometry inputs.

## Missing Inputs
- Boat size range for first release.
- Maximum mainsail area or reefed sail area.
- Reefing system type for first release: slab reefing, single-line reefing, or both.
- Rope tension design load for each loaded line.
- Rope deflection angle at each ring, sheave, fairlead, guide, and turning point.
- Number of reeving parts and load path for each reefing configuration.
- Rope diameter range.
- Rope construction and cover material.
- Rope minimum bend radius requirement.
- Sliding speed or line movement rate for PV checks.
- Duty cycle for reefing, easing, hoisting, and stowage actions.
- Target vessel attachment substrates: aluminum boom, stainless fitting, deck laminate, mast base, or existing padeye.
- Fastener size, spacing, edge distance, and backing condition.
- Mounting surface thickness and material.
- Environmental limits, including saltwater exposure, UV exposure, and temperature range.
- Required service interval.
- Acceptance criterion for friction reduction versus baseline routing.

## Calculations
- No numerical calculations were performed because design loads, geometry, materials, and boundary conditions were not supplied.
- Load case definition required before calculation:
  - Rope tension: T
  - Rope deflection angle: theta
  - Radial redirection load: F_radial = 2 x T x sin(theta / 2)
  - Mount resultant: sum of applied line reactions at each mounting point
- Bearing pressure method required for plain bearing or bushing checks:
  - P = F / (d x L)
  - Pressure calculated using projected area method; actual distribution not evaluated
- PV method required for sliding bearing, bushing, ring, or fairlead checks:
  - PV_operating = P x v
  - Material FoS = PV_max / PV_operating
  - PV_allowable = PV_max / Required FoS
  - Design margin = PV_allowable / PV_operating
  - PASS if Design margin >= 1.0
- Structural checks required before prototype release:
  - Pin shear stress check.
  - Pin bending stress check.
  - Bracket bearing stress check.
  - Bracket bending stress check.
  - Fastener tension and shear check.
  - Mounting substrate bearing and pullout check.
  - Edge-distance check.
  - Rope bend radius check.
  - Chafe and wear test requirement.

## Results
- Likely load origins identified:
  - Reefing line tension.
  - Radial redirection load at sheaves, rings, and fairleads.
  - Mounting fastener shear from line redirection.
  - Mounting fastener tension from bracket eccentricity.
  - Local bearing load at pins, bushings, sheaves, and rings.
  - Rope abrasion load at fairleads and stowage features.
- Likely rope diameter class cannot be numerically selected from supplied inputs.
- Friction reduction methods available for prototype screening:
  - Sheave module for loaded moving redirections where rope motion and wrap angle require rolling contact.
  - Low-friction ring module for simple compact redirection where load, motion, bend radius, and wear are validated.
  - Fairlead or guide module for line separation and low-deflection control where loaded redirection is not required.
- Preliminary architecture options:
  - Option A: reefing-only low-friction path module.
  - Option B: reefing path module plus cockpit line-separation module.
  - Option C: reefing path module plus cockpit line-separation module plus stowage or clearance module.
- Prototype scope:
  - Bench prototype only.
  - Adjustable reefing-path rig.
  - Interchangeable sheave, ring, and fairlead stations.
  - Instrumented line tension measurement.
  - Repeatable baseline path and modified path comparison.
  - Representative line diameters only after rope diameter inputs are supplied.
- Risk assessment:
  - Load underdefinition: High severity, High likelihood.
  - Geometry variance: High severity, High likelihood.
  - Chafe creation at new routing points: High severity, Medium likelihood.
  - Fastener or substrate overload: High severity, Medium likelihood.
  - Excessive product variant count: Medium severity, Medium likelihood.
  - Service access obstruction: Medium severity, Medium likelihood.
  - Scope expansion into furling diagnosis: High severity, Medium likelihood.

## Governing Criterion
- Governing criterion: input sufficiency for safe prototype development.
- Governing value: 0 complete numerical load cases supplied.
- Required value: at least 1 complete representative load case before structural or bearing validation.
- Utilization: N/A because no allowable value was supplied.
- Input deficit: 1 required complete load case - 0 supplied complete load cases = 1.
- Prototype development gate classification: 1 > 0 = FAIL.

## Safety Assessment
- Yield FoS: N/A.
- Ultimate FoS: N/A.
- Bearing/PV FoS: N/A.
- Material FoS: N/A.
- Design margin: N/A.
- Required FoS used for future checks: 2.0.
- Dynamic factor: none applied.
- PASS / FAIL status: FAIL.
- Governing failure mode: not evaluated because load cases, materials, and geometry are missing.
- Safety conclusion: does not pass for prototype development release using supplied inputs.
- Excluded checks:
  - Yield stress.
  - Ultimate stress.
  - Bearing stress.
  - PV limit.
  - Fastener pullout.
  - Mount substrate failure.
  - Rope bend radius.
  - Wear life.
  - Corrosion compatibility.

## Recommendations (only if requested)
- HOLD prototype development until the missing load, rope, geometry, material, and mounting inputs are supplied.
- Proceed only with non-load-rated bench layout mockup work if used to define measurement setup and user workflow, not to validate strength.
- First validation requirement: define at least one representative reefing load case with rope tension, deflection angle, rope diameter, mounting geometry, and attachment substrate.
- Second validation requirement: bench compare baseline route and modified route using measured line tension under the same input tension and path geometry.
- Third validation requirement: test sheave, ring, and fairlead options separately before selecting a first-release architecture.

## Sources
- C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\PRODUCT_INCUBATION\outputs\PRODUCT_CONCEPTS\2026-06-12_MORAAAAA-97_low-friction_sail-handling_simplification_retrofit_kit_concept.md
- C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\PRODUCT_INCUBATION\outputs\FEASIBILITY_REPORTS\2026-06-12_MORAAAAA-97_low-friction_sail-handling_simplification_retrofit_kit_feasibility.md
- C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\ENGINEERING_RULES.md
- C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\PROJECT_RULES.md

## Related Links
- [[2026-06-12_MORAAAAA-97_low-friction_sail-handling_simplification_retrofit_kit_concept]]
- [[2026-06-12_MORAAAAA-97_low-friction_sail-handling_simplification_retrofit_kit_feasibility]]
- [[MORAAAAA-99_Decisions_PrototypeGate]]
