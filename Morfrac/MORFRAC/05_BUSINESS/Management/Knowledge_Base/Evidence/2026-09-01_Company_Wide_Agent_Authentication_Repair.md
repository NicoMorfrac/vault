---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-01
as_of: 2026-09-01
audience: internal
record_class: setup_knowledge
status: repaired_and_validated
approval_status: owner_authorised
approval_reference: owner instruction "check and repair all"
related_findings:
  - All 43 non-Raffa Paperclip agents have usable Codex authentication
  - CEO, CTO and Engineering errors were cleared
  - Nine validation runs succeeded across GPT-5.6 Sol, Terra and Luna
  - Legacy Nico AI and SEO secret-reference mistakes were corrected
  - Research remains manually paused
related_concepts:
  - Paperclip agent authentication
  - Codex isolated runtime
  - Encrypted secret bindings
  - GPT-5.6 model validation
  - Human-controlled repair
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Nico_AI_Authentication_Repair]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair]]"
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
---

# Company-wide agent authentication repair

> [!important] Current runtime addendum
> Authentication remained valid, but the Paperclip 2026.824.1 runtime also needed a CLI connector, stale environment override, scoped attachment and blocked-state compatibility repair. Use [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair|the 2026-09-02 repair record]] as the current operational evidence.

## Outcome

The Paperclip organisation now has 43 agents in `idle`, one manually paused agent (`Research`) and no agents in `error`. All 43 non-Raffa agents have a usable Codex authentication path. Raffa AI was explicitly excluded and was not modified.

## Authentication repair

- Fourteen non-Raffa agents use isolated `CODEX_HOME` directories. Nico AI's isolated authentication had already been repaired; the authenticated local cache was copied to the other 13 isolated homes.
- The remaining 29 non-Raffa agents use the authenticated main local Codex home.
- `codex login status` returned `Logged in using ChatGPT` for the main home and every isolated non-Raffa home.
- File hashes confirmed that all 14 isolated authentication caches match the current local source cache. Credential contents were never printed, copied into the vault or included in Paperclip comments.

The 13 isolated agents repaired in this operation were B2B Problem Discovery, B2C Product Discovery, Business Intel, CEO, CTO, Engineering, Marketing, Research, SEO Execution, SEO Intelligence, Technical Content Production, Technical Content Strategy and Tomeu AI.

## Secret-binding corrections

- Nico AI's `OPENAI_API_KEY` reference was corrected from the obsolete Anthropic secret to the current encrypted OpenAI secret.
- SEO Execution and SEO Intelligence now use the correctly spelled `ANTHROPIC_API_KEY` path; the prior `ANTRHROPIC_API_KEY` typo was removed.
- Final audit: 14 current OpenAI bindings, 12 current Anthropic bindings, zero obsolete Anthropic bindings, zero typo paths and zero invalid secret references.
- No secret values were exposed or stored in this report.

## Runtime validation

Nine taskless validation runs completed successfully:

| Agent | Model | Runtime-home case | Paperclip run |
| --- | --- | --- | --- |
| Nico AI | `gpt-5.6-sol` | isolated | `ce159e57-e0d8-4624-aeb4-3eea6cc06bd5` |
| CEO | `gpt-5.6-sol` | isolated | `753dae83-0c4d-4b09-bf6f-cb2bec2573e0` |
| CTO | `gpt-5.6-sol` | isolated | `ed23dfd2-b72d-4bdf-b85c-ba8db8ebcb1f` |
| Engineering | `gpt-5.6-sol` | isolated | `078db6ae-82c1-4828-90b0-5b0b2edfa58b` |
| Marketing | `gpt-5.6-terra` | isolated | `f3084b83-1660-49b1-b377-6ac014610eb3` |
| Drafting/CAD | `gpt-5.6-sol` | main | `91ecbafe-f8c9-48e4-92e9-809333a24230` |
| Accounting | `gpt-5.6-terra` | main | `89a1fe86-0e0d-4379-9ec8-cc93ccaad941` |
| Assistant | `gpt-5.6-luna` | main | `8235aff5-ccac-4b37-b293-7514efe5b0dc` |
| SEO Execution | `gpt-5.6-luna` | isolated | `6aa8cee2-da9f-46af-b210-dac6d9e7568c` |

These runs validate authentication, adapter startup and the deployed model tiers. They were deliberately taskless, so task-scoped Paperclip connectors were unavailable and individual business workflows or external integrations were not production-tested.

## Preserved boundaries

- Raffa AI remained unchanged: `idle`, GPT-5.5 and heartbeat disabled. It remains outside the vault-managed company-agent rollout.
- Heartbeats remain disabled for every agent.
- Research remains manually paused and was not resumed.
- No live task, project, approval, vault-content workflow, external system, Odoo record, Fusion model or CAD file was mutated by the validation runs.
- `MORAAAAA-141` remains blocked and assigned to CEO; this repair did not reassign or execute it.
- Fusion execution, Odoo writes and all other approval-gated integrations retain their existing holds.

## Official source

- OpenAI authentication and credential storage: https://developers.openai.com/codex/auth

## Related Links

- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[000 - DASHBOARD MORFRAC|Main MORFRAC dashboard]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Nico_AI_Authentication_Repair|Earlier Nico-only repair snapshot]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6|GPT-5.6 migration evidence]]
