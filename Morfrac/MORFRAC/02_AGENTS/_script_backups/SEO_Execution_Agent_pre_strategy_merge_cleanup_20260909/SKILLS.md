# SEO Execution Agent Skills

## Skill 1 - Metadata Drafting

Convert metadata recommendations and Search Console opportunities into page-level title and meta description drafts.

Use inputs from:

Metadata_Recommendations
Merged_Analysis
Executive_Reviews
Topic_Authority_Map

Required output per page:

* URL
* current title if available
* current meta description if available
* suggested title
* suggested meta description
* target topic
* target intent
* reason
* priority

Rules:

* Titles should normally be 45-65 characters.
* Meta descriptions should normally be 120-160 characters.
* Avoid keyword stuffing.
* Avoid fake claims.
* Match commercial intent.
* Keep MORFRAC brand tone direct and technical.

---

## Skill 2 - Internal Link Task Generation

Convert contextual link recommendations into implementation-ready link tasks.

Use inputs from:

Contextual_Links
Internal_Linking
Entity_Relationship_Map
Topic_Authority_Map

Required output per task:

* source URL
* target URL
* suggested anchor text
* suggested page section if known
* reason
* topic/entity relationship
* priority
* review status

Rules:

* Prioritize links from authority content to commercial pages.
* Prioritize links from pillar pages to product/category pages.
* Avoid footer spam.
* Avoid exact-match overuse.
* Avoid EN/ES mixed-language linking unless intentional.
* Avoid linking duplicate product route variants.

---

## Skill 3 - Content Brief Generation

Create SEO content briefs from content gaps, topic authority weaknesses, and entity opportunities.

Use inputs from:


Content_Gap_Analysis
Topic_Authority_Map
Entity_Relationship_Map
Semantic_Clusters


Required output per brief:

* content title
* target topic
* target entity
* commercial page to support
* user/search intent
* recommended structure
* internal links to include
* products/categories to mention
* evidence source
* priority

Rules:

* Do not write full articles unless requested.
* Do not generate generic SEO filler.
* Every brief must support a commercial or authority objective.
* Technical guides should connect back to relevant MORFRAC products.
* Content should reflect engineering credibility.

---

## Skill 4 - Pillar Page Planning

Create page structures for missing or weak pillar pages.

Use inputs from:

Content_Gap_Analysis
Topic_Authority_Map
Entity_Relationship_Map

Required output:

* proposed pillar page title
* target product family
* target commercial intent
* supporting entities
* target internal links
* recommended sections
* product/category links
* content gaps addressed
* implementation priority

Rules:

* Pillar pages must consolidate and clarify topics.
* Do not create pillar pages for topics without commercial value.
* Do not duplicate existing category pages unless the recommendation is to improve them.

---

## Skill 5 - Semantic Consolidation Planning

Convert cannibalization and overlap findings into reviewable decisions.

Use inputs from:

Semantic_Clusters
Semantic_Cannibalization
Topic_Authority_Map

Required output:

* overlapping pages
* similarity score
* overlap type
* recommended action
* reason
* review status

Allowed actions:

Differentiate
Consolidate
Canonicalize
Noindex
Keep Separate
Manual Review

Rules:

* Do not recommend deletion without strong evidence.
* SKU variants are not automatically cannibalization.
* EN/ES equivalents are not automatically cannibalization.
* Product variants may need differentiation, not consolidation.

---

## Skill 6 - Execution Queue Building

Combine metadata, internal links, briefs, and pillar tasks into one prioritized execution queue.

Required columns:

* task_id
* task_type
* topic
* target_url
* priority
* effort
* impact
* reason
* evidence_source
* owner
* status

Priority scale:

P1 - High impact / low risk
P2 - High impact / medium effort
P3 - Medium impact
P4 - Low priority / monitor

Effort scale:

Low
Medium
High

Status scale:

Draft
Needs Review
Approved
Implemented
Skipped

---

## Skill 7 - Executive Summary for Action

Summarize what should be done next from the execution queue.

Required output:

* top 5 actions
* why they matter
* expected SEO benefit
* dependencies
* risks
* next review point

Rules:

* Keep executive summaries short.
* Focus on decisions and actions.
* Do not dump raw tables unless requested.

---

## Skill 8 - Entity Opportunity Expansion

Convert entity relationship opportunities into authority and commercial execution tasks.

Use inputs from:

Entity_Relationship_Map
Topic_Authority_Map
Content_Gap_Analysis

Required output:

* entity
* entity type
* authority weakness
* commercial opportunity
* proposed supporting content
* suggested internal links
* suggested pillar relationships
* implementation priority

Rules:

* Prioritize entities connected to product families.
* Prioritize entities with impressions but weak authority support.
* Use entity relationships to strengthen semantic structure.
* Avoid isolated pages without internal routing.

---

## Skill 9 - Authority Support Mapping

Map authority-content opportunities toward commercial pages.

Use inputs from:

Topic_Authority_Map
Entity_Relationship_Map
Contextual_Links
Semantic_Clusters

Required output:

* authority page target
* supported commercial page
* target topic
* suggested supporting entities
* internal links required
* SEO purpose
* implementation priority

Rules:

* Authority pages must support commercial discovery.
* Avoid content disconnected from MORFRAC products/services.
* Prioritize high-commercial / low-authority topics.
* Build topic ecosystems, not isolated blog posts.

---

## Skill 10 - SEO Risk Review

Identify risky execution actions before implementation.

Required review areas:

* over-optimization
* duplicate intent
* weak content
* excessive exact-match anchors
* multilingual conflicts
* category duplication
* thin AI-generated pages
* weak commercial alignment

Required output:

* risk detected
* affected pages/topics
* severity
* recommended mitigation
* review requirement

Rules:

* Conservative SEO execution is preferred over aggressive automation.
* Human review is mandatory before destructive or structural actions.
* Avoid scaling low-quality SEO pages.


