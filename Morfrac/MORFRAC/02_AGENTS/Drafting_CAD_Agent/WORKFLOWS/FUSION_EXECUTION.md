# Fusion execution workflow

1. Confirm the read-only API probe has passed for the current Fusion installation.
2. Confirm licence/workspace capability and the intended active document/project.
3. Freeze source hashes, baseline, job manifest, script hash and allowlisted operations.
4. Prove that the run is disposable or has an approved non-overwriting destination and rollback.
5. Present exact expected geometry/drawing changes and verification checks.
6. Obtain the matching 3D or 2D build approval after the frozen plan.
7. Require a trained human to trigger and supervise the run.
8. Capture receipt, application/API version, document identity, results, warnings and errors.
9. Stop on ambiguity; never retry or change the script automatically.
10. Independently verify the result before proposing save/export.

No execution connector is currently enabled. This workflow documents the future controlled route and must not be simulated.
