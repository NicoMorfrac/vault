
## Purpose
Central knowledge base for MORFRAC agents, workflows, engineering references and business intelligence.

---

## Stack

- Paperclip (agent orchestration)
- Claude Sonnet 4.5 (engineering and strategic agents)
- GPT-4o (business and marketing agents)
- Ollama + Qwen2.5:7b (local fast tasks)
- Obsidian (knowledge base)
- Tailscale (remote access)

---

## Agents

- CEO — strategic orchestration
- CTO — technical execution
- Engineering — calculations and standards
- Business Intel — market research and competitor analysis
- Marketing — web traffic, SEO, campaigns
- Research — fast lookups and datasheet retrieval
- Assistant — document drafting and summaries
- Nico AI — director personal assistant
- Raffa AI — business manager personal assistant
- Tomeu AI — lead engineer personal assistant

---

## Vault Structure

- 00_SYSTEM — system rules and configuration
- 01_TOOLS — tool definitions and scripts
- 02_AGENTS — agent memory and logs
- 03_WORKFLOWS — workflow definitions
- 04_ENGINEERING — calculations, FEA, materials, standards, R&D
- 05_BUSINESS — market research, competitor data
- 06_MARKETING — campaigns, SEO, traffic
- 07_SUPPLIERS — supplier contacts and pricing
- 08_PROJECTS — active and archived projects
- 09_MEETINGS — meeting notes and decisions
- 10_REFERENCE — standards, datasheets, patents
- 11_PROMPTS — prompt templates
- 12_COMPETITOR_INTEL — competitor tracking, pricing, positioning, campaigns
- 99_TEMPLATES — reusable templates (project index, analyses, reports, emails)

---

## System Rules

Located in:

00_SYSTEM/

- FILE_RULES.md — file naming, writing, paths
- PROJECT_RULES.md — project structure and behavior
- GENERAL_AGENT_RULES.md — generic agent behavior
- ENGINEERING_RULES.md — engineering-specific logic

All agents must comply with these rules.

AGENTS.md files enforce them.

---

## File System

All files must be written to:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC

Rules:
- Use absolute paths
- Use file_write tool
- Do not simulate file creation
- All files must use `.md`

---

## Project Workflow

1. Create project manually in Paperclip
2. Link project to local folder in Obsidian
3. Assign tasks to agents
4. Agent:
   - verifies input sufficiency
   - performs analysis or blocks
   - writes results to project folder
   - updates 00_Project_Index.md

---

## Project Structure

08_PROJECTS/Active/<Project_Name>/

- 01_Structures
- 02_Bearings
- 03_Thermal
- 04_Cost
- 05_Decisions
- 00_Project_Index.md

---

## Engineering Philosophy

- No assumptions without explicit approval
- Input sufficiency is mandatory
- Blocking is preferred over guessing
- Calculations must be traceable
- Distinguish material limits vs design FoS
- Identify governing failure mode

---

## Additional Folders

12_COMPETITOR_INTEL
- Competitor products, pricing, positioning
- Campaign tracking
- Market comparisons

99_TEMPLATES
- Standard templates for:
  - Project Index
  - Engineering reports
  - Cost analysis
  - Emails and proposals
- Used by agents to ensure consistency

---

## Data vs Execution

- Obsidian → stores knowledge and results
- Paperclip → executes tasks and reasoning

Do not mix responsibilities.

---

## Logging

- Agents write logs to:
  02_AGENTS/<Agent_Name>/logs

- Engineering outputs go to:
  project folders or 04_ENGINEERING

---

## Final Rule

If uncertain:

- Stop
- Ask
- Do not guess