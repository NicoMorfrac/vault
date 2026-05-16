# Task Patterns

Defines how engineering tasks are executed.

---

## Input Check

- Verify inputs
- If missing → STOP
- List all missing inputs
- No assumptions

---

## Load Interpretation

- Load must be:
  - Rope tension
  - Radial load
  - Equivalent load

- If unclear → STOP

- Do not assume:
  - radial = input
  - load distribution

---

## Load Case Analysis

### Steps

- Define geometry
- Define load type
- Define load path
- Convert loads if required
- Calculate forces
- Identify critical components

### Rules

- No dynamic factors unless given
- Loads = design loads
- State assumptions

---

## Bearing Analysis

Use:
- [[bearing_design]]

### Required Steps

- Confirm radial load
- Confirm geometry (d, L)
- Calculate pressure
- Calculate velocity
- Calculate PV
- Retrieve material data from:
  04_ENGINEERING/Materials/
- Compare against material limits
- Calculate FoS (material and design)
- Identify governing criterion

---

## Material Comparison

Compare:
- Strength
- Stiffness
- Fatigue
- Corrosion
- Wear
- Cost

---

## Design Review

- Define function
- Identify load paths
- Identify failure modes
- Evaluate each
- Identify governing

---

## Output Structure

1. Problem  
2. Inputs  
3. Missing Inputs  
4. Calculations  
5. Results  
6. Governing Criterion  
7. Safety  
8. Recommendations  
9. Sources  

---

## Consistency Rule

- Same inputs must produce same outputs
- If results differ → STOP and report inconsistency

---

## Rules

Comply with:
- [[ENGINEERING_RULES]]