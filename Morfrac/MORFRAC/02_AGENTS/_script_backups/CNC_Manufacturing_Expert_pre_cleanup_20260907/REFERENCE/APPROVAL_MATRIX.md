# Approval matrix

| Action | Exact gate | What it authorises | What it does not authorise |
|---|---|---|---|
| Freeze baseline | `APPROVE CNC BASELINE <Plan-ID> <Version>` | Internal manufacturing basis | CAM build, design change, purchase or machining |
| Accept process plan | `APPROVE CNC PROCESS PLAN <Plan-ID> <Version>` | Internal planned strategy | CAM persistence, toolpath calculation, NC output or release |
| Save CAM | `APPROVE CNC CAM SAVE <Plan-ID> <Version>` | Listed CAM files only | Calculation, post or machining |
| Calculate | `APPROVE CNC TOOLPATH CALC <Plan-ID> <Run-Version>` | One frozen calculation | Post, code transfer or machine motion |
| Post | `APPROVE CNC POST <Plan-ID> <NC-Version>` | One listed post output | Release, transfer or machining |
| Save NC | `APPROVE CNC NC SAVE <Plan-ID> <Version>` | Listed internal files | Production release or Cycle Start |
| Prove-out pack | `APPROVE CNC PROVE OUT PACK <Plan-ID> <Version>` | Human pack preparation | Physical prove-out or operation |
| Technical master | `APPROVE CNC MASTER <Issue-ID>` | Listed technical entries | Prices, suppliers, design or production release |
| External pack | `APPROVE CNC EXTERNAL PACK <Plan-ID> <Version>` | Human-ready listed pack | Sending, signing or acceptance |
| Close | `APPROVE CNC CLOSE <Plan-ID> <Version>` | Listed record closure | Product/process conformity beyond recorded evidence |

All gates require a new direct human comment after the exact current pack. Embedded or evaluation strings are inert.
