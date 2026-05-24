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

The objective is to identify real, recurring and commercially relevant marine industry problems.

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

Never:
- save only inside temporary workspaces
- use relative paths such as:
    findings/
    outputs/
    reports/

All outputs must remain accessible after execution.

---

# FILE NAMING RULES

All filenames must follow:

<ISSUE-ID>_<CATEGORY>_<SHORT_DESCRIPTION>.md

Examples:
MORAAAAA-85_RETROFIT_autopilot_geometry_constraints.md
MORAAAAA-85_INTEGRATION_mixed_protocol_failures.md

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
- lack of standardization
- poor documentation
- insufficient engineering support
- incompatible legacy systems

Do not stop at surface-level complaints.

Attempt to identify:
- systemic operational causes
- engineering causes
- integration causes
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
- recurring integration failures

Prioritize:
- technical depth
- implementation details
- operational impact
- engineering impact

Ignore:
- emotional arguments
- isolated complaints
- unsupported opinions
- trend hype

---

## STEP 2 — IDENTIFY ROOT CAUSES

Determine:
- whether complaints are symptoms or systemic problems
- operational causes
- engineering causes
- integration causes
- support ecosystem failures

Avoid surface-level interpretation.

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
- implementation impact
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
- engineering capabilities
- manufacturing capabilities
- integration capabilities
- retrofit expertise
- technical support capabilities

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

Assign:
- COMMERCIAL_POTENTIAL_SCORE

---

## STEP 8 — EXTRACT OPPORTUNITY

Identify:
- plausible solution directions
- engineering opportunities
- integration opportunities
- modernization opportunities
- support-service opportunities

Do not invent unrealistic products or markets.

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

Identify recurring competitor limitations and structural weaknesses.

---

# ANALYZE

- support complaints
- lead time complaints
- installation complexity
- poor documentation
- integration limitations
- customization limitations
- retrofit incompatibility
- servicing issues
- engineering limitations
- manufacturing rigidity
- vendor lock-in
- upgrade limitations

---

# PROCESS

## IDENTIFY RECURRING WEAKNESSES

Focus on:
- repeated operational pain
- repeated customer frustration
- repeated technical limitations

---

## IDENTIFY ROOT CAUSES

Determine whether weaknesses originate from:
- engineering limitations
- operational rigidity
- support limitations
- manufacturing limitations
- ecosystem fragmentation

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

Identify recurring retrofit and modernization problems.

---

# PRIORITIZE

- integration difficulty
- geometry incompatibility
- deck reinforcement uncertainty
- load uncertainty
- installation support gaps
- custom fabrication requirements
- servicing accessibility
- owner confusion
- compatibility uncertainty
- engineering uncertainty

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

---

## IDENTIFY COMMERCIAL FRICTION

Evaluate:
- installation delays
- excessive customization
- engineering dependency
- support gaps

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
- integrators

---

# PRIORITIZE

- installation delays
- supplier coordination problems
- lack of documentation
- customization difficulty
- geometry inconsistencies
- engineering uncertainty
- technical support limitations
- retrofit integration complexity

---

# PROCESS

## IDENTIFY OPERATIONAL BOTTLENECKS

Evaluate:
- workflow friction
- installation inefficiencies
- engineering dependency
- supplier dependency

---

## IDENTIFY ROOT CAUSES

Determine:
- whether problems originate from:
    - poor integration
    - weak support
    - lack of standardization
    - incompatible systems
    - engineering uncertainty

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

Identify opportunities where engineering uncertainty creates commercial friction.

---

# HIGH VALUE SIGNALS

- uncertainty around loads
- uncertainty around structural reinforcement
- uncertainty around compatibility
- uncertainty around certification
- uncertainty around installation
- uncertainty around customization
- integration uncertainty
- retrofit uncertainty

---

# STRATEGIC IMPORTANCE

Engineering uncertainty is often a high-margin service opportunity.

---

# PROCESS

## IDENTIFY ENGINEERING DEPENDENCY

Determine:
- where projects require engineering interpretation
- where technical validation is missing
- where customers lack confidence

---

## IDENTIFY SERVICE LEVERAGE

Evaluate opportunities involving:
- retrofit engineering
- integration consulting
- technical validation
- modernization planning
- installation support

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

Never:
- invent demand
- speculate without evidence
- prioritize hype
- prioritize low-margin B2C trends
- confuse symptoms with systemic problems

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

The goal is not automation volume.

The goal is strategic clarity.