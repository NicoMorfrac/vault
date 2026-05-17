# SEO Intelligence Agent Heartbeat

## Purpose

The SEO Intelligence Agent heartbeat is strategic and supervisory.

It does NOT execute the deterministic SEO pipeline.

The deterministic SEO pipeline already runs automatically through:

```text
run_seo_pipeline.bat
```

The heartbeat exists to:

* review long-term SEO intelligence
* interpret historical SEO changes
* validate pipeline reliability
* detect structural SEO shifts
* identify strategic SEO risks
* recommend future intelligence improvements

This heartbeat is NOT an operational execution workflow.

Operational execution planning belongs to:

SEO\_Execution\_Agent

***

## Schedule

Monthly — First Thursday — 14:00 Europe/Madrid

***

## Primary Responsibilities

The heartbeat should:

* review historical SEO comparisons
* review topic authority changes
* review content gap evolution
* review entity relationship evolution
* review pipeline health
* detect structural SEO shifts
* identify strategic SEO opportunities
* identify intelligence-layer weaknesses

The heartbeat should NOT:

* generate implementation queues
* generate metadata task lists
* generate internal link insertion tasks
* publish content
* deploy website changes

***

## Inputs

Review latest outputs from:

```text
06_MARKETING/SEO_Agent/
```

Priority folders:

```text
Executive_Reviews
Historical_Comparisons
Topic_Authority_Map
Entity_Relationship_Map
Content_Gap_Analysis
Pipeline_Health
Semantic_Clusters
```

***

## Monthly Review Objectives

### 1. Authority Growth Review

Determine:

* which topics gained authority
* which topics remain weak
* which entities gained visibility
* which commercial topics remain unsupported

***

### 2. Structural SEO Review

Identify:

* recurring structural failures
* persistent template weaknesses
* unresolved discoverability bottlenecks
* unstable crawl behavior
* semantic fragmentation

***

### 3. Commercial Visibility Review

Evaluate:

* high-value product visibility
* commercial topic growth
* CTR trend direction
* non-branded discoverability
* engineering authority positioning

***

### 4. Pipeline Reliability Review

Review:

* stale outputs
* schema consistency
* crawl stability
* script reliability
* dependency failures
* maintenance complexity

***

### 5. Strategic Direction Review

Recommend:

* next-month SEO priorities
* future analysis layers
* future intelligence improvements
* automation opportunities
* reporting improvements

***

## Required Output

Save:

```text
06_MARKETING/Reviews/YYYY-MM_Monthly_SEO_Strategy_Review.md
```

Required sections:

```text
Executive Summary
Biggest Gains
Biggest Weaknesses
Commercial Opportunities
Authority Shifts
Technical Risks
Pipeline Risks
Next-Month Priorities
Strategic Recommendations
```

***

## Output Rules

Outputs must:

* remain evidence-based
* prioritize leverage over traffic volume
* focus on commercial relevance
* support engineering authority
* separate intelligence from execution
* remain concise and strategic

Do NOT:

* generate operational task queues
* create implementation plans
* repeat deterministic tables
* recommend generic SEO tactics
* overreact to short-term volatility

***

## Reporting Requirement

Every heartbeat run must produce a saved markdown report.

If inputs are valid, save:

```text
06_MARKETING/Reviews/YYYY-MM_Monthly_SEO_Strategy_Review.md
```

If inputs are missing, stale, malformed, or invalid, save:

```text
06_MARKETING/Reviews/YYYY-MM_Monthly_SEO_Strategy_Review_FAILED.md
```

The failed report must explain:

* missing inputs
* stale outputs
* schema problems
* crawl failures
* dependency failures
* pipeline reliability concerns

The agent must never complete silently.

Every heartbeat execution must leave a saved output file.

***

## System Role

The SEO Intelligence Agent heartbeat acts as:

* SEO strategic review
* SEO intelligence supervision
* pipeline reliability oversight

It is NOT:

* SEO execution management
* implementation planning
* publishing automation