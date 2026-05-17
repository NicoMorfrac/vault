# SEO Intelligence Agent Heartbeat

## Purpose

The SEO Intelligence Agent heartbeat is strategic and supervisory.

It does not execute the deterministic pipeline.

The deterministic SEO pipeline already runs automatically through:

```text
run_seo_pipeline.bat
```

The heartbeat exists to:

* review long-term SEO intelligence
* interpret historical changes
* validate pipeline reliability
* detect structural SEO shifts
* identify strategic SEO risks
* recommend future intelligence improvements

The heartbeat is not an operational execution workflow.

Operational execution planning belongs to:

```text
SEO_Execution_Agent
```

***

# Schedule

Monthly - First Tuesday - 09:00 Europe/Madrid

***

# Primary Responsibilities

The heartbeat should:

* review historical SEO comparisons
* review topic authority changes
* review content gap evolution
* review entity relationship evolution
* review pipeline health
* detect structural SEO shifts
* identify strategic SEO opportunities
* identify intelligence-layer weaknesses

The heartbeat should not:

* generate implementation queues
* generate metadata tasks
* generate link insertion tasks
* publish content
* deploy website changes

***

# Inputs

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

# Monthly Review Objectives

## 1. Authority Growth Review

Determine:

* which topics gained authority
* which topics remain weak
* which entities gained visibility
* which commercial topics remain unsupported

## 2. Structural SEO Review

Identify:

* recurring structural failures
* persistent template weaknesses
* unresolved discoverability bottlenecks
* unstable crawl behavior
* semantic fragmentation

## 3. Commercial Visibility Review

Evaluate:

* high-value product visibility
* commercial topic growth
* CTR trend direction
* non-branded discoverability
* engineering authority positioning

## 4. Pipeline Reliability Review

Review:

* stale outputs
* schema consistency
* crawl stability
* script reliability
* dependency failures
* maintenance complexity

## 5. Strategic Direction Review

Recommend:

* next-month SEO priorities
* future analysis layers
* future intelligence improvements
* automation opportunities
* reporting improvements

***

# Required Output

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

# Output Rules

Outputs must:

* remain evidence-based
* prioritize leverage over traffic volume
* focus on commercial relevance
* support engineering authority
* separate intelligence from execution
* remain concise and strategic

Do not:

* generate operational task queues
* create implementation plans
* repeat deterministic tables
* recommend generic SEO tactics
* overreact to short-term volatility

***

# System Role

The SEO Intelligence Agent heartbeat acts as:

```text
SEO strategic review and intelligence supervision
```

not:

```text
SEO execution management
```

# Reporting Requirement

Every heartbeat run must produce a saved markdown report.

If inputs are valid, save:

06\_MARKETING/Reviews/YYYY-MM\_Monthly\_SEO\_Strategy\_Review.md

If inputs are missing or invalid, save:

06\_MARKETING/Reviews/YYYY-MM\_Monthly\_SEO\_Strategy\_Review\_FAILED.md

The agent must never complete silently.# Reporting Requirement