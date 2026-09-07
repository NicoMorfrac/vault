# Cutting data and calculations

Metric milling symbols:

- `vc`: cutting speed, m/min;
- `D`: effective cutting diameter, mm;
- `n`: spindle speed, rev/min;
- `zc`: effective cutting teeth;
- `fz`: feed per tooth, mm/tooth;
- `fn`: feed per revolution, mm/rev;
- `vf`: table feed, mm/min;
- `ap`: axial depth, mm;
- `ae`: radial width, mm;
- `Q`: metal-removal rate, cm3/min.

Equations:

- `n = (vc x 1000) / (pi x D)`;
- `vf = n x zc x fz`;
- `fn = zc x fz` for applicable milling representation;
- `Q = (ap x ae x vf) / 1000`.

Use manufacturer-specific effective diameter, chip-thickness correction and thread-milling/path formulas where applicable. Record every input and unit. Check tool, holder and machine limits, torque/power, rigidity, coolant, runout and life. A computed candidate remains unproven until authorised prove-out and inspection.
