---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-05
as_of: 2026-09-05
audience: internal
record_class: setup_knowledge
status: repaired_and_validated
approval_status: owner_authorised
approval_reference: owner instruction that Nico AI, CEO and CTO must use the ChatGPT subscription correctly
related_findings:
  - Nico AI and CEO had been switched to an API-key adapter and failed with invalid_api_key
  - CTO referenced a deleted versioned Codex executable
  - All three isolated Codex homes retained valid ChatGPT login sessions
  - Nico AI, CEO and CTO now complete scoped Paperclip tasks through ChatGPT-authenticated Codex
  - Raffa AI was not modified
related_concepts:
  - ChatGPT subscription authentication
  - Paperclip Codex adapter
  - Scoped MCP connectors
  - Stable runtime paths
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-04_Paperclip_Task_Creation_and_Agent_Runtime_Repair]]"
---

# Nico AI, CEO and CTO ChatGPT subscription repair

## Outcome

Nico AI, CEO and CTO are configured on Paperclip's `codex_local` adapter and authenticate through their isolated ChatGPT login sessions. None of the three uses an `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` binding. All three returned to Idle after successful live canaries.

## Root causes

- Nico AI used `opencode_local`, model `openai/gpt-5.2-codex`, and injected OpenAI and Anthropic API-key references. Its latest runs failed with `401 invalid_api_key`.
- CEO used `opencode_local` with an OpenAI API-key reference. Its latest runs failed with the same `401 invalid_api_key` response.
- CTO used `codex_local` but referenced a deleted versioned executable under the Codex desktop installation, causing immediate adapter failures.
- The default current-user Codex home is not logged in, but the isolated Nico AI, CEO and CTO Codex homes each independently returned `Logged in using ChatGPT`.

## Applied configuration

All three now use:

- adapter: `codex_local`
- engine: `cli`
- executable: `C:\Users\nicol\.paperclip\runtimes\codex-stable\codex.exe`
- model: `gpt-5.6-sol`
- reasoning: `high`
- environment: only the agent's isolated `CODEX_HOME`
- shell, patch, multi-agent and broad filesystem access disabled
- heartbeat schedule disabled; wake-on-demand retained

Nico AI uses `company_scoped`, including the current direct CAD routing and assigned-attachment tools. CEO and CTO use `org_scoped`, including their leadership planning and internal-record tools. Existing instructions, reporting lines, runtime settings and permissions were preserved.

## Live verification

| Agent | Task | Run | Result |
| --- | --- | --- | --- |
| Nico AI | MORAAAAA-168 | 0ffaf3c1-67ff-4d97-9399-e53c960217d2 | succeeded; task Done |
| CEO | MORAAAAA-169 | c6df717e-726c-48d9-8c4a-88d87d638f77 | succeeded; task Done |
| CTO | MORAAAAA-170 | 3774d648-b705-499e-ae1a-9873e658f64f | succeeded; task Done |

Readback after the canaries showed all three agents as Idle with no current error code. Raffa AI remained untouched.

## Maintenance

Use `paperclip-config/leadership-chatgpt-auth-repair-20260905/repair.ps1` for audited recovery. Run it without arguments for preflight; use `-Deploy` only after reviewing the exact target state. Do not replace the stable executable with the Codex desktop application's versioned path.

## Related Links

- [[000 - DASHBOARD MORFRAC|Main MORFRAC dashboard]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest reports and information]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-04_Paperclip_Task_Creation_and_Agent_Runtime_Repair|Task creation and runtime repair]]

