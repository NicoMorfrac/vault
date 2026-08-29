# Workflow - Measurement Readiness

## Objective

Determine whether Google Ads spend could be evaluated against a meaningful business outcome.

## Checklist

1. Define one primary conversion and its business meaning.
2. List secondary conversions separately.
3. Identify where each event is generated: website, call, form, ecommerce, CRM, or offline sale.
4. Record current GA4, Google Ads, Tag Manager, CRM/Odoo, consent, and call-tracking status from verified sources.
5. Confirm or flag event firing, value/currency, deduplication, attribution, cross-domain issues, auto-tagging/UTM conventions, and lead-source persistence.
6. Confirm consent/privacy review owner and any regional constraint.
7. Review landing-page message match, form/call function, mobile experience, response ownership, qualification, and sales capacity.
8. Define a test protocol with evidence required before launch readiness.

## Output

| Requirement | Status | Evidence | Owner | Action/test |
|---|---|---|---|---|

Use:

- `READY`: verified enough for planning/implementation handoff;
- `PARTIAL`: usable with explicit limitations;
- `BLOCKED`: cannot judge paid performance reliably.

Return `MEASUREMENT_BLOCKED` when the primary conversion cannot be tested or linked to business value. Traffic, button clicks, and sessions are not automatically business conversions.
