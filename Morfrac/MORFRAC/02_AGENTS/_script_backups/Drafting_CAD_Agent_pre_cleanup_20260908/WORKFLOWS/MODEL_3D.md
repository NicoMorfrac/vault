# 3D model workflow

1. Confirm approved CAD baseline and intended model purpose.
2. Define components, bodies, occurrences, origins, construction geometry and configurations.
3. Define named sketches, constraints, profiles, features, patterns and dependencies in order.
4. Prefer parameters and stable references; expose topology-sensitive selections.
5. Define assembly joints/interfaces and clearance/interference checks where required.
6. Prepare the exact Fusion script or operator build manifest and hash.
7. Show active-document, save, overwrite, rollback and verification behavior.
8. Require `APPROVE CAD 3D BUILD <CAD-ID> <Run-Version>` only when a validated executor is available.
9. Verify supplied execution receipt, feature health, units, parameters, body/component count and required checks.

Without a validated executor, stop at `CAD_EXECUTION_NOT_AVAILABLE` and provide a human-run build specification.
