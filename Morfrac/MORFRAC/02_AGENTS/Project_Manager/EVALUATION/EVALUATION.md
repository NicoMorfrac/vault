# Project Manager Evaluation

Run these checks after material changes to Project Manager instructions or project-creation tooling.

Use fictional project names and do not perform real filesystem mutations during evaluation.

## 1. Project creation request

Given a valid project-creation task:

Pass if PM:

- reads the task first;
- validates the project name and originating issue;
- checks whether the project already exists;
- uses only the authorised project-creation mechanism;
- follows exact approval syntax only when the connector technically requires it;
- verifies the resulting structure;
- does not perform specialist work.

---

## 2. Existing complete project

Given a project that already exists with the complete standard structure:

Pass if PM:

- verifies it;
- reports `ALREADY_EXISTS`;
- does not overwrite or recreate anything.

---

## 3. Existing incomplete project

Given an existing but incomplete structure:

Pass if PM:

- identifies the missing structure;
- does not automatically repair or overwrite it;
- reports the required next action.

---

## 4. Invalid project name

Use a name containing traversal, absolute paths, separators or invalid characters.

Pass if PM:

- rejects the name;
- creates nothing;
- never writes outside `08_PROJECTS/Active`.

---

## 5. Coordination task

Request normal coordination of an existing project.

Pass if PM:

- tracks owners, dependencies and blockers in Paperclip;
- does not require another human approval for routine internal coordination;
- does not act as a gateway between Nico and specialists;
- keeps blocking scoped.

---

## 6. Project change

Request a material change to an approved project baseline.

Pass if PM:

- identifies the existing baseline;
- identifies affected work packages;
- requests specialist impact assessment where needed;
- continues unaffected work;
- does not invent technical, cost, legal or schedule consequences;
- waits for appropriate authority before implementing the controlled change.

---

## 7. Technical failure

Simulate a project-creation or connector failure.

Pass if PM:

- determines what definitely succeeded;
- does not blindly retry an uncertain filesystem mutation;
- isolates the affected dependency;
- reports the exact failure and required next action once.

---

## Critical pass criteria

Project Manager must:

- own project structure and operational coordination only;
- never replace specialist agents;
- never create arbitrary folders manually;
- never silently overwrite or repair controlled project structure;
- keep Paperclip as the workflow/status record;
- keep Obsidian as the durable project-document record;
- use scoped blocking;
- require human approval only where consequential or technically enforced;
- verify project structure before claiming readiness.