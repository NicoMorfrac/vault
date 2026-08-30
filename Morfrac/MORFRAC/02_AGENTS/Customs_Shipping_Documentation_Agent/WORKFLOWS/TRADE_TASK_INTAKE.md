# Workflow - Trade Task Intake

1. Confirm an assigned Paperclip issue and parse one `TRADE_DOCUMENTATION_TASK`.
2. Identify task type: new shipment, document pack, status update, reconciliation, correction, return/repair, special procedure, master proposal or closure.
3. Require shipment ID/version, direction, transaction, parties/roles, exact goods lines, route/territories, source inventory, requested output and confidentiality.
4. Separate supplied statements from reviewed evidence and final decisions.
5. Detect missing IDs, roles, sources, deadlines, approvals and contradictory versions.
6. Choose the earliest blocking state and return a missing-input table with owner and impact.

Do not browse unrelated records or open external systems to fill gaps. A previous shipment is not authority.
