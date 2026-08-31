# Data Access

## Allowed

- Assigned Paperclip issue and directly linked project records.
- Existing authorised files in the MORFRAC vault.
- Approved client-safe price and commercial references.
- Supplied client documents and current attributable public context when required.
- Read-only Odoo/CRM exports or connector output only when explicitly authorised and necessary.

## Restricted

- Internal costing, margin, discount limits, price floors, supplier terms and unrelated project economics are CEO-confidential.
- Minimise personal data and client contact details.
- Do not copy confidential values into employee-facing issues or client drafts.
- Do not request passwords, tokens, API keys or credentials.

## Approved proposal-only file scope

After the exact current save approval and global `ProposalWorkflow-v1` checks, create only the listed new versioned Markdown client draft and/or internal pack in the existing `06_Proposals/Client_Drafts` and `06_Proposals/Internal_Review` folders. These organisational folders do not themselves enforce access controls. Respect verified audience/need-to-know boundaries.

No alternate folder, project-index write, overwrite, automatic version change, directory creation/repair, or source-document modification is permitted. Use the PM storage handoff if required. Release manifests/checklists remain in Paperclip; release approval does not authorise additional files or edits.

## Forbidden system mutations

No Odoo, CRM, accounting, procurement, supplier, client, email, e-signature, tender portal, or cloud-drive mutations. Vault writes require the exact save gate.
