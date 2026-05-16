# Project Index — Sheave Titanium Iglidur X

## Objective
Evaluate feasibility of titanium cheek sheave with iglidur X bearing.

## Scope
Includes:
- Structural cheek stresses
- Bearing pressure / PV
- Thermal effects
- Cost / material tradeoff

Excludes:
- Final production detailing (for now)

## Active Tasks
- MORAAAAA-13 Structural analysis - ✓ COMPLETE
- MORAAAAA-14 Bearing PV analysis - ✓ COMPLETE (1 kN baseline)
- MORAAAAA-17 Bearing PV analysis - ✓ COMPLETE (4 kN load case) - **NO-GO**
- MORAAAAA-18 Bearing PV analysis - ✓ COMPLETE (1t rope, 39 kN bearing load) - **CATASTROPHIC FAIL**
- MORAAAAA-15 Thermal analysis
- MORAAAAA-16 Cost-benefit analysis

## Design Inputs
- FoS target: 2.0
- Dynamic factor: 2.0
- Working geometry revision: pending

## Assumptions
- Current geometry provisional
- Marine duty loading
- Iglidur X as baseline bushing option

## Decisions
- Use project folder as primary record
- Bearing analyses include PV checks mandatory
- **CRITICAL:** Iglidur X bearing FAILS at 4 kN load (PV SF = 1.26 < 2.0 required)
- **CRITICAL:** 1-ton rope load (39 kN bearing) produces CATASTROPHIC FAILURE - exceeds all limits
- **DECISION:** Current 12mm × 20mm iglidur X concept is NOT VIABLE for loads >2.5 kN
- **DECISION:** 1-ton rope loads require rolling element bearing OR complete geometry redesign (2-3× larger components)

## Open Questions
- **CRITICAL: Is 1-ton rope specification correct? Current geometry can only handle ~64 kg rope loads**
- **Path forward: Rolling element bearing OR complete redesign with 2-3× larger components?**
- If plain bearing required: acceptable to increase pin to 25-30mm diameter, bearing to 50-60mm length?
- If load negotiable: can rope load be reduced to <70 kg to make current design viable?
- Continue with titanium cheeks if complete redesign required?
- Thermal analysis still relevant given fundamental sizing issue?
- Cost analysis meaningful when basic concept fails load requirements?

## Linked Analyses
- 01_Structures/MORAAAAA-13_Structural_TiCheek.md (✓ PASS - Ti cheek approved)
- 02_Bearings/MORAAAAA-12_Bearing_PV_Analysis.md (✓ PASS - 1 kN baseline, SF = 5.04)
- 02_Bearings/MORAAAAA-17_Bearing_IglidurX_4kN.md (❌ FAIL - 4 kN load, PV SF = 1.26)
- 02_Bearings/MORAAAAA-18_Bearing_IglidurX_1t_Redirect.md (❌ CATASTROPHIC FAIL - 39 kN load, PV exceeds limit by 778%, exceeds capacity by 15.7×)
- 03_Thermal/MORAAAAA-15_Thermal_Assessment.md
- 04_Cost/MORAAAAA-16_Cost_Trade_Study.md

## Status
Concept evaluation phase