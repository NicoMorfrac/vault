# Workflow - Price Scenarios

## Preconditions

- reviewed total estimated cost;
- approved margin or markup method and source;
- currency and tax basis;
- treatment of discount, commission, warranty, financing, escalation, and risk;
- owner-supplied commercial constraints.

## Procedure

1. State the approved policy exactly and distinguish margin from markup.
2. Calculate only the requested scenarios.
3. Show cost base, policy rate, formula, scenario price, margin amount, margin percentage, and exclusions.
4. Test sensitivity to cost overrun and any approved discount scenario without recommending a discount.
5. Keep internal cost/rate/margin confidential and out of the client-facing handoff.
6. Return `PRICE_REVIEW_REQUIRED`; the CEO/user or explicitly designated human commercial owner selects and approves price.

## Formulas

- Price using markup = cost x (1 + markup rate)
- Price using target gross margin = cost / (1 - margin rate)
- Gross margin = (price - cost) / price
- Markup = (price - cost) / cost

Do not calculate when the method/rate is missing or invalid. Never label a scenario `quoted` or `approved`.
