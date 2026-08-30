# Odoo Model and Field Boundary

No live Odoo scope is approved. This is a design reference for a future separate connector decision, not permission to connect.

A connector proposal must list exact instance/database, allowed companies, technical user, authentication custody, models/reports, readable fields, blocked fields, domains, maximum rows, frequency, logging, retention and incident owner. Sensitive fields require explicit purpose and review.

Potential read-only subject areas may include posted accounting summaries, invoices, accepted sales/purchase orders, CRM opportunities, projects/tasks, timesheets, products, inventory summaries and approved employee aggregates. Actual model names and semantics must be confirmed against MORFRAC's instance/version and modules.

Block create/write/unlink, posting, reconciliation, validation, confirmation, messaging, imports, scheduled actions and any method that can mutate state. A nominal HTTP GET or read call is not sufficient proof of non-mutation; system-owner testing and logs are required.

