# Data definitions and reconciliation

- Job, operation, part, lot and revision are separate identifiers. Do not merge them because names are similar.
- On-hand, released, reserved/allocated, available, expected and received quantities are different. Use source definitions and units, including cross-job reservations.
- For a specified operation/population/as-of time, partition unique input units into mutually exclusive completed, WIP, reported scrap/disposition-pending, and other explicitly accounted states. Verify the partition and don't force balance. Rework is often a subset/flag, not an extra unit count. Do not add WIP totals from consecutive operations for the same pieces.
- Completed machining is not inspected/accepted/released. Accepted and rejected totals require Quality/human evidence, not operator optimism. Reporting scrap does not authorise disposal or inventory movement.
- Elapsed duration, machine occupancy, summed person-hours, setup, run, cleanup, downtime and queue are different. Two people working one hour may produce two labour-hours but only one machine-hour. Parallel machine work needs explicit supervision/capacity evidence.
- Deduplicate only using an attributable event ID or confirmed duplicate source; same numeric value alone is not a duplicate. Correct by linked amendment, never replacing raw records.
- Use explicit timezone and durations/units. Missing time periods or quantity denominators remain gaps. Forecasts, standards and estimates never become actuals without source evidence.
- No assumed eight-hour days, productivity multipliers, setup standards, shrinkage or overtime.
