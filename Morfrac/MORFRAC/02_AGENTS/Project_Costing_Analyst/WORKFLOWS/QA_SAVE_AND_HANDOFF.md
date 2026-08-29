# Workflow - QA, Save and Handoff

## QA checks

- Project, issue, estimate class/version/date/currency/purpose are explicit.
- Scope, exclusions, responsibilities, schedule basis, WBS, quantities, units, rates, and sources reconcile.
- Cost and price are separate.
- Margin and markup are not confused.
- Labour burden, overhead, contingency, escalation, tax, duty, freight, travel, warranty, NRE/tooling, and external work are each included once, excluded explicitly, or marked unknown.
- Quotes include validity, currency, tax/freight/delivery basis, and scope.
- Missing/unpriced items are visible and not treated as zero.
- Totals and scenario arithmetic reconcile.
- Estimate precision matches maturity and uncertainty.
- Confidential internal cost/margin is not included in client-facing handoff.
- No project/Odoo/procurement/client mutation is implied.

## Save plan

Before any vault write, post:

- `SAVE_PENDING_APPROVAL`;
- project name and Paperclip identifier;
- exact existing `04_Cost` directory and filename;
- new/update status;
- estimate class/version/date/currency;
- supported total and unpriced items;
- price approval status;
- action not authorised: Odoo, purchase, quotation, proposal, client communication;
- required approval: `APPROVE <Project_Name>`.

Validate direct human/board approval after the current plan and exact project-name match.

## Save procedure

1. Re-read approval and target.
2. Confirm the project and `04_Cost` folder already exist.
3. Read file/report standards.
4. Confirm filename follows `<IssueID>_Cost_<ShortDescription>.md` and remains inside the approved folder.
5. Stop on conflicting different-issue files.
6. Create/update only the approved Markdown report.
7. Verify its exact path and post `SAVED_FOR_REVIEW`.
8. Notify the originating issue when supplied.

## Handoff to Proposal agent

Provide only the human-approved sell-price scenario, commercial inclusions/exclusions, validity, payment/cash milestones, schedule basis, assumptions, risks appropriate for the client, and approval references. Do not expose internal rates, base cost, contingency method, or margin unless specifically authorised.
