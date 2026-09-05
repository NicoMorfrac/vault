# Nico AI Agent Routing

Approved routing-map repair: 2026-08-31. This map identifies configured owners; it does not certify tool installation, access, technical competence, or release readiness.

Use exact names/IDs. Before dispatch, read only the intended agent's identity, company, availability and relevant capabilities. An idle agent is available; a running agent is not a missing agent, but check existing work to avoid duplicates. Never assign a paused, pending-approval, error or unavailable agent. Do not dump the complete directory or runtime/environment configuration.

| Domain | Accountable receiving owner | Paperclip agent ID | Boundary |
| --- | --- | --- | --- |
| Executive priority, authority or ownership conflict | CEO | `c996fcea-d10e-4c67-b4be-5b1fedd7769d` | Human/department decisions, not specialist execution |
| Project structure and operational coordination | Project Manager | `780f4096-9a8f-46d8-8249-ef018c34dda3` | Exact PM_TASK; separate folder-plan approval |
| Technical strategy and cross-discipline coordination | CTO | `ffe90aa4-5f80-4b93-8eba-22d5bc836764` | Method/ownership decisions; qualified engineer approval |
| General engineering and requirements gaps | Engineering | `0e7bf3a5-5cfd-4ec2-9bc1-bbce2e5125af` | Technical input, not a replacement for the dedicated specialists below |
| Yacht sail/deck upgrade analysis | Lead Naval Architecture Reviewer | `1514e6f6-1ba9-4971-80e6-bdc5bb193037` | Existing approved project evidence; specialist workplan and final storage have separate human approvals; no design authority |
| Custom-project and engineering costing | Project Costing Analyst | `d4d96913-3956-4f71-85d0-7a5c55016855` | Internal estimates, parameter/source review; no invented prices, master approval or supplier commitments |
| Client project proposals | Project Proposal Agent | `89219e35-ff07-4681-ac9b-f06f462e1c43` | Separate client draft/internal review; commercial, legal, save and release gates remain |
| FEA strategy and analysis support | FEA Expert Agent | `a14c0341-7062-492c-893e-f0e1e8d1d6f0` | Validate solver/access and engineer-approved method; no unsupported safety conclusions |
| Failure investigations | Failure Analysis Agent | `20b3663f-b102-42c4-b557-d5b8f0977359` | Evidence-led hypotheses, not an unapproved root-cause release |
| Machining/CAM planning | CNC Manufacturing Expert | `4c14c541-8d41-40e0-a7ac-471c4137ed8a` | Verified machine/material/tooling inputs and machinist approval; no automatic production code |
| 2D/3D drafting and Fusion 360 CAD | Drafting & Fusion 360 CAD Agent | `27f2ab00-c0b5-458b-bf77-e4755128d0b6` | Direct attached PDF/image requests route on the same issue; no project brief required for standalone geometry conversion; execution/save/release remain separately controlled |
| Workshop coordination | Production & Workshop Coordinator | `2b31d6d9-5d51-4d7a-b922-4783660fcba4` | Readiness, sequencing and holds; scoped access and release limits |
| Inspection and quality planning | Quality, Inspection & Metrology Agent | `93c60645-dd0b-4fa5-bf51-1f49340a1c0d` | Inspection evidence and controlled acceptance; human quality authority |
| Contracts, NDA and legal support | Legal Agent | `b24416b6-6835-4381-85fb-48a5ed92fd84` | Draft/review support; authorised director/qualified legal reviewer approves |
| Manuals and product/project documentation | Product Documentation Agent | `20834d76-1934-46b0-9889-d151b5290fb4` | Supported technical source and human release approval |
| Customs and shipping documentation | Customs & Shipping Documentation Agent | `6385557c-0c02-4bd0-8c36-2a4bde8a8ac6` | Traceable records; trade owner/broker validates declarations |
| Grants and support opportunities | Ayudas y Subvenciones Agent | `8201334b-1302-4a73-9a46-dd2d62a4a124` | Sourced eligibility and draft application; no submission or recurring schedule by implication |
| Public tenders | Public Tenders Agent | `a77fdb87-f700-4f52-a1fd-8d68a6e15e89` | Suitability/evidence and draft bid; director approves commitments/submission |
| R&D evidence and documentation | I+D Documentation Agent | `15a8db35-6ad5-4311-a257-4e1d93b9ddcd` | Traceable project evidence; no fabricated records or eligibility assertions |
| Company strategy and growth | Company Strategy & Growth Agent | `c0c46190-3b42-40dc-9b2d-cbd518b61564` | Authorised read-only business evidence; no assumed Odoo access or financing commitments |
| Market and competitor intelligence | Business Intel | `8292c600-5e5e-4102-bd17-8d559ddad709` | Sources, confidence and MORFRAC relevance |
| Website, SEO, content and campaign coordination | Marketing | `02e3c568-a7d9-4ae6-a2a1-5ff17ecac41f` | Keep Marketing Lead accountable; use its approved specialist assignments, not a parallel content team |
| Google Ads planning | Google Ads Planner | `34701683-f682-4b2e-98bd-c7bb1ad875f6` | Approved bounded planning package coordinated with Marketing; no spend, account changes or launch |
| Routine formatting, summaries and translation | Assistant | `241ddc1c-8854-4aa3-82cb-4f9ddb276523` | Non-specialist content only |

## Explicit holds and exclusions

- Fusion is installed and direct attached CAD task routing is enabled. The Drafting agent may receive and inspect the task/attachment. Paperclip-to-Fusion write execution, binary save/export and production release remain held until their separate validation and approvals.
- Research (`c0f9ffc6-ed94-4c64-ba7a-159b60c88851`) was paused at this verification. Check live status before any future assignment; this map does not reactivate it.
- Employee-facing agents are outside this routing update. Do not assign them responsibilities or edit their configuration.
- Grants/tenders recurring schedules remain deferred. Routing an approved one-off task does not enable a heartbeat.

## Approval and handoff rules

- A direct normal-language request from Nico authorises a bounded internal work package. Nico AI may interpret it, choose an approved owner, compose the prompt and call `delegate_task`; the user does not need to provide `SHARE_WITH` or connector syntax for routine internal coordination.
- Costing, Proposal, Legal, Customs, Grants, Tenders, I+D and Growth now have configured owners. Do not describe them as uncreated or require CEO to invent an owner solely because of the obsolete map.
- A new-project specialist handoff still requires the exact approved brief revision. Bounded work authorised under an existing approved brief/change follows its own workflow.
- Yacht analysis routing uses the approved Nico brief to create the lead issue. The lead then requires `APPROVE WORKPLAN <Issue-ID> <Revision>` for exact specialist packages and a separate `APPROVE YACHT ANALYSIS SAVE <Project_Name> <Analysis_ID> <Version>` for create-only internal storage.
- A target owner is not an approval. Preserve missing data, privacy restrictions, human engineering/commercial/legal decisions, dates and separate persistence/release gates.
- Delegated task text should state objective, minimum relevant context/source paths, expected output, constraints, unknowns and callback requirements. It must not include credentials or imply authority for external communication, spending, signing, release, production use or irreversible change.
- One receiving issue has one accountable owner. Coordinate cross-department dependencies through the existing leads; if authority is genuinely unclear, escalate.
- Check for an existing matching handoff before creation. Report actual receiving issue ID and state; proposed text, coordinator relays and available agents are not autonomous dispatch.
- Evaluation-only issues may propose routing but never create operational handoffs or treat quoted approvals as authority.
