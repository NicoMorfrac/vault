# MORAAAAA-17: Bearing Analysis - Iglidur X @ 4 kN Load

**Date:** 2026-04-29  
**Engineer:** Engineering Agent  
**Task:** [MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17)  
**Project:** Sheave_Titanium_IglidurX  
**Related:** [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) (1kN baseline), [MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13) (Ti cheek structure)

---

## 1. PROBLEM STATEMENT

Evaluate a 12 mm diameter pin with iglidur X bearing for **4 kN radial load** (4× higher than baseline MORAAAAA-12). Verify bearing pressure, PV limits, and pin bending stress. Identify governing failure criterion and assess safety factors per Engineering skill requirements.

**Design Criteria:** 
- Required FoS: 2.0 (marine hardware, static basis)
- All checks must pass with FoS ≥ 2.0
- Governing utilization must be <100%

---

## 2. INPUTS & ASSUMPTIONS

### 2.1 Provided Inputs
- **Radial load:** F = 4000 N (4 kN)
- **Pin diameter:** d = 12 mm
- **Bearing material:** iglidur X (polymer bushing)
- **Application:** Marine rigging sheave, intermittent duty

### 2.2 Geometry (from MORAAAAA-13)
- **Bearing length:** L = 20 mm
- **Cheek thickness:** t = 6 mm (Ti-6Al-4V)
- **Configuration:** Double shear (two cheeks, one bearing)
- **Sheave diameter:** 75 mm outer diameter

### 2.3 Assumptions

**Operating Conditions (from MORAAAAA-12):**
- **Rotation speed:** 100 rpm (assumed from baseline analysis)
- **Pin material:** 316 Stainless Steel, hardened condition
- **Environment:** Saltwater, natural convection cooling
- **Duty cycle:** Intermittent (conservative baseline, no duty cycle credit applied)
- **Lubrication:** Dry running (self-lubricating polymer)

**Load Distribution:**
- Entire 4000 N radial load carried by bearing (conservative)
- No dynamic factor applied (load stated as 4 kN already includes factors)

**Pin Bending Configuration:**
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

**None critical for baseline assessment.**

Optional refinements for future iterations:
- Exact pin material condition (annealed vs cold-worked) - assumed conservative
- Detailed duty cycle % for intermittent operation credit
- Shaft surface finish specification (Ra < 1 μm recommended)
- Shaft hardness (assume HRC 45+ for polymer bearing compatibility)
- Exact pin support configuration (assumed simply supported at bearing edges)

**Decision:** Proceed with conservative assumptions. Flag any marginal results for refinement.

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
P = F / A_projected
P = 4000 N / 0.000240 m²
P = 16,666,667 Pa
P = 16.67 MPa
```

**Allowable pressure (iglidur X):**
```
P_allowable = 35 MPa (manufacturer's recommendation)
```

**Safety factor (pressure):**
```
SF_P = P_allowable / P_operating
SF_P = 35 MPa / 16.67 MPa
SF_P = 2.10
```

**Check:** ✓ **PASS** - Pressure safety factor = 2.10 (just meets requirement SF ≥ 2.0)

**Utilization:**
```
Utilization_P = (P_operating / P_allowable) × 100%
Utilization_P = (16.67 / 35) × 100% = 47.6%
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

**Check:** ✓ **PASS** - Velocity well within limits

---

### 4.3 PV Value Check

**PV calculation:**
```
PV = P × V
PV = 16.67 MPa × 0.0628 m/s
PV = 1.047 MPa·m/s
```

**Allowable PV (iglidur X, dry continuous):**
```
PV_allowable = 1.32 MPa·m/s
```

**Safety factor (PV):**
```
SF_PV = PV_allowable / PV_operating
SF_PV = 1.32 MPa·m/s / 1.047 MPa·m/s
SF_PV = 1.26
```

**Check:** ❌ **FAIL** - PV safety factor = 1.26 (below required SF ≥ 2.0)

**Utilization:**
```
Utilization_PV = (PV_operating / PV_allowable) × 100%
Utilization_PV = (1.047 / 1.32) × 100% = 79.3%
```

**Critical Finding:** PV limit is the governing constraint and fails the FoS = 2.0 requirement.

---

### 4.4 Pin Bending Stress Check

**Configuration:** Simply supported beam, uniformly distributed load over bearing length

**Maximum bending moment (center of span):**
```
M_max = (w × L²) / 8
where w = F / L = 4000 N / 20 mm = 200 N/mm

M_max = (200 N/mm × (20 mm)²) / 8
M_max = (200 × 400) / 8
M_max = 10,000 N·mm
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
σ_bending = 10,000 N·mm / 169.6 mm³
σ_bending = 59.0 MPa
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
SF_bending_yield = 290 MPa / 59.0 MPa
SF_bending_yield = 4.92
```

**Safety factor (pin bending ultimate):**
```
SF_bending_ultimate = σ_u / σ_bending
SF_bending_ultimate = 590 MPa / 59.0 MPa
SF_bending_ultimate = 10.0
```

**Check:** ✓ **PASS** - Pin bending stress well within limits

**Utilization:**
```
Utilization_bending = (σ_bending / σ_allowable) × 100%
Utilization_bending = (59.0 / 145) × 100% = 40.7%
```

---

### 4.5 Pin Shear Stress Check

**Configuration:** Double shear (load split between two shear planes)

**Shear force per plane:**
```
V_shear = F / 2
V_shear = 4000 N / 2 = 2000 N
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
τ = 2000 N / 113.1 mm²
τ = 17.7 MPa
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
SF_shear = 167.5 MPa / 17.7 MPa
SF_shear = 9.46
```

**Check:** ✓ **PASS** - Pin shear stress well within limits

**Utilization:**
```
Utilization_shear = (τ / τ_allowable) × 100%
Utilization_shear = (17.7 / 83.8) × 100% = 21.1%
```

---

## 5. RESULTS SUMMARY

| **Check** | **Operating** | **Allowable** | **Safety Factor** | **Utilization** | **Status** |
|-----------|---------------|---------------|-------------------|-----------------|------------|
| Bearing pressure | 16.67 MPa | 35 MPa | 2.10 | 47.6% | ✓ PASS |
| Surface velocity | 0.063 m/s | 1.5 m/s | 23.9 | 4.2% | ✓ PASS |
| **PV value** | **1.047 MPa·m/s** | **1.32 MPa·m/s** | **1.26** | **79.3%** | **❌ FAIL** |
| Pin bending (yield) | 59.0 MPa | 145 MPa | 4.92 | 40.7% | ✓ PASS |
| Pin bending (ultimate) | 59.0 MPa | 295 MPa | 10.0 | 20.0% | ✓ PASS |
| Pin shear | 17.7 MPa | 83.8 MPa | 9.46 | 21.1% | ✓ PASS |

---

## 6. GOVERNING CRITERION

**Governing Failure Mode:** **PV Limit (Bearing Wear/Thermal Overload)**

**Critical Result:**
- PV operating: 1.047 MPa·m/s
- PV allowable: 1.32 MPa·m/s
- **Safety factor: 1.26 (FAILS requirement SF ≥ 2.0)**
- **Governing utilization: 79.3%**

**Failure Mechanism:**
At PV values approaching the material limit, the iglidur X bearing will experience:
1. Excessive frictional heating
2. Accelerated wear rate
3. Potential thermal softening of polymer matrix
4. Reduced bearing life and increased friction
5. Possible bearing seizure under sustained operation

**Secondary Constraints:**
- Bearing pressure: SF = 2.10 (marginal, just meets requirement)
- Pin bending: SF = 4.92 (adequate margin)
- Pin shear: SF = 9.46 (excellent margin)

---

## 7. SAFETY ASSESSMENT

### 7.1 Overall Status

**DECISION:** ❌ **NO-GO** - Design fails PV safety factor requirement

**Required FoS:** 2.0 (marine hardware standard)  
**Achieved FoS (governing):** 1.26 (PV limit)  
**Achieved FoS (yield):** 4.92 (pin bending)  
**Achieved FoS (ultimate):** 10.0 (pin bending)  
**Governing Criterion:** PV limit  
**Governing Utilization:** 79.3%  
**PASS/FAIL Status:** **FAIL**

### 7.2 Comparison with Baseline (MORAAAAA-12)

| Parameter | Baseline (1 kN) | Current (4 kN) | Ratio |
|-----------|-----------------|----------------|-------|
| Load | 1000 N | 4000 N | 4.0× |
| Pressure | 4.17 MPa | 16.67 MPa | 4.0× |
| PV value | 0.262 MPa·m/s | 1.047 MPa·m/s | 4.0× |
| PV safety factor | 5.04 | 1.26 | 0.25× |

**Observation:** PV scales linearly with load. The 4× load increase results in 4× PV increase, reducing safety factor from 5.04 to 1.26.

### 7.3 Sensitivity Analysis

**Load sensitivity:**
- At 3 kN: PV = 0.785 MPa·m/s, SF = 1.68 (still below 2.0)
- At 2.64 kN: PV = 0.690 MPa·m/s, SF = 1.91 (marginal, <2.0)
- At 2.5 kN: PV = 0.654 MPa·m/s, SF = 2.02 (just meets requirement)

**Conclusion:** Maximum allowable load for SF = 2.0 is approximately **2.5 kN** at 100 rpm.

**Speed sensitivity:**
- At 50 rpm: V = 0.0314 m/s, PV = 0.524 MPa·m/s, SF = 2.52 (acceptable)
- At 75 rpm: V = 0.0471 m/s, PV = 0.785 MPa·m/s, SF = 1.68 (marginal)

**Conclusion:** Reducing speed to 50 rpm would achieve SF ≥ 2.0 at 4 kN load.

### 7.4 Intermittent Duty Consideration

**igus guidelines** allow PV limit increases for short-duration operation:
- Typical intermittent correction factor: 1.5× to 2.0× for duty cycles <20%
- **Effective PV limit (intermittent, 20% duty):** ~2.0-2.6 MPa·m/s

**Intermittent safety factor:**
```
SF_PV_intermittent = 2.0 MPa·m/s / 1.047 MPa·m/s = 1.91 (marginal)
SF_PV_intermittent = 2.6 MPa·m/s / 1.047 MPa·m/s = 2.48 (acceptable)
```

**Conclusion:** If duty cycle can be confirmed as <20% (intermittent use, short duration), the design may be acceptable. However, without explicit duty cycle data, baseline continuous rating must be used.

---

## 8. RECOMMENDATIONS

### 8.1 Immediate Decision

❌ **DO NOT PROCEED** with iglidur X bearing at 4 kN continuous load without modifications.

**Governing constraint:** PV limit (SF = 1.26, below required 2.0)

### 8.2 Design Options to Achieve Compliance

**Option 1: Reduce Operating Speed**
- Reduce rotation speed from 100 rpm to **50 rpm**
- New PV: 0.524 MPa·m/s
- New SF: 2.52 ✓
- **Pro:** Simple operational change, no hardware modification
- **Con:** Reduced sheave capacity, slower operation

**Option 2: Increase Bearing Length**
- Increase bearing length from 20 mm to **40 mm**
- New pressure: 8.33 MPa
- New PV: 0.524 MPa·m/s
- New SF: 2.52 ✓
- **Pro:** Achieves required SF, stays within iglidur X capability
- **Con:** Increased bearing cost, longer assembly width, heavier

**Option 3: Upgrade Bearing Material**

*Alternative 1: iglidur X6 (enhanced iglidur X)*
- Higher pressure capability: ~40-50 MPa
- Higher PV capability: ~1.8-2.0 MPa·m/s (estimated)
- SF (estimated): 1.72-1.91 (marginal improvement)
- **Pro:** Drop-in replacement, similar characteristics
- **Con:** Still marginal, higher cost

*Alternative 2: Bronze-PTFE Composite (DU bushing)*
- Maximum PV: 3.0-3.6 MPa·m/s
- Current operating PV: 1.047 MPa·m/s
- New SF: 2.87-3.44 ✓
- **Pro:** Excellent margin, proven marine performance
- **Con:** Requires harder shaft (HRC 55+), higher cost, heavier

*Alternative 3: Torlon (PAI)*
- Maximum PV: 5.0+ MPa·m/s
- New SF: 4.77 ✓
- **Pro:** Extreme performance, excellent chemical resistance
- **Con:** Very high cost, may be overkill for application

*Alternative 4: Silicon Nitride Ceramic Bearings*
- Extremely high PV capability (>10 MPa·m/s)
- **Pro:** Ultimate performance, corrosion-proof
- **Con:** Very high cost, brittle (impact sensitive), specialized design

**Option 4: Confirm Intermittent Duty Cycle**
- If duty cycle can be documented as <20% active operation
- Apply intermittent correction factor per igus guidelines
- Effective PV limit: 2.0-2.6 MPa·m/s
- Resulting SF: 1.91-2.48 (marginal to acceptable)
- **Pro:** No hardware changes required
- **Con:** Requires operational constraints, duty cycle monitoring

**Option 5: Reduce Design Load**
- Reduce maximum operating load to **2.5 kN**
- New PV: 0.654 MPa·m/s
- New SF: 2.02 ✓
- **Pro:** Achieves compliance with iglidur X
- **Con:** May not meet application requirements

### 8.3 Recommended Path Forward

**Primary Recommendation:**

1. **Clarify operating requirements:**
   - Confirm actual duty cycle (continuous vs intermittent)
   - Confirm maximum operating speed (100 rpm is assumption)
   - Confirm load factor application (is 4 kN already factored or nominal?)

2. **If continuous duty at 4 kN is required:**
   - **Option 2:** Increase bearing length to 40 mm (most robust solution)
   - **Option 3.2:** Upgrade to Bronze-PTFE composite bearing (higher performance)

3. **If intermittent duty (<20%) can be confirmed:**
   - Apply intermittent correction factor
   - Re-evaluate with effective PV limit ~2.0-2.6 MPa·m/s
   - May achieve acceptable SF with current design

4. **If speed flexibility exists:**
   - Reduce operating speed to 50 rpm (simplest solution)

### 8.4 Cost-Performance Tradeoff

| Solution | Est. Cost Impact | Performance | Complexity |
|----------|-----------------|-------------|------------|
| Reduce speed to 50 rpm | None | Moderate | Low |
| Increase bearing length to 40mm | +30% | Good | Low |
| Bronze-PTFE composite | +150% | Excellent | Medium |
| Torlon bearing | +300% | Extreme | Medium |
| Confirm intermittent duty | None | Moderate* | Low |

*Depends on actual duty cycle documentation

---

## 9. SOURCES

### Material Properties
1. **igus GmbH - iglidur X Material Data:**  
   https://www.igus.eu/plain-bearing/materials/high-temperatures/iglidur-x-material-data  
   (Maximum PV: 1.32 MPa·m/s, Maximum pressure: 35 MPa)

2. **RS Online - iglidur X Technical Datasheet (PDF 8070):**  
   https://docs.rs-online.com/8070/0900766b80debd6b.pdf  
   (PV value confirmation, intermittent duty guidelines)

3. **igus GmbH - PV Value and Lubrication Guide:**  
   https://www.igus.eu/plain-bearing/wiki/px-v-value-and-lubrication  
   (Intermittent duty correction factors)

4. **ASTM A276 - Stainless Steel Bar and Shapes:**  
   (316 SS mechanical properties: σ_y = 290 MPa annealed, σ_u = 590 MPa)

5. **ASM Aerospace Specification Metals Inc:**  
   (Stainless steel properties, hardness vs strength relationships)

### Design Standards
6. **ISO 4565 - Wire rope sheaves for lifting appliances:**  
   (Bearing pressure calculations, safety factors)

7. **ABYC H-41 - Deck Hardware and Rigging Components:**  
   (Marine hardware safety factors, duty cycle considerations)

8. **Bruhn, "Analysis and Design of Flight Vehicle Structures", Chapter C8:**  
   (Bearing stress allowables, pin bending calculations)

### Calculation Methods
9. **02_AGENTS/Engineering/SKILLS/bearing_design.md.md**  
   (Bearing design methodology, PV check requirements, safety factor standards)

10. **02_AGENTS/Engineering/TASK_PATTERNS.md.md**  
    (Task Pattern #1: Load Case Analysis, input sufficiency requirements)

### Related Analyses
11. **[MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - Baseline Bearing PV Analysis (1 kN)**  
    Confirms iglidur X is suitable at 1 kN load (PV = 0.262 MPa·m/s, SF = 5.04)

12. **[MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13) - Ti Cheek Structural Analysis**  
    Provides geometry inputs (bearing length 20mm, cheek thickness 6mm, diameter 12mm)

---

## 10. DESIGN VERIFICATION CHECKLIST

- [x] Geometry inputs verified (from MORAAAAA-13)
- [x] Load case defined (4 kN radial)
- [x] Material properties confirmed (iglidur X, 316 SS)
- [x] Bearing pressure calculated (16.67 MPa)
- [x] Surface velocity calculated (0.0628 m/s)
- [x] PV value calculated (1.047 MPa·m/s) ← **GOVERNING**
- [x] Pin bending stress calculated (59.0 MPa)
- [x] Pin shear stress calculated (17.7 MPa)
- [x] Safety factors determined
- [x] Governing failure mode identified (PV limit)
- [x] NO-GO decision made (SF < 2.0 for PV)
- [x] Design alternatives identified
- [x] Recommendations provided

---

## 11. REVISION HISTORY

| Rev | Date | Description | Engineer |
|-----|------|-------------|----------|
| A | 2026-04-29 | Initial analysis - 4 kN load case evaluation | MORFRAC Engineering |

---

**Analysis Status:** ✓ COMPLETE  
**Decision:** ❌ **NO-GO** - PV limit exceeded (SF = 1.26 < required 2.0)  
**Governing Criterion:** PV limit (bearing wear/thermal)  
**Next Action:** CTO decision on design modifications (see Section 8 recommendations)
