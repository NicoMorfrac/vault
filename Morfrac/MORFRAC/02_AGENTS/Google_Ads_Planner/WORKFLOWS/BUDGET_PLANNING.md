# Workflow - Budget Planning

## Required inputs

- currency;
- maximum media spend and time period;
- confirmed or assumed CPC range;
- confirmed or assumed conversion-rate range;
- primary conversion definition;
- lead-to-sale rate and gross-profit/value inputs when ROI modelling is requested;
- sales/fulfilment capacity and test duration.

## Procedure

1. Keep confirmed values and assumptions in separate tables.
2. State whether each input is historical Ads data, platform forecast, commercial input, external benchmark, or planning assumption.
3. Calculate conservative, base, and upper scenarios without exceeding the human cap.
4. Show formulas, units, rounding, and excluded costs.
5. Run sensitivity across CPC and conversion rate; add lead quality/close rate for lead-generation ROI.
6. Define what the spend is intended to learn and the minimum evidence needed for a decision.
7. Add stop conditions and owner approval fields.

## Core formulas

- Estimated clicks = media spend / assumed average CPC
- Estimated conversions = estimated clicks x assumed conversion rate
- Estimated CPA = media spend / estimated conversions
- Estimated sales = leads x assumed qualified-lead rate x assumed close rate, when those stages are defined
- Estimated revenue = estimated sales x confirmed average revenue per sale
- Estimated ROAS = estimated attributed revenue / media spend

If a denominator is zero or unknown, do not calculate the metric. Never hide uncertainty with excessive decimal precision.

## Output label

Every scenario must say `planning scenario - not an approved budget or forecast guarantee`.
