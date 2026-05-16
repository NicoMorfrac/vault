# MORAAAAA-18: Bearing Analysis - Iglidur X @ 1t Rope Redirect (180°)

**Date:** 2026-04-29  
**Engineer:** Engineering Agent  
**Task:** [MORAAAAA-18](/MORAAAAA/issues/MORAAAAA-18)  
**Project:** Sheave_Titanium_IglidurX  
**Related:** [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) (1kN PASS), [MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17) (4kN FAIL)

---

## 1. PROBLEM STATEMENT

Evaluate iglidur X plain bearing for a sheave block deflecting a rope through 180° with 1 ton (1000 kg) rope tension. Verify bearing pressure, PV limits, and pin bending stress against required safety factors.

**Design Criteria:** 
- Required FoS: 2.0 (marine hardware, static basis)
- Dynamic factor: 2.0 (project specification)
- All checks must pass with FoS ≥ 2.0
- Governing utilization must be <100%

---

## 2. INPUTS & ASSUMPTIONS

### 2.1 Provided Inputs

**Rigging Configuration:**
- **Rope deflection angle:** 180° (simple redirect sheave)
- **Rope tension:** T = 1 ton = 1000 kg
- **Configuration:** Single sheave block, rope redirected through 180°

**Bearing Geometry (from MORAAAAA-13, MORAAAAA-17):**
- **Pin diameter:** d = 12 mm
- **Bearing length:** L = 20 mm
- **Bearing material:** iglidur X (polymer bushing)
- **Cheek thickness:** t = 6 mm (Ti-6Al-4V)
- **Configuration:** Double shear (two cheeks, one bearing)
- **Sheave diameter:** 75 mm outer diameter

### 2.2 Operating Conditions

**From project baseline (MORAAAAA-12, MORAAAAA-17):**
- **Rotation speed:** 100 rpm (baseline assumption)
- **Pin material:** 316 Stainless Steel, hardened condition
- **Environment:** Saltwater, natural convection cooling
- **Duty cycle:** Intermittent (marine rigging)
- **Lubrication:** Dry running (self-lubricating polymer)

### 2.3 Load Calculation

**Rope tension:**
```
T_rope = 1000 kg × 9.81 m/s²
T_rope = 9810 N = 9.81 kN
```

**Bearing radial load (180° redirect):**

For a rope deflected through 180° over a sheave, the resultant load on the pin is:
```
F_radial = 2 × T_rope × sin(θ/2)

For 180° deflection:
θ = 180°
sin(90°) = 1

F_radial = 2 × T_rope × 1
F_radial = 2 × 9810 N
F_radial = 19,620 N = 19.62 kN
```

**Design load with dynamic factor:**

Per project specification, dynamic factor = 2.0:
```
F_design = F_radial × DF
F_design = 19.62 kN × 2.0
F_design = 39.24 kN
```

### 2.4 Assumptions

**Load Application:**
- Nominal rope tension (1t) does not include dynamic factor
- Dynamic factor of 2.0 applied per project requirement
- Vector geometry: rope loads combine at 180° to create radial pin load
- Entire load transmitted through bearing (conservative)

**Pin Configuration:**
- Simply supported beam model
- Support span = bearing length = 20 mm (conservative)
- Uniform radial load over bearing length
- Critical bending at mid-span

**Material Properties:**

*Iglidur X (Source: igus GmbH, RS Online):*
- Maximum PV value (dry, continuous): 1.32 MPa·m/s
- Maximum surface pressure (recommended): 35 MPa
- Maximum surface velocity: 1.5 m/s
- Friction coefficient vs SS316: μ ≈ 0.15-0.25
- Temperature range: -100°C to +250°C
- Chemical resistance: Excellent in saltwater

*316 Stainless Steel (ASTM A276, hardened):*
- Yield strength: σ_y = 290 MPa (annealed), 520 MPa (cold worked)
- Ultimate strength: σ_u = 590 MPa (annealed), 860 MPa (cold worked)
- Modulus: E = 193 GPa
- **Conservative baseline:** σ_y = 290 MPa (annealed condition)

---

## 3. MISSING INPUTS

**None critical for analysis.**

Optional refinements:
- Exact pin material condition (assumed annealed 316 SS, conservative)
- Detailed duty cycle % for intermittent operation credit
- Shaft surface finish specification (assume Ra < 1 μm)
- Actual operating speed confirmation (using 100 rpm from baseline)

**Decision:** Proceed with conservative assumptions.

---

## 4. CALCULATIONS

### 4.1 Bearing Pressure Check

**Projected bearing area:**
```
A_projected = d × L
A_projected = 12 mm × 20 mm = 240 mm²
A_projected = 240 × 10⁻⁶ m² = 0.000240 m²
```

**Bearing pressure:**
```
P = F_design / A_projected
P = 39,240 N / 0.000240 m²
P = 163,500,000 Pa
P = 163.5 MPa
```

**Allowable pressure (iglidur X):**
```
P_allowable = 35 MPa (manufacturer's recommendation)
```

**Safety factor (pressure):**
```
SF_P = P_allowable / P_operating
SF_P = 35 MPa / 163.5 MPa
SF_P = 0.21
```

**Check:** ❌ **CATASTROPHIC FAIL** - Pressure exceeds allowable by **467%**

**Utilization:**
```
Utilization_P = (P_operating / P_allowable) × 100%
Utilization_P = (163.5 / 35) × 100% = 467%
```

---

### 4.2 Surface Velocity Calculation

**Shaft circumference:**
```
C = π × d
C = π × 12 mm = 37.7 mm = 0.0377 m
```

**Surface velocity:**
```
V = C × n
V = 0.0377 m/rev × 100 rev/min
V = 3.77 m/min = 0.0628 m/s
```

**Allowable velocity (iglidur X):**
```
V_allowable = 1.5 m/s
```

**Safety factor (velocity):**
```
SF_V = V_allowable / V_operating
SF_V = 1.5 m/s / 0.0628 m/s
SF_V = 23.9
```

**Check:** ✓ **PASS** - Velocity within limits (not governing)

---

### 4.3 PV Value Check

**PV calculation:**
```
PV = P × V
PV = 163.5 MPa × 0.0628 m/s
PV = 10.27 MPa·m/s
```

**Allowable PV (iglidur X, dry continuous):**
```
PV_allowable = 1.32 MPa·m/s
```

**Safety factor (PV):**
```
SF_PV = PV_allowable / PV_operating
SF_PV = 1.32 MPa·m/s / 10.27 MPa·m/s
SF_PV = 0.13
```

**Check:** ❌ **CATASTROPHIC FAIL** - PV exceeds allowable by **778%**

**Utilization:**
```
Utilization_PV = (PV_operating / PV_allowable) × 100%
Utilization_PV = (10.27 / 1.32) × 100% = 778%
```

**Critical Finding:** PV value exceeds material limit by nearly 8×. Bearing would experience immediate thermal failure and rapid wear.

---

### 4.4 Pin Bending Stress Check

**Configuration:** Simply supported beam, uniformly distributed load over bearing length

**Maximum bending moment (center of span):**
```
M_max = (w × L²) / 8
where w = F_design / L = 39,240 N / 20 mm = 1962 N/mm

M_max = (1962 N/mm × (20 mm)²) / 8
M_max = (1962 × 400) / 8
M_max = 98,100 N·mm
```

**Section modulus (circular cross-section):**
```
Z = (π × d³) / 32
Z = (π × (12 mm)³) / 32
Z = (π × 1728) / 32
Z = 169.6 mm³
```

**Bending stress:**
```
σ_bending = M_max / Z
σ_bending = 98,100 N·mm / 169.6 mm³
σ_bending = 578 MPa
```

**Allowable stress (316 SS, annealed, with FoS = 2.0):**
```
σ_allowable = σ_y / FoS
σ_allowable = 290 MPa / 2.0
σ_allowable = 145 MPa
```

**Safety factor (pin bending yield):**
```
SF_bending_yield = σ_y / σ_bending
SF_bending_yield = 290 MPa / 578 MPa
SF_bending_yield = 0.50
```

**Safety factor (pin bending ultimate):**
```
SF_bending_ultimate = σ_u / σ_bending
SF_bending_ultimate = 590 MPa / 578 MPa
SF_bending_ultimate = 1.02
```

**Check:** ❌ **FAIL** - Pin bending exceeds yield strength

**Utilization:**
```
Utilization_bending = (σ_bending / σ_allowable) × 100%
Utilization_bending = (578 / 145) × 100% = 399%
```

**Critical Finding:** Pin stress exceeds yield by 199%. Pin would experience permanent plastic deformation.

---

### 4.5 Pin Shear Stress Check

**Configuration:** Double shear (load split between two shear planes)

**Shear force per plane:**
```
V_shear = F_design / 2
V_shear = 39,240 N / 2 = 19,620 N
```

**Shear area (circular cross-section):**
```
A_shear = (π × d²) / 4
A_shear = (π × (12 mm)²) / 4
A_shear = 113.1 mm²
```

**Shear stress:**
```
τ = V_shear / A_shear
τ = 19,620 N / 113.1 mm²
τ = 173.5 MPa
```

**Shear yield strength (von Mises criterion):**
```
τ_y = σ_y / √3
τ_y = 290 MPa / 1.732
τ_y = 167.5 MPa
```

**Allowable shear stress (with FoS = 2.0):**
```
τ_allowable = τ_y / 2.0
τ_allowable = 167.5 / 2.0 = 83.8 MPa
```

**Safety factor (pin shear):**
```
SF_shear = τ_y / τ
SF_shear = 167.5 MPa / 173.5 MPa
SF_shear = 0.97
```

**Check:** ❌ **FAIL** - Pin shear stress exceeds yield

**Utilization:**
```
Utilization_shear = (τ / τ_allowable) × 100%
Utilization_shear = (173.5 / 83.8) × 100% = 207%
```

**Critical Finding:** Pin shear stress exceeds yield strength. Pin would experience plastic deformation under load.

---

## 5. RESULTS SUMMARY

| **Check** | **Operating** | **Allowable** | **Safety Factor** | **Utilization** | **Status** |
|-----------|---------------|---------------|-------------------|-----------------|------------|
| **Bearing pressure** | **163.5 MPa** | **35 MPa** | **0.21** | **467%** | **❌ CATASTROPHIC FAIL** |
| Surface velocity | 0.063 m/s | 1.5 m/s | 23.9 | 4.2% | ✓ PASS |
| **PV value** | **10.27 MPa·m/s** | **1.32 MPa·m/s** | **0.13** | **778%** | **❌ CATASTROPHIC FAIL** |
| **Pin bending (yield)** | **578 MPa** | **145 MPa** | **0.50** | **399%** | **❌ FAIL** |
| Pin bending (ultimate) | 578 MPa | 295 MPa | 1.02 | 98% | ⚠️ MARGINAL |
| **Pin shear (yield)** | **173.5 MPa** | **83.8 MPa** | **0.97** | **207%** | **❌ FAIL** |

---

## 6. GOVERNING CRITERION

**Multiple Critical Failures - All Criteria Fail:**

1. **GOVERNING: PV Limit** - SF = 0.13 (778% over limit)
2. **Bearing Pressure** - SF = 0.21 (467% over limit)
3. **Pin Bending Yield** - SF = 0.50 (199% over yield)
4. **Pin Shear Yield** - SF = 0.97 (3% over yield)

**Failure Mechanisms:**

**Bearing Failure (PV limit, most critical):**
- PV value 7.8× material limit
- Immediate frictional heating and thermal runaway
- Rapid polymer degradation and wear
- Probable bearing seizure within seconds to minutes
- Potential melting/smoking of bearing material

**Bearing Crushing (Pressure limit):**
- Pressure 4.7× material limit
- Immediate plastic deformation and crushing of bearing
- Extrusion of polymer material from bearing surfaces
- Loss of dimensional stability

**Pin Failure (Bending):**
- Stress 2× yield strength (annealed 316 SS)
- Permanent plastic deformation of pin
- Bent pin, loss of alignment
- Even cold-worked 316 SS (σ_y = 520 MPa) would yield (SF = 0.90)

**Pin Failure (Shear):**
- Shear stress at yield limit
- Incipient plastic deformation at shear planes
- Progressive yielding under repeated loading

---

## 7. SAFETY ASSESSMENT

### 7.1 Overall Status

**DECISION:** ❌ **NO-GO - CATASTROPHIC FAILURE - UNSAFE CONFIGURATION**

**Required FoS:** 2.0 (marine hardware standard)  
**Achieved FoS (PV):** 0.13 (governing criterion)  
**Achieved FoS (Pressure):** 0.21  
**Achieved FoS (Pin Bending Yield):** 0.50  
**Achieved FoS (Pin Shear Yield):** 0.97  
**Governing Criterion:** PV limit (bearing thermal/wear failure)  
**Governing Utilization:** 778%  
**PASS/FAIL Status:** **❌ CATASTROPHIC FAIL**

### 7.2 Failure Severity Assessment

**This configuration is fundamentally unsafe and would fail immediately under load.**

**Expected failure sequence:**
1. **Initial loading:** Bearing pressure immediately crushes polymer, causing deformation
2. **Within seconds:** Frictional heating drives PV thermal runaway
3. **Within minutes:** Bearing material begins to degrade, smoke, potentially melt
4. **Simultaneously:** Pin yields in bending and shear, causing permanent deformation
5. **Result:** Complete bearing destruction, bent/deformed pin, possible seizure

**Safety risk:** 
- Uncontrolled failure under load
- Potential for sudden rope release or block jamming
- Risk of injury if block fails while loaded
- **DO NOT BUILD OR TEST THIS CONFIGURATION**

### 7.3 Load Comparison

**Current geometry maximum capacity:**

From MORAAAAA-17 analysis, maximum bearing load at SF = 2.0:
```
F_max = 2.5 kN (with dynamic factor already applied)
```

**Current design load:**
```
F_design = 39.24 kN
```

**Overload factor:**
```
Overload = F_design / F_max
Overload = 39.24 / 2.5 = 15.7×
```

**Conclusion:** Design load exceeds bearing capability by **15.7×** (1570%).

### 7.4 What Load IS Feasible?

**Working backwards from bearing PV limit:**

To achieve SF_PV = 2.0 with current geometry (12mm × 20mm, 100 rpm):
```
PV_allowable = 1.32 MPa·m/s
Required PV_operating = 1.32 / 2.0 = 0.660 MPa·m/s

P_max = PV_operating / V
P_max = 0.660 / 0.0628 = 10.5 MPa

F_max = P_max × A
F_max = 10.5 MPa × 240 mm² = 2520 N = 2.52 kN
```

**Maximum rope tension for current configuration:**

With dynamic factor 2.0 and 180° deflection:
```
F_max = 2 × T_rope × DF
2.52 kN = 2 × T_rope × 2.0
T_rope = 2.52 / 4.0 = 0.63 kN = 630 N = 64 kg

Maximum rope load = 64 kg (0.064 tons)
```

**Conclusion:** Current geometry can handle maximum rope load of **~64 kg**, not 1000 kg (1 ton).

**Current specification exceeds capability by 16×** (1000 kg / 64 kg = 15.6×).

---

## 8. RECOMMENDATIONS

### 8.1 Immediate Decision

❌ **DO NOT PROCEED** with current design.

**Critical Issues:**
1. PV limit exceeded by 778%
2. Bearing pressure exceeded by 467%
3. Pin bending yield exceeded by 199%
4. Pin shear at yield limit

**Risk:** Catastrophic bearing and pin failure under load.

### 8.2 Design Alternatives Required

**The current 12mm × 20mm iglidur X bearing configuration is fundamentally unsuitable for 1-ton rope loads.**

**Option 1: Increase Bearing Length Dramatically**

Required bearing length to achieve SF = 2.0 (PV-limited):
```
PV_required = 0.660 MPa·m/s (for SF = 2.0)
P_required = PV / V = 0.660 / 0.0628 = 10.5 MPa

L_required = F / (P × d)
L_required = 39,240 N / (10.5 MPa × 12 mm)
L_required = 39,240 / (10.5 × 12)
L_required = 312 mm
```

**Verdict:** Bearing length of **312 mm** is completely impractical (15.6× current length).

**Option 2: Increase Pin Diameter Dramatically**

Required pin diameter to achieve SF = 2.0:
```
Target: Reduce pressure and increase pin strength

For PV limit (pressure-limited):
P_required = 10.5 MPa (from above)
d_required = F / (P × L)
d_required = 39,240 / (10.5 × 20) = 187 mm
```

**Verdict:** Pin diameter of **187 mm** is absurd (15.6× current diameter).

**Option 3: Upgrade Bearing Material**

*Bronze-PTFE Composite (DU bushing):*
- Maximum PV: 3.0-3.6 MPa·m/s (2.3-2.7× iglidur X)
- Still grossly insufficient:
  - SF_PV = 3.0 / 10.27 = 0.29 (still catastrophic)

*Torlon (PAI):*
- Maximum PV: 5.0+ MPa·m/s
- Still insufficient:
  - SF_PV = 5.0 / 10.27 = 0.49 (still fails)

**Verdict:** Even high-performance polymers cannot handle this load with current geometry.

**Option 4: Rolling Element Bearing**

*Ball or roller bearing (sealed, marine grade):*
- Typical load capacity: 10-100 kN (depending on size)
- Could potentially handle 39 kN design load
- Requires proper sizing and selection
- Sealed units required for saltwater environment

**Verdict:** Rolling element bearings are the ONLY viable option for this load level.

**Option 5: Completely Redesign Geometry**

For 1-ton rope loads with plain bearings, typical marine block sizing:
- Pin diameter: 25-40 mm (2-3× current)
- Bearing length: 40-80 mm (2-4× current)
- Stronger pin material or larger diameter to handle bending

Even with upgraded geometry, plain bearings may be marginal. Rolling element bearings strongly recommended for this duty.

### 8.3 Recommended Path Forward

**Primary Recommendation:**

**Switch to rolling element bearing (ball or roller) with appropriate load rating.**

Required bearing specifications:
- Static load rating: ≥ 40 kN (to handle 39.24 kN design load with margin)
- Dynamic load rating: ≥ 60 kN (for fatigue life)
- Sealed or shielded design for marine environment
- Corrosion-resistant materials (stainless steel or ceramic)
- Inner diameter: 12 mm (to use existing pin) OR resize entire assembly

**Alternative (if plain bearing required):**

Complete geometry redesign:
- Increase pin diameter to 25-30 mm
- Increase bearing length to 50-60 mm
- Consider bronze-PTFE composite bearing (higher PV capability)
- Redesign cheeks and structure for larger bearing
- Re-analyze all checks with new geometry

**Cost Reality:**

For 1-ton working loads in marine environments, standard practice is:
- Rolling element bearings OR
- Bronze bushings with substantial sizing (typical d > 25mm for 1t loads)

The original concept (12mm × 20mm iglidur X) is sized for light-duty applications (<100 kg rope loads), not 1-ton marine duty.

### 8.4 If Load Specification Is Negotiable

**If the actual load could be reduced:**

Maximum rope load for current geometry:
- **64 kg rope tension** (0.064 tons)
- This is 1/16 of the specified 1-ton load

**If application permits:**
- Reduce rope load to <70 kg
- Current design becomes viable
- All checks would achieve SF ≥ 2.0

---

## 9. SOURCES

### Material Properties
1. **igus GmbH - iglidur X Material Data:**  
   https://www.igus.eu/plain-bearing/materials/high-temperatures/iglidur-x-material-data  
   (Maximum PV: 1.32 MPa·m/s, Maximum pressure: 35 MPa)

2. **RS Online - iglidur X Technical Datasheet (PDF 8070):**  
   https://docs.rs-online.com/8070/0900766b80debd6b.pdf  
   (PV value confirmation, intermittent duty guidelines)

3. **ASTM A276 - Stainless Steel Bar and Shapes:**  
   (316 SS mechanical properties: σ_y = 290 MPa annealed, σ_u = 590 MPa)

### Design Standards
4. **ISO 4565 - Wire rope sheaves for lifting appliances:**  
   (Bearing pressure calculations, safety factors, sheave sizing)

5. **ABYC H-41 - Deck Hardware and Rigging Components:**  
   (Marine hardware safety factors, duty cycle considerations)

6. **Bruhn, "Analysis and Design of Flight Vehicle Structures", Chapter C8:**  
   (Bearing stress allowables, pin bending calculations)

### Calculation Methods
7. **02_AGENTS/Engineering/SKILLS/bearing_design.md**  
   (Bearing design methodology, PV check requirements, safety factor standards)

8. **02_AGENTS/Engineering/TASK_PATTERNS.md**  
   (Task Pattern #1: Load Case Analysis, input sufficiency requirements)

### Related Analyses
9. **[MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - Baseline Bearing PV Analysis (1 kN)**  
   iglidur X suitable at 1 kN load (PV = 0.262 MPa·m/s, SF = 5.04)

10. **[MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13) - Ti Cheek Structural Analysis**  
    Provides geometry inputs (bearing length 20mm, cheek thickness 6mm, diameter 12mm)

11. **[MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17) - Bearing PV at 4 kN**  
    iglidur X FAILS at 4 kN: PV = 1.047 MPa·m/s, SF = 1.26

---

## 10. DESIGN VERIFICATION CHECKLIST

- [x] Rigging geometry defined (180° rope deflection)
- [x] Rope tension specified (1 ton = 9.81 kN)
- [x] Bearing radial load calculated (19.62 kN geometric, 39.24 kN with DF)
- [x] Geometry verified (12mm × 20mm from previous analyses)
- [x] Material properties confirmed (iglidur X, 316 SS)
- [x] Bearing pressure calculated (163.5 MPa) ← **CATASTROPHIC FAIL**
- [x] Surface velocity calculated (0.0628 m/s)
- [x] PV value calculated (10.27 MPa·m/s) ← **CATASTROPHIC FAIL (GOVERNING)**
- [x] Pin bending stress calculated (578 MPa) ← **FAIL (exceeds yield)**
- [x] Pin shear stress calculated (173.5 MPa) ← **FAIL (at yield)**
- [x] Safety factors determined (all checks fail)
- [x] Governing failure mode identified (PV limit, thermal runaway)
- [x] NO-GO decision made (multiple catastrophic failures)
- [x] Design alternatives identified (rolling element bearing required)
- [x] Load capacity limit determined (max 64 kg rope, not 1000 kg)

---

## 11. REVISION HISTORY

| Rev | Date | Description | Engineer |
|-----|------|-------------|----------|
| A | 2026-04-29 | Initial analysis - 1t rope, 180° deflection, 39.24 kN design load | MORFRAC Engineering |

---

**Analysis Status:** ✓ COMPLETE  
**Decision:** ❌ **NO-GO - CATASTROPHIC FAILURE - DO NOT BUILD**  
**Governing Criterion:** PV limit (778% over, bearing thermal/wear failure)  
**Secondary Failures:** Bearing pressure (467% over), Pin bending (199% over yield), Pin shear (at yield)  
**Design load exceeds capability:** 15.7× (1570%)  
**Recommendation:** Switch to rolling element bearing OR completely redesign geometry with 2-3× larger components
