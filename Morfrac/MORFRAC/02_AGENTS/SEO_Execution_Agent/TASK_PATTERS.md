# SEO Execution Agent Task Patterns

## Task Pattern 1 - Weekly SEO Execution Plan

### Trigger

Use when the user asks:

What should we do next?
Create SEO execution tasks.
Turn the SEO report into actions.
Prepare this week's SEO work.

### Inputs

Read latest files from:

Executive_Reviews
Topic_Authority_Map
Content_Gap_Analysis
Entity_Relationship_Map
Contextual_Links

### Process

1. Identify high commercial / low authority topics.
2. Identify highest content gaps.
3. Identify strongest internal link tasks.
4. Identify metadata tasks for commercial pages.
5. Select only realistic implementation actions.
6. Build one prioritized weekly queue.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_SEO_Execution_Plan.md

Required sections:

Executive Summary
Top Priorities
Metadata Tasks
Internal Link Tasks
Content Briefs
Pillar Page Tasks
Risks / Review Notes
Execution Queue

---

## Task Pattern 2 - Metadata Execution Pack

### Trigger

Use when the user asks:

Create metadata tasks.
Fix metadata.
Generate titles and descriptions.

### Inputs

Use:

Merged_Analysis
Metadata_Recommendations
Executive_Reviews
Topic_Authority_Map

### Process

1. Select high-priority commercial pages.
2. Review current metadata if available.
3. Draft improved title and description.
4. Assign intent and priority.
5. Flag pages needing manual product verification.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Metadata_Tasks.md

Rules:

* Do not publish automatically.
* Avoid duplicate titles.
* Preserve technical accuracy.
* Match search intent.

---

## Task Pattern 3 - Internal Link Implementation Pack

### Trigger

Use when the user asks:

Create internal link tasks.
Which links should I add?
Prepare link implementation list.

### Inputs

Use:

Contextual_Links
Entity_Relationship_Map
Topic_Authority_Map
Semantic_Clusters

### Process

1. Select links from authority pages to commercial pages.
2. Remove duplicate, outlet, system, or mixed-language links.
3. Prioritize high commercial / low authority targets.
4. Suggest natural anchor text.
5. Create implementation-ready task list.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Internal_Link_Tasks.md

Required output fields:

Source URL
Target URL
Anchor Suggestion
Reason
Priority
Review Status

---

## Task Pattern 4 - Content Brief Pack

### Trigger

Use when the user asks:

Create content briefs.
What articles/pages should we create?
Turn content gaps into briefs.

### Inputs

Use:

Content_Gap_Analysis
Topic_Authority_Map
Entity_Relationship_Map
Semantic_Clusters

### Process

1. Select highest gap score topics.
2. Separate technical authority briefs from commercial pillar briefs.
3. Define target intent.
4. Define linked commercial pages.
5. Create structured brief, not full article.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Content_Briefs.md

Required brief structure:

Brief Title
Target Topic
Target Entity
SEO Purpose
Commercial Page Supported
Recommended H1
Recommended Sections
Internal Links
Products/Categories To Mention
Evidence Source
Priority
Review Notes

---

## Task Pattern 5 - Pillar Page Plan

### Trigger

Use when the user asks:

Plan a pillar page.
Which pillar pages are missing?
Create pillar page structure.

### Inputs

Use:

Content_Gap_Analysis
Topic_Authority_Map
Entity_Relationship_Map

### Process

1. Identify product-heavy clusters without landing/pillar support.
2. Check whether a category page already exists.
3. Decide whether to improve an existing page or create a new page.
4. Draft page structure.
5. Define internal links and commercial targets.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Pillar_Page_Tasks.md

Required sections:

Target Topic
Commercial Objective
Supporting Products
Suggested H1
Suggested Sections
Suggested Internal Links
SEO Purpose
Priority
Review Notes

---

## Task Pattern 6 - Cannibalization Review Pack

### Trigger

Use when the user asks:

Review cannibalization.
Which pages overlap?
What should we consolidate?

### Inputs

Use:

Semantic_Clusters
Semantic_Cannibalization
Topic_Authority_Map

### Process

1. Separate true cannibalization from SKU similarity.
2. Separate EN/ES equivalents from duplicate intent.
3. Identify pages that need differentiation.
4. Recommend action only with clear reason.
5. Flag uncertain cases for manual review.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Cannibalization_Review.md

Allowed actions:

Differentiate
Consolidate
Canonicalize
Noindex
Keep Separate
Manual Review

---

## Task Pattern 7 - Entity Opportunity Execution Pack

### Trigger

Use when the user asks:

What entities should we expand?
Create entity execution tasks.
Find commercial authority gaps.

### Inputs

Use:

Entity_Relationship_Map
Topic_Authority_Map
Content_Gap_Analysis
Contextual_Links

### Process

1. Identify entities with commercial visibility but weak authority support.
2. Identify missing supporting content.
3. Identify missing internal links.
4. Identify missing pillar relationships.
5. Create execution-ready recommendations.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Entity_Execution_Plan.md

Required fields:

Entity
Entity Type
Opportunity Type
Suggested Action
Commercial Support Target
Suggested Content
Suggested Internal Links
Priority
Review Status

---

## Task Pattern 8 - Monthly SEO Execution Review

### Trigger

Use when the user asks:

Review progress.
What changed this month?
What should we prioritize next month?

### Inputs

Use:

Executive_Reviews
Historical_Comparisons
Pipeline_Health
SEO_Execution_Queue

### Process

1. Compare previous priorities with current outputs.
2. Identify completed, repeated, and unresolved tasks.
3. Check whether topic authority improved.
4. Check whether content gaps reduced.
5. Produce next-month priorities.

### Output

Save:

06_MARKETING\SEO_Execution_Queue\YYYY-MM-DD_Monthly_SEO_Execution_Review.md

Required sections:

Progress Summary
Completed Actions
Pending Actions
Recurring Problems
Authority Improvements
Remaining Gaps
Next Priorities
Risks

---

## Global Task Rules

All outputs must be:

* evidence-based
* sourced to current pipeline files
* practical to implement
* reviewable by a human
* commercially prioritized

Never:

* publish automatically
* invent claims
* create fake metrics
* recommend deleting pages without review
* over-optimize anchors
* recommend generic low-value SEO content
* generate thin AI pages


