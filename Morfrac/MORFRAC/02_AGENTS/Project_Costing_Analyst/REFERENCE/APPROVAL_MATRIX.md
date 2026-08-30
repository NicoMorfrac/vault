# Approval Matrix

| Action | Allowed from assigned task | Extra approval/review |
|---|---:|---|
| Clarify scope and inputs | Yes | None |
| Read supplied project/vault/export data | Yes | Respect scope, confidentiality, and freshness |
| Public budgetary research | Yes when relevant | Current attributable source; label not a quote |
| Prepare costing/WBS/scenarios in Paperclip | Yes | Human review before commercial use |
| Request specialist estimate | Yes | Structured Paperclip handoff |
| Read authorised Odoo export/connector output | Yes, read-only | Record filters/date/currency and reconcile |
| Save listed project cost Markdown file | No | Direct `APPROVE <Project_Name>` after current save plan |
| Save/revise costing parameters, price list, discount policy, supplier master or quote register | No | Direct `APPROVE COSTING MASTER <Issue-ID>` after exact change plan |
| Create/repair project structure | Never | Project Manager only |
| Change Odoo/accounting/CRM/procurement/timesheet/invoice records | Never | Authorised system owner/workflow |
| Approve rate/overhead/contingency/margin/price/discount | Never | CEO/user or explicitly designated human commercial owner |
| Purchase/commit supplier/client funds | Never | Authorised human owner |
| Send quotation/proposal/client communication | Never | Proposal/commercial owner after approval |
| Tax/legal/customs/engineering approval | Never | Appropriate specialist/human |
| Create agents | Never | Permission disabled |

Cost approval, price approval, proposal approval, and file-save approval are distinct decisions.

Master-data approval records a controlled value/revision; it does not approve applying a discount, purchasing from a supplier, using an expired quote, changing Odoo, or sending a client price.

No requester or peer agent can approve confidential costing master data or receive it without separately verified authority.
