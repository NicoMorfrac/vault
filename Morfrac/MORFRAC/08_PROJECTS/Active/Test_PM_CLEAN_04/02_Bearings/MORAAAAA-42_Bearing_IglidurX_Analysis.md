# Bearing PV Analysis - IglidurX

IssueID: MORAAAAA-42
Project: Test_PM_CLEAN_04
Component: Plain bearing
Material: IglidurX

## Problem Statement

Evaluate plain bearing under radial load for PV limit compliance.

## Inputs and Assumptions

### Given Inputs
- Radial load F = 1000 N
- Shaft diameter d = 10 mm
- Bearing length L = 12 mm
- Rotational speed n = 30 rpm
- Required FoS = 2.0

### Material Properties
Source: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md
- PV_max = 1.32 MPa*m/s
- P_max_dynamic = 52 MPa
- v_max = 2.0 m/s

### Assumptions
- Radial load treated as design load
- Pressure calculated using projected area method; actual distribution not evaluated

## Missing Inputs

None

## Calculations

### Bearing Pressure
P = F / (d x L)
P = 1000 / (10 x 12)
P = 1000 / 120
P = 8.333 MPa

### Sliding Velocity
v = (pi x d x n) / 60000
v = (3.14159 x 10 x 30) / 60000
v = 942.478 / 60000
v = 0.01571 m/s

### PV Value
PV = P x v
PV = 8.333 x 0.01571
PV = 0.1309 MPa*m/s

### Material FoS
Material FoS = PV_max / PV_operating
Material FoS = 1.32 / 0.1309
Material FoS = 10.08

### Design Margin
PV_allowable = PV_max / Required FoS
PV_allowable = 1.32 / 2.0
PV_allowable = 0.66 MPa*m/s

Design margin = PV_allowable / PV_operating
Design margin = 0.66 / 0.1309
Design margin = 5.04

## Results

| Parameter | Value | Limit | Status |
|-----------|-------|-------|--------|
| Pressure | 8.333 MPa | 52 MPa | PASS |
| Velocity | 0.01571 m/s | 2.0 m/s | PASS |
| PV | 0.1309 MPa*m/s | 0.66 MPa*m/s | PASS |
| Material FoS | 10.08 | 2.0 | PASS |
| Design margin | 5.04 | 1.0 | PASS |

## Governing Criterion

PV limit (design margin = 5.04)

## Safety Assessment

Status: PASS

Checks:
- Pressure: 8.333 <= 52 MPa (PASS)
- Velocity: 0.01571 <= 2.0 m/s (PASS)
- Design margin: 5.04 >= 1.0 (PASS)

Utilization: 19.8% of PV_allowable

## Sources

- IglidurX material data: 04_ENGINEERING/Materials/IglidurX_Bearing_Data.md
- Required FoS: 2.0 (specified)
