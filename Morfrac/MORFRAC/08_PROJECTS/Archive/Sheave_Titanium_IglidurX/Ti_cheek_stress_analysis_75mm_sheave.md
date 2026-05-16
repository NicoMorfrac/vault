# Titanium Cheek Stress Analysis - 75mm Sheave

**Project**: Sheave Bearing Assessment  
**Issue**: [MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13)  
**Parent**: [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11)  
**Date**: 2026-04-29  
**Engineer**: MORFRAC Engineering Agent  
**Status**: ✓ GO - Design Approved

---

## EXECUTIVE SUMMARY

**Decision**: ✓ **GO** - Structural integrity confirmed with large safety margins

**Key Results**:
- Peak stress: 38.0 MPa (4.3% of yield)
- Safety factor: 23.2 (exceeds required SF ≥ 2.0)
- Governing mode: Cheek plate bending at bearing hole
- Weight: ~230g (two cheeks)

**Recommendations**:
1. Approve baseline 6mm Ti-6Al-4V design
2. Consider optimization opportunities (50% weight reduction possible)
3. Evaluate lower-cost material alternatives (CP Ti Gr2 or 7075-T6 Al)

---

## 1. PROBLEM STATEMENT

Calculate stresses in Ti-6Al-4V cheek plates for a 75mm diameter rope sheave with polymer bearing under marine rigging loads. Verify stress remains below 50% of yield strength (SF ≥ 2.0) per GO criteria.

---

## 2. DESIGN INPUTS

### Geometry
- **Sheave outer diameter**: D = 75mm (radius R = 37.5mm)
- **Bearing hole diameter**: d = 12mm (radius r = 6mm)
- **Bearing length**: L = 20mm
- **Cheek thickness**: t = 6mm

### Loading
- **Bearing radial load**: F = 1000N
- **Rope tension**: T = 2000N (max)
- **Rope diameter**: 10mm
- **Wrap angle**: 180°
- **Duty cycle**: Intermittent

### Material: Ti-6Al-4V (Grade 5)
- **Yield strength**: σ_y = 880 MPa
- **Ultimate strength**: σ_u = 950 MPa
- **Density**: ρ = 4.43 g/cm³
- **Endurance limit**: ~510 MPa

### Environment
- **Application**: Marine rigging
- **Environment**: Saltwater
- **Corrosion resistance**: Excellent (Ti-6Al-4V)

### Design Criteria
- **Required safety factor**: SF ≥ 2.0
- **Allowable stress**: σ_allow = σ_y / 2.0 = 440 MPa
- **GO criterion**: Stress ≤ 50% yield strength

---

## 3. ASSUMPTIONS

1. **Load distribution**: Pin load split equally between two cheek plates (500N per cheek)
2. **Configuration**: Double-shear bearing arrangement
3. **Dynamic loads**: Already included in stated 1000N bearing load
4. **Cheek geometry**: Circular disc with central bearing hole
5. **Load path**: From bearing hole through cheek material to outer rim
6. **Boundary conditions**: Conservative cantilever bending from bearing hole
7. **Stress concentration**: K_t = 2.5 for hole in plate under tension
8. **Material condition**: Annealed or solution-treated Ti-6Al-4V

---

## 4. CALCULATIONS

### 4.1 BEARING PRESSURE (Pin on Bore)

Contact stress between pin and bearing bore:

**Formula**:
```
P_bearing = F / (d × L)
```

**Calculation**:
```
P_bearing = 1000N / (12mm × 20mm)
P_bearing = 1000 / 240
P_bearing = 4.17 MPa
```

**Allowable bearing pressure** (Ti-6Al-4V on steel pin):
```
P_allow = 0.9 × σ_y = 0.9 × 880 = 792 MPa
```

**Check**:
```
Utilization = 4.17 / 792 = 0.5%
```
✓ **PASS** - Bearing pressure negligible

---

### 4.2 CHEEK PLATE BENDING STRESS

The cheek plates experience bending as the pin load attempts to spread them apart.

**Load per cheek** (double shear):
```
F_cheek = F / 2 = 1000 / 2 = 500N
```

**Bending moment arm**:
```
a = L / 2 = 20mm / 2 = 10mm
```
(Distance from pin centerline to cheek plate)

**Bending moment**:
```
M = F_cheek × a = 500N × 10mm = 5,000 N·mm
```

**Section modulus** at bearing hole:

Treating the critical section as a rectangular beam:
```
Z = (t × d²) / 6
Z = (6mm × (12mm)²) / 6
Z = (6 × 144) / 6
Z = 144 mm³
```

**Bending stress**:
```
σ_bending = M / Z = 5,000 N·mm / 144 mm³
σ_bending = 34.7 MPa
```

**Check**:
```
Utilization = 34.7 / 440 = 7.9%
```
✓ **PASS** - Well below allowable

---

### 4.3 TENSILE STRESS AT NET SECTION

Tensile load path from bearing hole to outer rim.

**Net section area**:

Critical section across the diameter through the bearing hole:
```
A_net = (D - d) × t
A_net = (75mm - 12mm) × 6mm
A_net = 63mm × 6mm
A_net = 378 mm²
```

**Nominal tensile stress**:
```
σ_nominal = F_cheek / A_net
σ_nominal = 500N / 378mm²
σ_nominal = 1.32 MPa
```

**Stress concentration factor**:
```
K_t = 2.5 (circular hole in finite-width plate, conservative)
```

**Peak tensile stress**:
```
σ_tensile_peak = K_t × σ_nominal
σ_tensile_peak = 2.5 × 1.32
σ_tensile_peak = 3.3 MPa
```

**Check**:
```
Utilization = 3.3 / 440 = 0.8%
```
✓ **PASS** - Minimal tensile stress

---

### 4.4 SHEAR TEAR-OUT AT BEARING HOLE

Shear failure mode: tearing through cheek from bearing hole to outer edge.

**Edge distance**:
```
e = R - r = 37.5mm - 6mm = 31.5mm
```

**Shear area** (two shear planes):
```
A_shear = 2 × e × t
A_shear = 2 × 31.5mm × 6mm
A_shear = 378 mm²
```

**Shear stress**:
```
τ = F_cheek / A_shear
τ = 500N / 378mm²
τ = 1.32 MPa
```

**Shear yield strength** (von Mises criterion):
```
τ_y = σ_y / √3 = 880 / 1.732 = 508 MPa
```

**Allowable shear stress**:
```
τ_allow = τ_y / SF = 508 / 2.0 = 254 MPa
```

**Check**:
```
Utilization = 1.32 / 254 = 0.5%
```
✓ **PASS** - Shear stress negligible

---

### 4.5 COMBINED STRESS

Peak combined stress at bearing hole edge (bending + tension):

```
σ_combined = σ_bending + σ_tensile_peak
σ_combined = 34.7 + 3.3
σ_combined = 38.0 MPa
```

**Safety factor against yield**:
```
SF = σ_y / σ_combined
SF = 880 / 38.0
SF = 23.2
```

**Percentage of yield**:
```
% Yield = (σ_combined / σ_y) × 100%
% Yield = (38.0 / 880) × 100%
% Yield = 4.3%
```

✓ **PASS** - Far below 50% yield GO criterion

---

## 5. RESULTS SUMMARY

| **Stress Check** | **Value** | **Allowable** | **Utilization** | **Status** |
|------------------|-----------|---------------|-----------------|------------|
| Bearing pressure | 4.17 MPa | 792 MPa | 0.5% | ✓ PASS |
| Bending stress | 34.7 MPa | 440 MPa | 7.9% | ✓ PASS |
| Tensile stress (w/ K_t) | 3.3 MPa | 440 MPa | 0.8% | ✓ PASS |
| Shear stress | 1.32 MPa | 254 MPa | 0.5% | ✓ PASS |
| **Combined peak stress** | **38.0 MPa** | **440 MPa** | **8.6%** | **✓ PASS** |

### Key Findings

**Peak stress location**: Bearing hole edge, bending plane at outer cheek face

**Governing failure mode**: Cheek plate bending (34.7 MPa, 7.9% utilization)

**Actual safety factor**: SF = 23.2 (requirement: SF ≥ 2.0) ✓

**Stress vs yield**: 4.3% (requirement: ≤ 50%) ✓

---

## 6. GOVERNING FAILURE MODE

**Cheek plate bending** governs at **34.7 MPa** (7.9% of allowable).

This stress occurs at the bearing hole edge where the pin load creates a bending moment attempting to spread the cheek plates apart.

**Failure sequence** (in order of likelihood):
1. **Cheek bending**: Most highly stressed, but still very low utilization
2. **Tensile tear-out**: Across net section from hole to rim
3. **Shear tear-out**: Through edge distance from hole to rim
4. **Bearing crush**: At pin/bore interface (negligible stress)

**Conclusion**: All failure modes have large margins. Design is structurally sound and highly conservative.

---

## 7. FATIGUE ASSESSMENT

### Stress Amplitude
For intermittent duty cycle with peak stress of 38 MPa:

**Endurance limit** (Ti-6Al-4V):
```
σ_e ≈ 510 MPa (smooth specimen, fully reversed)
```

**Fatigue margin**:
```
Margin = σ_e / σ_combined = 510 / 38.0 = 13.4
```

**Stress ratio**:
```
% of endurance = (38.0 / 510) × 100% = 7.5%
```

**Fatigue life**: Effectively **infinite** at this stress level

✓ **Fatigue not a concern** for this design

---

## 8. WEIGHT ESTIMATE

### Current Baseline Design (6mm cheek, Ti-6Al-4V)

**Volume per cheek**:
```
V = π × (R² - r²) × t
V = π × (37.5² - 6²) × 6
V = π × (1406.25 - 36) × 6
V = π × 1370.25 × 6
V = 25,800 mm³ = 25.8 cm³
```

**Weight per cheek**:
```
W = V × ρ
W = 25.8 cm³ × 4.43 g/cm³
W = 114 g
```

**Total weight (two cheeks)**: **~230g**

---

## 9. OPTIMIZATION OPPORTUNITIES

The design is **highly conservative** with SF = 23.2. Significant weight and cost reductions are possible.

### Option 1: Reduce Cheek Thickness

**Current**: t = 6mm → SF = 23.2  
**Optimized**: t = 3mm → SF ≈ 11.6

**Benefits**:
- 50% weight reduction: 230g → 115g
- 50% material cost reduction
- Faster machining (less material removal)
- Still maintains very high safety margin

**Risk**: Minimal - SF still >10x

---

### Option 2: Downgrade Material to CP Ti (Grade 2)

**Current**: Ti-6Al-4V (Gr5) - σ_y = 880 MPa  
**Alternative**: CP Ti (Gr2) - σ_y = 275 MPa

**Safety factor with Gr2**:
```
SF = 275 / 38.0 = 7.2
```

**Benefits**:
- 30-40% material cost reduction
- Better machinability (easier to machine)
- Excellent corrosion resistance (equal to Gr5)
- Still adequate SF > 7.0

**Considerations**:
- Slightly lower fatigue performance (not critical here)
- Lower strength-to-weight ratio (not critical with current low stress)

---

### Option 3: Switch to Aluminum Alloy

#### 7075-T6 Aluminum
- **Yield strength**: 505 MPa
- **Safety factor**: SF = 505 / 38.0 = 13.3
- **Density**: 2.81 g/cm³ (vs 4.43 for Ti)
- **Weight**: ~145g (37% lighter than Ti)
- **Cost**: ~70% less than Ti-6Al-4V
- **Corrosion**: Requires anodizing for marine use

#### 6061-T6 Aluminum
- **Yield strength**: 276 MPa
- **Safety factor**: SF = 276 / 38.0 = 7.3
- **Density**: 2.70 g/cm³
- **Weight**: ~140g (39% lighter than Ti)
- **Cost**: ~80% less than Ti-6Al-4V
- **Corrosion**: Requires anodizing; adequate with proper treatment

**Recommendation**: 7075-T6 offers best balance of strength, weight, and cost for this application.

---

### Option 4: Hybrid Design

**Optimized configuration**:
- Material: 7075-T6 Aluminum
- Thickness: 4mm (vs 6mm baseline)
- Weight: ~95g (59% lighter than baseline)
- Cost: ~75% less than baseline
- SF: Still >8.0

**Manufacturing**: Easier machining, faster production, standard anodizing process

---

## 10. RECOMMENDATIONS

### Immediate Actions

1. ✓ **Approve baseline 6mm Ti-6Al-4V design** - structurally sound with excellent margins
2. **Proceed with bearing PV analysis** ([MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12)) - structural integrity confirmed
3. **Consider thermal analysis** ([MORAAAAA-14](/MORAAAAA/issues/MORAAAAA-14)) - verify fit tolerances with thermal expansion

### Design Optimization (Consider for Rev 2)

1. **Weight reduction priority**:
   - Reduce thickness to 3mm: 50% weight savings, SF still >11
   - OR switch to 7075-T6 Al (4mm): 60% weight savings, SF ~8

2. **Cost reduction priority**:
   - Switch to 7075-T6 Al: ~75% cost reduction, adequate SF, lighter
   - OR downgrade to CP Ti Gr2: ~35% cost reduction, easier machining

3. **Performance priority**:
   - Keep Ti-6Al-4V: Best corrosion resistance, best strength-to-weight
   - Reduce to 3mm: Optimize weight while maintaining titanium benefits

### Marine Environment Considerations

**Ti-6Al-4V** (current):
- ✓ Excellent saltwater corrosion resistance
- ✓ No galvanic corrosion concerns with stainless pin
- ✓ No protective coating required

**7075-T6 Aluminum** (alternative):
- Requires hard anodizing (Type III) for marine use
- Potential galvanic corrosion if coupled with dissimilar metals
- Periodic inspection/maintenance recommended

**CP Ti Gr2** (alternative):
- Equal corrosion resistance to Ti-6Al-4V
- Better value for non-structural-critical applications
- Good choice if cost is concern

---

## 11. SOURCES

### Material Properties
- **Ti-6Al-4V properties**: ASM Aerospace Specification Metals Inc., AMS 4928
- **Aluminum properties**: ASM Aluminum Standards and Data
- **Bearing stress allowables**: Bruhn, "Analysis and Design of Flight Vehicle Structures", Chapter C8

### Design Standards
- **Bearing pressure**: ISO 4565 (Wire rope sheaves for lifting appliances)
- **Stress concentration factors**: Peterson's Stress Concentration Factors, 3rd Edition
- **Marine hardware**: ABYC H-41 (Deck Hardware and Rigging Components)
- **Fatigue**: MIL-HDBK-5J (Metallic Materials and Elements for Aerospace Vehicle Structures)

### Calculation Methods
- **Bearing design**: 02_AGENTS/Engineering/SKILLS/bearing_design.md.md
- **Task patterns**: 02_AGENTS/Engineering/TASK_PATTERNS.md.md
- **Load case analysis**: Task Pattern #1 (Load Case Analysis)

### Related Analyses
- **Bearing PV validation**: [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - iglidur X bearing
- **Thermal analysis**: [MORAAAAA-14](/MORAAAAA/issues/MORAAAAA-14) - Thermal expansion effects
- **Parent assessment**: [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11) - Overall bearing concept

---

## 12. DESIGN VERIFICATION CHECKLIST

- [x] Geometry inputs verified
- [x] Load case defined
- [x] Material properties confirmed
- [x] Bearing pressure calculated
- [x] Bending stress calculated
- [x] Tensile stress calculated (with stress concentration)
- [x] Shear stress calculated
- [x] Combined stress evaluated
- [x] Safety factor determined
- [x] Governing failure mode identified
- [x] Fatigue assessed
- [x] Weight estimated
- [x] GO/NO-GO decision made
- [x] Optimization opportunities identified
- [x] Recommendations provided

---

## 13. REVISION HISTORY

| Rev | Date | Description | Engineer |
|-----|------|-------------|----------|
| A | 2026-04-29 | Initial analysis - baseline 6mm Ti-6Al-4V cheeks | MORFRAC Engineering |

---

**Analysis Status**: ✓ COMPLETE  
**Decision**: ✓ GO - Design Approved  
**Next Review**: After optimization implementation (if pursued)
