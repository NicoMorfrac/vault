---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-02
as_of: 2026-09-02
audience: internal
record_class: setup_knowledge
status: repaired_and_validated
approval_status: owner_authorised
approval_reference: owner instructions "APPROVE NICO AUTH REPAIR", "check and repair all", "continue"
related_findings:
  - 42 approved company agents use the Codex CLI runtime and scoped connectors
  - Scoped assigned-task attachments can be read without broad file access
  - Obsolete OPENAI_API_KEY overrides were removed from 14 isolated runtimes
  - Paperclip blocked-state writes now include the required first-class unblock descriptor
  - MORAAAAA-141 is blocked cleanly with no active execution
  - Raffa AI and Drafting/Fusion routing were not changed
related_concepts:
  - Paperclip connector runtime
  - Codex CLI and MCP configuration
  - Assigned-task attachment isolation
  - Human approval boundaries
  - Engineering evidence handling
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Company_Wide_Agent_Authentication_Repair]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Fusion_360_and_Drafting_CAD_Agent]]"
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
---

# Paperclip connector runtime and attachment repair

## Outcome

The company-agent runtime repair is installed and validated. Forty-two approved agents now run through the Codex CLI path that loads their scoped MCP connector. They can read only the current assigned task, approved guidance and that task's exact attachments. No broad Paperclip, vault or filesystem access was introduced.

Raffa AI was excluded and not modified. The Drafting & Fusion 360 CAD Agent also remains outside the runtime-routing change because its separate owner approval has not been granted. All scheduled heartbeats remain disabled.

## Root causes

1. Paperclip `2026.824.1` selected its ACP path by default. That path did not consume the existing CLI `extraArgs`, so the scoped connector tools were absent even though agent authentication and model configuration were valid.
2. Fourteen isolated agent environments still injected an obsolete `OPENAI_API_KEY`. It overrode their valid ChatGPT login cache and caused `401` failures.
3. The upgraded issue API requires a first-class `unblockDescriptor` when an issue is changed to `blocked`.
4. The scoped connector could list task attachments but originally had no safe operation for reading their contents.

## Applied repair

- Pinned the 42 approved, non-Raffa and non-Drafting agents to `adapterConfig.engine = "cli"`.
- Removed only the obsolete `OPENAI_API_KEY` binding from the 14 isolated runtimes. Existing `CODEX_HOME`, model, instructions, permissions and other environment bindings were preserved.
- Added `read_attachment` to the company, organisation and yacht scoped connectors and to the 42 approved live agent configurations.
- Restricted attachment reads to the exact attachment ID already listed on the current assigned task. The reader validates metadata, byte size and SHA-256 before returning bounded PDF text and a rendered page image.
- Updated guarded blocked-state writes so Paperclip receives both `status: blocked` and the required board-owned unblock descriptor.
- Preserved heartbeats as disabled and made no Odoo, Fusion execution, external release or machine-control change.

Change scripts and before-state snapshots are retained under `paperclip-config/connector-runtime-repair-20260901/`. No credentials or secret values are stored in this note.

## Live proof

The CTO runtime read `MORAAAAA-141`, its scoped guidance and attachment `123.pdf` through `org_scoped`. The attachment was verified as:

- attachment ID: `82fff6ef-7859-4760-8c91-95b38d1bf232`
- bytes: `178832`
- SHA-256: `40b79b1e47ba3b8bf1cf57a5e08a2082b95dc628ad694a4073f8eb05c84c6c6e`
- pages: `1`

The agent could visually inspect the drawing and identify visible values including 36.66 overall length, 22 height, 12 depth, an Ø12 opening, 25 mounting-centre spacing and an M5 callout. It correctly refused to create a production CAD model because important geometry, tolerances, material/finish and side-profile information are missing, and because Drafting/Fusion runtime routing remains approval-gated.

`MORAAAAA-141` is now first-class `blocked`, has no active execution or checkout run, and records this board-owned unblock action: provide the missing manufacturing geometry or approve a non-production visual approximation; confirm `.f3d` and/or STEP deliverables; then separately approve Drafting/Fusion runtime routing before CAD execution.

## Verification

- JavaScript connector/workflow suite: **115 passed, 0 failed**.
- Python PDF extraction suite: **3 passed, 0 failed**.
- Fleet audit: **44 total agents**; **42 approved agents on CLI**; **42 with scoped attachment reading**; **0 approved agents with obsolete `OPENAI_API_KEY`**; **0 heartbeats enabled**.
- Raffa AI: idle and unchanged since its prior configuration date.
- Drafting & Fusion 360 CAD Agent: idle; shared runtime routing still held.

The final automatic CTO recovery run was interrupted by the Codex provider usage quota before it could post its own disposition. This is an account-capacity condition rather than a connector regression. The board-owned issue state was then applied directly through the same Paperclip issue API and read back successfully.

## Remaining human decisions

The repair itself is complete. CAD execution is intentionally not started. To continue `MORAAAAA-141`, the owner must supply the complete drawing/CAD definition or approve a non-production approximation, confirm output formats, and separately approve Drafting/Fusion runtime routing. Provider quota must also be available when the agent is next run.

## Official references

- [Codex MCP configuration](https://developers.openai.com/codex/mcp)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference)

## Related links

- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[000 - DASHBOARD MORFRAC|Main MORFRAC dashboard]]
- [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest reports and information]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Company_Wide_Agent_Authentication_Repair|Earlier authentication repair]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Fusion_360_and_Drafting_CAD_Agent|Drafting/Fusion configuration evidence]]
