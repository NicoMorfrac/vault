# MORAAAAA-18: Bearing Analysis - Load Specification Clarification Required

**Date:** 2026-04-29  
**Engineer:** Engineering Agent  
**Task:** [MORAAAAA-18](/MORAAAAA/issues/MORAAAAA-18)  
**Project:** Sheave_Titanium_IglidurX  
**Related:** [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) (1kN baseline, PASS), [MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17) (4kN load, FAIL)

---

## 1. PROBLEM STATEMENT

**Task Specification:** "Check an iglidur X plain bearing for a block with a working load of 2t."

**Issue:** The term "working load of 2t" is **ambiguous** and insufficient to proceed with bearing analysis.

**Status:** ⚠️ **BLOCKED** - Critical input clarification required

---

## 2. SPECIFICATION AMBIGUITY

The specification "2t working load" could mean:

### Interpretation 1: **2-ton (20 kN) bearing load**
- Direct radial load on the bearing pin = 20,000 N
- This would be an extremely high load for the current geometry

### Interpretation 2: **2-ton rope Safe Working Load (SWL)**
- Rope rated capacity = 2000 kg
- Actual bearing load depends on:
  - Rigging configuration (single sheave, redirect, purchase system)
  - Number of rope parts through block
  - Wrap angle
  - Dynamic load factors
- For a simple redirect: bearing load ≈ 2 × rope tension
- For a 2:1 purchase: bearing load ≈ rope tension
- **Without rigging geometry, bearing load cannot be determined**

### Interpretation 3: **2-ton block rating (manufacturer WLL)**
- Block assembly rated for 2t total system load
- Bearing load would depend on internal mechanical advantage
- Typically bearing load > system WLL due to geometry

---

## 3. PRELIMINARY FEASIBILITY ASSESSMENT

Based on previous analyses in this project, I can provide bounds on what the iglidur X bearing can handle:

### 3.1 Known Performance Limits

**Geometry (from MORAAAAA-13, MORAAAAA-17):**
- Pin diameter: 12 mm
- Bearing length: 20 mm
- Bearing material: iglidur X
- Operating speed: 100 rpm

**Previous Results:**

| Load Case | PV Value | PV Safety Factor | Status |
|-----------|----------|------------------|--------|
| 1 kN ([MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12)) | 0.262 MPa·m/s | 5.04 | ✓ PASS |
| 4 kN ([MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17)) | 1.047 MPa·m/s | 1.26 | ❌ FAIL |
| **Maximum @ SF=2.0** | **0.660 MPa·m/s** | **2.0** | **~2.5 kN limit** |

**Critical Finding:** Current geometry is limited to approximately **2.5 kN bearing load** at 100 rpm to achieve required safety factor of 2.0.

### 3.2 Preliminary Estimate: 20 kN Bearing Load (If Interpretation 1)

**If the specification means 20 kN direct bearing load:**

**PV Calculation:**
```
Pressure:
P = F / (d × L)
P = 20,000 N / (12 mm × 20 mm)
P = 20,000 / 240 = 83.3 MPa

Surface velocity (@ 100 rpm):
V = π × d × n = π × 0.012 m × (100/60) rev/s = 0.0628 m/s

PV value:
PV = P × V
PV = 83.3 MPa × 0.0628 m/s
PV = 5.23 MPa·m/s
```

**Comparison to limits:**
```
PV_allowable (iglidur X) = 1.32 MPa·m/s
PV_operating = 5.23 MPa·m/s

Safety Factor:
SF_PV = 1.32 / 5.23 = 0.25
```

**Result:** ❌ **CATASTROPHIC FAILURE** 
- PV exceeds material limit by **396%**
- Safety factor = 0.25 (operating at 4× material limit)
- **This configuration is completely infeasible**

**Bearing pressure check:**
```
P_allowable (iglidur X) = 35 MPa
P_operating = 83.3 MPa

Safety Factor:
SF_P = 35 / 83.3 = 0.42
```

**Result:** ❌ **ALSO FAILS pressure limit**
- Pressure exceeds material limit by **238%**
- Immediate bearing crushing would occur

### 3.3 Scenario: 2-ton Rope SWL in Simple Redirect (If Interpretation 2)

**Assumptions for estimation:**
- 2t rope working load = 2000 kg × 9.81 = 19,620 N rope tension
- Simple redirect sheave: bearing load ≈ 2 × rope tension (vector addition)
- Dynamic factor: 2.0 (already specified in project)

**Bearing load estimate:**
```
F_bearing = 2 × T_rope × DF
F_bearing = 2 × 19,620 N × 2.0
F_bearing = 78,480 N ≈ 78 kN
```

**Result:** Even worse than Interpretation 1 - completely infeasible.

**Alternative (no dynamic factor applied yet):**
```
F_bearing = 2 × 19,620 N = 39,240 N ≈ 39 kN
```

**Result:** Still catastrophically exceeds bearing capability by ~16×.

### 3.4 What Load IS Feasible?

**Maximum bearing load for current geometry:**
- With iglidur X at 100 rpm: **~2.5 kN** (with SF = 2.0)

**If "2t working load" must be achieved, design changes required:**

**Option 1: Increase bearing length** (keeping iglidur X, 100 rpm)
- To handle 20 kN: Need bearing length ≈ 160 mm (8× current)
- To handle 10 kN: Need bearing length ≈ 80 mm (4× current)
- **Practical limit:** ~40-50 mm before other issues dominate

**Option 2: Upgrade bearing material**
- Bronze-PTFE composite: PV limit ~3.0-3.6 MPa·m/s (2.3-2.7× iglidur X)
- Could handle ~5.8-6.3 kN with current geometry
- Still insufficient for 20 kN

**Option 3: Reduce speed**
- 50 rpm: doubles allowable load to ~5 kN
- 25 rpm: quadruples allowable load to ~10 kN
- Still insufficient for 20 kN direct bearing load

**Option 4: Hybrid ball/roller bearing**
- Could handle 20 kN with appropriate sizing
- Requires sealed unit for marine environment
- Different cost/complexity profile

**Conclusion:** If bearing load truly exceeds ~5-10 kN, iglidur X plain bearing is fundamentally unsuitable. A completely different bearing solution would be required.

---

## 4. MISSING CRITICAL INPUTS

Per Engineering Agent TASK_PATTERNS Step 0 and bearing_design skill:
> "If critical inputs are missing, request them before proceeding."
> "Do not invent, infer or assume missing load, geometry, material, speed, duty cycle, temperature or boundary conditions."

**Required clarifications:**

### Critical:
1. **What does "2t working load" mean?**
   - [ ] 2-ton direct bearing radial load (20 kN)?
   - [ ] 2-ton rope Safe Working Load (SWL)?
   - [ ] 2-ton block assembly rating?
   - [ ] Other interpretation?

2. **What is the actual bearing load in Newtons?**
   - If rope load: what is the rigging configuration?
   - How many rope parts through the sheave?
   - What is the wrap angle or load vector geometry?
   - Has dynamic factor already been applied, or should I apply it?

3. **Load factor clarification:**
   - Is 2t the nominal working load (requiring dynamic factor)?
   - Or is 2t already factored load?
   - Project specifies DF = 2.0, but unclear if already applied

### Important for design alternatives:
4. **Are design changes acceptable?**
   - Can bearing length be increased?
   - Can bearing material be changed?
   - Can operating speed be reduced?
   - Can bearing type be changed (plain → ball/roller)?

5. **What is the actual application context?**
   - Single sheave redirect?
   - Block and tackle (what ratio)?
   - Halyard block?
   - Sheet block?
   - Other rigging function?

---

## 5. RECOMMENDED CLARIFICATION PATH

### Option A: Provide Direct Bearing Load
**If you know the actual radial load on the bearing pin:**
- Provide bearing load in Newtons or kN
- Specify if this is nominal or factored load
- I will immediately proceed with PV analysis

### Option B: Provide Rigging Context
**If you know the rope load and rigging configuration:**
- Rope working load or tension (in kg, N, or kN)
- Rigging configuration (sketch or description)
- Number of rope parts through sheave
- Wrap angle or load vectors
- Whether dynamic factor has been applied
- I will calculate bearing load and proceed

### Option C: Provide Application Description
**If starting from functional requirements:**
- What is this block for? (halyard, sheet, purchase, etc.)
- What size boat or load case?
- Maximum rope tension expected
- I will work backwards to bearing load requirements

---

## 6. PRELIMINARY RECOMMENDATION

**Based on context from MORAAAAA-17 (4 kN failure):**

The jump from 4 kN (which FAILED) to a potential 20 kN (if "2t" means bearing load) suggests either:

1. **Specification error** - Perhaps "2t" is meant to be "2 kN" (2000 N)?
   - This would be within feasible range
   - Would require detailed analysis but likely achievable with current geometry

2. **Different block concept** - Perhaps this refers to a completely different design?
   - Not the 12mm pin × 20mm bearing configuration from MORAAAAA-13/17?
   - Requires starting from scratch with new geometry

3. **System-level rating** - Perhaps "2t block" refers to total assembly rating?
   - Bearing load would need to be calculated from system requirement
   - Requires mechanical advantage and load path analysis

**Recommended next step:**
- CTO to clarify load specification
- Provide either direct bearing load OR complete rigging context
- I will then proceed with appropriate analysis

---

## 7. SOURCES

### Previous Project Analyses
1. **[MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - Baseline Bearing PV Analysis (1 kN)**  
   iglidur X suitable at 1 kN: PV = 0.262 MPa·m/s, SF = 5.04 ✓

2. **[MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13) - Ti Cheek Structural Analysis**  
   Current geometry: 12mm pin × 20mm bearing length

3. **[MORAAAAA-17](/MORAAAAA/issues/MORAAAAA-17) - Bearing PV at 4 kN**  
   iglidur X FAILS at 4 kN: PV = 1.047 MPa·m/s, SF = 1.26 ❌

### Engineering Standards
4. **02_AGENTS/Engineering/TASK_PATTERNS.md**  
   Step 0 — Input Sufficiency Check: "If critical inputs are missing, classify BLOCKED"

5. **02_AGENTS/Engineering/SKILLS/bearing_design.md**  
   "Do not invent, infer or assume missing load... If any critical bearing input is missing, classify BLOCKED"

6. **08_PROJECTS/Active/Sheave_Titanium_IglidurX/00_Project_Index.md**  
   Project context: FoS target 2.0, Dynamic factor 2.0, Marine duty

---

## 8. ACTION REQUIRED

**Status:** ⚠️ **BLOCKED** - Awaiting CTO clarification

**Cannot proceed with bearing analysis until:**
- Load specification ambiguity is resolved
- Actual bearing radial load (in Newtons) is confirmed
- OR complete rigging geometry is provided to calculate bearing load

**Recommended response:**
Please clarify what "2t working load" means:
- If direct bearing load: state in kN (I will show it's infeasible with current geometry)
- If rope load: provide rigging configuration (I will calculate bearing load)
- If system rating: provide mechanical advantage details (I will determine bearing load)

Alternatively: If this is a specification error and you meant "2 kN" (not "2 tons"), please confirm and I will proceed immediately.

---

## 9. REVISION HISTORY

| Rev | Date | Description | Engineer |
|-----|------|-------------|----------|
| A | 2026-04-29 | Task BLOCKED - Load specification ambiguous, clarification required | MORFRAC Engineering |

---

**Analysis Status:** ⚠️ **BLOCKED**  
**Blocking Issue:** Load specification "2t working load" is ambiguous  
**Required Action:** CTO to clarify actual bearing load or provide rigging configuration  
**Next Step:** Upon clarification, proceed with appropriate bearing PV analysis
