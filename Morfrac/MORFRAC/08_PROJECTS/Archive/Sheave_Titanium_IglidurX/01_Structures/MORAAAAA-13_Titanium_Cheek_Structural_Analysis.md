# MORAAAAA-13: Titanium Cheek Structural Analysis

**Date:** 2026-04-29  
**Engineer:** Engineering Agent  
**Task:** [MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13)  
**Parent:** [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11)

---

## 1. PROBLEM STATEMENT

Calculate stresses in Ti-6Al-4V titanium cheek plates supporting a marine rigging sheave with polymer bearing under maximum expected loads. Verify structural integrity with minimum 2× safety factor against yield.

---

## 2. INPUTS & ASSUMPTIONS

### Design Specifications (Provided by CTO)
- **Application:** Marine rigging sheave, small-medium size, intermittent duty
- **Bearing:** 12 mm bore × 20 mm length, iglidur X material
- **Load:** 1000 N radial load from 2000 N rope tension (confirmed by PV analysis)
- **Material:** Ti-6Al-4V (Grade 5 titanium alloy)
- **Environment:** Saltwater, natural convection cooling

### Material Properties - Ti-6Al-4V (Annealed)
*(Source: ASM Handbook, MMPDS-01, AMS 4928)*

- **Yield strength (σ_y):** 880 MPa (128 ksi) minimum
- **Ultimate tensile strength (σ_ult):** 950 MPa (138 ksi) minimum
- **Modulus of elasticity (E):** 114 GPa
- **Poisson's ratio (ν):** 0.34
- **Density (ρ):** 4430 kg/m³
- **Fatigue endurance limit:** ~500 MPa at 10⁷ cycles (R = -1)
- **Corrosion resistance:** Excellent in saltwater (passive oxide film)

### Geometric Assumptions (Baseline Sheave Design)

**CRITICAL NOTE:** CTO did not provide specific cheek geometry. The following represents a reasonable baseline design for a small-medium marine sheave with 12mm bearing bore. CTO should validate or provide actual geometry.

**Cheek plate assumptions:**
- Material: Ti-6Al-4V plate, 3 mm thickness (typical for this size class)
- Sheave diameter: 60 mm (rope groove diameter, 5× bearing bore is typical)
- Cheek outer diameter: 70 mm (provides edge margin)
- Bearing bore: 12 mm diameter (per spec)
- Bearing housing: 20 mm OD × 20 mm length (press-fit iglidur X bushing)

**Load path:**
1. Rope applies 2000 N tension across sheave groove
2. Resultant force on bearing: 1000 N radial (per PV analysis)
3. Bearing distributes load to cheek plates via press fit
4. Cheek plates transfer load to shaft/pin

**Fastening:** Assumes cheek plates are captured between shaft shoulders or retained by snap rings (axial constraint). Plates do not carry bending moment from shaft cantilever.

**Geometry sketch (side view):**
```
    |<-- 70 mm OD -->|
    
    +-------O-------+  ← Cheek plate (3 mm thick)
            |
        [Bearing]
        20mm OD
        12mm ID
            |
    +-------O-------+  ← Opposite cheek plate
    
    Rope groove Ø60 mm
    Load: 2000 N rope tension → 1000 N radial on bearing
```

### Critical Assumptions
1. **Load distribution:** Bearing load uniformly distributed over 20 mm length (conservative, per PV analysis assumption)
2. **Constraint:** Each cheek plate carries 500 N radial load (half of total 1000 N)
3. **Load case:** Maximum static load; dynamic/shock loads analyzed separately
4. **Bearing fit:** Press fit provides full radial support (no localized stress concentration at edge)
5. **No bending moment:** Shaft is simply supported, cheeks only carry radial bearing loads
6. **Corrosion allowance:** None applied initially (Ti-6Al-4V has excellent corrosion resistance)

---

## 3. MISSING INPUTS

**CRITICAL - Requires CTO validation:**
1. **Actual cheek plate thickness** (assumed 3 mm)
2. **Actual sheave outer diameter** (assumed 70 mm)
3. **Bearing housing diameter** (assumed 20 mm OD to suit iglidur X bushing)
4. **Shaft support configuration** (simply supported? cantilevered?)
5. **Cheek attachment method** (snap rings? threaded? integral with shaft?)

**Optional refinements:**
- Exact rope groove profile (if bending loads present)
- Cyclic load history for fatigue analysis
- Shock load magnitude and frequency

**Proceed with baseline assumptions pending CTO feedback.**

---

## 4. CALCULATIONS

### 4.1 Load Analysis

**Total bearing load (from PV analysis):** F_bearing = 1000 N radial

**Load per cheek plate (conservative assumption):**
```
F_cheek = F_bearing / 2
F_cheek = 1000 N / 2 = 500 N per cheek
```

**Projected bearing area per cheek (cylindrical bearing surface):**
```
A_bearing = D_bore × L_bearing
A_bearing = 12 mm × 20 mm = 240 mm²
```

### 4.2 Bearing Stress at Hole (Cheek-to-Bushing Interface)

**Bearing stress (compressive contact stress on cheek bore):**

The bearing load is distributed over the projected contact area. For a cylindrical bearing in a through-hole:

```
σ_bearing = F_cheek / A_projected
```

Where:
- A_projected = bore diameter × bearing length = 12 mm × 20 mm = 240 mm²

However, the cheek plate is only 3 mm thick. The **actual bearing area** is:

```
A_cheek_bearing = D_bore × t_cheek
A_cheek_bearing = 12 mm × 3 mm = 36 mm²
```

**Peak bearing stress in cheek plate:**
```
σ_bearing = F_cheek / A_cheek_bearing
σ_bearing = 500 N / 36 mm²
σ_bearing = 13.9 N/mm² = 13.9 MPa
```

**Safety factor against yield (bearing):**
```
SF_bearing = σ_y / σ_bearing
SF_bearing = 880 MPa / 13.9 MPa
SF_bearing = 63.3×
```

✅ **Bearing stress is negligible** - extremely low stress due to large contact area.

### 4.3 Tensile Stress at Minimum Section (Net Section Failure)

The critical cross-section is at the bearing bore, where material is removed. The **net section** carries tensile load.

**Assumptions for tensile stress:**
- Load path: radial load creates tension on one side of cheek, compression on other
- Critical section: diameter through center of bearing bore
- Net width: w_net = D_outer - D_bore

**Geometry:**
```
D_outer = 70 mm (cheek outer diameter)
D_bore = 12 mm (bearing bore)
t_cheek = 3 mm (plate thickness)
```

**Net section width (approximate, along load direction):**

For a circular plate with central hole, the minimum net section is approximately:
```
w_net = D_outer - D_bore
w_net = 70 mm - 12 mm = 58 mm
```

**Net section area:**
```
A_net = w_net × t_cheek
A_net = 58 mm × 3 mm = 174 mm²
```

**Tensile stress at net section:**
```
σ_tension = F_cheek / A_net
σ_tension = 500 N / 174 mm²
σ_tension = 2.87 MPa
```

**Safety factor against yield (tension):**
```
SF_tension = σ_y / σ_tension
SF_tension = 880 MPa / 2.87 MPa
SF_tension = 307×
```

✅ **Tensile stress is negligible** - very low stress due to large net section.

### 4.4 Stress Concentration at Hole Edge

For a plate with a circular hole under tensile loading, stress concentration occurs at the hole edge perpendicular to the load direction.

**Theoretical stress concentration factor (Kt) for circular hole in infinite plate:**
```
Kt = 3.0 (classical elasticity solution)
```

**Geometry effect correction:**
For finite-width plate:
```
d/w = D_bore / (effective width)
```

Approximating effective width as ~30 mm (conservative, half the net width):
```
d/w = 12 mm / 30 mm = 0.4
```

For d/w = 0.4, **Kt ≈ 2.5** (from Peterson's Stress Concentration Factors)

**Peak stress at hole edge:**
```
σ_peak = Kt × σ_tension
σ_peak = 2.5 × 2.87 MPa
σ_peak = 7.18 MPa
```

**Safety factor against yield (stress concentration):**
```
SF_peak = σ_y / σ_peak
SF_peak = 880 MPa / 7.18 MPa
SF_peak = 122×
```

✅ **Even with stress concentration, peak stress is negligible.**

### 4.5 Bending Stress in Cheek Plate

**Critical check:** Does the cheek plate experience bending moment?

**Scenario 1: Bearing load is uniformly distributed**
If the bearing load is uniformly distributed over the bearing length (20 mm), and the cheek plate is only 3 mm thick, there is a bending effect due to eccentricity.

However, the bearing press-fit into the cheek provides **continuous radial support**, not a point load. The plate acts as a **thick-walled pressure vessel element** rather than a simply-supported beam.

**For thick-walled cylinder under internal pressure:**

Approximate as a ring under radial pressure:
```
p_radial = F_cheek / A_cheek_bearing (same as bearing stress calculated)
p_radial = 13.9 MPa (already calculated, negligible)
```

**Tangential (hoop) stress in cheek plate ring:**

For thin ring approximation (t << r):
```
σ_hoop = p × r / t
```

Where:
- p = radial pressure = 13.9 MPa (bearing stress)
- r = bearing radius = 6 mm
- t = cheek thickness = 3 mm

```
σ_hoop = 13.9 MPa × 6 mm / 3 mm
σ_hoop = 27.8 MPa
```

**Safety factor against yield (hoop stress):**
```
SF_hoop = σ_y / σ_hoop
SF_hoop = 880 MPa / 27.8 MPa
SF_hoop = 31.7×
```

✅ **Hoop stress is low** - well within allowable limits.

**Scenario 2: Cantilever bending (if shaft is cantilevered)**

If the cheek plate is rigidly attached to a cantilevered shaft and the sheave load creates a bending moment, this would be the governing failure mode.

**Assumption for bending analysis:**
- Cantilever length: L_cant = 10 mm (typical for small sheave, distance from cheek to support bearing)
- Bending moment: M = F_cheek × L_cant
- Cheek acts as a cantilevered disk

```
M = 500 N × 10 mm = 5000 N·mm = 5 N·m
```

**Section modulus of cheek plate at root (assuming rigid attachment at inner bore):**

For a disk with central hole, approximate bending section modulus:
```
Z ≈ π × (D_outer³ - D_bore³) / (32 × D_outer)
```

This is a rough approximation; actual stress distribution is complex.

For hollow circular cross-section (conservative, treats cheek as annular beam):
```
I = π/64 × (D_outer⁴ - D_bore⁴)
I = π/64 × (70⁴ - 12⁴)
I = π/64 × (24,010,000 - 20,736)
I = π/64 × 23,989,264
I = 1,178,300 mm⁴
```

**Section modulus:**
```
Z = I / c
Z = 1,178,300 mm⁴ / 35 mm (outer radius)
Z = 33,666 mm³
```

**Bending stress:**
```
σ_bending = M / Z
σ_bending = 5000 N·mm / 33,666 mm³
σ_bending = 0.149 MPa
```

**Safety factor against yield (bending):**
```
SF_bending = σ_y / σ_bending
SF_bending = 880 MPa / 0.149 MPa
SF_bending = 5906×
```

✅ **Bending stress is negligible** - even with cantilever assumption.

**Conclusion:** Bending is not a concern for this geometry. The thick disk geometry and short moment arm result in very low bending stresses.

### 4.6 Shear Stress

**Shear plane:** If cheek plates are retained by snap rings or shoulders, shear stress in the retaining feature could be critical.

**Scenario:** Snap ring groove in shaft, retaining axial load from rigging.

Assume **axial load component** from rope angle (e.g., 30° from horizontal):
```
F_axial = F_rope × sin(30°)
F_axial = 2000 N × 0.5 = 1000 N (conservative)
```

**Shear area in shaft (snap ring groove):**

Assume shaft diameter at groove root: d_root = 10 mm (conservative, 2 mm groove depth in 12 mm shaft)
```
A_shear = π × d_root × groove_width
```

Typical snap ring groove width: 1.5 mm
```
A_shear = π × 10 mm × 1.5 mm = 47.1 mm²
```

**Shear stress in shaft:**
```
τ_shaft = F_axial / A_shear
τ_shaft = 1000 N / 47.1 mm²
τ_shaft = 21.2 MPa
```

**For 316 SS shaft (assuming hardened condition):**
- Shear strength: τ_yield ≈ 0.6 × σ_y ≈ 0.6 × 500 MPa = 300 MPa (316 SS annealed)

**Safety factor against yield (shear):**
```
SF_shear = τ_yield / τ_shaft
SF_shear = 300 MPa / 21.2 MPa
SF_shear = 14.2×
```

✅ **Shear stress is acceptable** - shaft retention is not critical.

**NOTE:** If axial loads are higher or shaft diameter is smaller, this should be re-evaluated.

---

## 5. RESULTS

### Stress Summary Table

| Failure Mode | Location | Peak Stress | Material Limit | Safety Factor | Status |
|--------------|----------|-------------|----------------|---------------|--------|
| **Bearing stress** | Cheek bore surface | 13.9 MPa | 880 MPa (yield) | **63.3×** | **PASS** |
| **Net section tension** | Diameter through bore | 2.87 MPa | 880 MPa (yield) | **307×** | **PASS** |
| **Stress concentration** | Hole edge (tension side) | 7.18 MPa | 880 MPa (yield) | **122×** | **PASS** |
| **Hoop stress** | Bearing interface ring | 27.8 MPa | 880 MPa (yield) | **31.7×** | **PASS** |
| **Bending stress** | Cheek outer edge (cantilever) | 0.149 MPa | 880 MPa (yield) | **5906×** | **PASS** |
| **Shaft shear** | Snap ring groove (assumed) | 21.2 MPa | 300 MPa (SS yield) | **14.2×** | **PASS** |

**Overall Assessment:** ✅ **GO - All stress levels far below allowable limits**

---

## 6. GOVERNING FAILURE MODE

**Governing constraint:** Hoop stress at bearing interface (lowest safety factor at 31.7×)

Despite being the "governing" mode, the safety factor of 31.7× indicates the structure is **vastly over-designed** for the baseline load case.

### Failure Progression (Hypothetical)

If loads were increased progressively, expected failure sequence:
1. **First yield:** Hoop stress at bearing interface (σ ≈ 28 MPa currently)
2. **Subsequent yield:** Stress concentration at hole edge (σ ≈ 7 MPa currently)
3. **Ultimate failure:** Net section rupture or bearing pullout (σ ≈ 3 MPa currently)

**Load to first yield:**
```
F_yield = F_baseline × SF_governing
F_yield = 1000 N × 31.7 = 31,700 N bearing load
```

This corresponds to rope tension of **~63,400 N (6.4 metric tons)** before first yield in titanium cheeks.

**Conclusion:** Structural failure is **not credible** for this application. Bearing PV limit (SF = 5.0×) will fail first, well before titanium cheeks reach yield.

---

## 7. SAFETY ASSESSMENT

### Primary Safety Factors
- **Minimum safety factor: 31.7×** (hoop stress)
- **Target safety factor: 2.0×** (per decision criteria: stress < 50% yield)
- **Margin over requirement: 15.9×** (exceeds requirement by factor of 15.9)

**Compliance:** ✅ **PASS** - All stresses far below 50% yield threshold.

### Key Sensitivities (Parametric Analysis)

#### Load Sensitivity
- **2× load increase** (2000 N bearing load, 4000 N rope tension):
  - Peak stress: 55.6 MPa (hoop stress)
  - Safety factor: 15.8× → **PASS**

- **5× load increase** (5000 N bearing load, 10,000 N rope tension):
  - Peak stress: 139 MPa (hoop stress)
  - Safety factor: 6.3× → **PASS**

- **10× load increase** (10,000 N bearing load, 20,000 N rope tension):
  - Peak stress: 278 MPa (hoop stress)
  - Safety factor: 3.2× → **PASS** (still above 2× target)

**Conclusion:** Titanium cheeks can handle **10× overload** before approaching minimum safety factor. Bearing PV limit (5× margin) will govern design, not structural strength.

#### Geometry Sensitivity

**Cheek thickness reduction:**
- **2 mm thick (instead of 3 mm):**
  - Hoop stress: 41.7 MPa
  - Safety factor: 21.1× → **PASS**
  - **Mass savings: 33%**

- **1.5 mm thick (50% reduction):**
  - Hoop stress: 83.4 MPa
  - Safety factor: 10.6× → **PASS**
  - **Mass savings: 50%**

**Conclusion:** Cheek thickness can be **reduced to 1.5-2 mm** for significant mass/cost savings while maintaining >10× safety factor.

**Cheek outer diameter reduction:**
- Current: 70 mm OD
- Minimum feasible: ~40 mm OD (bearing OD + 10 mm edge margin)
- At 40 mm OD, net section stress increases ~2×, still results in SF > 150×
- **Mass savings: ~50%** (proportional to area reduction)

**Conclusion:** Cheek OD can be significantly reduced without structural concerns.

### Fatigue Analysis (Cyclic Loading)

**Fatigue consideration:** If sheave operates under cyclic loading (repeated tensioning/release), fatigue life should be evaluated.

**Fatigue endurance limit for Ti-6Al-4V:**
- σ_fatigue ≈ 500 MPa at 10⁷ cycles (fully reversed, R = -1)
- For tensile cycling (R = 0), endurance limit ≈ 600-700 MPa

**Current peak stress:** 27.8 MPa (hoop stress)

**Fatigue safety factor:**
```
SF_fatigue = σ_fatigue / σ_peak
SF_fatigue = 500 MPa / 27.8 MPa
SF_fatigue = 18.0×
```

**Infinite life expectancy:** ✅ At this stress level, infinite fatigue life is expected (>10⁷ cycles).

**Conclusion:** No fatigue concerns. Even at 10× load increase (278 MPa), fatigue life would still be excellent.

### Environmental Considerations

**Saltwater corrosion:**
- Ti-6Al-4V has **excellent corrosion resistance** in seawater (passive TiO₂ film)
- No corrosion allowance needed
- Galvanic compatibility with 316 SS shaft: Good (both passive metals)
- No crevice corrosion risk at bearing interface (press fit)

**Maintenance:**
- Periodic freshwater rinse recommended (removes salt deposits)
- Visual inspection for mechanical damage (impact, overload)
- No corrosion-related inspections required

---

## 8. RECOMMENDATIONS

### GO Decision with Mass Optimization Opportunity

✅ **Proceed with Ti-6Al-4V cheeks** - baseline design has exceptional structural margin.

### Design Optimization Opportunities

#### 1. **CRITICAL: Validate Geometry Assumptions**

The CTO must provide or validate actual cheek geometry:
- Cheek plate thickness (assumed 3 mm)
- Cheek outer diameter (assumed 70 mm)
- Bearing housing OD (assumed 20 mm)
- Shaft support configuration

If actual geometry differs significantly from assumptions, **re-run this analysis**.

#### 2. **Mass Reduction (High Priority)**

Current design is **vastly overdesigned** (31.7× safety factor vs 2× target). Significant mass savings possible:

**Recommended optimizations:**
- **Reduce cheek thickness to 2 mm** → 33% mass savings, SF still >20×
- **Reduce cheek OD to 50 mm** → additional 30% mass savings, SF still >15×
- **Combined optimization:** 2 mm × 50 mm OD → **~50% total mass savings**, SF ≈ 15×

**Mass estimate (current baseline):**
```
Volume per cheek ≈ π/4 × (70² - 12²) × 3 mm = 11,090 mm³
Mass per cheek = 11,090 mm³ × 4.43 g/cm³ = 49.1 grams
Total (2 cheeks) = 98.2 grams
```

**Optimized mass (2 mm × 50 mm OD):**
```
Volume per cheek ≈ π/4 × (50² - 12²) × 2 mm = 3,694 mm³
Mass per cheek = 3,694 mm³ × 4.43 g/cm³ = 16.4 grams
Total (2 cheeks) = 32.8 grams
```

**Mass savings: 65.4 grams (67% reduction)** - significant for marine rigging applications where weight matters.

#### 3. **Material Considerations**

**Ti-6Al-4V is appropriate** for this application:
- Excellent strength-to-weight ratio
- Superior corrosion resistance in saltwater
- Good fatigue properties

**Alternative materials (if cost is a concern):**
- **Aluminum 7075-T6** (less expensive, ~3× heavier for same strength)
  - Yield strength: 500 MPa
  - Safety factor at baseline: 18× (still acceptable)
  - Corrosion resistance: Good with anodizing
  - Cost savings: ~70% vs titanium

- **316 Stainless Steel** (lowest cost, much heavier)
  - Yield strength: 290 MPa (annealed)
  - Safety factor at baseline: 10.4× (acceptable)
  - Corrosion resistance: Excellent
  - Cost savings: ~80% vs titanium
  - Weight penalty: ~80% heavier than titanium

**Recommendation:** Keep Ti-6Al-4V for performance applications. Consider Al 7075 for cost-sensitive designs.

#### 4. **Manufacturing Considerations**

**For 2-3 mm thick cheek plates:**
- **Waterjet or laser cutting** from Ti-6Al-4V plate stock (most cost-effective for low volume)
- **CNC machining** from billet (if higher tolerances needed for bearing bore)
- **Press-fit bearing installation:** Requires H7 bore tolerance (per bearing analysis MORAAAAA-12)

**For optimized thin plates (1.5-2 mm):**
- Consider **stamping or forming** if production volume justifies tooling
- **Anodize finish:** Type II anodizing provides additional surface hardness and color coding

#### 5. **Design Validation**

**Recommended next steps:**
1. **CTO provides actual geometry** → re-run analysis if needed
2. **Prototype testing:** Static load test to 2× design load (2000 N bearing load)
3. **Cyclic load test:** 10,000 cycles at design load to verify fatigue performance
4. **Saltwater immersion test:** 30-day saltwater exposure to verify corrosion resistance

**FEA validation (optional but recommended):**
- Run FEA on actual CAD geometry to validate hand calculations
- Verify stress concentration factors at hole edge
- Optimize thickness distribution (variable thickness plate for further mass savings)

---

## 9. SOURCES

### Material Properties
1. **ASM Handbook, Volume 2: Properties and Selection: Nonferrous Alloys and Special-Purpose Materials**  
   Ti-6Al-4V yield strength, ultimate strength, modulus

2. **MMPDS-01 (Metallic Materials Properties Development and Standardization)**  
   Ti-6Al-4V fatigue properties, design allowables

3. **AMS 4928 (Aerospace Material Specification)**  
   Ti-6Al-4V annealed sheet/plate specifications

### Stress Calculations
4. **Roark's Formulas for Stress and Strain (8th Edition)**  
   - Bearing stress: Chapter 14 (Contact Stresses)
   - Tensile stress at net section: Chapter 17 (Axially Loaded Members)
   - Thick-walled cylinder: Chapter 13 (Cylindrical Shells)

5. **Peterson's Stress Concentration Factors (3rd Edition)**  
   - Stress concentration factor for circular hole: Figure 4.24
   - Finite width correction factors: Section 4.5

6. **Shigley's Mechanical Engineering Design (11th Edition)**  
   - Bearing stress calculations: Chapter 3
   - Fatigue analysis: Chapter 6
   - Safety factor guidelines: Chapter 1

### Corrosion Resistance
7. **ASM Handbook, Volume 13B: Corrosion: Materials**  
   Ti-6Al-4V corrosion resistance in seawater

8. **ASTM G48 (Standard Test Methods for Pitting and Crevice Corrosion Resistance)**  
   Ti-6Al-4V saltwater compatibility data

---

## APPENDIX A: FREE BODY DIAGRAM

```
                        Rope Tension (2000 N)
                               ↓
                     ╔═══════════════╗
                     ║    Sheave     ║  ← Groove Ø60 mm
                     ║   Ø70 mm OD   ║
                     ╚═══════╤═══════╝
                             │
                         [Bearing]  ← 12mm bore, 20mm length
                         Load: 1000 N radial
                             │
                 ┌───────────┴───────────┐
                 │                       │
            Cheek Plate            Cheek Plate
             500 N each             500 N each
            (3 mm thick)           (3 mm thick)
                 │                       │
            ─────┴───────────────────────┴─────
                       Shaft (316 SS)
                       Ø12 mm
```

**Load path:**
1. Rope applies 2000 N tension across sheave groove
2. Sheave transfers 1000 N radial load to bearing
3. Bearing (press-fit) distributes load to two cheek plates (500 N each)
4. Cheek plates transfer load to shaft via bearing bore
5. Shaft reacts load through support bearings (not shown)

---

## APPENDIX B: COMPARISON TO DECISION CRITERIA

**Decision criteria (from task description):**
- **GO:** Stress stays below 50% of yield strength
- **NO-GO:** Insufficient structural margin

**Results:**
- Ti-6Al-4V yield strength: 880 MPa
- 50% of yield: 440 MPa
- **Peak stress (governing): 27.8 MPa**

**Compliance:**
```
Peak stress / (50% yield) = 27.8 MPa / 440 MPa = 0.063 = 6.3%
```

**Conclusion:** Peak stress is **6.3% of the allowable limit** (50% yield). This represents a **15.9× margin** over the decision criteria threshold.

✅ **PASS** - Comfortably exceeds GO criteria.

---

## APPENDIX C: WEIGHT ESTIMATE

**Current baseline design (3 mm thick, 70 mm OD):**
- Material: Ti-6Al-4V, density 4.43 g/cm³
- Volume per cheek: 11,090 mm³
- Mass per cheek: 49.1 grams
- **Total cheek mass: 98.2 grams**

**Optimized design (2 mm thick, 50 mm OD):**
- Volume per cheek: 3,694 mm³
- Mass per cheek: 16.4 grams
- **Total cheek mass: 32.8 grams**

**Mass savings: 65.4 grams (67% reduction)**

**For comparison:**
- **Aluminum 7075-T6** (optimized 2mm × 50mm): ~8.3 grams per cheek, 16.6 grams total
- **316 SS** (optimized 2mm × 50mm): ~29 grams per cheek, 58 grams total

**Recommendation:** Use optimized Ti-6Al-4V geometry (2 mm × 50 mm) for best strength-to-weight ratio in marine environment.

---

**END OF ANALYSIS**
