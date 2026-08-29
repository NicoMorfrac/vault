# Nico AI Agent Routing

Use agent names and IDs to prevent ambiguous assignment. Confirm the agent is active before creating a handoff.

| Domain | Primary owner | Paperclip agent ID | Routing rule |
|---|---|---|---|
| Executive priority, authority, ownership conflict | CEO | `c996fcea-d10e-4c67-b4be-5b1fedd7769d` | Escalate decision; do not execute specialist work |
| Project structure and operational coordination | Project Manager | `780f4096-9a8f-46d8-8249-ef018c34dda3` | Use exact PM_TASK protocol for missing projects |
| Technical strategy and specialist coordination | CTO | `ffe90aa4-5f80-4b93-8eba-22d5bc836764` | Route complex method, ownership, or cross-discipline questions |
| Engineering calculations, FEA planning, failure analysis, manufacturing feasibility | Engineering | `0e7bf3a5-5cfd-4ec2-9bc1-bbce2e5125af` | Use until dedicated CAD/CNC/FEA/failure agents are approved |
| Market, competitor, commercial-opportunity intelligence | Business Intel | `8292c600-5e5e-4102-bd17-8d559ddad709` | Request evidence, sources, confidence, and commercial relevance |
| Website, SEO, content, campaigns, Meta concepts, analytics | Marketing | `02e3c568-a7d9-4ae6-a2a1-5ff17ecac41f` | Route through Marketing Lead rather than individual SEO workers |
| Routine document support, summaries, formatting, translation | Assistant | `241ddc1c-8854-4aa3-82cb-4f9ddb276523` | Use only for non-specialist content |
| Datasheets, supplier specifications, factual web retrieval | Research | `c0f9ffc6-ed94-4c64-ba7a-159b60c88851` | Currently paused; do not assign until status is active |

## Functions without a dedicated approved agent

Until the planned agents exist:

- Project costing and proposals -> CEO selects the commercial owner; Engineering supplies technical work estimates only.
- CAD and drafting -> CTO/Engineering coordinates the named human designer.
- CNC and PowerMill -> CTO/Engineering coordinates the named machinist/CAM owner.
- Legal/contracts -> authorised director and external/internal qualified legal reviewer.
- Customs -> authorised trade owner or customs broker.
- Grants, tenders, and R&D compliance -> CEO assigns a named human owner.
- Odoo finance and growth planning -> CEO assigns a named finance owner; no direct Odoo access is assumed.

## Routing rules

- Do not assign to a paused, pending, or unavailable agent.
- Do not bypass department leads to reduce apparent turnaround time.
- One issue has one accountable receiving owner.
- Supporting agents contribute through linked issues or comments.
- If two routing rules apply and responsibility is unclear, escalate to CEO.
