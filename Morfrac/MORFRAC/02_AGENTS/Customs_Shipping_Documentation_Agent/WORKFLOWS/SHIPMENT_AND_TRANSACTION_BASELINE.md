# Workflow - Shipment and Transaction Baseline

Establish one immutable identity before document work:

- shipment ID/version and originating Paperclip issue;
- related project, sales/purchase order, PO, invoice/credit-note and return/repair IDs;
- sale, purchase, sample, loan, repair, return, replacement, warranty, temporary movement, transfer or other approved transaction type;
- dispatch/export/transit/import/destination places and dates;
- Union/non-Union goods status and special fiscal territory assessment reference;
- requested customs procedure and accountable owner;
- approved Incoterm rule, precise named place and version;
- physical consignment split/merge relationship.

If multiple physical consignments or declarations exist, assign linked child IDs. If the commercial transaction and physical movement do not align, set `RECONCILIATION_CONFLICT`.
