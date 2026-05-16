# MORAAAAA-13 - Titanium Cheek Stress Analysis - BLOCKED

**Date**: 2026-04-29 14:20 UTC
**Status**: Blocked - Awaiting Design Specifications
**Issue**: [MORAAAAA-13](/MORAAAAA/issues/MORAAAAA-13)
**Parent**: [MORAAAAA-11](/MORAAAAA/issues/MORAAAAA-11) - Bearing test (sheave with Ti cheeks + iglidur X)

## Action Taken

Performed Step 0 input sufficiency check per TASK_PATTERNS and bearing_design skill.

**Result**: INSUFFICIENT INPUTS - Cannot proceed with structural calculations.

## Missing Critical Parameters

### Geometry
- Cheek thickness [mm]
- Cheek width/height [mm]
- Bearing hole diameter [mm]
- Sheave outer diameter [mm]
- Pin/shaft diameter [mm]
- Material cross-sections at critical locations

### Load Case
- Maximum rope tension [N or kN]
- Rope diameter [mm]
- Wrap angle around sheave [degrees]
- Static vs dynamic loading (duty cycle)
- Load distribution pattern

### Materials
- Titanium grade (Ti-6Al-4V Gr5 vs CP Ti Gr2)
- Material properties for specific grade selected

### Operating Conditions
- Environment (marine/freshwater/dry)
- Duty cycle
- Temperature range

## Analysis Protocol

Following engineering rules:
1. **No silent assumptions** for load/geometry/material parameters
2. **Request inputs** before proceeding with calculations
3. **Verify sufficiency** per TASK_PATTERNS Step 0

## Deliverables Ready Once Inputs Provided

1. Free body diagram showing load path
2. Stress calculations:
   - Bearing stress at pin/bore interface
   - Bending stress in cheek plates
   - Shear stress at critical sections
   - Combined stress evaluation
3. Peak stress location and magnitude
4. Safety factor vs yield (target: SF ≥ 2.0 for 50% utilization per GO criteria)
5. Weight estimate
6. Failure mode identification
7. Geometry recommendations if modifications needed

## Decision Criteria (from parent task)

- **GO**: Stress stays below 50% of yield strength (SF ≥ 2.0)
- **NO-GO**: Insufficient structural margin

## Next Steps

1. CTO provides design specifications
2. Engineering performs structural analysis
3. Report findings with GO/NO-GO recommendation

## References

- Bearing design skill: 02_AGENTS/Engineering/SKILLS/bearing_design.md.md
- Task patterns: 02_AGENTS/Engineering/TASK_PATERNS.md.md
- Parent plan: [/MORAAAAA/issues/MORAAAAA-11#document-plan](/MORAAAAA/issues/MORAAAAA-11#document-plan)
- Related: [MORAAAAA-12](/MORAAAAA/issues/MORAAAAA-12) - iglidur X PV validation
