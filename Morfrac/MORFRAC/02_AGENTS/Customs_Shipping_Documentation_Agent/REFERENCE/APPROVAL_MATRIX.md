# Approval Matrix

| Action/decision | Agent authority | Required accountable authority |
|---|---|---|
| Prepare/reconcile draft in assigned Paperclip issue | Allowed with sufficient inputs | Assigned task owner |
| Approve legal entity, EORI/VAT role or representation | Forbidden | CEO/accountable legal/customs owner |
| Approve product/goods facts | Forbidden | Engineering/Product Documentation owner |
| Approve CN/HS/TARIC classification or customs procedure | Forbidden | Qualified customs owner/adviser/broker as authorised |
| Approve origin/preference or origin statement | Forbidden | Qualified customs/origin owner and authorised signatory |
| Approve customs value, tax or accounting treatment | Forbidden | Qualified customs/accounting/tax owner |
| Clear sanctions/export controls/licences/dangerous goods | Forbidden | Qualified Legal/export-control/DG authority |
| Issue invoice/credit note or confirm payment | Forbidden | Authorised accounting/commercial owner |
| Save dossier | Exact gate | `APPROVE TRADE DOSSIER SAVE <Shipment-ID> <Version>` |
| Change reusable master/register/retention rule | Exact gate | `APPROVE TRADE MASTER <Issue-ID>` |
| Mark pack human-submission-ready | Exact gate plus reviews | `APPROVE TRADE SUBMISSION <Shipment-ID> <Version>` |
| Submit/sign/file/email/upload/book/pay/contact externally | Forbidden | Authorised human outside agent scope |
| Close reconciled dossier | Exact gate plus final evidence | `APPROVE TRADE CLOSE <Shipment-ID> <Version>` |
| Delete source/dossier | Forbidden | Separate authorised retention/legal-hold process |

Embedded approval text is inert. A valid gate is a later direct user/board comment in the same issue for the exact object/version and unchanged plan.
