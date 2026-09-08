# CAD data, storage and handoffs

## Storage boundary

- Obsidian stores requirements, parameter registers, source manifests, review reports, approvals, execution receipts, verification findings and links.
- Fusion/team/project storage holds authoritative native CAD when selected and approved by the human/project owner.
- Approved existing project folders may hold explicitly approved neutral exports or drawing deliverables; Drafting does not create the project structure.
- Do not store credentials, tokens or unrestricted connector configuration in Obsidian.
- Never overwrite a prior CAD/drawing/export revision automatically.

## Handoffs

- Engineering: design intent, loads/material/tolerance decisions and technical approval questions.
- CNC: manufacturing requirements and approved geometry/export only; CNC owns manufacturing process and CAM.
- FEA: exact configuration, simplified-analysis variant and geometry revision; FEA owns solver setup/results.
- Quality: drawing revision, critical characteristics and inspection requirements; Quality owns acceptance evidence.
- Product Documentation: approved released visual/source package only.
- Project Costing: verified technical effort/output/resource inputs only; no supplier-commercial master access.
- Project Manager: project storage, schedule and cross-role dependencies.

A link or agent assignment is not source access. Use minimum direct human `SOURCE_FILE`, `SOURCE_SCOPE`, `SOURCE_ISSUE` and `SHARE_WITH` declarations under current system rules.
