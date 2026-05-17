# SEO Execution Agent Heartbeat

## Schedule

Weekly — Thursday — 08:00 Europe/Madrid

## Purpose

Review the latest MORFRAC SEO intelligence outputs and generate actionable SEO execution tasks for implementation review.

This heartbeat is operational, not analytical.

It converts existing SEO intelligence into implementation-ready recommendations.

---

# Inputs

Read latest outputs from:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\

Priority folders:

Executive_Reviews
Topic_Authority_Map
Content_Gap_Analysis
Entity_Relationship_Map
Contextual_Links
Pipeline_Health
Semantic_Clusters
Merged_Analysis

---

# Required Actions

## 1. Validate Pipeline Health

Review latest Pipeline Health report.

If:

* FAIL > 0
* missing required outputs
* schema failures
* missing crawl
* unreadable outputs

STOP execution and generate only a warning summary.

Do not create execution tasks from broken data.

---

## 2. Identify Highest-Priority Opportunities

Focus only on:

* high commercial / low authority topics
* missing pillar-page opportunities
* weak metadata on commercial pages
* strong contextual internal link opportunities
* entity opportunities with commercial value
* authority-content opportunities supporting product discovery

Avoid low-value SEO work.

---

## 3. Generate Execution Recommendations

Generate:

### Metadata Tasks

Include:

* URL
* suggested title
* suggested meta description
* target intent
* reason
* priority

---

### Internal Link Tasks

Include:

* source URL
* target URL
* suggested anchor
* reason
* priority

Prioritize:

* authority → commercial
* pillar → category/product
* high authority → weak commercial targets

---

### Content Brief Recommendations

Generate only:

* high-value authority opportunities
* commercial-supporting content
* engineering/technical guides
* semantic expansion opportunities

Do not generate generic SEO filler content.

---

### Pillar Page Opportunities

Identify:

* product-heavy clusters lacking authority structure
* missing landing pages
* fragmented semantic clusters
* weak commercial routing

---

## 4. Build Weekly Execution Queue

Create a concise implementation queue.

Required fields:

task_id
task_type
topic
target_url
priority
effort
impact
reason
evidence_source
status

Priority scale:

P1 - High impact / low risk
P2 - High impact / medium effort
P3 - Medium impact
P4 - Monitor

Status default:

Draft

---

# Required Outputs

Save outputs under:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Execution_Queue

Required files:

YYYY-MM-DD_SEO_Execution_Plan.md
YYYY-MM-DD_Metadata_Tasks.md
YYYY-MM-DD_Internal_Link_Tasks.md
YYYY-MM-DD_Content_Briefs.md
YYYY-MM-DD_Pillar_Page_Tasks.md

---

# Output Rules

Outputs must be:

* evidence-based
* commercially relevant
* implementation-oriented
* concise
* reviewable by humans

Avoid:

* vague SEO advice
* inflated priorities
* fake metrics
* over-optimization
* excessive keyword repetition
* low-value AI content

---

# Human Review Requirement

This agent does not:

* publish content
* modify Odoo
* edit the website
* deploy metadata
* inject links automatically
* create pages automatically

All outputs are recommendations only.

Human review is mandatory before implementation.

---

# Strategic Objective

The objective of this heartbeat is to bridge:

SEO intelligence
→
SEO operational execution


while maintaining:

* technical credibility
* commercial focus
* controlled implementation quality
* deterministic SEO planning
