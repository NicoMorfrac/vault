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
- Current revision status: COMPLETED for supplied maximum roller diameter.
- Latest correction: rollers are cylindrical; race is angled in by 15 deg.
- Latest clarified geometry: race is angled in by 15 deg.
- The previous conical-roller basis is superseded by the latest correction and must not be used for design acceptance.
- Combined roller diameter and quantity optimisation uses max roller diameter = 12.0 mm and gap >= 1.1 mm.
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
| MORFRAC angled race contact diameter, inner side | 87.89 mm | N/A | 87.89 mm |
| MORFRAC angled race contact diameter, external side | 94.36 mm | N/A | 94.36 mm |
| MORFRAC angled race transverse distance | 12.07 mm | N/A | 12.07 mm |
| MORFRAC maximum roller diameter for optimisation | 12.0 mm | N/A | N/A |

- Material values used from controlled material files:

| Material | E | nu | Density | Strength basis |
|---|---:|---:|---:|---:|
| Titanium Grade 5 | 114000 MPa | 0.34 | 4430 kg/m3 | yield 880 MPa, ultimate 950 MPa |
| Silicon nitride | 310000 MPa | 0.27 | 3210 kg/m3 | flexural 1000 MPa, compressive 3800 MPa |

- Load input:
  - Competitor published working load benchmark = 12000 kgf = 117.7 kN total block load.
  - Load interpreted as total radial block load for a 180 deg wrap.
  - Line tension = 117.7 / 2 = 58.9 kN = 6.0 T.
  - Radial sheave bearing load = 117.7 kN.
- Loaded roller count:
  - 180 deg wrap means loaded arc fraction = 180 / 360 = 0.5.
  - Active roller count = rollers per row x rows x 0.5.
  - Actual load distribution was not evaluated.
  - MORFRAC design load share per active roller = radial load / active roller count / cos(15 deg).
  - Competitor design load share per active roller = radial load / active roller count / cos(7.5 deg).
- Calculated dimensions:
  - Competitor pitch diameter, Dp = Di + Dr.
  - Competitor outer race diameter, Do = Di + 2 x Dr.
  - MORFRAC angled race mean contact diameter = (87.89 + 94.36) / 2 = 91.13 mm.
  - MORFRAC roller center pitch diameter = angled race mean contact diameter + Dr.
  - MORFRAC Hertzian contact length = 12.0 mm cylindrical roller length.
  - Pitch spacing = pi x roller center pitch diameter / rollers per row.
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
- Minimum manufacturable cage web and pocket clearance for roller-size optimisation.
- Outer or sheave conical race contact diameter at each side of each roller row.
- Roller axis angle and contact-normal angle for the cylindrical roller on conical races.
- Race conformity between cylindrical rollers and conical race surfaces.

## Calculations

- Load conversion:
  - Total block load benchmark = 117.7 kN.
  - 180 deg wrap line tension = 117.7 / 2 = 58.9 kN.
  - Radial bearing load = 117.7 kN.
  - MORFRAC contact angle correction = cos(15 deg) = 0.9659.
  - Competitor row angle correction = cos(7.5 deg) = 0.9914.

- Geometry and active roller calculations:

| Case | Dp | Do | Pitch spacing | Circumferential gap | Active rollers |
|---|---:|---:|---:|---:|---:|
| MORFRAC titanium | 91.13 mm | 95.63 mm | 5.73 mm | 1.23 mm | 50.0 |
| Competitor titanium | 82.45 mm | 90.05 mm | 9.59 mm | 1.99 mm | 27.0 |
| MORFRAC silicon nitride | 91.13 mm | 95.63 mm | 5.73 mm | 1.23 mm | 50.0 |

- Load per active roller:

| Case | Equation | Fn |
|---|---|---:|
| MORFRAC titanium | 117.7 kN / 50.0 / cos(15 deg) | 2.44 kN |
| Competitor titanium | 117.7 kN / 27.0 / cos(7.5 deg) | 4.40 kN |
| MORFRAC silicon nitride | 117.7 kN / 50.0 / cos(15 deg) | 2.44 kN |

- Combined modulus:

| Contact pair | E_star |
|---|---:|
| Titanium roller on titanium race | 64450 MPa |
| Silicon nitride roller on titanium race | 93036 MPa |

- Hertzian contact results at 117.7 kN total block load benchmark:

| Case | Inner contact width | Inner p0 | Outer contact width | Outer p0 | Governing contact |
|---|---:|---:|---:|---:|---|
| MORFRAC titanium | 0.182 mm | 1368 MPa | 0.189 mm | 1302 MPa | Inner race |
| Competitor titanium | 0.344 mm | 1605 MPa | 0.377 mm | 1463 MPa | Inner race |
| MORFRAC silicon nitride | 0.151 mm | 1643 MPa | 0.157 mm | 1564 MPa | Inner race |

- Static load capability based on titanium contact-yield limit, no Required FoS:

| Case | Rope tension at contact-yield limit | Radial load at contact-yield limit |
|---|---:|---:|
| MORFRAC titanium | 88.0 kN | 175.9 kN |
| Competitor titanium | 63.9 kN | 127.7 kN |
| MORFRAC silicon nitride | 60.9 kN | 121.9 kN |

- Working-load capability based on Required FoS = 2.0:

| Case | Defensible rope tension | Defensible radial load |
|---|---:|---:|
| MORFRAC titanium | 22.0 kN | 44.0 kN |
| Competitor titanium | 16.0 kN | 31.9 kN |
| MORFRAC silicon nitride | 15.2 kN | 30.5 kN |

- Roller mass estimate:

| Case | Mass per roller |
|---|---:|
| MORFRAC titanium | 0.845 g |
| Competitor titanium | 2.040 g |
| MORFRAC silicon nitride | 0.613 g |

- MORFRAC titanium conical roller-size optimisation sensitivity:
  - Mean pitch diameter fixed at 91.13 mm from supplied conical geometry.
  - Nominal roller length fixed at 12.0 mm.
  - Conical contact length fixed at 12.50 mm.
  - Total radial block load fixed at 117.7 kN.
  - Number of rows fixed at 2.
  - Loaded arc fixed at 180 deg.
  - Contact angle fixed at 15 deg.
  - Roller count fixed at 50 per row.
  - Effective mean inner race diameter = Dp - Dr.
  - Effective mean outer race diameter = Dp + Dr.
  - This is a fixed-envelope packing sensitivity, not a final manufacturing definition.

| Roller diameter | Rollers per row | Gap | Load per active roller | Inner p0 | Outer p0 | Design margin | Utilization | Defensible radial load |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.5 mm | 50 | 1.23 mm | 2.44 kN | 1368 MPa | 1302 MPa | 0.61 | 1.64 | 44.0 kN |
| 5.0 mm | 50 | 0.73 mm | 2.44 kN | 1301 MPa | 1232 MPa | 0.64 | 1.56 | 48.6 kN |
| 5.5 mm | 50 | 0.23 mm | 2.44 kN | 1244 MPa | 1171 MPa | 0.67 | 1.49 | 53.1 kN |

- MORFRAC titanium conical roller-count optimisation sensitivity:
  - Mean pitch diameter fixed at 91.13 mm.
  - Roller diameter fixed at 4.5 mm.
  - Conical contact length fixed at 12.50 mm.
  - Total radial block load fixed at 117.7 kN.
  - Number of rows fixed at 2.
  - Loaded arc fixed at 180 deg.
  - Contact angle fixed at 15 deg.
  - Active roller count = rollers per row for the two-row 180 deg loaded arc.
  - Circumferential gap = pi x 91.13 / rollers per row - 4.5.

| Rollers per row |     Gap | Load per active roller | Inner p0 | Outer p0 | Design margin | Utilization | Defensible radial load |
| --------------: | ------: | ---------------------: | -------: | -------: | ------------: | ----------: | ---------------------: |
|              35 | 3.68 mm |                3.48 kN | 1635 MPa | 1556 MPa |          0.51 |        1.96 |                30.8 kN |
|              40 | 2.66 mm |                3.05 kN | 1529 MPa | 1455 MPa |          0.55 |        1.83 |                35.2 kN |
|              45 | 1.86 mm |                2.71 kN | 1442 MPa | 1372 MPa |          0.58 |        1.72 |                39.6 kN |
|              50 | 1.23 mm |                2.44 kN | 1368 MPa | 1302 MPa |          0.61 |        1.64 |                44.0 kN |
|              55 | 0.71 mm |                2.22 kN | 1304 MPa | 1241 MPa |          0.64 |        1.56 |                48.4 kN |
|              58 | 0.44 mm |                2.10 kN | 1270 MPa | 1209 MPa |          0.66 |        1.52 |                51.0 kN |
|              60 | 0.27 mm |                2.03 kN | 1249 MPa | 1188 MPa |          0.67 |        1.49 |                52.8 kN |
|              62 | 0.12 mm |                1.97 kN | 1228 MPa | 1169 MPa |          0.68 |        1.47 |                54.5 kN |
|              63 | 0.04 mm |                1.93 kN | 1218 MPa | 1160 MPa |          0.69 |        1.46 |                55.4 kN |

- MORFRAC titanium combined roller diameter and roller-count optimisation with gap >= 1.1 mm:
  - Angled race mean contact diameter fixed at 91.13 mm.
  - Roller center pitch diameter = 91.13 mm + roller diameter.
  - Hertzian contact length fixed at cylindrical roller length = 12.0 mm.
  - Total radial block load fixed at 117.7 kN.
  - Number of rows fixed at 2.
  - Loaded arc fixed at 180 deg.
  - Contact angle fixed at 15 deg.
  - Roller diameter swept from 4.5 mm to 12.0 mm in 0.01 mm increments.
  - For each roller diameter, rollers per row set to maximum integer satisfying gap >= 1.1 mm.
  - Contact stress evaluated on the supplied angled Titanium Grade 5 race.

| Roller diameter | Rollers per row |     Gap | Load per active roller |  Race p0 | Design margin | Utilization | Defensible radial load |
| --------------: | --------------: | ------: | ---------------------: | -------: | ------------: | ----------: | ---------------------: |
|          4.5 mm |              53 | 1.17 mm |                2.30 kN | 1354 MPa |          0.62 |        1.62 |                44.9 kN |
|          5.5 mm |              45 | 1.25 mm |                2.71 kN | 1336 MPa |          0.63 |        1.60 |                46.1 kN |
|          6.0 mm |              42 | 1.26 mm |                2.90 kN | 1327 MPa |          0.63 |        1.59 |                46.7 kN |
|          7.0 mm |              38 | 1.11 mm |                3.21 kN | 1299 MPa |          0.64 |        1.55 |                48.8 kN |
|          8.0 mm |              34 | 1.16 mm |                3.58 kN | 1291 MPa |          0.65 |        1.54 |                49.4 kN |
|         10.0 mm |              28 | 1.35 mm |                4.35 kN | 1285 MPa |          0.65 |        1.54 |                49.8 kN |
|         11.8 mm |              25 | 1.11 mm |                4.87 kN | 1262 MPa |          0.66 |        1.51 |                51.7 kN |
|         12.0 mm |              24 | 1.50 mm |                5.08 kN | 1280 MPa |          0.65 |        1.53 |                50.2 kN |

- Effect of many smaller rollers versus fewer larger rollers:
  - MORFRAC has 100 total rollers versus competitor 54 total rollers.
  - MORFRAC has 50 active rollers in the 180 deg loaded arc versus competitor 27 active rollers.
  - MORFRAC titanium has lower design load share per active roller: 2.44 kN versus 4.40 kN.
  - Competitor larger roller diameter increases contact width, but the lower active roller count increases load per active roller.
  - MORFRAC smaller roller pitch gap is 1.23 mm, making cage control and debris tolerance more restrictive than the competitor 1.99 mm gap.
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
| Load per active roller | 2.44 kN | 4.40 kN | 2.44 kN |
| Governing p0 | 1368 MPa | 1605 MPa | 1643 MPa |
| Yield FoS | 1.22 | 1.04 | 1.02 |
| Ultimate FoS | 1.32 | 1.12 | 1.10 |
| Material FoS | 1.22 | 1.04 | 1.02 |
| Design margin | 0.61 | 0.52 | 0.51 |
| Utilization | 1.64 | 1.92 | 1.97 |
| Classification | FAIL | FAIL | FAIL |

- Benchmark plausibility:
  - Competitor published 117.7 kN total block load benchmark produces calculated inner race contact pressure of 1605 MPa.
  - 1605 > 836 -> FAIL.
  - Published 117.7 kN total block load does not pass the simplified Titanium Grade 5 contact-yield criterion with Required FoS = 2.0.
  - Published 117.7 kN total block load is below the calculated no-FoS contact-yield limit of 127.7 kN total radial load for the competitor geometry.
- MORFRAC titanium estimated working-load capability:
  - Defensible line tension = 22.0 kN using Required FoS = 2.0.
  - Defensible radial load = 44.0 kN using Required FoS = 2.0.
- Ceramic roller conclusion:
  - Silicon nitride rollers reduce roller mass.
  - Silicon nitride rollers reduce elastic contact width.
  - Silicon nitride rollers increase calculated titanium race contact pressure from 1368 MPa to 1643 MPa.
  - Silicon nitride rollers transfer the governing limitation to the Titanium Grade 5 race.
  - Silicon nitride rollers do not increase MORFRAC working load in the evaluated titanium-race configuration.
  - Silicon nitride rollers are technically worthwhile only for mass and elastic-deflection reduction in this evaluated configuration, not for load-capacity increase.
  - Hardened metallic race inserts are required if ceramic rollers are to be used for higher working load than the titanium roller configuration.
- Roller-size optimisation conclusion:
  - Best evaluated fixed-envelope titanium roller diameter is 5.5 mm with 50 rollers per row.
  - 5.5 mm x 50 rollers per row gives inner p0 = 1244 MPa.
  - 1244 > 836 -> FAIL.
  - Design margin improves from 0.61 to 0.67.
  - Defensible radial load improves from 44.0 kN to 53.1 kN.
  - Capacity increase from 4.5 mm x 50 rollers per row to 5.5 mm x 50 rollers per row = 53.1 / 44.0 = 1.21.
  - 5.5 mm x 50 rollers per row leaves 0.23 mm calculated circumferential gap.
  - The 0.23 mm gap requires cage and manufacturing validation before acceptance.
  - Roller diameter optimisation alone does not change classification.
- Roller-count optimisation conclusion:
  - If current 1.23 mm circumferential gap is retained as the minimum spacing constraint, 50 rollers per row is already the maximum count.
  - Increasing count above 50 reduces p0 but also reduces circumferential gap.
  - 60 rollers per row gives inner p0 = 1249 MPa with 0.27 mm calculated gap.
  - 1249 > 836 -> FAIL.
  - Maximum geometric count before negative gap is 63 rollers per row.
  - 63 rollers per row gives inner p0 = 1218 MPa with 0.04 mm calculated gap.
  - 1218 > 836 -> FAIL.
  - Required roller count to reach p0 <= 836 by roller count alone is approximately 134 rollers per row.
  - 134 rollers per row is not geometrically possible with 4.5 mm rollers on 91.13 mm pitch diameter.
  - Roller count optimisation alone does not change classification.
- Combined roller diameter and count optimisation conclusion:
  - Best evaluated gap-constrained point with Dr <= 12.0 mm is 11.8 mm rollers with 25 rollers per row.
  - Gap = 1.11 mm.
  - Race p0 = 1262 MPa.
  - 1262 > 836 -> FAIL.
  - Design margin = 0.66.
  - Defensible radial load = 51.7 kN.
  - Capacity increase from current 4.5 mm x 50 rollers per row = 51.7 / 44.0 = 1.18.
  - Combined roller diameter and count optimisation alone does not change classification.

## Governing Criterion

- Governing criterion: Titanium Grade 5 inner race Hertzian contact-yield allowable.
- Governing equation: p0 <= 836.
- Governing evaluated case: MORFRAC silicon nitride at 117.7 kN total block load benchmark.
- Governing value: 1643 MPa.
- Strict evaluation: 1643 > 836 -> FAIL.

## Safety Assessment

- Required FoS = 2.0.
- Dynamic factor = not applied.
- Yield FoS:
  - MORFRAC titanium = 1.22.
  - Competitor titanium = 1.04.
  - MORFRAC silicon nitride = 1.02.
- Ultimate FoS:
  - MORFRAC titanium = 1.32.
  - Competitor titanium = 1.12.
  - MORFRAC silicon nitride = 1.10.
- Bearing/PV FoS:
  - Not applicable to rolling-element Hertzian line-contact calculation.
  - PV was not evaluated.
- Material FoS:
  - MORFRAC titanium = 1.22.
  - Competitor titanium = 1.04.
  - MORFRAC silicon nitride = 1.02.
- Design margin:
  - MORFRAC titanium = 0.61.
  - Competitor titanium = 0.52.
  - MORFRAC silicon nitride = 0.51.
- Utilization:
  - MORFRAC titanium = 1.64.
  - Competitor titanium = 1.92.
  - MORFRAC silicon nitride = 1.97.
- Classification:
  - MORFRAC titanium: 1368 > 836 -> FAIL.
  - Competitor titanium: 1605 > 836 -> FAIL.
  - MORFRAC silicon nitride: 1643 > 836 -> FAIL.
- Pass criterion:
  - Design margin >= 1.0 -> PASS.
- Evaluated design margins:
  - MORFRAC titanium design margin = 0.61 -> FAIL.
  - Competitor titanium design margin = 0.52 -> FAIL.
  - MORFRAC silicon nitride design margin = 0.51 -> FAIL.

## Recommendations

- Rank 1: add hardened replaceable inner and outer race inserts.
  - Capacity effect: addresses governing titanium race contact yield.
  - Friction effect: not quantified.
  - Manufacturing complexity: high.
  - Marine reliability: depends on insert material, corrosion isolation, sealing, and retained lubrication.
- Rank 2: optimise MORFRAC titanium roller diameter and count with gap >= 1.1 mm.
  - Capacity effect: best evaluated variant is 11.8 mm x 25 rollers per row, reducing p0 from 1368 MPa to 1262 MPa.
  - Friction effect: not quantified.
  - Manufacturing complexity: medium.
  - Marine reliability: depends on cage spacing and debris clearance.
  - Classification effect: 1262 > 836 -> FAIL.
- Rank 3: increase MORFRAC roller count only if gap below 1.1 mm is later accepted.
  - Capacity effect: 60 rollers per row with 4.5 mm rollers reduces p0 from 1368 MPa to 1249 MPa.
  - Friction effect: not quantified.
  - Manufacturing complexity: medium.
  - Marine reliability: depends on cage web strength, debris clearance, and corrosion control.
  - Classification effect: 1249 > 836 -> FAIL.

## Sources

- MORAAAAA-103 issue description and resume comments through 2026-07-24.
- 04_ENGINEERING/Materials/Titanium grade 5 Ti6Al4v controlled material file.
- 04_ENGINEERING/Materials/Silicon nitride bearing grade SN101C representative controlled material file.
- 00_SYSTEM/ENGINEERING_RULES.md.
- 00_SYSTEM/PROJECT_RULES.md.

---

## Related Links

- [MORAAAAA-103](app://obsidian.md/MORAAAAA-103)
