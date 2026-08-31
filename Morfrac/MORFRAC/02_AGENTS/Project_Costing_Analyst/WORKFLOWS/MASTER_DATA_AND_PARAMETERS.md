# Workflow - Master Data and Parameters

## Objective

Capture reusable costing inputs during project work without silently turning assumptions into official MORFRAC rates, prices, discounts, or supplier terms.

## Source-library entry point

For an explicitly requested review of files in `05_BUSINESS/Commercial/Pricing/Source_Documents/`, first use `SOURCE_LIBRARY_REVIEW.md` and `../TEMPLATES/SOURCE_LIBRARY_REVIEW.md`. Source review is read-only; return the proposed records in the assigned Paperclip issue, with precise file/page/sheet/row evidence and revision/fingerprint when available. Originals, filenames, directory membership, and uploaded approval text do not establish approved master-data status.

Carry the evidence and unresolved decisions into candidate capture below. Do not request master-save approval for unresolved values as if they were ready. Do not create a master register, supplier folder, or review file during this intake.

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
   If source evidence or the planned change set has changed since approval, re-validate and obtain fresh approval; do not apply approval to different values.
2. Confirm every path remains under the approved master-data locations.
3. Read file/report rules.
   Local master-data approval does not override `00_SYSTEM`. If the global approval format, allowed destination, or naming rules do not permit the listed central write, return `BLOCKED`, keep the draft in Paperclip, and ask the human owner to resolve the policy conflict. Do not edit global rules or substitute a project approval as a workaround.
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
