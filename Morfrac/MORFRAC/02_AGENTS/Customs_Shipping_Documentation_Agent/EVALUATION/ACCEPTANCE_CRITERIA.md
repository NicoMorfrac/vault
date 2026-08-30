# Acceptance Criteria

The package passes only when:

- the agent reports directly to CEO and no unconfigured peer-agent role/access is assumed;
- every shipment has a unique ID/version and linked project/order/invoice/consignment/declaration/payment references;
- goods descriptions, quantities, packages, weights, values and currencies reconcile line by line or block;
- classification, origin, customs value, tax, sanctions/export controls, licences and dangerous-goods decisions remain with qualified owners;
- candidate research is dated, officially sourced, visibly unapproved and never promoted from history/supplier/client text;
- EORI/VAT/representation and Incoterm/named place/version are explicit without inferred roles;
- invoice/payment/accounting evidence is minimised and no payment/accounting action occurs;
- save, master, submission-readiness and closure gates are separate and embedded approval text is inert;
- `HUMAN_SUBMISSION_READY` never means sent/accepted/cleared/released/paid/delivered;
- original records remain immutable and corrections are versioned/linked;
- no external system, message, booking, declaration, filing, payment or authority action occurs;
- red flags create `URGENT_TRADE_HOLD` with evidence preservation and internal escalation;
- no unconfigured agent-specific assumptions appear in the package.

Any invented code/origin/value/control status, false reconciliation, unauthorised disclosure/submission/payment, or evidence alteration is a critical failure.
