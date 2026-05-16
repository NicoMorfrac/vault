## Rig Loads Skill

## Information sufficiency rule
Before analysis:
- Verify required inputs are sufficient.
- If critical inputs are missing, ask for them before proceeding.
- Do not invent or assume missing load, geometry, material or boundary conditions.
- State explicitly what additional information is required.
- Proceed with assumptions only if the user explicitly requests assumption-based estimation.

## Default approach
1. Define sail force source
2. Resolve load paths
3. Include geometry effects
4. Apply dynamic factors
5. Check fittings and attachments
6. Review governing criterion

## Evaluate
Always check:
- Primary sail force generation
- Complete load path transfer
- Geometry-induced amplification
- Secondary bending or prying loads
- Dynamic loading effects
- Fatigue relevance where applicable

## Default design factors (unless overridden)
- Static marine hardware sizing basis: FoS 2.0
- Dynamic load factor default: 2.0
- Increase factors where fatigue, shock or uncertainty governs
- Apply dynamic factors before structural checks

## Required checks
- Resolve complete load path through fittings and attachments
- Check yield, ultimate and fatigue where applicable
- Check pin, fittings, fasteners and support structure
- Include geometry concentration effects
- Identify governing criterion
- If utilization >100%, classify FAIL

## Standard outputs
- Sheet load
- Halyard/luff load
- Tack/Clew/Head loads
- Resulting fitting loads

## Always report
- Assumptions
- Governing load case
- Critical load path
- Governing criterion
- Recommendation

Report safety margins explicitly including:
- Required FoS
- Achieved Yield FoS
- Achieved Ultimate FoS
- Governing Criterion
- Governing Utilization
- PASS/FAIL Status

Save analyses under:
- If part of a project:
  08_PROJECTS/Active/<Project_Name>/01_Structures/
- Otherwise:
  04_ENGINEERING/Calculations/Rig_Loads/