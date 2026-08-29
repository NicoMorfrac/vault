# Workflow - Costing Task Intake

## Procedure

1. Read the assigned issue, comments, scope brief, project index, approvals, source files, and dependencies.
2. Confirm assignment to this agent.
3. Classify the request and decision: concept/budget estimate, detailed baseline, price scenario, change, actual variance, or estimate at completion.
4. Confirm project name/existence, estimate date, currency, version, schedule basis, and required confidence/maturity.
5. Extract deliverables, scope, exclusions, client/MORFRAC responsibilities, quantities, work packages, rate sources, supplier sources, overhead, contingency, margin, tax/duty/freight, and origin.
6. Mark each input confirmed, quoted, historical, specialist estimate, public benchmark, assumption, stale, missing, or contradictory.
7. Identify engineering, manufacturing, procurement, customs, commercial, finance, legal, and schedule dependencies.
8. If the scope cannot be broken into costable work, return `SCOPE_BLOCKED`.
9. If rates/quantities are missing but a partial model is useful, show only supported subtotals and exact missing inputs.

## Required for any total

- estimate purpose and date;
- currency;
- sufficiently defined scope/WBS;
- quantity/hours and attributable rates or quoted lump sums;
- explicit treatment of overhead, contingency, tax, duty, freight, and exclusions.

Without an approved margin/markup policy, stop at cost and return `PRICE_REVIEW_REQUIRED` for price.
