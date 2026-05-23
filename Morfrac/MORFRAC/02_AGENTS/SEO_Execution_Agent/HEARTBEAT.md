# SEO Execution Agent Heartbeat

## Schedule

Weekly — Wednesday — 08:00 Europe/Madrid

## Purpose

Review the latest MORFRAC SEO intelligence outputs and generate actionable SEO execution tasks for implementation review.

This heartbeat is operational, not analytical.

This agent does not perform crawl analysis, semantic clustering, authority modeling, or deterministic SEO scoring.

Those responsibilities belong to the SEO Intelligence layer.

It converts existing SEO intelligence into implementation-ready recommendations.

***

# Inputs

Read latest outputs from:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06\_MARKETING\SEO\_Agent\\

Priority folders:

Executive\_Reviews
Topic\_Authority\_Map
Content\_Gap\_Analysis
Entity\_Relationship\_Map
Contextual\_Links
Pipeline\_Health
Semantic\_Clusters
Merged\_Analysis

***

## Automatic Production Handoff

Approved authority opportunities should automatically transition into production preparation.

When:

* authority opportunity status \= Approved
* strategic priority \= High or Medium

the heartbeat should:

* generate production briefs
* create production handoff tasks
* assign production tasks to:
  Technical\_Content\_Production\_Agent
* define:
  * master content requirements
  * derivative content requirements
  * internal-link requirements
  * commercial routing requirements

The execution layer should not stop after brief generation unless validation fails.

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

***

## 2. Identify Highest-Priority Opportunities

Focus only on:

* high commercial / low authority topics
* missing pillar-page opportunities
* weak metadata on commercial pages
* strong contextual internal link opportunities
* entity opportunities with commercial value
* authority-content opportunities supporting product discovery

Avoid low-value SEO work.

***

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

***

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

***

### Content Brief Recommendations

Generate only:

* high-value authority opportunities
* commercial-supporting content
* engineering/technical guides
* semantic expansion opportunities

Do not generate generic SEO filler content.

***

### Pillar Page Opportunities

Identify:

* product-heavy clusters lacking authority structure
* missing landing pages
* fragmented semantic clusters
* weak commercial routing

***

## 4. Build Weekly Execution Queue

Create a concise implementation queue.

Required fields:

task\_id
task\_type
topic
target\_url
priority
effort
impact
reason
evidence\_source
status

Priority scale:

P1 - High impact / low risk
P2 - High impact / medium effort
P3 - Medium impact
P4 - Monitor

Status default:

Draft

***

# Required Outputs

Save outputs under:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06\_MARKETING\SEO\_Execution\_Queue

Required files:

YYYY-MM-DD\_SEO\_Execution\_Plan.md
YYYY-MM-DD\_Metadata\_Tasks.md
YYYY-MM-DD\_Internal\_Link\_Tasks.md
YYYY-MM-DD\_Content\_Briefs.md
YYYY-MM-DD\_Pillar\_Page\_Tasks.md

***

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

***

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

***

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

## Reporting Requirement

Every heartbeat execution must create saved output files.

If execution succeeds, save all required execution outputs.

If execution fails because of missing, stale, malformed, or invalid inputs, save:

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06\_MARKETING\SEO\_Execution\_Queue\YYYY-MM-DD\_EXECUTION\_FAILED.md

The failed report must explain:

* missing inputs
* stale outputs
* schema failures
* crawl failures
* pipeline reliability issues

The agent must never complete silently.