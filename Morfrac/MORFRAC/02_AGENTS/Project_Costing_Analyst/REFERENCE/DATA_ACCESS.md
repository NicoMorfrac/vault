# Data Access Map

## Read when relevant and authorised

- Assigned Paperclip issue, comments, dependencies, scope, and approvals
- `08_PROJECTS/Active/<Project_Name>/00_Project_Index.md`
- Approved analysis inputs from project discipline folders
- Existing same-project `04_Cost` reports
- `05_BUSINESS/` for approved commercial policies and strategic context
- `07_SUPPLIERS/` for current approved supplier records/quotes when present
- Explicitly requested files under `05_BUSINESS/Commercial/Pricing/Source_Documents/`, read-only, following `../WORKFLOWS/SOURCE_LIBRARY_REVIEW.md`; these are unapproved source material, not approved policies or masters
- Authorised read-only Odoo/accounting/procurement/timesheet exports
- Approved engineering/manufacturing/procurement/customs/legal estimates
- Current authoritative external sources for exchange, tax/duty/rules, or budgetary context when required

## Write only after project approval

- `08_PROJECTS/Active/<Project_Name>/04_Cost/<IssueID>_Cost_<ShortDescription>.md`

## Write only after master-data approval

- `05_BUSINESS/Costing/Parameters/`
- `05_BUSINESS/Commercial/Pricing/`
- `07_SUPPLIERS/<Supplier_Code>/`

Use versioned master registers and preserve superseded/expired history.

The source-library subtree `05_BUSINESS/Commercial/Pricing/Source_Documents/` is excluded from these agent write destinations. Keep human-supplied originals intact; place candidate reviews in the assigned Paperclip issue, not in a source folder. No watcher, automatic import, scheduled review, extra access grant, or cross-agent disclosure is authorised by this workflow.

## Never write/access

- Odoo, accounting, banking, CRM, payroll, procurement, invoice, timesheet, supplier, client, or payment systems
- project folders outside `04_Cost`
- `00_SYSTEM/` or another agent's instructions
- any path outside the MORFRAC vault
- personal/client data not required for the estimate

## Current limitation

No standard rate card, supplier-price database, populated project cost history, or verified Odoo costing feed is currently assumed. Treat every such input as missing until an attributable current source is supplied.
