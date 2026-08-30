# Workflow - Broker, Carrier and Human Submission Handoff

Prepare a support draft that states:

- shipment/pack version and deadline;
- exact parties/roles/representation;
- goods lines and reconciled totals;
- approved classification/origin/value/procedure/control decisions;
- route, mode, Incoterm and named place;
- required documents with IDs/hashes/status;
- explicit questions, missing facts and stop conditions;
- named MORFRAC human owner and external recipient/system.

Require the submission-readiness gate only after all accountable reviews. The agent may mark `HUMAN_SUBMISSION_READY` but cannot email, upload, enter portal data, book transport, sign or declare.

After a human acts, require immutable receipt evidence: sender/submitter, timestamp, recipient/system, exact version, acknowledgement, declaration/MRN/reference and status. Do not infer acceptance from “sent.”
