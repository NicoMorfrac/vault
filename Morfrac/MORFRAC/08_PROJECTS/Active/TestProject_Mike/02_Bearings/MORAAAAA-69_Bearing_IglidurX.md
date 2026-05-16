# Bearing Analysis - Tail Pulley Assembly

## Problem Statement

Evaluate IglidurX plain bearing for tail pulley assembly under static radial load.

## Inputs and Assumptions

### Geometry
- Shaft diameter: d = 31 mm
- Bearing length: L = 39 mm

### Loading
- Radial load: F = 620 N
- Load type: Static radial bearing load

### Operating Conditions
- Sliding velocity: v = 0.52 m/s
- Operating temperature: 49 degC

### Material
- Bearing material: IglidurX

### Design Criteria
- Required safety factor: 2.0

### Assumptions
- Load values are design loads
- Pressure calculated using projected area method; actual distribution not evaluated

## Missing Inputs

None

## Calculations

### Projected Area
A = d x L = 31 x 39 = 1209 mm^2

### Bearing Pressure
P = F / A = 620 / 1209 = 0.513 MPa

### PV Product
PV = P x v = 0.513 x 0.52 = 0.267 MPa*m/s

### Material FoS
Material FoS = PV_max / PV_operating
Material FoS = 1.32 / 0.267 = 4.94

### PV Allowable
PV_allowable = PV_max / Required_FoS
PV_allowable = 1.32 / 2.0 = 0.66 MPa*m/s

### Design Margin
Design margin = PV_allowable / PV_operating
Design margin = 0.66 / 0.267 = 2.47

## Results

| Parameter | Value | Limit | Status |
|-----------|-------|-------|--------|
| Pressure | 0.513 MPa | 100 MPa | PASS |
| Velocity | 0.52 m/s | 2.0 m/s | PASS |
| PV Product | 0.267 MPa*m/s | 0.66 MPa*m/s | PASS |
| Material FoS | 4.94 | N/A | N/A |
| Design margin | 2.47 | >= 1.0 | PASS |

## Governing Criterion

Design margin: 2.47

## Safety Assessment

**Status: PASS**

All checks satisfied:
- Pressure: 0.513 <= 100 MPa
- Velocity: 0.52 <= 2.0 m/s
- Design margin: 2.47 >= 1.0

Utilization: 37.5%

## Sources

Material data: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md
