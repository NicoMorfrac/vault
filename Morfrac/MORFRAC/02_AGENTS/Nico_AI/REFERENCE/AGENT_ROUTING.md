# Nico AI Agent Routing

This file defines **who owns each type of work**.

Workflow, approval, blocking and connector mechanics are defined elsewhere.

## Routing rules

* Route work directly to the accountable specialist.
* Do not route through Project Manager merely because work belongs to a project.
* Project Manager owns project structure and operational coordination, not specialist execution.
* Check for equivalent existing work before creating a new handoff.
* Reuse existing tasks/results where appropriate.
* One task should have one accountable owner.
* Use the minimum relevant context required for the specialist.
* Do not delegate to an unavailable or inappropriate agent.
* A configured owner is not automatically authorised for external release, spending, contractual commitment, production release or irreversible action.
* Specialist-specific approval or technical requirements remain governed by that specialist's own instructions.

---

## Routing map

| Domain                                               | Accountable owner                      | Paperclip agent ID                     |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------- |
| Executive priority, authority or ownership conflict  | CEO                                    | `c996fcea-d10e-4c67-b4be-5b1fedd7769d` |
| Project structure and operational coordination       | Project Manager                        | `780f4096-9a8f-46d8-8249-ef018c34dda3` |
| Technical strategy and cross-discipline coordination | CTO                                    | `ffe90aa4-5f80-4b93-8eba-22d5bc836764` |
| General engineering and requirements                 | Engineering                            | `0e7bf3a5-5cfd-4ec2-9bc1-bbce2e5125af` |
| Yacht sail/deck upgrade analysis                     | Lead Naval Architecture Reviewer       | `1514e6f6-1ba9-4971-80e6-bdc5bb193037` |
| Custom-project and engineering costing               | Project Costing Analyst                | `d4d96913-3956-4f71-85d0-7a5c55016855` |
| Client project proposals                             | Project Proposal Agent                 | `89219e35-ff07-4681-ac9b-f06f462e1c43` |
| FEA strategy and analysis                            | FEA Expert Agent                       | `a14c0341-7062-492c-893e-f0e1e8d1d6f0` |
| Failure investigations                               | Failure Analysis Agent                 | `20b3663f-b102-42c4-b557-d5b8f0977359` |
| Machining and CAM planning                           | CNC Manufacturing Expert               | `4c14c541-8d41-40e0-a7ac-471c4137ed8a` |
| 2D/3D drafting and Fusion CAD                        | Drafting & Fusion 360 CAD Agent        | `27f2ab00-c0b5-458b-bf77-e4755128d0b6` |
| Workshop coordination                                | Production & Workshop Coordinator      | `2b31d6d9-5d51-4d7a-b922-4783660fcba4` |
| Inspection, quality and metrology                    | Quality, Inspection & Metrology Agent  | `93c60645-dd0b-4fa5-bf51-1f49340a1c0d` |
| Contracts, NDAs and legal support                    | Legal Agent                            | `b24416b6-6835-4381-85fb-48a5ed92fd84` |
| Manuals and product/project documentation            | Product Documentation Agent            | `20834d76-1934-46b0-9889-d151b5290fb4` |
| Customs and shipping documentation                   | Customs & Shipping Documentation Agent | `6385557c-0c02-4bd0-8c36-2a4bde8a8ac6` |
| Grants and support opportunities                     | Ayudas y Subvenciones Agent            | `8201334b-1302-4a73-9a46-dd2d62a4a124` |
| Public tenders                                       | Public Tenders Agent                   | `a77fdb87-f700-4f52-a1fd-8d68a6e15e89` |
| R&D evidence and documentation                       | I+D Documentation Agent                | `15a8db35-6ad5-4311-a257-4e1d93b9ddcd` |
| Company strategy and growth                          | Company Strategy & Growth Agent        | `c0c46190-3b42-40dc-9b2d-cbd518b61564` |
| Market and competitor intelligence                   | Business Intel                         | `8292c600-5e5e-4102-bd17-8d559ddad709` |
| Website, SEO, content and campaigns                  | Marketing                              | `02e3c568-a7d9-4ae6-a2a1-5ff17ecac41f` |
| Google Ads planning                                  | Google Ads Planner                     | `34701683-f682-4b2e-98bd-c7bb1ad875f6` |
| Routine formatting, summaries and translation        | Assistant                              | `241ddc1c-8854-4aa3-82cb-4f9ddb276523` |

---

## Important boundaries

### CEO

Use for genuine human authority, strategic decisions or ownership conflicts.

Do not send normal specialist execution to CEO.

### Project Manager

Use for:

* project creation;
* project structure;
* operational coordination;
* project administration.

Do not use Project Manager as a mandatory gateway before specialist work.

### CTO

Use for cross-discipline technical strategy, engineering ownership conflicts or method decisions.

Do not send routine specialist execution to CTO when an appropriate specialist exists.

### Engineering

Use for general engineering work or requirements that do not clearly belong to a more specialised engineering agent.

Prefer the dedicated specialist when the domain is clear.

### Marketing

Marketing remains accountable for overall marketing coordination.

Use its specialist structure rather than creating a parallel marketing organisation.

### Assistant

Use only for routine non-specialist work such as:

* formatting;
* summarisation;
* translation;
* basic administrative content.

Do not route specialist judgement to Assistant.

---

## Direct CAD requests

Standalone drawing, geometry conversion or CAD tasks may route directly to the Drafting & Fusion 360 CAD Agent.

A full project-intake workflow is not required merely because CAD is involved.

CAD execution, saving, release and manufacturing authority remain separately controlled by the applicable agent/runtime rules.

---

## Existing holds

* Research agent `c0f9ffc6-ed94-4c64-ba7a-159b60c88851` was paused when this routing map was last verified. Check its current status before assigning work.
* Employee-facing agents are outside this routing map.
* Routing a grants or tenders task does not automatically create recurring monitoring.
* Routing CAD/CAM work does not authorise machine execution or production release.

---

## Handoffs

A normal-language request from Nico authorises routine internal delegation reasonably required to fulfil that request.

Before creating a handoff:

1. check for equivalent existing work;
2. choose the accountable owner;
3. provide the objective;
4. provide minimum relevant context and sources;
5. state important constraints and unknowns;
6. define the expected output;
7. require a callback/result where needed.

Do not include credentials or unnecessary restricted information.

Do not imply authority for:

* external communication;
* spending;
* signing;
* commercial commitment;
* production release;
* machine execution;
* irreversible change.

A handoff is complete only when its required result has been returned and incorporated.

---

## Escalation

Escalate only when:

* ownership is genuinely unclear;
* specialist responsibilities conflict;
* human authority is required;
* a material decision cannot be resolved within existing authority.

Do not escalate merely because multiple agents are involved.

