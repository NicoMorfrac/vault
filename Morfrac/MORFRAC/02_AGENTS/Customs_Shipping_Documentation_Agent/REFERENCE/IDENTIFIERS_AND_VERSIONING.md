# Identifiers and Versioning

## Shipment identity

Use an approved unique `Shipment-ID`; do not derive one silently from invoice, tracking or MRN. Link but do not substitute:

- Paperclip issue;
- project/order/PO/invoice/credit-note/return IDs;
- package/consignment/tracking IDs;
- customs declaration/MRN/security/Intrastat references;
- transport document and payment/accounting references.

## Status labels

- `DRAFT - NOT SUBMITTED`: working document.
- `SUPPORT DRAFT - NOT APPROVED/DECLARED`: classification/origin/value/control support.
- `SAVED_NOT_SUBMITTED`: approved persistence only.
- `HUMAN_SUBMISSION_READY`: pack reviewed for human action, not sent/accepted.
- `SUBMITTED_BY_HUMAN - RECEIPT REQUIRED`: only with actual action evidence.
- `ACCEPTED/RELEASED/EXITED/DELIVERED`: only with source-specific evidence and timestamp.
- `CLOSED_RECONCILED`: exact close gate and retained evidence; not a legal validation.

Corrections create a new version and record reason, owner, affected documents/declarations, approval and superseded version. Never rewrite history.
