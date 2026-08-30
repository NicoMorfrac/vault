# Odoo Read-Only Scope and Export

Start with `ODOO_ACCESS_NOT_CONFIGURED`. Do not attempt login, API discovery or credential use.

When Odoo data is needed, prepare a manifest specifying decision purpose, authorised owner, instance/company, model/report, fields, domain/filters, period, status rules, currency/tax basis, relational fields, personal-data minimisation, extraction timestamp, expected format and control totals. The human or authorised system owner performs the export.

A connector proposal remains `ODOO_SCOPE_APPROVAL_REQUIRED` until separately approved. Read-only still requires least privilege, logs, field allowlists and a documented prohibition on method calls that mutate state.

