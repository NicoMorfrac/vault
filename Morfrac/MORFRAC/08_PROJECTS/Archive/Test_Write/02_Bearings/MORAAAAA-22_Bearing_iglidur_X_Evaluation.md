# Bearing Evaluation - iglidur X

**Issue ID**: MORAAAAA-22  
**Date**: 2026-05-01  
**Analyst**: Engineering Agent  
**Status**: COMPLETE

---

## 1. Problem Statement

Evaluate iglidur X polymer bearing for marine application under specified loading and operating conditions.

---

## 2. Inputs & Assumptions

### Given Inputs
- **Radial load**: F = 1000 N
- **Pin diameter**: d = 10 mm
- **Bearing length**: L = 12 mm
- **Bearing material**: iglidur X (self-lubricating polymer)
- **Rotational speed**: n = 30 rpm
- **Duty cycle**: Intermittent
- **Operating environment**: Marine
- **Temperature**: T = 25°C

### Assumptions
- **Pin material**: Stainless steel 316 (standard for marine applications)
- **Dynamic load factor**: 2.0 (standard for intermittent duty, marine hardware)
- **Required safety factor**: 2.0 (marine critical applications)
- **Clean operating conditions** (no abrasive contamination)
- **Proper installation** (no edge loading or misalignment)

---

## 3. Applicable Standards & References

- iglidur X material data: `04_ENGINEERING/Materials/iglidur_X_bearing_data.md`
- Maximum PV limit for iglidur X: **1.32 MPa·m/s**
- Design allowable with SF 2.0: **0.66 MPa·m/s**
- Bearing design methodology: `02_AGENTS/Engineering/SKILLS/bearing_design.md`

---

## 4. Calculations

### 4.1 Applied Load with Dynamic Factor

**Dynamic load factor** = 2.0 (intermittent duty)

**Design load**:
```
F_design = F × DF
F_design = 1000 N × 2.0
F_design = 2000 N
```

### 4.2 Bearing Pressure

**Projected bearing area**:
```
A_proj = d × L
A_proj = 10 mm × 12 mm
A_proj = 120 mm²
```

**Bearing pressure**:
```
P = F_design / A_proj
P = 2000 N / 120 mm²
P = 16.67 N/mm²
P = 16.67 MPa
```

### 4.3 Surface Velocity

**Surface velocity at bearing interface**:
```
V = (π × d × n) / 60000
V = (π × 10 mm × 30 rpm) / 60000
V = 942.48 / 60000
V = 0.0157 m/s
```

### 4.4 PV Value

**Operating PV**:
```
PV = P × V
PV = 16.67 MPa × 0.0157 m/s
PV = 0.262 MPa·m/s
```

---

## 5. Results Summary

| Parameter | Value | Unit |
|-----------|-------|------|
| Design Load (with DF 2.0) | 2000 | N |
| Bearing Pressure | 16.67 | MPa |
| Surface Velocity | 0.0157 | m/s |
| Operating PV | 0.262 | MPa·m/s |
| Maximum PV (iglidur X) | 1.32 | MPa·m/s |
| Allowable PV (SF 2.0) | 0.66 | MPa·m/s |

---

## 6. Governing Criterion

**Governing check**: PV limit

**PV Utilization**:
```
Utilization = PV_operating / PV_allowable
Utilization = 0.262 / 0.66
Utilization = 39.7%
```

---

## 7. Safety Assessment

### Safety Margins

- **Required Safety Factor**: 2.0
- **Achieved PV Safety Factor**: 5.04 (= 1.32 / 0.262)
- **Against Design Allowable**: 2.52 (= 0.66 / 0.262)
- **Governing Criterion**: PV limit
- **Governing Utilization**: 39.7%

### Pass/Fail Status

**PASS** ✓

The operating PV of 0.262 MPa·m/s is **well below** the design allowable of 0.66 MPa·m/s (SF 2.0).

**Margin to design allowable**: 60.3%

---

## 8. Recommendations

### Design Adequacy
- ✓ iglidur X is **suitable** for this application
- ✓ Low utilization (39.7%) provides robust margin
- ✓ Intermittent duty and low speed are favorable for polymer bearings
- ✓ Marine environment is acceptable (iglidur X is corrosion resistant)

### Design Notes
1. **Fit tolerance**: Ensure proper press-fit or retention to prevent bearing rotation in housing
2. **Chamfers**: Provide chamfers on bearing edges to reduce edge loading risk
3. **Shaft finish**: Recommend Ra ≤ 0.8 μm for SS316 pin to minimize wear
4. **Temperature**: Operating at 25°C is well within iglidur X limits (~250°C max)
5. **Contamination**: Protect from abrasive contamination which accelerates wear
6. **No lubrication required**: iglidur X is self-lubricating

### Monitoring
- Monitor for wear during initial service cycles
- Check for proper bearing retention and alignment
- Inspect for edge loading (uneven wear patterns)

---

## 9. Failure Modes & Mitigation

| Failure Mode | Risk | Mitigation |
|--------------|------|------------|
| Excessive wear | Low (PV well below limit) | Proper shaft finish, avoid contamination |
| Bearing creep/rotation | Medium | Proper press-fit, retention groove if needed |
| Edge loading | Medium | Chamfer edges, ensure alignment |
| Thermal expansion mismatch | Low (at 25°C) | Allow for thermal growth if temp varies |
| Abrasive contamination | Medium (marine) | Seal design, regular inspection |

---

## 10. Sources

1. iglidur X bearing data: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\04_ENGINEERING\Materials\iglidur_X_bearing_data.md`
2. Bearing design skill: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Engineering\SKILLS\bearing_design.md`
3. System engineering rules: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\00_SYSTEM\ENGINEERING_RULES.md`
4. igus bearing calculator reference: https://www.igus.com/info/bearing-calculation

---

## Revision History

| Date | Rev | Description |
|------|-----|-------------|
| 2026-05-01 | A | Initial evaluation |
