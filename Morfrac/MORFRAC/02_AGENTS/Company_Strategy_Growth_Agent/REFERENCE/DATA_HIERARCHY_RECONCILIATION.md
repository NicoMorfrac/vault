# Data Hierarchy and Reconciliation

Use closed accounting plus verified control balances for actual financial totals. Use authorised system exports for detail only after company/filter/status/period/currency/tax checks. Use approved operational records for delivery and capacity facts. Contracts and accepted orders support backlog only when status and value are verified.

Every reconciliation records both source IDs, timestamps, row counts, totals, materiality and a bridge. Never silently resolve discrepancies by choosing the convenient source, inserting a plug, changing filters or deleting outliers.

Data-quality checks include duplicates, orphan IDs, cancelled/credit records, status drift, date leakage, foreign currency, tax inclusion, units, sign, intercompany, related parties and consolidation. Block only the conclusions affected by a material conflict, while clearly marking what remains usable.

