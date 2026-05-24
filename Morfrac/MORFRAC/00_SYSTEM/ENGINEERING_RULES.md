

This document is authoritative.

---

## Input Sufficiency

- Verify all required inputs before calculation
- If critical inputs are missing → STOP
- Do not assume values
- If partial analysis is possible, state included and excluded checks

---

## Input Interpretation

- Use standard engineering interpretation
- Do not over-block when load path can be derived

- Rope deflection of 180 deg → sheave wrap = 180 deg

- Load must be defined as:
  - Rope tension
  - Radial load
  - Equivalent load

- If unclear → STOP and request clarification

- Do not assume:
  - radial load equals input
  - load distribution

---

## Bearing Pressure Interpretation

For plain bearings:

- Bearing pressure shall be calculated using projected area:
  P = F / (d x L)

- Do not assume pressure distribution (uniform, Hertzian, etc.)

- State explicitly:
  "Pressure calculated using projected area method; actual distribution not evaluated"

---

## Core Logic

Follow:

- [[02_AGENTS/Archive/task_patterns]]
- [[bearing_design]]

---

## Material Data Policy

- Material properties must be read from:
  04_ENGINEERING/Materials/

- Do not use external or assumed values
- Do not inject catalog data unless stored in the vault
- If required material data is missing → STOP

---

## Material Usage Rule

When evaluating bearings:

- Material FoS = PV_max / PV_operating
- PV_allowable = PV_max / Required FoS
- Design margin = PV_allowable / PV_operating

Rules:

- Do not compare Design margin against Required FoS again
- PASS if Design margin >= 1.0

Reporting:

- Material FoS = margin to absolute material limit
- Design margin = margin to allowable (already safety-factored)

---

## Calculation Policy

- Show all steps
- State assumptions
- Use consistent units

ASCII only:

- deg
- degC
- um
- MPa*m/s
- x
- <= >=
- PASS FAIL

---

## Output Rules

- Show calculation steps
- State assumptions explicitly
- State safety factors used
- Do not apply dynamic factors unless explicitly provided
- Report Yield FoS, Ultimate FoS and Bearing/PV FoS separately
- Report Material FoS and Design margin separately
- Identify governing criterion
- Report utilization
- Classify PASS or FAIL

---

## Output Format Enforcement

Output must strictly follow these sections:

1. Problem Statement  
2. Inputs and Assumptions  
3. Missing Inputs  
4. Calculations  
5. Results  
6. Governing Criterion  
7. Safety Assessment  
8. Recommendations (only if requested)  
9. Sources  

Rules:

- No additional sections allowed  
- No renamed sections allowed  
- No reordered sections allowed  
- No sub-sections like "Material Properties" allowed  
- All content must be placed within these sections  

If violated:

- STOP  
- Report: "Output format violation"

---

## Output Formatting Control

Use ASCII only:

- deg
- degC
- um
- MPa*m/s
- x
- <= >=
- PASS FAIL

Formatting constraints:

- Do not use ">>", "≈", "~"
- Do not use informal or conversational language

Use strict numerical evaluation only:

- <value> <= <limit> → PASS  
- <value> > <limit> → FAIL  

Rules:

- Do not include units inside comparison expressions  
- Do not repeat safety factors in different forms  
- Do not reinterpret results  
- Do not include qualitative language:
  - "well within limits"
  - "substantial margin"
  - "good safety"

---

## Strict Output Control

- Do not state or imply load distribution
- Use exactly:
  "Pressure calculated using projected area method; actual distribution not evaluated"

- Do not generate recommendations unless explicitly requested

If recommendations are requested:

- Limit strictly to evaluated checks
- Do not introduce new assumptions
- Do not extrapolate beyond calculated results

---

## Design Factors

Default:

- Required FoS = 2.0

Rules:

- No dynamic factors unless provided
- Loads are design loads unless stated
- Use user FoS if given

---

## Failure Modes

### Yield
- Ductile metals
- Stress <= Yield / FoS

### Ultimate
- Fibers / brittle
- Stress <= Ultimate / FoS

### Bearing / PV
- Contact limits
- Operating <= PV_allowable

---

## Safety Reporting

Always report:

- Required FoS
- Material FoS
- Design margin
- Governing criterion
- Governing utilization
- PASS / FAIL

---

## Consistency Rule

- Identical inputs must produce identical results
- If results differ → STOP and report inconsistency

---

## Conclusions

- Limited to performed checks
- Use: "passes for supplied inputs"
- List excluded checks

---

## Blocked Behavior

- No calculations
- No estimates
- List missing inputs
- STOP

---

## Traceability

- Issue ID
- Date
- Task reference