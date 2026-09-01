# 2D drawing workflow

1. Confirm the exact source model/configuration/revision and approved baseline.
2. Freeze projection standard, units, sheet size, template/title block and drawing purpose.
3. Plan base, projected, section, detail and auxiliary views with scales.
4. Define source-backed dimensions, tolerances, datums, GD&T, finish and process notes.
5. Define parts list/balloons, revision table and critical-characteristic identification when applicable.
6. Check over/under-dimensioning, duplicates, conflicts, broken references and readability.
7. Prepare the exact supervised build manifest and require `APPROVE CAD 2D BUILD <CAD-ID> <Run-Version>` only when validated.
8. Verify supplied drawing evidence against model revision and approved requirements.

Because automated drawing creation uses preview API capability, do not use an automated result as released production evidence. Human drawing review remains mandatory.
