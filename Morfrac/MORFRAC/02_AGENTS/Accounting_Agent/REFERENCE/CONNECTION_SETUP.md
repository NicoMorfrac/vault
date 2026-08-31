# Odoo connection setup — human administrator

Connection is currently disabled. Do not place secrets in Obsidian, Paperclip task comments, configuration JSON, source control or chat. No credentials have been created or copied by this setup.

Required non-secret details: exact HTTPS Odoo instance, database, Odoo version/API availability, dedicated API user's ID and the allowed MORFRAC Odoo company IDs. Confirm contractual/API entitlement where applicable and inspect the deployment-specific models and fields.

1. Have the authorised Odoo administrator review a dedicated read-only integration user. It must have only the approved company/record/field access, with create/write/delete and privileged accounting actions denied. Do not assume a role named "accounting" or a successful read proves read-only permissions. Confirm custom methods/overrides do not introduce side effects.
2. Review record rules and effective rights for `account.move` and `account.move.line`; exclude payroll/personnel and unnecessary personal data. Keep a dated administrator review record. Do not conduct a destructive write test on production.
3. Create a dedicated API key through the approved Odoo account-security workflow. Provision it privately as a Windows DPAPI-encrypted PSCredential file at `C:\Users\nicol\.credentials\paperclip-odoo-accounting.clixml`, accessible only to the required Windows user and administrators. Use a secure prompt, not a command-line literal. Verify the account that runs Paperclip can decrypt it. DPAPI does not isolate agents sharing that Windows identity.
4. Set only non-secret approved values in `tools/organisation-scoped/odoo-connection.json`: origin without a trailing slash, database, protocol (`json2` for a reviewed Odoo 19+ deployment, `jsonrpc` for a reviewed compatible older deployment), userId, companyIds. `readOnlyAccessReviewed` and `enabled` remain false until administrator review and explicit connection approval. There is no automatic discovery or privilege change.
5. Run a minimal assigned-task scoped read, confirm company/records/fields/currency/date meaning, and record success without exposing credentials or unrelated financial data. Test negative company/field/method cases with mocks and inspect server rights; do not create test accounting transactions. Only then describe the connection as verified.
6. Record retention, rotation/expiry and revocation responsibilities. Rotate privately; never put a key in an agent-visible field.

## Separate approval-gated write setup

The user has authorised preparing limited writes only after exact human approval. Read access does not enable write access. Prepare a separate least-privilege write account/credential, with no payment, posting, reconciliation, deletion, bank, user-management or installation authority. Its only supported operation in this connector is `account.move.write` on one existing draft customer invoice or supplier bill, and only `ref`, `invoice_date`, `invoice_date_due`. Review the deployment's ACLs, record rules, overrides, recomputations and side effects before enabling it.

The fixed private write credential path is `C:\Users\nicol\.credentials\paperclip-odoo-accounting-write.clixml`. Review the effective write user ID and company scope separately. Configure `writeUserId`, `writeEnabled`, `draftCorrectionAccessReviewed` and `concurrencyProcedureReviewed` only after approval of this connection setup. Do not reuse a broad administrator credential.

Standard Odoo read-then-write is not atomic compare-and-swap. The connector rechecks the current row including `write_date` immediately before writing, but this does not eliminate concurrent-edit races. A reviewed exclusive-edit procedure or equivalent server-side concurrency control is required before production writes; the configuration flag records administrator review, not a technical lock. If the deployment cannot provide an acceptable control, keep writes disabled and let the human accountant apply proposals. Odoo model side effects require deployment-specific validation; a target-field readback is not a complete side-effect audit.

Each real correction requires a latest frozen plan and later exact direct human approval in its assigned issue. The connector logs one attempt before mutation and stops after any uncertain outcome. There is no automatic retry, elevated-credential fallback or generic RPC/UI route. Write tests in this rollout use mocks only; no production accounting record has been changed.

Normal Odoo reads use fixed `search_read` calls (HTTPS POST at the transport level); authentication/access logging may occur. These are not business-record writes. If any schema or permission differs, stop and review.

Official references: [Odoo 19 external API](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) and [Odoo 18 external API](https://www.odoo.com/documentation/18.0/developer/reference/external_api.html).
