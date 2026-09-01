---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-01
as_of: 2026-09-01
audience: internal
record_class: setup_knowledge
status: configured_with_routing_hold
approval_status: approved
approval_reference: Paperclip approval adf2203e-ea85-4263-950c-fb3ee50c9337 and owner instruction "ok. go for it"
related_findings:
  - Fusion 360 executable detected and process running
  - Drafting & Fusion 360 CAD Agent created under CTO
  - Both controlled 2D and 3D workflows configured
  - Read-only Fusion API probe installed with startup disabled
  - Shared scoped runtime routing not enabled and awaiting separate owner approval
  - Paperclip-to-Fusion execution not yet validated
  - Automated 2D drawing creation remains preview capability
related_concepts:
  - Fusion 360
  - Parametric 3D CAD
  - Manufacturing drawings
  - CAD parameter and revision control
  - Human approval gates
related_projects: []
related_reports:
  - "[[00_SYSTEM/ORGANISATION]]"
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
  - "[[02_AGENTS/Drafting_CAD_Agent/AGENTS]]"
---

# Fusion 360 installation and Drafting/CAD agent configuration

## Objective and scope

Record the owner's confirmation that Fusion 360 is installed and configure one controlled MORFRAC specialist for both 3D modelling and 2D drafting. This record distinguishes installed/configured capability from validated CAD execution or design release.

## Verified facts

- `Fusion360.exe` was detected in the current user's Autodesk webdeploy production installation on 2026-09-01.
- Fusion 360, Fusion Launcher and Autodesk Identity Manager processes were observed running.
- Paperclip server version was `2026.824.1` and healthy during configuration.
- The active MORFRAC company had 43 agents before this addition and no Drafting/CAD/Fusion-specific agent.
- Existing CNC metadata still recorded CAM/PowerMill access as not configured.

## Approved configuration

| Item | Recorded result |
| --- | --- |
| Paperclip agent | Drafting & Fusion 360 CAD Agent |
| Agent ID | `27f2ab00-c0b5-458b-bf77-e4755128d0b6` |
| Reports to | CTO `ffe90aa4-5f80-4b93-8eba-22d5bc836764` |
| Model | `gpt-5.6-sol`, high reasoning |
| Runtime | Idle in Paperclip; shared scoped routing not enabled; heartbeat disabled |
| Hire approval | `adf2203e-ea85-4263-950c-fb3ee50c9337`, approved |
| Instruction root | `02_AGENTS/Drafting_CAD_Agent` |
| Configured scope | 2D and 3D requirements, parameters, plans/scripts, reviews and controlled handoffs |
| Direct CAD execution | Not enabled pending supervised validation |
| Raffa AI | Excluded and unchanged |

## 3D capability

The agent can establish sourced parametric baselines and prepare deterministic Fusion component/body/sketch/feature/assembly plans or bounded Python scripts. It records units, coordinates, named parameters, formulas, configuration, revision, interfaces and expected verification. It does not invent engineering decisions or execute/save models without the separate applicable gate and validated connector.

## 2D capability

The agent can prepare 2D sketches and manufacturing-drawing plans covering source model/configuration, projection, sheets/templates, views, sections/details, dimensions, tolerances, datums/GD&T, notes, parts lists, title blocks and verification. Production drawings require supervised creation and human engineering/quality review.

## Fusion API probe

A read-only add-in named `MORFRACFusionBridge` version `0.1.0` was installed in Fusion's user AddIns folder with `runOnStartup: false`. When manually run from Fusion's Scripts and Add-Ins dialog, it records application/document/API context and explicitly performs no geometry, drawing, save or export action.

The probe has not yet been run. Therefore current state is `FUSION_INSTALLED_API_NOT_VALIDATED`, not operational CAD automation.

## Approval separation

- Requirements/parameters: `APPROVE CAD BASELINE <CAD-ID> <Version>`.
- 3D execution: `APPROVE CAD 3D BUILD <CAD-ID> <Run-Version>`.
- 2D execution: `APPROVE CAD 2D BUILD <CAD-ID> <Run-Version>`.
- Binary save: `APPROVE CAD SAVE <CAD-ID> <Version>`.
- Export: `APPROVE CAD EXPORT <CAD-ID> <Export-Version>`.
- External human handoff: `APPROVE CAD EXTERNAL PACK <CAD-ID> <Version>`.
- Internal Markdown review storage continues to use SpecialistRecords-v1.

An approval in one row never authorises another row, design release, CAM/NC, machine operation, sending or external commitment.

## Limitations and next validation

1. Separately approve and validate the minimum `org_scoped` role and recipient routing required for live assignments.
2. Manually run the read-only probe inside Fusion and verify its receipt.
3. Review installed Fusion licence/workspace/API context.
4. Approve and execute a disposable supervised 3D smoke test.
5. Approve and execute a disposable supervised 2D drawing smoke test.
6. Review the exact allowlisted connector/job schema before enabling Paperclip-to-Fusion actions.
7. Keep 2D automation under human control: Autodesk currently documents `DrawingManager.createDrawing` as preview functionality introduced in July 2026.

No production CAD file, drawing, export or project record was created by this setup. The existing Engineering agent error and the organisation-wide `canCreateSkills` permission review are separate unresolved matters.

## Official sources

- Autodesk, creating scripts/add-ins and default Windows paths: https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954
- Autodesk, Fusion Scripts API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Scripts.htm
- Autodesk, script/add-in structure and manifest: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm
- Autodesk, preview drawing creation API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/DrawingManager_createDrawing.htm

## Related Links

- [[02_AGENTS/Drafting_CAD_Agent/AGENTS|Drafting/CAD agent instructions]]
- [[02_AGENTS/Drafting_CAD_Agent/REFERENCE/FUSION_CAPABILITY|Fusion capability and limitations]]
- [[00_SYSTEM/ORGANISATION|Current organisation and readiness holds]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[05_BUSINESS/Management/Knowledge_Base/README|Company knowledge index]]
