
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

## Project Creation Workflow

- Engineering and other agents must not create projects
- Project Manager is the only agent allowed to create project structure

Project Manager must:

- Request explicit user approval before creation
- Wait for user response

Approval format:

APPROVE <Project_Name>

If approval is not received:
- Do not create project
- Report PENDING APPROVAL

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