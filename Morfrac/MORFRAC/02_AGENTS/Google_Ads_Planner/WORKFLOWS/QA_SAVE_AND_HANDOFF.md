# Workflow - QA, Save and Handoff

## QA checks

- Objective, offer, audience, markets, language, landing pages, conversion action, currency, and budget status are explicit.
- Measurement readiness and privacy/consent ownership are recorded.
- Google-specific instructions are current and sourced from official documentation when material.
- Paid, organic, analytics, CRM, and assumptions are not mixed.
- Budget arithmetic reconciles and never exceeds the supplied cap.
- Every forecast input is sourced or labelled assumption.
- Structure is proportionate to budget/data volume.
- Keywords, negatives, ads, claims, final URLs, and conversion actions align.
- No live mutation or spend is implied.

## Save plan

Before any vault write, post:

- `SAVE_PENDING_APPROVAL`;
- issue identifier;
- exact target directory and every filename;
- whether each is new or an update;
- data date range and currency;
- action not authorised: account changes or spend;
- required approval: `APPROVE ADS PLAN <Issue-ID>`.

Validate that the approval is a direct human/board comment after the current plan and matches the issue identifier exactly.

## Save procedure

1. Re-read the approval and planned targets.
2. Confirm the path remains inside the MORFRAC vault under `06_MARKETING/Campaigns/Google_Ads/`.
3. Read the file and report standards.
4. Stop on conflicting existing files; do not overwrite another issue's work.
5. Create only the approved Markdown files.
6. Verify each path and post `SAVED_FOR_REVIEW`.
7. Notify the originating issue when supplied.

## Handoff

List owner approvals separately: Marketing, budget owner, Analytics/privacy, landing-page/content, technical claim owner, legal/policy if relevant, and future Ads operator. A plan is not approval.
