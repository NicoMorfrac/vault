## General

- All files must use .md extension
- All files must be written inside:
  C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC
- Do not write outside the vault
- Do not overwrite existing files unless explicitly instructed or updating same IssueID
- If write fails, report error and STOP

---

## Naming Convention

All analysis files must follow:

<IssueID>_<Discipline>_<ShortDescription>.md

Example:
MORAAAAA-33_Bearing_IglidurX.md

Rules:

- IssueID is mandatory
- Discipline must be one of:
  - Structures
  - Bearing
  - Thermal
  - Cost
- ShortDescription:
  - must be concise
  - no spaces
  - no special characters
  - max 3 words
- Use CamelCase for materials and descriptors
- Do not use alternative suffixes (e.g. Evaluation, Analysis)
- Do not change naming structure

---

## Index Link Consistency

- Filename and Project Index link must match exactly
- Link must exclude .md extension

Example:
File:
MORAAAAA-33_Bearing_IglidurX.md

Link:
[[MORAAAAA-33_Bearing_IglidurX]]

---

## Deduplication Rule

- Files are uniquely identified by IssueID
- Same IssueID → update existing file
- Different IssueID → create new file
- Do not merge analyses across IssueIDs

---

## Write Behavior

- Confirm file path before writing
- Write file to correct project discipline folder
- Verify file exists after writing
- Report created or updated files

If file does not exist after write:

- STOP
- Report: File write failure