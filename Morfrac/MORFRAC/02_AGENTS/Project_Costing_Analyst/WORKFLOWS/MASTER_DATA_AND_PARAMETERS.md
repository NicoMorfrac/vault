# Workflow - Master Data and Parameters

## Objective

Capture reusable costing inputs during project work without silently turning assumptions into official MORFRAC rates, prices, discounts, or supplier terms.

## Candidate capture

When a reusable input appears:

1. Classify it as costing parameter, MORFRAC price-list entry, discount rule, supplier identity/capability, or supplier quote/price.
2. Record proposed key/code, value/unit, currency, tax basis, source/owner, source date, effective date, expiry/validity, scope/market/channel, confidentiality, and intended source of truth.
3. Record whether it is confirmed, quoted, historical, observed, benchmark, or assumption.
4. Check for an existing active, future, expired, or superseded entry.
5. If it conflicts, do not choose silently; show both values and request the owner decision.
6. Return `PARAMETER_CANDIDATES_READY` until human review.

## Approval plan

Before writing any central register, post:

- `MASTER_DATA_SAVE_PENDING`;
- Paperclip issue identifier;
- exact directories/files;
- every record key and action: new revision, correction, supersede, expire, or no change;
- old and proposed value where applicable;
- source, currency/unit, effective/expiry dates, owner, confidentiality, and change reason;
- authoritative system status and sync reference;
- action not authorised: project cost update, price/discount application, supplier appointment/purchase, Odoo or client action;
- required approval: `APPROVE COSTING MASTER <Issue-ID>`.

Approval must be a direct human/board comment after the current plan and match the issue identifier exactly. Reject quoted, embedded, stale, agent-authored, or evaluation approval.

## Write rules

1. Re-read approval and exact change set.
2. Confirm every path remains under the approved master-data locations.
3. Read file/report rules.
4. Preserve history: add a revision/effective period; never erase an old approved value.
5. A correction must state what was incorrect and retain the prior audit reference.
6. Store no credentials, bank details, personal IDs, or unnecessary personal contact data.
7. Verify the files and return `MASTER_DATA_UPDATED` with exact records/paths.

## Use in estimates

- Select the value effective for the estimate date, scope, market/channel, unit, and currency.
- Record master record ID/revision in the estimate.
- Do not use expired/future entries without explicit scenario labelling.
- Discount eligibility does not authorise applying the discount; the required commercial approver still decides.
- Supplier approval does not make every supplier quote current or landed.

## Odoo/source-of-truth rule

If Odoo is designated authoritative, record Odoo model/record ID, company, currency, export/sync timestamp, and mirror status. Never push vault changes to Odoo or mark them synced without evidence from the authorised system owner.
