# Workflow - New Project Intake

## Trigger

A request describes a new client opportunity, internal development, product, engineering, manufacturing, marketing, or compliance project.

## Procedure

1. Read the full Paperclip issue and linked authorised records.
2. Search active and archived project records for a likely duplicate.
3. Classify the request as `NEW_PROJECT`.
4. Create a `DRAFT` brief in the issue using `TEMPLATES/PROJECT_INTAKE_BRIEF.md`.
5. Label each material item as Fact, User statement, Source evidence, Assumption, Inference, or Unknown.
6. Identify all blockers that can change safety, compliance, scope, deliverables, cost, schedule, acceptance, or routing.
7. Ask one grouped set of currently known blocking questions.
8. Update the brief. Do not silently replace prior approved information.
9. When sufficient, mark it `READY_FOR_APPROVAL` and request `APPROVE BRIEF <Project_Name> <Revision>`.
10. After exact approval, mark that revision `APPROVED`.
11. If the project structure is missing, create the exact `PM_TASK` assigned to Project Manager.
12. Wait for Project Manager confirmation that the project is ready.
13. Create specialist handoffs only from the approved brief.
14. Report `HANDED_OFF`, listing receiving issue IDs, owners, deliverables, and dependencies.

## Do not proceed when

- client/sponsor or authority is unclear;
- the request may duplicate an existing project;
- a safety, regulatory, confidentiality, or legal constraint is unresolved;
- scope or required deliverables cannot be distinguished;
- the proposal or delivery deadline is unknown and materially affects routing;
- approval refers to a different brief revision.

## Completion

The workflow is complete when the approved brief exists in Paperclip, the project structure is confirmed or deliberately deferred, and every approved handoff has a traceable issue/owner.
