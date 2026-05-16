# Bearing PV Analysis - IglidurX Plain Bearing

## Problem Statement

Evaluate IglidurX plain bearing for radial load application under rotating shaft conditions.

## Inputs and Assumptions

### Given Inputs
- Radial load: F = 1000 N
- Shaft diameter: d = 10 mm
- Bearing length: L = 12 mm
- Rotational speed: n = 30 rpm

### Material Properties
Source: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md

- PV_max: 1.32 MPa*m/s
- PV_allowable: 0.66 MPa*m/s (with FoS = 2.0)
- P_max_dynamic: 52 MPa
- v_max: 2.0 m/s

### Design Requirements
- Required FoS: 2.0

### Assumptions
- Load is uniformly distributed across bearing length
- Continuous rotation
- Ambient operating conditions
- No shock or impact loads

## Missing Inputs

None. All required inputs provided.

## Calculations

### Bearing Pressure

P = F / (d x L)
P = 1000 / (10 x 12)
P = 1000 / 120
P = 8.33 MPa

### Surface Velocity

v = (pi x d x n) / 60000
v = (3.1416 x 10 x 30) / 60000
v = 942.48 / 60000
v = 0.0157 m/s

### PV Value

PV = P x v
PV = 8.33 x 0.0157
PV = 0.131 MPa*m/s

### Safety Factors

Material FoS = PV_max / PV_operating
Material FoS = 1.32 / 0.131
Material FoS = 10.08

Design margin = PV_allowable / PV_operating
Design margin = 0.66 / 0.131
Design margin = 5.04

### Verification Checks

Pressure check:
P = 8.33 MPa <= P_max_dynamic = 52 MPa
Pressure ratio = 8.33 / 52 = 0.16 (16%)

Velocity check:
v = 0.0157 m/s <= v_max = 2.0 m/s
Velocity ratio = 0.0157 / 2.0 = 0.008 (0.8%)

## Results

- PV_operating: 0.131 MPa*m/s
- Material FoS: 10.08
- Design margin: 5.04
- Bearing pressure: 8.33 MPa (16% of limit)
- Surface velocity: 0.0157 m/s (0.8% of limit)
- PV utilization: 19.8% of allowable

## Governing Criterion

PV limit governs the design.

All criteria satisfied with substantial margin:
- Design margin = 5.04 >= 1.0

## Safety Assessment

PASS

The bearing meets all requirements with significant safety margin.

Design margin of 5.04 indicates the bearing is operating at 19.8% of its allowable PV capacity. Both pressure and velocity are well below their individual limits.

## Recommendations

1. Bearing is suitable for specified application
2. Large safety margin allows for:
   - Potential load increase up to 5x current value
   - Higher rotational speeds if needed
   - Tolerance for misalignment or non-uniform loading
3. Consider smaller bearing dimensions for cost optimization if application permits
4. Monitor bearing wear during initial operation to validate assumptions

## Sources

- Material data: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md
- Analysis rules: 00_SYSTEM/ENGINEERING_RULES.md
