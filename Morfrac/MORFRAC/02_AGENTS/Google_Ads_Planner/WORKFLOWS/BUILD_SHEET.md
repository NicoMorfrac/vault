# Workflow - Campaign Build Sheet

## Objective

Translate an approved strategy into an exact, reviewable implementation specification for a separate operator.

## Required sections

- account/customer identifier: human-supplied, never guessed;
- campaign and ad-group naming convention;
- status on creation: `PAUSED` recommendation only;
- objective, campaign type, networks, geography, location option, language, schedule, dates;
- budget amount/currency/period and approval reference;
- bidding recommendation, data prerequisite, and fallback;
- campaign/ad-group structure;
- keyword, match type, negative, and final-URL rows;
- responsive search-ad assets and other justified assets;
- conversion actions and primary/secondary setting recommendation;
- tracking/UTM conventions;
- audiences and exclusions;
- policy, legal, claim, and landing-page approvals;
- preflight tests, owner, rollback/stop plan, and post-build review.

## Boundary

`BUILD_SHEET_READY` means specification complete. It does not mean the campaign exists. This agent never imports an editor sheet, calls the Google Ads API, or changes an account.
