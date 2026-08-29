# Workflow - Risk and Contingency

## Objective

Represent uncertainty transparently without hiding scope gaps or padding the estimate.

## Procedure

1. Build a risk register linked to WBS items.
2. Separate known scope/cost, allowance, risk event, estimate uncertainty, escalation, and management reserve.
3. Record cause, affected cost, likelihood/range, impact/range, mitigation, owner, trigger, and whether already included.
4. Use the CEO/user's approved method: item ranges, expected value, class-based percentage, scenario allowance, or another documented method.
5. Show the contingency calculation and base explicitly.
6. Exclude double-counted risk already present in quoted values, hours, or allowances.
7. Do not use contingency to cover missing mandatory scope; return `SCOPE_BLOCKED` or list unpriced work.

## Output

| Risk/uncertainty | Cost base | Method/input | Allowance | Owner/mitigation | Included? |
|---|---:|---|---:|---|---|

If no approved method exists, show risk exposure qualitatively and request the method. Do not invent a contingency percentage.
