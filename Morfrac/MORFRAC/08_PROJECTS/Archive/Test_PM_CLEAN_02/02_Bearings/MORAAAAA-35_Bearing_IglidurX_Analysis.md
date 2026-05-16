# Bearing PV Analysis - IglidurX Plain Bearing

## Problem Statement

Evaluate bearing PV performance for a plain bearing operating under radial load.

Component: Plain bearing
Material: IglidurX
Analysis type: PV limit evaluation

## Inputs and Assumptions

### Given Inputs

- Radial load F = 1000 N
- Shaft diameter d = 10 mm
- Bearing length L = 12 mm
- Rotational speed n = 30 rpm
- Required FoS = 2.0

### Assumptions

- Load is uniformly distributed over bearing surface
- Continuous rotation at steady speed
- Radial load only (no axial component)
- Loads are design loads

## Material Data

Source: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md

- PV_max = 1.32 MPa*m/s
- PV_allowable = 0.66 MPa*m/s
- P_max_dynamic = 52 MPa
- v_max = 2.0 m/s

## Calculations

### Bearing Pressure

P = F / (d x L)
P = 1000 N / (10 mm x 12 mm)
P = 1000 / 120
P = 8.33 MPa

Check: P <= P_max_dynamic
8.33 MPa <= 52 MPa ✓

### Sliding Velocity

v = (pi x d x n) / 60000
v = (3.14159 x 10 mm x 30 rpm) / 60000
v = 942.478 / 60000
v = 0.0157 m/s

Check: v <= v_max
0.0157 m/s <= 2.0 m/s ✓

### PV Value

PV = P x v
PV = 8.33 MPa x 0.0157 m/s
PV = 0.131 MPa*m/s

### Safety Factors

Material FoS = PV_max / PV_operating
Material FoS = 1.32 / 0.131
Material FoS = 10.08

Design FoS = PV_allowable / PV_operating
Design FoS = 0.66 / 0.131
Design FoS = 5.04

## Results

| Parameter | Value | Limit | Status |
|-----------|-------|-------|--------|
| Bearing pressure P | 8.33 MPa | 52 MPa | PASS |
| Sliding velocity v | 0.0157 m/s | 2.0 m/s | PASS |
| PV operating | 0.131 MPa*m/s | 0.66 MPa*m/s | PASS |
| Material FoS | 10.08 | >= 2.0 | PASS |
| Design FoS | 5.04 | >= 2.0 | PASS |

## Governing Criterion

**PV limit with Design FoS**

- Governing value: PV = 0.131 MPa*m/s
- Design FoS = 5.04
- Utilization = 19.8% (PV_operating / PV_allowable)

## Safety Assessment

**Status: PASS**

All criteria satisfied:
- Bearing pressure within dynamic limit
- Sliding velocity within material limit
- Material FoS = 10.08 > 2.0 required ✓
- Design FoS = 5.04 > 2.0 required ✓

The bearing operates well within allowable limits with substantial safety margin.

## Recommendations

- Design is suitable for the specified operating conditions
- PV utilization at 19.8% provides substantial margin for load variations
- Consider periodic inspection intervals per standard bearing maintenance practice

## Traceability

- Issue ID: MORAAAAA-35
- Date: 2026-05-02
- Analysis: Bearing PV evaluation per system rules

## Sources

- IglidurX material data: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md
- Calculation methods: Per material file calculation rules
- Engineering rules: 00_SYSTEM/ENGINEERING_RULES.md
