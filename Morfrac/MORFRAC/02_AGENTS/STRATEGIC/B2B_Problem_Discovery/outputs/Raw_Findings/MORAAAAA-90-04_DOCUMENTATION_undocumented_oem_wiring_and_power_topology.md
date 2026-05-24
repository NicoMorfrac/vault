# MORAAAAA-90-04 Undocumented OEM wiring and power topology inflate integration risk

---

# SOURCES

| Platform | URL | Date | Discussion Type | Reliability |
|---|---|---|---|---|
| YBW Forum | https://forums.ybw.com/threads/boat-wiring-simplify-and-upgrade-beneteau-antares.613557/ | 2024-10-27 | OEM wiring-upgrade discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/electrical-wiring-diagram.138656/ | 2007-10-08 | Wiring-documentation discussion | MEDIUM |
| YBW Forum | https://forums.ybw.com/threads/wiring-diagram.12371/ | 2002-08-18 | Legacy builder-support discussion | LOW |
| Reddit | https://www.reddit.com/r/sailing/comments/1t97kre/nmea_2000_install_question/ | 2026-05-10 | Recent installer power-topology discussion | LOW |

---

# INDUSTRY_SEGMENT

OEM_BUILDERS

---

# PROBLEM_TYPE

DOCUMENTATION

---

# OPPORTUNITY_TYPE

TECHNICAL_SUPPORT

---

# SUMMARY

Owners upgrading OEM-installed systems repeatedly encounter poor labeling, incomplete diagrams, unclear trunking logic, and ambiguous power architecture. The result is that retrofit and service work starts with reverse engineering rather than implementation. The deeper operational problem is that many boats carry enough wiring complexity to support modern upgrades, but not enough trustworthy documentation to let installers integrate confidently without exploratory work.

---

# EVIDENCE

## Directly observed evidence

- In the YBW `Boat Wiring Simplify and Upgrade - Beneteau Antares` thread, the owner begins a modernization project by describing an unlabelled switch-panel backside, stacked terminals, absent busbars, and wires that are "all red or black." The first step becomes identifying circuits and drawing a new wiring diagram before major system work can proceed.
- In the YBW `Electrical wiring diagram` thread, a new Beneteau owner states that the information supplied with the boat is very basic and asks where to obtain a wiring diagram. Replies state that diagrams are often only guides, that even identical boats may not be wired the same, and that tracing wires manually may be more reliable than the supplied documentation.
- The same `Electrical wiring diagram` thread also contains a contrasting case where a similar Antares owner reports that cable runs and trunking positions are documented and an added NMEA 2000 backbone was straightforward. That contrast is operationally important: some OEM layouts are serviceable, but the field cannot assume documentation quality or consistency.
- In the YBW `Wiring Diagram` thread, a Beneteau owner asks for a diagram for a 345 because the builder no longer appears to support the aging boat. Replies complain about wiring hidden behind inner mouldings and proprietary looms, underscoring the maintenance burden of production-boat packaging once the OEM support window closes.
- In the Reddit `NMEA 2000 Install Question` thread from May 10, 2026, a recent Catalina 42 electronics installation leaves the NMEA backbone and autopilot-related power connected directly to the battery bus, creating confusion about what should be always-on, switched, or sequenced. The thread turns into interpretation of installer intent rather than reference to a clear documented power design.

## Repeated pattern

- The recurring pain is not simply "the wiring is messy." The repeated issue is that upgrade scope begins with forensic mapping of the existing installation.
- OEM boats often preserve enough hidden complexity to make later additions possible, but not enough reliable labeling or topology documentation to make them low-risk.
- Power topology is part of the documentation gap: installers and owners repeatedly have to infer why something was wired in a specific way and whether it should remain that way.

---

# ROOT CAUSE ANALYSIS

## Symptom

- Missing or generic wiring diagrams
- Unlabelled conductors and stacked terminals
- Unclear always-on versus switched power behavior
- Need to trace circuits manually before upgrading

## Likely root operational causes

- OEM production favors assembly efficiency and option flexibility over lifecycle service transparency.
- Multiple owners, optional equipment, and undocumented yard changes erode any original documentation value over time.
- Marine upgrades layer new digital systems onto legacy DC distribution without preserving a single current-state diagram.
- Builders and dealers often support initial delivery better than long-tail retrofit engineering.

---

# OPERATIONAL IMPACT

- Installation time expands before any new hardware is fitted because the existing state must be reconstructed.
- Troubleshooting risk rises when installers cannot tell whether behavior is intentional, inherited, or faulty.
- Quoting becomes difficult because hidden electrical cleanup and documentation work can dominate the visible upgrade.
- Mixed-system modernization carries higher callback risk when the baseline topology was never fully understood.

---

# STRATEGIC SCORES

## Severity Score:
3

## Frequency Score:
4

## MORFRAC Fit Score:
4

## Commercial Potential Score:
4

## Repeatability Score:
4

## Technical Complexity Score:
4

---

# POTENTIAL OPPORTUNITY

Observed evidence supports a pre-retrofit electrical documentation and integration-readiness service: current-state mapping, labeling standards, power-topology normalization, network and breaker schedule creation, and handoff documentation for yards and owners before larger electronics or systems upgrades.

This is an interpretation from repeated technical friction, not validated demand.

---

# CONFIDENCE_LEVEL

MEDIUM

---

# NOTES

- Source reliability is mixed because owner discussions dominate, but the repeated need to reverse engineer existing boats is strong.
- This finding matters commercially because documentation gaps are a recurring prerequisite problem that creates paid engineering work before the visible installation starts.
