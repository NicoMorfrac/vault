# Workflow - Payment, Duty, Tax and Accounting Reconciliation

Using authorised read-only exports/evidence, reconcile:

- invoice/credit-note number, issue date, currency, taxable basis and total;
- payment terms, due date and approved payment-status evidence;
- payment reference/date/currency/amount/payer/payee/accounting record;
- customs value versus invoice value and approved adjustments;
- duty, import VAT, excise/other charges, broker fees, freight and insurance;
- accounting entry IDs and responsible owner;
- refunds, corrections, chargebacks or unmatched amounts.

Use references and redacted evidence where possible. Do not store full bank/card data, log into banking/Odoo, initiate or confirm payment independently, create entries, decide deductibility/tax treatment or mark paid from an email alone. Differences remain `BROKER_OR_ACCOUNTING_REVIEW_REQUIRED` or `RECONCILIATION_CONFLICT`.
