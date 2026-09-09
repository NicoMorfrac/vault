# PURPOSE

This document defines standardized execution patterns for the B2B Problem Discovery Agent.

Task patterns ensure:
- repeatable investigations
- structured outputs
- deterministic analysis
- evidence-based findings
- reduced hallucination risk
- strategic consistency
- long-term intelligence accumulation

The objective is to identify real, recurring and commercially relevant marine industry problems aligned with MORFRAC's mechanical retrofit and engineering capabilities.

The goal is not automation volume.

The goal is strategic clarity.

---

# OUTPUT STORAGE RULES

All outputs must be written directly into the MORFRAC Obsidian vault using absolute filesystem paths.

Never use:
- relative paths
- temporary workspace paths
- sandbox execution directories

All generated outputs must persist after execution.

---

# RAW FINDINGS OUTPUT PATH

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\B2B_PROBLEM_DISCOVERY\outputs\RAW_FINDINGS\

---

# SUMMARY REPORT OUTPUT PATH

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\B2B_PROBLEM_DISCOVERY\outputs\WEEKLY_REPORTS\

---

# MASTER INDEX PATH

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\STRATEGIC\B2B_PROBLEM_DISCOVERY\outputs\MASTER_INDEX.md

---

# FILE WRITING RULES

Always:
- create directories if missing
- verify files were successfully written
- use deterministic filenames
- report final absolute output paths
- save outputs as markdown files
- update MASTER_INDEX.md when creating findings
- comply with 00_SYSTEM/OBSIDIAN_REPORT_STANDARD.md
- include YAML frontmatter with type, source_agent, created, related_findings, related_concepts, related_projects, and related_reports
- include exactly one ## Related Links section
- use Obsidian wiki links only for structured entities: finding note names, taxonomy/concept note names, project note names, report note names, and agent note names

Never:
- save only inside temporary workspaces
- use relative paths such as:
    findings/
    outputs/
    reports/
- auto-link generic words such as engineering, retrofit, hardware, serviceability, analysis, marketing, SEO, or project

All outputs must remain accessible after execution.

---

# FILE NAMING RULES

All filenames must follow:

<ISSUE-ID>_<CATEGORY>_<SHORT_DESCRIPTION>.md

Examples:
MORAAAAA-85_RETROFIT_autopilot_geometry_constraints.md
MORAAAAA-85_SERVICEABILITY_furling_geometry_constraints.md

Use:
- uppercase categories
- lowercase descriptions
- underscores only
- deterministic naming

---

# SOURCE RELIABILITY RULES

Highest reliability:
- installer discussions
- yard discussions
- engineering discussions
- technical implementation discussions
- rigger discussions

Medium reliability:
- owner reports
- product reviews
- operational discussions

Low reliability:
- emotional arguments
- trend speculation
- influencer content
- vague complaints

Prioritize technical depth over popularity.

---

# CONFIDENCE LEVEL RULES

LOW:
- isolated discussion
- weak evidence
- unclear recurrence

MEDIUM:
- repeated evidence across multiple discussions
- moderate technical specificity

HIGH:
- repeated cross-platform evidence
- strong technical specificity
- operational and commercial relevance clearly demonstrated

---

# DUPLICATION RULES

Before creating a new finding:
- check for similar existing findings
- merge overlapping findings where appropriate
- update recurrence scoring instead of duplicating identical problems

Avoid:
- multiple findings describing the same root problem

Prioritize:
- pattern accumulation
over
- redundant finding generation

---

# ROOT CAUSE ANALYSIS

Always attempt to distinguish:
- symptom
from
- root operational problem

Example:

Symptom:
- installation complexity

Possible root causes:
- geometry inconsistency
- hidden structural conditions
- uncertain load paths
- inaccessible service areas
- poor retrofit documentation
- incompatible legacy systems

Do not stop at surface-level complaints.

Attempt to identify:
- systemic operational causes
- engineering causes
- retrofit causes
- mechanical integration causes
- support ecosystem failures

---

# STRATEGIC CAUTION RULE

Repeated complaints do not automatically validate:
- market size
- willingness to pay
- commercial viability

The agent must distinguish:
- recurring pain
from
- validated business opportunity

Do not generate exaggerated strategic conclusions from weak evidence.

---

# UNCERTAINTY LANGUAGE RULE

Avoid definitive strategic claims unless evidence is strong.

Use calibrated language such as:
- evidence suggests
- recurring patterns indicate
- preliminary convergence appears
- commercial validation remains limited
- operational relevance appears meaningful

Do not:
- overstate market certainty
- assume scalability
- assume willingness to pay
- imply validated demand without evidence

---

# STRATEGIC SCOPE BOUNDARY

Prioritize:
- mechanical systems
- rigging systems
- deck hardware
- structural retrofit
- geometry-sensitive installations
- serviceability of mechanical systems
- load-path dependent systems
- hardware integration complexity
- retrofit engineering
- servicing constraints
- installation-risk transfer

Deprioritize:
- marine electronics troubleshooting
- network configuration
- software ecosystems
- digital integration consulting
- generic electrical diagnostics
- electronics-only modernization
- generic marine IT support

Electronics-related findings are only relevant when:
- they directly affect mechanical retrofit
- they create installation geometry constraints
- they create operational integration burden tied to mechanical systems
- they reinforce broader uncertainty-transfer patterns

---

# MECHANICAL DOMAIN EXCLUSION RULE

Do not drift into:
- generic marine systems integration
- software ecosystems
- electronics support businesses
- marine IT troubleshooting
- network-management consulting

The strategic focus is:
- mechanical retrofit
- structural integration
- geometry-sensitive systems
- serviceability of mechanical systems
- installation-risk reduction
- engineering uncertainty in physical systems

---

# SCALABILITY FILTER

Before proposing a potential opportunity evaluate whether the problem appears:
- repeatable
- structurally recurring
- operationally bounded
- standardizable
- realistically serviceable

Deprioritize opportunities requiring:
- unlimited customization
- open-ended diagnosis
- uncontrolled engineering scope
- highly vessel-specific redesign
- excessive field troubleshooting
- continuous manual support

Prioritize opportunities where:
- intake requirements can be standardized
- geometry can be validated
- engineering boundaries are clear
- workflows are repeatable
- support burden is bounded

---

# LIABILITY AWARENESS

Flag findings involving:
- structural modification
- load-bearing systems
- steering systems
- primary rigging attachments
- safety-critical hardware
- hidden structural conditions
- uncertain certification requirements

Evaluate whether:
- engineering responsibility is ambiguous
- installer liability transfer exists
- hidden conditions increase failure risk
- certification/signoff may be required

High commercial pain does not automatically mean acceptable liability exposure.

---

# CONVERGENCE SIGNALING

When findings reinforce existing recurring themes, explicitly flag convergence with:
- ENGINEERING_UNCERTAINTY
- RETROFIT_COMPLEXITY
- SERVICEABILITY_COMPLEXITY
- MECHANICAL_INTEGRATION_COMPLEXITY
- INTEGRATION_FRAGMENTATION
- SUPPORT_OBSOLESCENCE

Do not force convergence.

Convergence outputs must preserve the existing `outputs/PATTERN_CONVERGENCE/` taxonomy structure and use `outputs/PATTERN_CONVERGENCE/Pattern_Convergence_Template.md`.

Only flag convergence when:
- root causes recur
- operational structures repeat
- uncertainty patterns appear across multiple domains

---

# TASK_PATTERN_01_RECURRING_PROBLEM_DETECTION

# OBJECTIVE

Identify recurring technical or operational pain points across multiple discussions or sources.

---

# INPUTS

- forum discussions
- Reddit threads
- LinkedIn discussions
- YouTube comments
- technical reviews
- installer discussions
- yard discussions
- owner discussions
- modernization discussions
- retrofit discussions
- servicing discussions
- rigger workflow discussions

---

# PROCESS

## STEP 1 — IDENTIFY PROBLEM SIGNALS

Search for:
- repeated complaints
- repeated failures
- repeated frustrations
- recurring operational inefficiencies
- recurring engineering limitations
- recurring retrofit problems
- recurring serviceability failures
- recurring geometry constraints
- recurring mechanical integration failures

Prioritize:
- technical depth
- implementation details
- operational impact
- engineering impact
- installation impact
- servicing burden
- retrofit burden
- uncertainty-transfer patterns

Ignore:
- emotional arguments
- isolated complaints
- unsupported opinions
- trend hype
- software feature complaints
- generic electronics troubleshooting

---

## STEP 2 — IDENTIFY ROOT CAUSES

Determine:
- whether complaints are symptoms or systemic problems
- operational causes
- engineering causes
- mechanical integration causes
- retrofit causes
- serviceability causes
- support ecosystem failures

Avoid surface-level interpretation.

Prioritize identifying:
- hidden-condition dependency
- geometry uncertainty
- load uncertainty
- integration ambiguity
- installation-risk transfer
- service escalation patterns

---

## STEP 3 — CLASSIFY PROBLEM

Assign:
- INDUSTRY_SEGMENT
- PROBLEM_TYPE
- OPPORTUNITY_TYPE

Using:
- STRATEGIC_TAXONOMY.md

No custom classifications allowed.

---

## STEP 4 — EVALUATE SEVERITY

Determine:
- operational impact
- financial impact
- technical impact
- installation impact
- retrofit impact
- servicing impact

Assign:
- SEVERITY_SCORE

---

## STEP 5 — EVALUATE FREQUENCY

Determine:
- number of repeated mentions
- number of independent discussions
- cross-platform recurrence

Assign:
- FREQUENCY_SCORE

---

## STEP 6 — EVALUATE MORFRAC FIT

Evaluate alignment with:
- retrofit engineering capabilities
- mechanical integration capabilities
- manufacturing capabilities
- geometry-sensitive systems expertise
- servicing knowledge
- installation-support capabilities

Assign:
- MORFRAC_FIT_SCORE

---

## STEP 7 — EVALUATE COMMERCIAL POTENTIAL

Estimate:
- willingness to pay
- recurrence potential
- scalability potential
- urgency of problem
- operational importance

Avoid assuming:
- validated demand
- scalable consulting models
- unlimited engineering support viability

Assign:
- COMMERCIAL_POTENTIAL_SCORE

---

## STEP 8 — APPLY SCALABILITY FILTER

Evaluate whether the opportunity appears:
- repeatable
- operationally bounded
- realistically serviceable
- standardizable
- scalable without uncontrolled engineering expansion

Flag risks involving:
- excessive customization
- open-ended troubleshooting
- undocumented vessel archaeology
- uncontrolled support burden
- vessel-specific redesign dependency

---

## STEP 9 — EXTRACT OPPORTUNITY

Identify:
- plausible mechanical retrofit opportunities
- engineering-validation opportunities
- geometry-review opportunities
- serviceability opportunities
- installation-support opportunities
- hardware-backed integration opportunities

Do not invent unrealistic products or markets.

---

## STEP 10 — IDENTIFY CONVERGENCE

Evaluate whether findings reinforce:
- ENGINEERING_UNCERTAINTY
- RETROFIT_COMPLEXITY
- SERVICEABILITY_COMPLEXITY
- MECHANICAL_INTEGRATION_COMPLEXITY

Only flag convergence when:
- root causes recur
- operational structures repeat
- uncertainty patterns appear across domains

Do not force convergence.

---

# REQUIRED OUTPUT

Each finding must include:
- Source
- URL
- Date
- Industry Segment
- Problem Type
- Severity Score
- Frequency Score
- MORFRAC Fit Score
- Commercial Potential Score
- Repeatability Score
- Technical Complexity Score
- Evidence Summary
- Root Cause Analysis
- Operational Impact
- Potential Opportunity
- Confidence Level

---

# TASK_PATTERN_02_COMPETITOR_WEAKNESS_ANALYSIS

# OBJECTIVE

Identify recurring competitor limitations and structural weaknesses related to mechanical systems, retrofit complexity and serviceability.

---

# ANALYZE

- support complaints
- installation complexity
- poor retrofit compatibility
- geometry limitations
- servicing inaccessibility
- poor documentation
- customization limitations
- retrofit incompatibility
- service escalation
- engineering limitations
- manufacturing rigidity
- vendor lock-in
- upgrade limitations

Exclude:
- generic electronics troubleshooting
- software complaints
- network-configuration issues not tied to mechanical systems

---

# PROCESS

## IDENTIFY RECURRING WEAKNESSES

Focus on:
- repeated operational pain
- repeated customer frustration
- repeated technical limitations
- repeated retrofit failures

---

## IDENTIFY ROOT CAUSES

Determine whether weaknesses originate from:
- engineering limitations
- retrofit constraints
- geometry dependence
- servicing inaccessibility
- operational rigidity
- support limitations
- mechanical integration failures

---

## APPLY SCALABILITY FILTER

Determine whether the weakness:
- creates bounded recurring opportunity
- creates scalable service opportunity
- requires uncontrolled customization
- depends on excessive field troubleshooting

---

## EVALUATE MORFRAC RELEVANCE

Determine:
- whether MORFRAC could realistically provide better solutions
- whether the weakness aligns with MORFRAC capabilities

---

# REQUIRED OUTPUT

- Competitor
- Weakness Type
- Root Cause
- Evidence Summary
- Frequency
- Potential Strategic Advantage
- MORFRAC Relevance
- Confidence Level

---

# TASK_PATTERN_03_RETROFIT_PAIN_ANALYSIS

# OBJECTIVE

Identify recurring retrofit and modernization problems related to mechanical systems and geometry-sensitive installations.

---

# PRIORITIZE

- geometry incompatibility
- deck reinforcement uncertainty
- load uncertainty
- installation support gaps
- custom fabrication requirements
- servicing accessibility
- owner confusion
- compatibility uncertainty
- engineering uncertainty
- load-path ambiguity
- hidden structural conditions
- inaccessible systems
- retrofit escalation
- uncertainty-transfer patterns

Deprioritize:
- electronics-only modernization
- software ecosystem complaints

---

# STRATEGIC IMPORTANCE

Retrofit complexity is a high-priority strategic area for MORFRAC.

---

# PROCESS

## IDENTIFY RETROFIT CONSTRAINTS

Determine:
- why retrofit complexity exists
- what prevents standard solutions
- where engineering uncertainty appears
- where hidden conditions increase risk

---

## IDENTIFY COMMERCIAL FRICTION

Evaluate:
- installation delays
- excessive customization
- engineering dependency
- service escalation
- uncertainty-driven scope expansion

---

## APPLY SCALABILITY FILTER

Evaluate whether the retrofit pain:
- is recurring
- can be operationally bounded
- can support repeatable workflows
- can avoid uncontrolled engineering escalation

---

## IDENTIFY CONVERGENCE

Evaluate convergence with:
- ENGINEERING_UNCERTAINTY
- RETROFIT_COMPLEXITY
- SERVICEABILITY_COMPLEXITY

---

# REQUIRED OUTPUT

- Vessel Type
- Existing System
- Retrofit Problem
- Root Cause
- Operational Impact
- Technical Complexity
- Potential Opportunity
- Confidence Level

---

# TASK_PATTERN_04_YARD_AND_INSTALLER_ANALYSIS

# OBJECTIVE

Identify recurring operational pain experienced by:
- boatyards
- installers
- riggers
- refit specialists

---

# PRIORITIZE

- installation delays
- lack of documentation
- customization difficulty
- geometry inconsistencies
- engineering uncertainty
- retrofit integration complexity
- serviceability limitations
- hidden conditions
- inaccessible systems
- retrofit scope escalation
- uncertainty-transfer burden

---

# PROCESS

## IDENTIFY OPERATIONAL BOTTLENECKS

Evaluate:
- workflow friction
- installation inefficiencies
- engineering dependency
- retrofit escalation
- uncertainty-transfer burden

---

## IDENTIFY ROOT CAUSES

Determine whether problems originate from:
- poor retrofit compatibility
- geometry sensitivity
- hidden structural conditions
- inaccessible service areas
- weak documentation
- lack of standardization
- engineering uncertainty

---

## APPLY SCALABILITY FILTER

Determine whether the operational friction:
- creates bounded recurring service opportunity
- creates scalable support opportunity
- requires excessive custom engineering

---

## IDENTIFY CONVERGENCE

Evaluate convergence with:
- ENGINEERING_UNCERTAINTY
- RETROFIT_COMPLEXITY
- SERVICEABILITY_COMPLEXITY

---

# REQUIRED OUTPUT

- Industry Segment
- Operational Problem
- Root Cause
- Workflow Impact
- Financial Impact
- Potential Opportunity
- MORFRAC Fit
- Confidence Level

---

# TASK_PATTERN_05_ENGINEERING_SERVICE_OPPORTUNITY

# OBJECTIVE

Identify opportunities where engineering uncertainty creates commercial friction in mechanical retrofit and servicing workflows.

---

# HIGH VALUE SIGNALS

- uncertainty around loads
- uncertainty around structural reinforcement
- uncertainty around compatibility
- uncertainty around installation
- uncertainty around customization
- geometry sensitivity
- retrofit uncertainty
- serviceability constraints
- hidden structural conditions
- inaccessible systems

Exclude:
- software-only uncertainty
- generic electronics support
- digital ecosystem troubleshooting

---

# STRATEGIC IMPORTANCE

Engineering uncertainty is often a high-margin service opportunity when tied to bounded retrofit and installation workflows.

---

# PROCESS

## IDENTIFY ENGINEERING DEPENDENCY

Determine:
- where projects require engineering interpretation
- where technical validation is missing
- where installers lack confidence
- where retrofit risk transfers to the field installer

---

## IDENTIFY SERVICE LEVERAGE

Evaluate opportunities involving:
- retrofit engineering
- load-path validation
- geometry review
- serviceability assessment
- installation support
- bounded retrofit validation
- hardware-backed integration support

Do not assume:
- recurring pain implies hardware opportunity
- recurring pain implies scalable consulting

---

## APPLY LIABILITY FILTER

Flag:
- safety-critical systems
- structural modification exposure
- hidden-condition dependency
- uncertain certification requirements
- installer liability transfer

---

## APPLY SCALABILITY FILTER

Evaluate whether:
- service boundaries can be defined
- intake can be standardized
- workflows can remain bounded
- support burden remains manageable

---

## IDENTIFY CONVERGENCE

Evaluate convergence with:
- ENGINEERING_UNCERTAINTY
- RETROFIT_COMPLEXITY
- SERVICEABILITY_COMPLEXITY
- MECHANICAL_INTEGRATION_COMPLEXITY

---

# REQUIRED OUTPUT

- Technical Problem
- Root Cause
- Source Evidence
- Industry Segment
- Engineering Complexity
- Potential Service Opportunity
- Commercial Potential
- Confidence Level

---

# EXECUTION RULES

Always:
- prioritize evidence
- prioritize recurrence
- prioritize technical depth
- prioritize operational relevance
- prioritize engineering relevance
- identify root causes
- use calibrated uncertainty-aware language

Never:
- invent demand
- speculate without evidence
- prioritize hype
- prioritize low-margin B2C trends
- confuse symptoms with systemic problems
- drift into generic electronics consulting
- assume scalability without evidence

---

# QUALITY CONTROL

Before finalizing findings verify:

- Is the problem real?
- Is the problem recurring?
- Is the problem commercially relevant?
- Does the problem align with MORFRAC capabilities?
- Is there evidence?
- Is the finding strategically meaningful?
- Was the root cause analyzed?
- Is the opportunity realistic?
- Is the finding mechanically relevant?
- Is the opportunity operationally bounded?
- Does the opportunity avoid uncontrolled customization?

If not:
- discard the finding

---

# LONG_TERM_OBJECTIVE

The objective of these task patterns is to create:
- structured strategic intelligence
- repeatable industry analysis
- opportunity discovery consistency
- long-term market understanding
- engineering-centered strategic insight

The objective is to identify:
- recurring mechanical retrofit pain
- geometry-sensitive integration friction
- serviceability complexity
- engineering uncertainty
- bounded engineering-risk reduction opportunities

The goal is not automation volume.

The goal is strategic clarity.
