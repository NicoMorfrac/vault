# Coordination state model

Lead with one main state plus all active holds/capability flags:

- `INTAKE_REQUIRED`: missing task identity/scope.
- `READINESS_GAPS`: required source, resource or dependency missing.
- `SOURCE_CONFLICT`: conflicting/stale/unattributable inputs block a dependent conclusion.
- `PLAN_DRAFT`: sourced proposal, not an allocation or schedule change.
- `PLAN_APPROVAL_PENDING`: exact internal plan awaits authority.
- `HUMAN_HANDOFF_REVIEW_READY`: prerequisites documented for pack review, not safe-to-run status.
- `PROGRESS_REPORTED`: operator/source reports progress, not yet corroborated.
- `PROGRESS_RECONCILED`: defined evidence checked; no product acceptance implied.
- `HOLD`: preserve specialist or safety/record-integrity restriction.
- `COORDINATION_CLOSE_PENDING` / `COORDINATION_CLOSED`: bounded coordination only.

Flags: `PRODUCTION_SYSTEM_ACCESS_NOT_CONFIGURED`, `PROJECT_LINK_REQUIRED`, `CAPACITY_DATA_REQUIRED`, `MATERIAL_ALLOCATION_REQUIRED`, `TECHNICAL_PACK_REQUIRED`, `QUALITY_HOLD`, `AUTHORISATION_REQUIRED`, `STORAGE_POLICY_REQUIRED`, `URGENT_WORKSHOP_SAFETY_HOLD`, `URGENT_PRODUCTION_RECORD_INTEGRITY_HOLD`.

Planned -> approved proposal -> human review -> reported activity -> reconciled evidence is not an automatic operational state machine. Product inspection, acceptance, release and shipment are separately evidenced human states. A paper job card or completed review issue never advances an ERP order.
