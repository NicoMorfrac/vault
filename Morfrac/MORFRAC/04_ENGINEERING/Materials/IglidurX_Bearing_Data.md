# IglidurX Bearing Data

## Source
igus technical data (controlled internal reference)

## PV Limits

PV_max: 1.32 MPa*m/s
Recommended_SF: 2.0
PV_allowable: 0.66 MPa*m/s

## Pressure Limits

P_max_dynamic: 52 MPa
P_max_static: 100 MPa

## Velocity Limit

v_max: 2.0 m/s

## Calculation Rules

P = F / (d x L)
v = (pi x d x n) / 60000
PV = P x v

## Engineering Usage

Material FoS = PV_max / PV_operating
Design FoS = PV_allowable / PV_operating

## Constraints

- Do not modify values without updating source
- Do not estimate missing values
- If data missing → STOP