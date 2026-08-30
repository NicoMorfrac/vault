# Data Quality and Reconciliation

For each extract, verify source, company, timezone, period, filters, statuses, units, currency, tax inclusion, sign convention, duplicate keys, missing values, row count and extraction timestamp. Hash or otherwise identify the immutable source file.

Reconcile totals to the applicable closed ledger, management control, order book, inventory count or project register. Document every bridge item and owner. Never force a plug or silently drop differences.

Material unexplained differences set `DATA_QUALITY_RECONCILIATION_REQUIRED` and block affected KPIs, scenarios and external packs.

