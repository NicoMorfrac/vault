# Bearing Analysis: iglidur X

**Issue ID**: MORAAAAA-23
**Date**: 2026-05-01
**Analyst**: Engineering Agent

---

## 1. Problem Statement

Evaluate iglidur X bearing suitability for given load, geometry, and operating conditions.

---

## 2. Inputs and Assumptions

### Given Inputs
- Radial load: 1000 N
- Pin diameter: 10 mm
- Bearing length: 12 mm
- Material: iglidur X
- Speed: 30 rpm
- Duty: intermittent
- Environment: marine
- Temperature: 25 degC

### Assumptions
- Load is radial and uniformly distributed
- Pin material not specified - pin bending and shear checks excluded
- Support geometry not specified - support checks excluded
- Static load case (no dynamic load factor applied per input specification)
- Input load is design load
- Sea water environment
- iglidur X max PV limit: 1.32 MPa*m/s (manufacturer limit)

---

## 3. Missing Inputs

The following inputs were not provided. Associated checks are excluded from this analysis:

- Pin material (excludes pin bending and shear checks)
- Support geometry (excludes support structure checks)

---

## 4. Calculations

### 4.1 Bearing Pressure

Projected bearing area:
A_proj = d x L = 10 mm x 12 mm = 120 mm²

Bearing pressure:
P = F / A_proj
P = 1000 N / 120 mm²
P = 8.33 MPa

### 4.2 Surface Velocity

Surface velocity at bearing interface:
V = (pi x d x n) / 60000
V = (pi x 10 mm x 30 rpm) / 60000
V = 942.48 / 60000
V = 0.0157 m/s

### 4.3 PV Value

Operating PV:
PV = P x V
PV = 8.33 MPa x 0.0157 m/s
PV = 0.131 MPa*m/s

---

## 5. Results

| Parameter | Value | Unit |
|-----------|-------|------|
| Bearing pressure | 8.33 | MPa |
| Surface velocity | 0.0157 | m/s |
| Operating PV | 0.131 | MPa*m/s |
| Maximum PV (iglidur X) | 1.32 | MPa*m/s |
| Allowable PV (with FoS 2.0) | 0.66 | MPa*m/s |

---

## 6. Governing Criterion

**Governing check**: PV limit

**Utilization**: 0.131 / 0.66 = 19.8%

---

## 7. Safety Assessment

### Required Design Factors
- Required FoS: 2.0 (marine application)

### Achieved Safety Factors
- Achieved FoS (PV): 1.32 / 0.131 = **10.08**
- Achieved FoS (bearing pressure): N/A (pressure limit not separately specified for iglidur X)

### Status
**PASS**

Operating PV (0.131 MPa*m/s) is well below allowable PV (0.66 MPa*m/s).

The bearing achieves FoS of 10.08 against the material PV limit, which significantly exceeds the required FoS of 2.0 for marine applications.

---

## 8. Recommendations

### Design Adequacy
The iglidur X bearing **passes** for the supplied inputs.

### Notes
1. Pin bending and shear checks were excluded due to missing pin material specification
2. Support structure checks were excluded due to missing support geometry
3. Low utilization (19.8%) suggests the bearing is significantly oversized for this application
4. Consider reducing bearing length or pin diameter if weight/space optimization is desired
5. Intermittent duty cycle is favorable for polymer bearing performance
6. Marine environment compatibility: iglidur X is suitable for seawater exposure
7. Temperature (25 degC) is well within iglidur X operating range

### Design Improvements (Optional)
- If weight reduction is desired, bearing length could be reduced to approximately 5-6 mm while maintaining adequate safety margin
- Verify actual pin material and perform complete pin stress analysis
- Consider edge loading effects if bearing mounting allows misalignment

---

## 9. Sources

- Material data: `04_ENGINEERING/Materials/iglidur_X_bearing_data.md`
- Analysis skill: `02_AGENTS/Engineering/SKILLS/bearing_design.md`
- Design rules: `00_SYSTEM/ENGINEERING_RULES.md`
- igus bearing technical documentation
