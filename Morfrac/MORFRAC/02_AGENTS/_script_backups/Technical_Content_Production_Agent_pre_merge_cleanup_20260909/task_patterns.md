# TASK PATTERNS

## Pattern 1 — Generate Technical Authority Guide

### Objective

Generate a technically credible authority-content article from an approved authority opportunity or execution-approved content brief.

### Inputs

* Content\_Briefs.md
* Internal\_Link\_Tasks.md
* Metadata\_Tasks.md
* approved authority opportunities
* approved engineering insights

### Required Actions

* interpret the approved brief
* build logical technical structure
* integrate commercial routing
* reinforce entity relationships
* integrate approved internal links
* maintain engineering credibility
* preserve AI retrieval structure
* preserve technical tone

### Output

Save markdown draft under:

```text
06_MARKETING/SEO_Content_Drafts/
```

Examples:

```text
YYYY-MM-DD_Dogbone_Technical_Guide.md
YYYY-MM-DD_Morfblock_Selection_Guide.md
```

### Constraints

Do NOT:

* invent engineering data
* fabricate test results
* create generic SEO filler
* create disconnected educational content
* exaggerate performance claims

***

## Pattern 2 — Generate Engineering Explainer Content

### Objective

Generate engineering-focused explainer content that helps technical buyers understand system-level tradeoffs and integration logic.

### Focus Areas

Examples:

* load-path behavior
* friction management
* textile interfaces
* geometry constraints
* retrofit integration
* material-selection tradeoffs
* system optimization

### Required Actions

* explain engineering reasoning clearly
* preserve technical credibility
* support commercial routing
* reinforce authority entities
* support AI retrieval clarity

### Output Requirements

Content must:

* answer real engineering questions
* support commercial discovery
* remain technically useful
* avoid shallow educational tone

***

## Pattern 3 — Generate Pillar Page Draft

### Objective

Generate a commercial pillar page draft for fragmented product-family ecosystems.

### Required Actions

* explain the product ecosystem
* clarify subfamilies
* support internal authority routing
* route users toward commercial pages
* integrate approved internal links
* reinforce semantic structure
* support AI retrieval discoverability

### Constraints

Do NOT:

* duplicate SKU descriptions
* create shallow category filler
* generate unsupported technical claims
* fragment topical authority

### Example Outputs

```text
YYYY-MM-DD_Powerfurl_Pillar_Page.md
YYYY-MM-DD_Textile_Connection_Systems.md
```

***

## Pattern 4 — Generate Project-Derived Authority Content

### Objective

Generate reusable authority content derived from engineering projects, rigging studies, optimization work, or technical troubleshooting.

### Source Types

* engineering projects
* rigging studies
* retrofit work
* manufacturing lessons
* integration constraints
* friction-management studies
* bearing/load-path analysis
* material-selection studies

### Required Actions

* extract reusable engineering insight
* generalize project-specific lessons
* preserve technical credibility
* support authority building
* reinforce commercial relevance

### Confidentiality Rules

Do NOT expose:

* client-sensitive information
* confidential geometry
* proprietary calculations
* unreleased specifications
* protected engineering documentation

### Example Outputs

```text
YYYY-MM-DD_Furling_Integration_Lessons.md
YYYY-MM-DD_Load_Path_Optimization_Insights.md
```

***

## Pattern 5 — Generate AI-Retrieval-Friendly Content

### Objective

Generate content optimized for discoverability and usefulness within AI-answer systems.

### Prioritize

* concise definitions
* explicit entity relationships
* answer-friendly formatting
* structured reasoning
* engineering tradeoffs
* problem-solution framing
* retrieval-friendly headings

### Target Ecosystems

* ChatGPT
* Claude
* Gemini
* Perplexity
* semantic search systems

### Constraints

Avoid:

* keyword stuffing
* repetitive phrasing
* shallow AI-blog formatting
* disconnected informational content

***

## Pattern 6 — Generate Derivative Distribution Content

### Objective

Generate derivative distribution content from a master authority article.

### Examples

* LinkedIn engineering posts
* FAQ snippets
* AI-answer summaries
* newsletter excerpts
* short authority summaries
* engineering insight posts
* social captions

### Required Actions

* preserve core authority topic
* reinforce the same entity relationships
* preserve commercial routing
* adapt tone to platform format
* support AI retrieval reinforcement

### Constraints

Derivative content must remain connected to the master authority topic.

Do NOT create disconnected standalone filler content.

***

## Pattern 7 — Generate LinkedIn Engineering Post

### Objective

Generate a LinkedIn post derived from a master authority article or engineering insight.

### Required Actions

* simplify technical framing without losing credibility
* highlight a real engineering problem or insight
* provoke professional interest or discussion
* preserve MORFRAC engineering positioning
* route readers toward authority content or commercial pages

### Tone Requirements

LinkedIn content should be:

* concise
* technically credible
* insight-oriented
* discussion-friendly
* commercially subtle

Avoid:

* aggressive sales tone
* clickbait phrasing
* generic motivational language
* shallow marketing copy

### Example Output

```text
YYYY-MM-DD_LinkedIn_Dogbone_Post.md
```

***

## Pattern 8 — Generate FAQ and AI-Answer Snippets

### Objective

Generate concise retrieval-friendly summaries derived from master authority content.

### Required Actions

* answer common engineering questions clearly
* reinforce core entities
* preserve technical accuracy
* support semantic discoverability

### Example Outputs

```text
YYYY-MM-DD_Dogbone_FAQ.md
YYYY-MM-DD_AI_Answer_Summary.md
```

### Constraints

Avoid:

* oversimplification
* fake certainty
* unsupported engineering claims

***

## Pattern 9 — Structured Markdown Validation

### Objective

Validate markdown draft quality before save.

### Validation Checklist

Before saving drafts:

* verify headings exist
* verify logical hierarchy exists
* verify internal links exist
* verify commercial routing exists
* verify tone consistency
* verify markdown formatting
* verify entity consistency
* verify no obvious filler sections
* verify no fabricated technical claims
* verify AI retrieval structure quality

### Failure Handling

If validation fails:

* revise before save
* do not save low-quality filler drafts

The agent must never knowingly save weak authority content.

***

## Pattern 10 — Multi-Format Authority Distribution

### Objective

Transform one approved authority topic into multiple coordinated authority-support outputs.

### Workflow

```text
Approved authority topic
→ Master authority article
→ LinkedIn post
→ FAQ snippets
→ AI-answer summary
→ newsletter excerpt
→ short authority summaries
```

### Goal

Reinforce:

* authority entities
* commercial routing
* AI retrieval visibility
* semantic consistency
* engineering positioning

One authority ecosystem should support multiple discovery surfaces while remaining structurally coherent.

***

## Pattern 11 - Obsidian Metadata Classification

### Objective

Classify every generated Markdown file before saving.

### Report Outputs

Use report metadata for production reviews, QA reports, approval summaries, execution summaries, or internal MORFRAC report notes.

Report outputs must comply with [[00_SYSTEM/OBSIDIAN_REPORT_STANDARD.md]]:

```yaml
---
type:
source_agent: Technical_Content_Production
created:
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---
```

Report outputs must include:

```markdown
## Related Links
```

### Content Assets

Use content-asset metadata for master articles, LinkedIn posts, FAQ snippets, AI-answer summaries, newsletters, social captions, and page drafts:

```yaml
---
type: content_asset
source_agent: Technical_Content_Production
created:
related_projects: []
related_topics: []
---
```

Do not force Business Intel report metadata into content assets.

Do not auto-link generic words such as engineering, retrofit, hardware, serviceability, analysis, marketing, SEO, or project.
