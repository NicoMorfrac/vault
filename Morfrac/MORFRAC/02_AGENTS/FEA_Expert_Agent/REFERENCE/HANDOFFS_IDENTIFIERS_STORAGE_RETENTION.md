# Handoffs, Identifiers, Storage and Retention

## Handoffs

- CTO/Engineering: question, loads/combinations, material/criteria, safety and final conclusion.
- Drafting/CAD: authoritative configuration, geometry/tolerances and changes.
- Failure Analysis: exact hypothesis, observed pattern and evidence limits.
- CNC/Manufacturing/Quality: as-built variation, process evidence and producibility.
- Test/measurement owner: independent validation configuration, calibration and raw data.
- Project Manager: existing project, tasks, owners and approved storage path.
- Product Documentation/Legal: approved downstream technical change or external-review package only.

## Identifiers

Suggested IDs: `FEA-YYYY-NNN`, model `...-MNN`, run `...-RNN`, result pack `...-PNN`. Every record includes versions/hashes, project/configuration, software, author/executor/reviewer, timestamps, states, approvals and superseded links.

## Storage and retention

Use only an exact approved path inside an existing `08_PROJECTS/Active/<Project>/` structure. Do not create a folder during configuration. A reusable `04_ENGINEERING/FEA/` library requires the master gate.

Retain frozen inputs, model/study files, solver logs/messages, raw results, reports, checks, convergence/sensitivity, reviews, approvals and adverse/failed runs according to project/product/contract/legal rules. Never silently overwrite or delete evidence supporting a released decision, failure analysis, audit or hold.

