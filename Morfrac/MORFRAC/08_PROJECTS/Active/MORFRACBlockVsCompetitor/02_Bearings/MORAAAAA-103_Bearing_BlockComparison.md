---
type: engineering_analysis
source_agent: Engineering
created: 2026-07-24
related_findings: []
related_concepts: []
related_projects:
  - MORFRACBlockVsCompetitor
related_reports: []
---

# Analysis

## Problem Statement

- Issue ID: MORAAAAA-103
- Date: 2026-07-24
- Task: compare MORFRAC and competitor rolling-element bearing arrangements and estimate radial bearing capability using Hertzian line-contact principles.
- Scope included:
  - Roller arrangement geometry
  - Estimated active roller count for a 180 deg loaded arc
  - Load per active roller
  - Inner race and outer race Hertzian line contact
  - Titanium roller option
  - Silicon nitride roller option for MORFRAC geometry
- Scope excluded:
  - Cheek plates
  - Attachments
  - Rope groove strength
  - Complete block structure
  - Radial clearance effects
  - Cage clearance effects
  - Manufacturing tolerance effects
  - Pin or race deformation effects
  - Dynamic factors
- Pressure calculated using projected area method; actual distribution not evaluated

## Inputs and Assumptions

- Supplied geometry:

| Parameter | MORFRAC titanium | Competitor titanium | MORFRAC silicon nitride |
|---|---:|---:|---:|
| Inner race diameter, Di | 82.2 mm | 74.85 mm | 82.2 mm |
| Roller diameter, Dr | 4.5 mm | 7.6 mm | 4.5 mm |
| Roller length, L | 12.0 mm | 10.15 mm | 12.0 mm |
| Rollers per row | 50 | 27 | 50 |
| Number of rows | 2 | 2 | 2 |
| Row included angle | 15 deg | 15 deg | 15 deg |
| Roller arrangement | Caged | Caged | Caged |
| Race material | Titanium Grade 5 | Titanium Grade 5 | Titanium Grade 5 |
| Roller material | Titanium Grade 5 | Titanium Grade 5 | Silicon nitride |

- Material values used from controlled material files:

| Material | E | nu | Density | Strength basis |
|---|---:|---:|---:|---:|
| Titanium Grade 5 | 114000 MPa | 0.34 | 4430 kg/m3 | yield 880 MPa, ultimate 950 MPa |
| Silicon nitride | 310000 MPa | 0.27 | 3210 kg/m3 | flexural 1000 MPa, compressive 3800 MPa |

- Load input:
  - Competitor published working load benchmark = 117.7 kN.
  - Load interpreted as rope tension because 180 deg wrap was supplied.
  - Radial sheave bearing load = 2 x rope tension = 235.4 kN.
- Loaded roller count:
  - 180 deg wrap means loaded arc fraction = 180 / 360 = 0.5.
  - Active roller count = rollers per row x rows x 0.5.
  - Actual load distribution was not evaluated.
  - Design load share per active roller = radial load / active roller count / cos(7.5 deg).
- Calculated dimensions:
  - Pitch diameter, Dp = Di + Dr.
  - Outer race diameter, Do = Di + 2 x Dr.
  - Pitch spacing = pi x Dp / rollers per row.
  - Circumferential gap = pitch spacing - Dr.
- Hertzian assumptions:
  - Parallel line contact.
  - Inner race contact reduced radius: R_inner = Rr x Ri / (Rr + Ri).
  - Outer race contact reduced radius: R_outer = Rr x Ro / (Ro - Rr).
  - Combined modulus: 1 / E_star = (1 - nu1^2) / E1 + (1 - nu2^2) / E2.
  - Contact half-width: b = sqrt((4 x Fn x R) / (pi x L x E_star)).
  - Maximum line-contact pressure: p0 = 2 x Fn / (pi x b x L).
- Safety factors:
  - Required FoS = 2.0.
  - No dynamic factor applied.
- Contact acceptance criterion:
  - Titanium contact-yield pressure limit = 1.9 x yield strength = 1672 MPa.
  - Titanium contact-yield allowable = 1672 / 2.0 = 836 MPa.
  - Titanium contact-ultimate pressure limit = 1.9 x ultimate tensile strength = 1805 MPa.
  - This criterion is a simplified Hertzian subsurface-yield screen, not a rolling bearing fatigue rating.

## Missing Inputs

- Exact race profile conformity.
- Race thickness.
- Raceway crown or edge relief.
- Surface finish.
- Lubrication condition.
- Saltwater contamination condition.
- Manufacturing tolerances.
- Radial clearance.
- Cage clearance.
- Actual measured loaded arc under deformation.
- Pin stiffness and inner-race support stiffness.
- Heat treatment beyond the controlled Titanium Grade 5 annealed data.
- Rolling contact fatigue allowables.
- Shock load case.

## Calculations

- Load conversion:
  - Rope tension benchmark = 117.7 kN.
  - 180 deg wrap radial load = 2 x 117.7 = 235.4 kN.
  - Row angle correction = cos(7.5 deg) = 0.9914.

- Geometry and active roller calculations:

| Case | Dp | Do | Pitch spacing | Circumferential gap | Active rollers |
|---|---:|---:|---:|---:|---:|
| MORFRAC titanium | 86.70 mm | 91.20 mm | 5.45 mm | 0.95 mm | 50.0 |
| Competitor titanium | 82.45 mm | 90.05 mm | 9.59 mm | 1.99 mm | 27.0 |
| MORFRAC silicon nitride | 86.70 mm | 91.20 mm | 5.45 mm | 0.95 mm | 50.0 |

- Load per active roller:

| Case | Equation | Fn |
|---|---|---:|
| MORFRAC titanium | 235.4 kN / 50.0 / cos(7.5 deg) | 4.75 kN |
| Competitor titanium | 235.4 kN / 27.0 / cos(7.5 deg) | 8.79 kN |
| MORFRAC silicon nitride | 235.4 kN / 50.0 / cos(7.5 deg) | 4.75 kN |

- Combined modulus:

| Contact pair | E_star |
|---|---:|
| Titanium roller on titanium race | 64450 MPa |
| Silicon nitride roller on titanium race | 93036 MPa |

- Hertzian contact results at 117.7 kN rope tension benchmark:

| Case | Inner contact width | Inner p0 | Outer contact width | Outer p0 | Governing contact |
|---|---:|---:|---:|---:|---|
| MORFRAC titanium | 0.258 mm | 1951 MPa | 0.272 mm | 1852 MPa | Inner race |
| Competitor titanium | 0.486 mm | 2270 MPa | 0.533 mm | 2069 MPa | Inner race |
| MORFRAC silicon nitride | 0.215 mm | 2344 MPa | 0.226 mm | 2225 MPa | Inner race |

- Static load capability based on titanium contact-yield limit, no Required FoS:

| Case | Rope tension at contact-yield limit | Radial load at contact-yield limit |
|---|---:|---:|
| MORFRAC titanium | 86.5 kN | 172.9 kN |
| Competitor titanium | 63.9 kN | 127.7 kN |
| MORFRAC silicon nitride | 59.9 kN | 119.8 kN |

- Working-load capability based on Required FoS = 2.0:

| Case | Defensible rope tension | Defensible radial load |
|---|---:|---:|
| MORFRAC titanium | 21.6 kN | 43.2 kN |
| Competitor titanium | 16.0 kN | 31.9 kN |
| MORFRAC silicon nitride | 15.0 kN | 29.9 kN |

- Roller mass estimate:

| Case | Mass per roller |
|---|---:|
| MORFRAC titanium | 0.845 g |
| Competitor titanium | 2.040 g |
| MORFRAC silicon nitride | 0.613 g |

- Effect of many smaller rollers versus fewer larger rollers:
  - MORFRAC has 100 total rollers versus competitor 54 total rollers.
  - MORFRAC has 50 active rollers in the 180 deg loaded arc versus competitor 27 active rollers.
  - MORFRAC titanium has lower design load share per active roller: 4.75 kN versus 8.79 kN.
  - Competitor larger roller diameter increases contact width, but the lower active roller count increases load per active roller.
  - MORFRAC smaller roller pitch gap is 0.95 mm, making cage control and debris tolerance more restrictive than the competitor 1.99 mm gap.
  - Competitor larger rollers have higher individual roller stiffness and larger contact width.
  - MORFRAC titanium arrangement has higher total active roller count and lower individual load, giving lower calculated contact stress than the competitor at the same 180 deg wrap benchmark.
  - Silicon nitride rollers increase E_star, reduce contact width, and increase titanium race contact stress.
  - Silicon nitride rollers reduce roller mass from 0.845 g to 0.613 g per roller for the same MORFRAC dimensions.
  - Silicon nitride rollers do not reduce titanium race indentation risk in this geometry.

## Results

- Concise comparison:

| Item | MORFRAC titanium | Competitor titanium | MORFRAC silicon nitride |
|---|---:|---:|---:|
| Total rollers | 100 | 54 | 100 |
| Active rollers used | 50.0 | 27.0 | 50.0 |
| Load per active roller | 4.75 kN | 8.79 kN | 4.75 kN |
| Governing p0 | 1951 MPa | 2270 MPa | 2344 MPa |
| Yield FoS | 0.86 | 0.74 | 0.71 |
| Ultimate FoS | 0.93 | 0.80 | 0.77 |
| Material FoS | 0.86 | 0.74 | 0.71 |
| Design margin | 0.43 | 0.37 | 0.36 |
| Utilization | 2.33 | 2.72 | 2.80 |
| Classification | FAIL | FAIL | FAIL |

- Benchmark plausibility:
  - Competitor published 117.7 kN rope tension benchmark produces calculated inner race contact pressure of 2270 MPa.
  - 2270 > 836 -> FAIL.
  - Published 117.7 kN rope tension does not pass the simplified Titanium Grade 5 contact-yield criterion with Required FoS = 2.0.
  - Published 117.7 kN rope tension also exceeds the calculated no-FoS contact-yield limit of 63.9 kN rope tension for the competitor geometry.
- MORFRAC titanium estimated working-load capability:
  - Defensible rope tension = 21.6 kN using Required FoS = 2.0.
  - Defensible radial load = 43.2 kN using Required FoS = 2.0.
- Ceramic roller conclusion:
  - Silicon nitride rollers reduce roller mass.
  - Silicon nitride rollers reduce elastic contact width.
  - Silicon nitride rollers increase calculated titanium race contact pressure from 1951 MPa to 2344 MPa.
  - Silicon nitride rollers transfer the governing limitation to the Titanium Grade 5 race.
  - Silicon nitride rollers do not increase MORFRAC working load in the evaluated titanium-race configuration.
  - Silicon nitride rollers are technically worthwhile only for mass and elastic-deflection reduction in this evaluated configuration, not for load-capacity increase.
  - Hardened metallic race inserts are required if ceramic rollers are to be used for higher working load than the titanium roller configuration.

## Governing Criterion

- Governing criterion: Titanium Grade 5 inner race Hertzian contact-yield allowable.
- Governing equation: p0 <= 836.
- Governing evaluated case: MORFRAC silicon nitride at 117.7 kN rope tension benchmark.
- Governing value: 2344 MPa.
- Strict evaluation: 2344 > 836 -> FAIL.

## Safety Assessment

- Required FoS = 2.0.
- Dynamic factor = not applied.
- Yield FoS:
  - MORFRAC titanium = 0.86.
  - Competitor titanium = 0.74.
  - MORFRAC silicon nitride = 0.71.
- Ultimate FoS:
  - MORFRAC titanium = 0.93.
  - Competitor titanium = 0.80.
  - MORFRAC silicon nitride = 0.77.
- Bearing/PV FoS:
  - Not applicable to rolling-element Hertzian line-contact calculation.
  - PV was not evaluated.
- Material FoS:
  - MORFRAC titanium = 0.86.
  - Competitor titanium = 0.74.
  - MORFRAC silicon nitride = 0.71.
- Design margin:
  - MORFRAC titanium = 0.43.
  - Competitor titanium = 0.37.
  - MORFRAC silicon nitride = 0.36.
- Utilization:
  - MORFRAC titanium = 2.33.
  - Competitor titanium = 2.72.
  - MORFRAC silicon nitride = 2.80.
- Classification:
  - MORFRAC titanium: 1951 > 836 -> FAIL.
  - Competitor titanium: 2270 > 836 -> FAIL.
  - MORFRAC silicon nitride: 2344 > 836 -> FAIL.
- Pass criterion:
  - Design margin >= 1.0 -> PASS.
- Evaluated design margins:
  - MORFRAC titanium design margin = 0.43 -> FAIL.
  - Competitor titanium design margin = 0.37 -> FAIL.
  - MORFRAC silicon nitride design margin = 0.36 -> FAIL.

## Recommendations

- Rank 1: add hardened replaceable inner and outer race inserts.
  - Capacity effect: addresses governing titanium race contact yield.
  - Friction effect: not quantified.
  - Manufacturing complexity: high.
  - Marine reliability: depends on insert material, corrosion isolation, sealing, and retained lubrication.
- Rank 2: increase MORFRAC roller diameter while maintaining active roller count as far as packaging allows.
  - Capacity effect: increases contact width and reduces contact pressure for titanium rollers.
  - Friction effect: not quantified.
  - Manufacturing complexity: medium.
  - Marine reliability: depends on cage spacing and debris clearance.
- Rank 3: increase inner-race and pin stiffness.
  - Capacity effect: protects loaded roller count and reduces edge-load sensitivity if deformation exists.
  - Friction effect: not quantified.
  - Manufacturing complexity: medium.
  - Marine reliability: depends on material pairing and corrosion control.

## Sources

- MORAAAAA-103 issue description and resume comments through 2026-07-24.
- 04_ENGINEERING/Materials/Titanium grade 5 Ti6Al4v controlled material file.
- 04_ENGINEERING/Materials/Silicon nitride bearing grade SN101C representative controlled material file.
- 00_SYSTEM/ENGINEERING_RULES.md.
- 00_SYSTEM/PROJECT_RULES.md.

---

## Related Links

- [MORAAAAA-103](app://obsidian.md/MORAAAAA-103)
