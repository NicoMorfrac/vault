---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-01
as_of: 2026-09-01
audience: internal
record_class: setup_knowledge
status: repaired_and_validated
approval_status: approved
approval_reference: owner reply "APPROVE NICO AUTH REPAIR"
related_findings:
  - Nico AI isolated Codex authentication was missing after adapter migration
  - Nico AI authentication repaired without changing its instructions or permissions
  - GPT-5.6 Sol direct and Paperclip validation runs succeeded
  - Nico AI returned to idle with no current error reason
  - CEO retains a separate authentication error
related_concepts:
  - Paperclip agent authentication
  - Codex isolated runtime
  - GPT-5.6 model migration
  - Human-approved repair
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6]]"
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
---

# Nico AI authentication repair

## Outcome

Nico AI's Paperclip authentication error was repaired and validated. Nico AI is now `idle`, uses `gpt-5.6-sol`, has no current Paperclip error reason and retains its existing instructions, permissions and disabled heartbeat.

## Diagnosis

- The three failed runs for `MORAAAAA-141` ended with `acpx_auth_required` and `Authentication required` during `ensure_session`.
- Paperclip had assigned Nico AI an isolated `CODEX_HOME` during the model-adapter migration.
- That isolated home had no authentication cache and `codex login status` reported `Not logged in`.
- The main local Codex installation remained authenticated with ChatGPT.
- CEO showed the same authentication error. Engineering's missing-secret-binding error is separate.

## Approved repair and validation

Under the owner's exact approval `APPROVE NICO AUTH REPAIR`:

1. The existing local Codex authentication cache was copied into Nico AI's isolated `CODEX_HOME`. No credential content was printed, indexed or stored in Obsidian.
2. `codex login status` in Nico AI's isolated home returned `Logged in using ChatGPT`.
3. An ephemeral read-only `gpt-5.6-sol` handshake returned `NICO_AUTH_OK`.
4. Paperclip validation run `ce159e57-e0d8-4624-aeb4-3eea6cc06bd5` completed successfully with `gpt-5.6-sol` and cleared Nico AI's error state.
5. The taskless validation run made no Paperclip, vault, project, handoff, approval, schedule, external or Fusion mutation. Its scoped connector was intentionally unavailable because the company-scoped bridge requires an assigned Paperclip issue and run ID.

## Preserved boundaries

- No other agent authentication was changed.
- Raffa AI was not changed.
- Nico AI's adapter configuration, model, instructions, permissions and heartbeat settings were not changed by the authentication repair.
- `MORAAAAA-141` remained blocked and assigned to CEO after Paperclip's earlier recovery action; the repair did not reassign or execute that CAD request.
- Authentication files contain access tokens and remain sensitive local runtime data. They must never be copied into Obsidian, source control, reports or issue comments.

## Current exceptions

- CEO remains in `error` with `Authentication required` and requires separate owner approval before repair.
- Engineering remains in `error` because its OpenAI and Anthropic secret bindings are incomplete.
- Research remains manually paused.

## Official source

- OpenAI authentication and credential storage: https://developers.openai.com/codex/auth

## Related Links

- [[02_AGENTS/Nico_AI/AGENTS|Nico AI instructions]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6|GPT-5.6 migration evidence]]

