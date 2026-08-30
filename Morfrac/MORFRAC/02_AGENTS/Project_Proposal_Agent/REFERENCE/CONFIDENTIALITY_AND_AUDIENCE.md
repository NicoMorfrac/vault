# Confidentiality and Audience Control

Classify every output:

- `CEO_CONFIDENTIAL_INTERNAL`: pricing strategy, approvals, deviations and internal review.
- `INTERNAL_PROJECT`: scoped operational content without restricted commercial details.
- `CLIENT_DRAFT_NOT_RELEASED`: proposed client-facing content awaiting approvals.
- `HUMAN_RELEASE_READY`: reviewed client package awaiting human transmission.

Before every handoff identify recipient, purpose, minimum fields, classification, and approval reference.

Another agent may receive only the minimum sanitised `INTERNAL_PROJECT` content explicitly needed for a verified authorised task. Do not infer its role from its name. It must not receive CEO-confidential internal cost, margin, discount, supplier, legal-strategy, or unrelated client information without explicit authority.
