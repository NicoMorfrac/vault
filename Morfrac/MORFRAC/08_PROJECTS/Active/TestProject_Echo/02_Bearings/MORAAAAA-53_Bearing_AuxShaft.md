# Bearing Analysis - Auxiliary Shaft

## Issue Reference
IssueID: MORAAAAA-53

## Component
Auxiliary shaft bearing assembly

## Material
IglidurX

## Geometry
- Shaft diameter: d = 22 mm
- Bearing length: L = 28 mm
- Projected area: A = d x L = 616 mm²

## Loading
- Radial load: F = 450 N
- Load type: Static

## Operating Conditions
- Sliding velocity: v = 0.35 m/s
- Operating temperature: 38 degC

## Design Criteria
- Required safety factor: 2.0

## Material Properties (IglidurX_Bearing_Data.md)
- PV_max: 1.32 MPa*m/s
- P_max_static: 100 MPa
- v_max: 2.0 m/s
- Recommended_SF: 2.0

## Calculations

### Bearing Pressure
P = F / A
P = 450 N / 616 mm²
P = 0.730 MPa

### PV Value
PV = P x v
PV = 0.730 MPa x 0.35 m/s
PV = 0.256 MPa*m/s

### Allowable PV
PV_allowable = PV_max / Required_FoS
PV_allowable = 1.32 MPa*m/s / 2.0
PV_allowable = 0.66 MPa*m/s

### Material FoS
Material_FoS = PV_max / PV_operating
Material_FoS = 1.32 / 0.256
Material_FoS = 5.16

### Design Margin
Design_margin = PV_allowable / PV_operating
Design_margin = 0.66 / 0.256
Design_margin = 2.58

## Checks

### Pressure Check
P = 0.730 MPa <= P_max_static = 100 MPa
Result: PASS

### Velocity Check
v = 0.35 m/s <= v_max = 2.0 m/s
Result: PASS

### PV Check
PV = 0.256 MPa*m/s <= PV_allowable = 0.66 MPa*m/s
Result: PASS
Design_margin = 2.58 >= 1.0
Result: PASS

## Summary

### Governing Criterion
PV limit

### Utilization
Utilization = PV_operating / PV_allowable
Utilization = 0.256 / 0.66
Utilization = 0.388 = 38.8%

### Safety Factors
- Material FoS: 5.16
- Design margin: 2.58

### Overall Result
PASS

## Notes
Pressure calculated using projected area method; actual distribution not evaluated
