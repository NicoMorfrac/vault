
## Project Structure

Each project must contain:

- 00_Project_Index.md
- 01_Structures
- 02_Bearings
- 03_Thermal
- 04_Cost
- 05_Decisions

## Project Location

Projects must exist under:

08_PROJECTS/Active/<Project_Name>/

If project does not exist:
- STOP
- Do not create the project unless acting as Project Manager
- Emit a PM_TASK request

PM_TASK format:

type: create_project
project_name: <Project_Name>
reason: Project folder missing

Project creation must be handled by the Project Manager agent.

---

---

## Project Creation Workflow

- Project Manager is the only normal agent allowed to create the standard MORFRAC project structure.
- Engineering and other specialist agents must not create or repair project folders.

A direct human request to create a project, or an authorised internal project-creation task from Nico AI, is sufficient authority to create the standard project structure.

No second `APPROVE <Project_Name>` comment is required for routine standard project creation.

Project Manager must:

1. Validate the exact project name.
2. Inspect whether the project already exists.
3. If the standard structure already exists and is complete, report `ALREADY_EXISTS`.
4. If the project exists but is incomplete or partial, do not overwrite or repair it automatically. Report the missing structure and required next action.
5. If the project is absent, use only the authorised Project Manager filesystem tool to create the standard structure.
6. Verify the actual resulting structure after creation.
7. Record the verified result in Paperclip.

Project creation authorises only the standard project structure.

It does not authorise:

- specialist technical work;
- project scope changes;
- pricing or commercial commitments;
- spending or purchasing;
- contracts;
- production or manufacturing release;
- external communication or publication;
- destructive or irreversible changes.

---
## Project Index

File:
00_Project_Index.md

Sections:

- Objective
- Active Tasks
- Assumptions
- Decisions
- Open Questions
- Linked Analyses
- Notes

## Index Update Rules

- Only update "Linked Analyses"
- Do not modify other sections
- Append or update entries
- Do not duplicate entries

## Entry Format

- [[<IssueID>_<ShortDescription>]] (<Date>)
  - Status: <PASS/FAIL>
  - Governing criterion: <criterion>
  - Key value: <value>
  - Material FoS: <value>
  - Design FoS: <value>

## Index Consistency

- Entry must match filename exactly
- If entry exists, update it
- If entry does not exist, append

---

## Optional Proposal Area (ProposalWorkflow-v1)

The five core folders and `00_Project_Index.md` above remain the standard project structure. A project without a proposal area is not incomplete on that basis. Do not add optional folders during ordinary project creation or migrate existing projects automatically.

After an explicit proposal-storage request and project-specific folder approval, Project Manager may prepare exactly:

- `06_Proposals/`
- `06_Proposals/Client_Drafts/`
- `06_Proposals/Internal_Review/`

This operation requires an existing complete core project, the matching `ProposalWorkflow-v1` global sections, and the separate `PM_TASK prepare_proposals` protocol. It creates no files and does not alter the project index or core folders.

Use only `C:\Users\nicol\tools\pm_fs.py`:

- Read-only check: `--check-proposals "<Project_Name>"`.
- After the exact current folder plan and direct `APPROVE <Project_Name>`: `--prepare-proposals "<Project_Name>"`.

Run with an available authorised Python interpreter and pass the name as one literal argument, not an interpolated shell command. No alternate vault/root option, tool installation, or permission change is authorised. Verify actual paths and output.

If all three folders exist safely, verify and report already prepared without modifying anything. If only some exist, a file occupies a folder path, the core project is incomplete/missing, or a link/path/error is unsafe, stop and report the exact blocker. Do not repair, retry automatically, or create a missing base project through this operation. Missing base projects use the original create_project workflow with their own approval.

Proposal save and human-release approvals are separate from this folder approval. Folder readiness does not approve project scope, engineering work, price, terms, or delivery.
