# Document Taxonomy and Storage

Proposed repository after `APPROVE TRADE MASTER <Issue-ID>`:

```text
05_BUSINESS/Trade_Operations/
  00_Controlled_Registers/
  01_Operator_and_Representative_Master/
  02_Product_Classification_and_Origin_Master/
  03_Broker_Carrier_and_Template_Master/
  Shipments/
    YYYY/
      <Shipment-ID>/
        00_Dossier_Index/
        01_Order_Parties_and_Authority/
        02_Commercial_Invoice_and_Payment/
        03_Goods_Classification_Origin_and_Controls/
        04_Packing_Transport_and_Insurance/
        05_Customs_Tax_and_Statistics/
        06_Exit_Delivery_Returns_and_Closure/
```

Do not create this structure because it appears here.

## Storage rules

- One shipment ID can have multiple immutable versions; never overwrite originals.
- Link related project/order/PO/invoice/declaration/MRN/payment IDs from the dossier index.
- Keep filenames stable, concise and free of credentials/personal-data leakage.
- Use a manifest/hash to prove the reviewed pack.
- Record a controlled source link when the authoritative original remains in Odoo/accounting, broker, carrier or authority systems.
- Separate draft support data from actual issued/submitted/accepted evidence.
- A register is an index, not authority to change its underlying master data.
