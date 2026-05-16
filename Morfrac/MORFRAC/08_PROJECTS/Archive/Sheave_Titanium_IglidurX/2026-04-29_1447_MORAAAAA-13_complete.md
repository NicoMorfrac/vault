# MORAAAAA-13 - Titanium Cheek Stress Analysis - COMPLETE

**Date**: 2026-04-29 14:47 UTC
**Status**: ✓ DONE - GO Decision
**Issue**: [MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13)
**Parent**: [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11) - Bearing test

---

## DECISION: ✓ GO

Titanium cheek structural analysis complete. **Design approved** with large safety margins.

---

## EXECUTIVE SUMMARY

### Key Results

- **Peak stress**: 38.0 MPa (combined at bearing hole edge)
- **Safety factor**: SF = 23.2 (requirement: SF ≥ 2.0) ✓
- **Stress vs yield**: 4.3% (requirement: ≤50%) ✓
- **Governing mode**: Cheek plate bending (34.7 MPa)
- **Weight**: ~230g total (two 6mm Ti-6Al-4V cheeks)
- **Decision**: **GO** - All structural checks pass

---

## STRESS ANALYSIS RESULTS

### Detailed Checks

| Stress Check | Value | Allowable | Utilization | Status |
|--------------|-------|-----------|-------------|--------|
| Bearing pressure | 4.17 MPa | 792 MPa | 0.5% | ✓ PASS |
| Bending stress | 34.7 MPa | 440 MPa | 7.9% | ✓ PASS |
| Tensile stress | 3.3 MPa | 440 MPa | 0.8% | ✓ PASS |
| Shear stress | 1.32 MPa | 254 MPa | 0.5% | ✓ PASS |
| **Combined peak** | **38.0 MPa** | **440 MPa** | **8.6%** | **✓ PASS** |

### Governing Failure Mode

**Cheek plate bending** governs at bearing hole edge:
- Stress: 34.7 MPa
- Utilization: 7.9%
- Location: Bearing hole edge, outer cheek face
- Mechanism: Pin load spreading cheek plates apart

---

## DESIGN INPUTS USED

### Geometry
- Sheave diameter: 75mm
- Bearing hole: 12mm diameter × 20mm length
- Cheek thickness: 6mm
- Material: Ti-6Al-4V (Grade 5)
  - Yield: 880 MPa
  - Ultimate: 950 MPa

### Loading
- Bearing radial load: 1000N
- Rope tension: 2000N max
- Wrap angle: 180°
- Duty: Intermittent
- Environment: Marine (saltwater)

---

## DESIGN STATUS

✓ **Structural integrity confirmed**  
✓ **Marine environment compatible** (Ti-6Al-4V excellent corrosion resistance)  
✓ **Fatigue life adequate** (7.5% of endurance limit, infinite life)  
✓ **Manufacturing feasible** (standard Ti machining)

---

## OPTIMIZATION OPPORTUNITIES

Design is **highly conservative** (SF = 23.2). Significant weight/cost reduction possible:

### Option 1: Reduce Thickness
- **Change**: 6mm → 3mm
- **Weight savings**: 50% (230g → 115g)
- **Cost savings**: ~50%
- **Safety factor**: Still >11 (very conservative)
- **Risk**: Minimal

### Option 2: Switch to Aluminum
- **Material**: 7075-T6 Aluminum (4mm)
- **Weight savings**: 60% (~95g)
- **Cost savings**: ~75%
- **Safety factor**: ~8 (adequate)
- **Requirement**: Hard anodizing for marine use

### Option 3: Downgrade Titanium
- **Material**: CP Ti Grade 2
- **Cost savings**: ~35%
- **Machinability**: Better (easier to machine)
- **Safety factor**: ~7 (adequate)
- **Corrosion**: Equal to Grade 5

**Recommendation**: Approve baseline, consider optimization for Rev 2 if weight/cost critical.

---

## DOCUMENTATION CREATED

### Calculation Report
**File**: `04_ENGINEERING/Calculations/Sheaves/Ti_cheek_stress_analysis_75mm_sheave.md`

**Contents**:
- Complete stress calculations with formulas
- Free body diagram description
- Failure mode analysis
- Fatigue assessment
- Weight estimates
- Detailed optimization analysis
- Material comparison tables
- Design verification checklist
- Sources and standards cited

---

## PROTOCOL APPLIED

### Analysis Methodology
1. Input sufficiency verification (Step 0)
2. Bearing pressure calculation
3. Cheek bending stress calculation
4. Tensile stress at net section (with K_t)
5. Shear tear-out check
6. Combined stress evaluation
7. Fatigue assessment
8. Weight estimation
9. Optimization analysis

### Standards Referenced
- **ISO 4565**: Wire rope sheaves
- **ABYC H-41**: Marine deck hardware
- **Peterson's**: Stress concentration factors
- **Bruhn**: Bearing stress allowables
- **ASM AMS 4928**: Ti-6Al-4V properties

---

## NEXT STEPS FOR CTO

1. ✓ **Structural analysis complete** - GO decision confirmed
2. **Review sister tasks**:
   - [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - Bearing PV validation
   - [MORAAAAA-14](/MORAAAAA/issues/MORAAAAA-14) - Thermal analysis
   - [MORAAAAA-15](/MORAAAAA/issues/MORAAAAA-15) - Cost-benefit analysis
3. **Make overall decision** on sheave concept per [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11)
4. **Consider optimization** if weight/cost reduction desired for Rev 2

---

## TASK PROGRESSION

**Initial**: 2026-04-29 14:17 - Checkout and input sufficiency check  
**Blocked**: 2026-04-29 14:20 - Awaiting design specifications  
**Unblocked**: 2026-04-29 14:27 - CTO provided baseline parameters  
**Analysis**: 2026-04-29 14:31-14:47 - Calculations and documentation  
**Complete**: 2026-04-29 14:47 - GO decision, issue closed

**Total duration**: ~30 minutes (excluding blocked time)

---

## LESSONS LEARNED

### What Worked Well
1. **Step 0 input sufficiency check**: Prevented wasted effort on incomplete specification
2. **Explicit blocking**: Clear communication of requirements to CTO
3. **Comprehensive analysis**: All failure modes checked systematically
4. **Optimization recommendations**: Added value beyond basic pass/fail
5. **Documentation**: Full calculation report for future reference

### Engineering Best Practices Applied
- No silent assumptions (verified inputs first)
- All calculations shown with formulas
- Assumptions explicitly stated
- Safety factors quoted
- Sources cited
- Governing failure mode identified
- Clear GO/NO-GO decision

---

## RELATED FILES

- **Parent plan**: [/MORAAAAA/issues/MORAAAAA-11#document-plan](/MORAAAAA/issues/MORAAAAA-11#document-plan)
- **Calculation report**: 04_ENGINEERING/Calculations/Sheaves/Ti_cheek_stress_analysis_75mm_sheave.md
- **Initial blocked log**: 2026-04-29_1420_MORAAAAA-13_blocked.md
- **Material data**: 04_ENGINEERING/Materials/iglidur_X_bearing_data.md (bearing material)
- **Engineering skills**: 02_AGENTS/Engineering/SKILLS/bearing_design.md.md
- **Task patterns**: 02_AGENTS/Engineering/TASK_PATERNS.md.md
