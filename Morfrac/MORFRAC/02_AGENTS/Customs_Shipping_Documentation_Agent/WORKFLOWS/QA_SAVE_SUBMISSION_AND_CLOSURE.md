# Workflow - QA, Save, Submission and Closure

## QA

Verify exact shipment/version, parties/roles, goods-line identity, quantities, packages, net/gross weight, values/currency, Incoterm/named place/version, classification/origin/value/control approvals, document IDs, deadlines and confidentiality.

Cross-foot line and pack totals. Reconcile order, invoice, packing, transport, declaration, payment and accounting references. List every missing/conflicting field; do not hide with `TBC`.

## Save

Present exact path/file/source/hash plan and require `APPROVE TRADE DOSSIER SAVE <Shipment-ID> <Version>`. Save only listed versioned files, verify them and set `SAVED_NOT_SUBMITTED`. Never overwrite originals.

## Submission readiness

Require all accountable decisions, exact pack/version/hash/system/recipient/deadline and `APPROVE TRADE SUBMISSION <Shipment-ID> <Version>`. Mark only `HUMAN_SUBMISSION_READY` and hand off. Do not submit or communicate.

## Closure

Require actual submission/acceptance evidence, final customs/transport/financial reconciliation, unresolved deviations, retention metadata and `APPROVE TRADE CLOSE <Shipment-ID> <Version>`. Mark `CLOSED_RECONCILED`; preserve the dossier and review triggers.
