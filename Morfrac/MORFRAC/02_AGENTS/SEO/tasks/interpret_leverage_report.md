---
type: generated_report
source_agent: MORFRAC
created: 2026-05-17
related_findings: []
related_concepts: []
related_projects:
  - Search Console
related_reports: []
---

# Interpret SEO Leverage Report

## Task

Interpret the latest SEO leverage intelligence reports for MORFRAC.

This is not a generic SEO audit.

This task identifies:

- highest commercial SEO leverage
- fastest search capture opportunities
- authority-building opportunities
- non-branded discovery opportunities
- template-level weaknesses
- metadata priority signals
- internal linking intelligence signals
- multilingual SEO opportunities
- commercial intent mismatches
- content and authority gaps

Operational implementation tasks belong to SEO_Execution_Agent.

---

# Required Inputs

Read and interpret the latest available files from:

## Leverage Reports

```text
06_MARKETING/SEO_Agent/Leverage_Reports/
```

File pattern:

```text
*_seo_query_page_crawl_leverage_opportunities.md
*_seo_query_page_crawl_leverage_opportunities.csv
```

## Crawl Audits

```text
06_MARKETING/SEO_Agent/Audits/
```

File pattern:

```text
*_seo_audit.md
```

## Search Console Analysis

```text
06_MARKETING/SEO/Query_Analysis/
```

File pattern:

```text
*_SEO_Query_Analysis.md
```

## Optional Strategic Inputs

```text
06_MARKETING/SEO_Agent/Topic_Authority_Map/
06_MARKETING/SEO_Agent/Content_Gap_Analysis/
06_MARKETING/SEO_Agent/Entity_Relationship_Map/
06_MARKETING/SEO_Agent/Pipeline_Health/
```

---

# Analysis Rules

Focus on:

- commercial leverage
- high-intent search visibility
- authority positioning
- discoverability
- CTR capture
- ranking improvement potential
- template-level scale
- strategic search capture

Avoid:

- vanity traffic
- generic SEO filler
- low-value blog spam recommendations
- generic add-more-keywords advice
- unsupported keyword-volume claims

---

# Required Output Structure

## Executive Summary

Summarize:

- strongest SEO opportunities
- biggest weaknesses
- highest-leverage fixes
- most commercially valuable query clusters

## Highest Leverage Pages

Identify:

- highest-priority pages
- why they matter
- expected strategic impact
- likely root causes

## Query Cluster Opportunities

Group related queries into semantic opportunities.

Example clusters:

- dogbone
- mloop
- shackle
- padeye
- powerfurl
- morfblock

For each cluster explain:

- search intent
- current positioning
- weaknesses
- strategic opportunity

## Metadata Priority Signals

Identify:

- pages likely needing title improvements
- pages likely needing meta description improvements
- pages with weak SERP capture

Explain likely CTR problems.

Do not produce final implementation metadata drafts here. That belongs to SEO_Execution_Agent.

## Technical SEO Priorities

Focus only on issues with real leverage.

Examples:

- multiple H1
- missing meta descriptions
- weak internal linking
- crawl discoverability gaps
- template-level metadata weaknesses

Do not produce generic audits.

## Commercial Opportunity Analysis

Identify:

- queries indicating buying intent
- queries indicating engineering authority
- multilingual opportunities
- market-expansion opportunities

## Recommended Intelligence Follow-Up

Recommend:

- analysis improvements
- pipeline improvements
- strategic focus areas
- topics requiring execution-agent review

Do not create operational execution queues in this task.

---

# Important Interpretation Rule

The leverage score is not a quality score.

It is a leverage and opportunity score.

Higher scores mean:

- existing visibility
- weak CTR capture
- ranking potential
- commercial relevance
- authority opportunity

The goal is commercial SEO intelligence, not generic SEO reporting.

## Related Links

### Projects
- [[Search Console]]
