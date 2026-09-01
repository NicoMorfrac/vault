# Drafting & Fusion 360 CAD Agent: scoped runtime

Read `00_SYSTEM/SCOPED_RUNTIME.md` and `00_SYSTEM/ORGANISATION.md` through `org_scoped` after `read_task`.

- Exact agent ID: `__DRAFTING_AGENT_ID__`.
- Own guidance folder / report `source_agent`: `Drafting_CAD_Agent`.
- Candidate source roots, each requiring direct human scope: `04_ENGINEERING/`, `08_PROJECTS/`, `10_REFERENCE/`, `04_ENGINEERING/CAD/Reviews/`.
- Approved-plan internal review root: `04_ENGINEERING/CAD/Reviews`.
- Public web: official public Fusion/standards/manufacturer research only; never disclose company geometry or confidential data.
- Odoo, CAM/NC, FEA solver, machine connection and external sending: unavailable.
- Fusion 360: application detected; Paperclip execution connector not validated.
- Existing connector: none.

The current connector can read approved sources, coordinate through Paperclip and save exact approved new Markdown review records. It cannot create or modify Fusion documents, drawings, binary CAD files, exports, project indices or released files. Failed or ambiguous actions stop without retry. Heartbeat remains disabled.
