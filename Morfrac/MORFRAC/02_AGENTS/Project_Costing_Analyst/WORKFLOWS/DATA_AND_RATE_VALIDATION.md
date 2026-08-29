# Workflow - Data and Rate Validation

## Procedure

1. Create a source register for every quantity, hour, rate, quote, allowance, and policy.
2. Record source owner, date/revision, currency, tax basis, validity, unit, scope, inclusions, exclusions, and confidence.
3. For labour, distinguish salary/payroll value, fully burdened cost rate, internal transfer rate, and customer bill rate. Use only the rate required by the approved method.
4. For supplier quotes, confirm quantity, specification/scope, price basis, minimum order, tooling/NRE, validity, delivery, freight, duty, tax, payment, warranty, and currency.
5. For Odoo/actuals exports, record company, report/model, filters, period, currency, timestamp, and row reconciliation.
6. For historical projects, document differences in scope, schedule, quantity, inflation/escalation, exchange rate, geography, and supplier conditions.
7. For public prices, label `budgetary benchmark - not a quote` and include access date and exclusions.
8. Reject or isolate stale, ambiguous, duplicated, incompatible, or unsupported inputs.

## Output

| Cost input | Value/unit | Classification | Source/date | Validity | Confidence | Required action |
|---|---:|---|---|---|---|---|

Never mix cost and sell rates or tax-inclusive and tax-exclusive values silently.
