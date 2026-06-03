# ============================================================
# MORFRAC SEO EXECUTIVE REVIEW
# Deterministic executive intelligence synthesis
# ============================================================

from pathlib import Path
import sys
from datetime import datetime
import re
import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_executive_review"
SOURCE_AGENT = "SEO_Agent"

SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

CRAWL_PATH = SEO_AGENT_PATH / "Crawls"
CONTEXTUAL_LINK_PATH = SEO_AGENT_PATH / "Contextual_Links"
IMPLEMENTATION_PATH = SEO_AGENT_PATH / "Implementation_Plans"
MERGED_PATH = SEO_AGENT_PATH / "Merged_Analysis"
SEMANTIC_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
CONTENT_GAP_PATH = SEO_AGENT_PATH / "Content_Gap_Analysis"
TOPIC_AUTHORITY_PATH = SEO_AGENT_PATH / "Topic_Authority_Map"

OUTPUT_PATH = SEO_AGENT_PATH / "Executive_Reviews"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

TODAY = datetime.today().strftime("%Y-%m-%d")

# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    if not files:
        return None

    dated = [
        f for f in files
        if re.match(r"^\d{4}-\d{2}-\d{2}_", f.name)
    ]

    candidates = dated if dated else files

    return max(candidates, key=lambda f: f.stat().st_mtime)


def safe_read_csv(path):
    if path and path.exists():
        return pd.read_csv(path).fillna("")
    return pd.DataFrame()


def to_numeric(df, column):
    if df.empty or column not in df.columns:
        return pd.Series([0] * len(df))

    return pd.to_numeric(
        df[column],
        errors="coerce"
    ).fillna(0)


def count_df(df):
    return 0 if df.empty else len(df)


def sum_col(df, column):
    if df.empty or column not in df.columns:
        return 0

    return float(to_numeric(df, column).sum())


def avg_col(df, column):
    if df.empty or column not in df.columns:
        return 0

    series = to_numeric(df, column)

    if len(series) == 0:
        return 0

    return round(float(series.mean()), 2)


def md_escape(value):
    text = str(value)
    text = text.replace("\n", " ")
    text = text.replace("|", "\\|")
    return text


def table(df, columns=None, limit=15, empty="No data available."):
    if df.empty:
        return empty

    if columns:
        columns = [c for c in columns if c in df.columns]

        if not columns:
            return empty

        df = df[columns]

    df = df.head(limit)

    headers = [md_escape(c) for c in df.columns]

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for _, row in df.iterrows():
        values = [md_escape(row[c]) for c in df.columns]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


def top_issue_table(crawl_df):
    if crawl_df.empty or "issues" not in crawl_df.columns:
        return pd.DataFrame(columns=["issue", "count"])

    counts = {}

    for value in crawl_df["issues"]:
        if not value:
            continue

        for issue in str(value).split("; "):
            issue = issue.strip()

            if issue:
                counts[issue] = counts.get(issue, 0) + 1

    rows = [
        {"issue": issue, "count": count}
        for issue, count in counts.items()
    ]

    if not rows:
        return pd.DataFrame(columns=["issue", "count"])

    return (
        pd.DataFrame(rows)
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )


def source_line(label, path):
    if path:
        return f"- {label}: `{path}`"
    return f"- {label}: `Not available`"


def action_list(items):
    if not items:
        return "- No immediate action required."

    return "\n".join([f"- {item}" for item in items])


# ============================================================

def main():
    # LOAD LATEST FILES
    # ============================================================

    print("Loading executive SEO datasets...")

    crawl_file = latest_file(CRAWL_PATH, "*_site_crawl.csv")
    contextual_link_file = latest_file(
        CONTEXTUAL_LINK_PATH,
        "*_contextual_link_recommendations_filtered.csv"
    )
    implementation_file = latest_file(
        IMPLEMENTATION_PATH,
        "*_seo_link_implementation_plan.csv"
    )
    merge_file = latest_file(MERGED_PATH, "*_search_console_merge.csv")
    semantic_clusters_file = latest_file(
        SEMANTIC_PATH,
        "*_semantic_clusters.csv"
    )
    semantic_pages_file = latest_file(
        SEMANTIC_PATH,
        "*_semantic_cluster_pages.csv"
    )
    cannibalization_file = latest_file(
        SEMANTIC_PATH,
        "*_semantic_cannibalization.csv"
    )
    orphan_topics_file = latest_file(
        SEMANTIC_PATH,
        "*_semantic_orphan_topics.csv"
    )
    content_gap_file = latest_file(
        CONTENT_GAP_PATH,
        "*_content_gap_analysis.csv"
    )
    authority_gap_file = latest_file(
        CONTENT_GAP_PATH,
        "*_authority_gap_analysis.csv"
    )
    pillar_gap_file = latest_file(
        CONTENT_GAP_PATH,
        "*_missing_pillar_pages.csv"
    )
    topic_authority_file = latest_file(
        TOPIC_AUTHORITY_PATH,
        "*_topic_authority_map.csv"
    )
    high_commercial_file = latest_file(
        TOPIC_AUTHORITY_PATH,
        "*_high_commercial_low_authority.csv"
    )
    topic_risk_file = latest_file(
        TOPIC_AUTHORITY_PATH,
        "*_topic_risk_topics.csv"
    )
    core_strength_file = latest_file(
        TOPIC_AUTHORITY_PATH,
        "*_core_topic_strengths.csv"
    )

    # ============================================================
    # READ DATA
    # ============================================================

    crawl_df = safe_read_csv(crawl_file)
    contextual_link_df = safe_read_csv(contextual_link_file)
    implementation_df = safe_read_csv(implementation_file)
    merge_df = safe_read_csv(merge_file)
    semantic_clusters_df = safe_read_csv(semantic_clusters_file)
    semantic_pages_df = safe_read_csv(semantic_pages_file)
    cannibalization_df = safe_read_csv(cannibalization_file)
    orphan_topics_df = safe_read_csv(orphan_topics_file)
    content_gap_df = safe_read_csv(content_gap_file)
    authority_gap_df = safe_read_csv(authority_gap_file)
    pillar_gap_df = safe_read_csv(pillar_gap_file)
    topic_authority_df = safe_read_csv(topic_authority_file)
    high_commercial_df = safe_read_csv(high_commercial_file)
    topic_risk_df = safe_read_csv(topic_risk_file)
    core_strength_df = safe_read_csv(core_strength_file)

    if crawl_df.empty:
        raise FileNotFoundError("No crawl data available for executive review.")

    # ============================================================
    # BASIC METRICS
    # ============================================================

    print("Calculating executive metrics...")

    total_pages = len(crawl_df)

    indexable_pages = int(
        to_numeric(crawl_df, "indexable").sum()
    ) if "indexable" in crawl_df.columns else 0

    high_priority_pages = len(
        crawl_df[
            crawl_df["business_priority"].astype(str).str.lower() == "high"
        ]
    ) if "business_priority" in crawl_df.columns else 0

    pages_with_issues = len(
        crawl_df[
            to_numeric(crawl_df, "issue_count") > 0
        ]
    ) if "issue_count" in crawl_df.columns else 0

    avg_word_count = int(
        avg_col(crawl_df, "word_count")
    )

    issue_df = top_issue_table(crawl_df)

    total_impressions = int(sum_col(merge_df, "impressions"))
    total_clicks = int(sum_col(merge_df, "clicks"))

    semantic_cluster_count = count_df(semantic_clusters_df)
    semantic_page_count = count_df(semantic_pages_df)
    cannibalization_pair_count = count_df(cannibalization_df)
    orphan_topic_count = count_df(orphan_topics_df)

    content_gaps_detected = count_df(content_gap_df)
    authority_gaps_detected = count_df(authority_gap_df)
    pillar_gaps_detected = count_df(pillar_gap_df)

    topic_count = count_df(topic_authority_df)
    high_commercial_low_authority_topics = count_df(high_commercial_df)
    at_risk_topics = count_df(topic_risk_df)
    core_strength_topics = count_df(core_strength_df)

    average_authority_score = avg_col(
        topic_authority_df,
        "topic_authority_score"
    )

    contextual_link_recommendations = count_df(contextual_link_df)
    implementation_ready_links = count_df(implementation_df)

    # ============================================================
    # EXECUTIVE STATUS
    # ============================================================

    risk_score = 0

    if pages_with_issues > total_pages * 0.5:
        risk_score += 20

    if cannibalization_pair_count > 50:
        risk_score += 20
    elif cannibalization_pair_count > 10:
        risk_score += 10

    if content_gaps_detected > 5:
        risk_score += 20
    elif content_gaps_detected > 0:
        risk_score += 10

    if high_commercial_low_authority_topics > 0:
        risk_score += 20

    if average_authority_score < 35:
        risk_score += 20
    elif average_authority_score < 50:
        risk_score += 10

    if risk_score >= 70:
        seo_health = "HIGH RISK"
    elif risk_score >= 45:
        seo_health = "NEEDS ATTENTION"
    elif risk_score >= 20:
        seo_health = "MODERATE"
    else:
        seo_health = "STABLE"

    # ============================================================
    # STRATEGIC OBSERVATIONS
    # ============================================================

    observations = []

    if pages_with_issues > total_pages * 0.5:
        observations.append(
            "More than half of crawled pages still contain SEO issues. Fixes should be prioritized by commercial value, not page count."
        )

    if high_commercial_low_authority_topics > 0:
        observations.append(
            "There are commercially important topics with insufficient authority support. These are the strongest strategic growth candidates."
        )

    if content_gaps_detected > 0:
        observations.append(
            "Content gaps exist across semantic clusters. Product-heavy clusters need technical guides, comparison pages, or stronger pillar pages."
        )

    if cannibalization_pair_count > 0:
        observations.append(
            "Semantic overlap exists between pages. Review whether these are true cannibalization cases, SKU variants, or acceptable multilingual/category duplicates."
        )

    if average_authority_score < 45:
        observations.append(
            "Average topic authority is weak. The site has product depth but not enough structured authority around product families."
        )

    if contextual_link_recommendations > 0:
        observations.append(
            "Internal linking opportunities are available and should be used to route authority toward commercial pages."
        )

    if not observations:
        observations.append(
            "No major structural SEO risks were detected in the latest pipeline output."
        )

    # ============================================================
    # ACTIONS
    # ============================================================

    immediate_actions = []

    if high_commercial_low_authority_topics > 0:
        immediate_actions.append(
            "Prioritize high-commercial / low-authority topics for new technical authority pages and stronger commercial pillar routing."
        )

    if pillar_gaps_detected > 0:
        immediate_actions.append(
            "Create or improve pillar/category landing pages for product-heavy clusters without central commercial support."
        )

    if content_gaps_detected > 0:
        immediate_actions.append(
            "Convert the highest gap-score rows into specific content briefs."
        )

    if cannibalization_pair_count > 0:
        immediate_actions.append(
            "Review the top cannibalization pairs and decide whether to consolidate, differentiate, canonicalize, or ignore as SKU variants."
        )

    if pages_with_issues > 0:
        immediate_actions.append(
            "Fix metadata, H1, thin-content, and image-alt issues on high-priority commercial pages first."
        )

    if contextual_link_recommendations > 0:
        immediate_actions.append(
            "Implement a shortlist of contextual internal links toward weak commercial pages."
        )

    mid_term_actions = [
        "Build topic ecosystems around product families: landing page, category support, technical guide, comparison page, and product links.",
        "Use topic authority score as a strategic KPI, not just crawl issue count.",
        "Refactor repeated SEO scripts into shared helpers once the pipeline stabilizes.",
        "Add competitor topic-gap comparison only after MORFRAC's internal topic map is stable.",
    ]

    # ============================================================
    # PRIORITY TABLES
    # ============================================================

    priority_pages = pd.DataFrame()

    if "commercial_seo_score" in crawl_df.columns:
        priority_pages = (
            crawl_df[
                crawl_df["business_priority"].astype(str).str.lower() == "high"
            ]
            .sort_values("commercial_seo_score", ascending=False)
            .head(20)
        )

    if not topic_authority_df.empty and "topic_authority_score" in topic_authority_df.columns:
        topic_authority_df["topic_authority_score"] = to_numeric(
            topic_authority_df,
            "topic_authority_score"
        )

        topic_authority_df = topic_authority_df.sort_values(
            "topic_authority_score",
            ascending=True
        )

    if not content_gap_df.empty and "gap_score" in content_gap_df.columns:
        content_gap_df["gap_score"] = to_numeric(
            content_gap_df,
            "gap_score"
        )

        content_gap_df = content_gap_df.sort_values(
            "gap_score",
            ascending=False
        )

    if not cannibalization_df.empty and "similarity_score" in cannibalization_df.columns:
        cannibalization_df["similarity_score"] = to_numeric(
            cannibalization_df,
            "similarity_score"
        )

        cannibalization_df = cannibalization_df.sort_values(
            "similarity_score",
            ascending=False
        )

    # ============================================================
    # MARKDOWN REPORT
    # ============================================================

    print("Generating executive review...")

    output_file = OUTPUT_PATH / f"{TODAY}_SEO_Executive_Review.md"
    stable_output_file = OUTPUT_PATH / "SEO_Executive_Review.md"

    md = f"""# MORFRAC SEO Executive Review

    ## Generated

    {TODAY}

    ---

    # Executive SEO Health Summary

    Overall SEO status:

    **{seo_health}**

    Risk score:

    **{risk_score}/100**

    ## Core Metrics

    | Metric | Value |
    |---|---:|
    | Total pages crawled | {total_pages} |
    | Indexable pages | {indexable_pages} |
    | High-priority commercial pages | {high_priority_pages} |
    | Pages with crawl issues | {pages_with_issues} |
    | Average word count | {avg_word_count} |
    | Search Console impressions captured | {total_impressions} |
    | Search Console clicks captured | {total_clicks} |
    | Semantic clusters | {semantic_cluster_count} |
    | Semantic pages mapped | {semantic_page_count} |
    | Cannibalization / overlap pairs | {cannibalization_pair_count} |
    | Orphan topics | {orphan_topic_count} |
    | Content gaps | {content_gaps_detected} |
    | Authority gaps | {authority_gaps_detected} |
    | Missing pillar-page gaps | {pillar_gaps_detected} |
    | Topics scored | {topic_count} |
    | Average topic authority score | {average_authority_score} |
    | High commercial / low authority topics | {high_commercial_low_authority_topics} |
    | At-risk topics | {at_risk_topics} |
    | Core topic strengths | {core_strength_topics} |
    | Contextual link recommendations | {contextual_link_recommendations} |
    | Implementation-ready links | {implementation_ready_links} |

    ---

    # Executive Interpretation

    {action_list(observations)}

    ---

    # Commercial Opportunity Summary

    The strongest commercial opportunities are topics or pages where MORFRAC already has product depth, search visibility, or commercial relevance, but insufficient authority structure.

    ## High Commercial / Low Authority Topics

    {table(
        high_commercial_df,
        columns=[
            "dominant_label",
            "topic_authority_score",
            "authority_tier",
            "strategic_status",
            "page_count",
            "product_pages",
            "landing_pages",
            "authority_content_pages",
            "total_impressions",
            "gap_type",
        ],
        limit=15,
        empty="No high-commercial / low-authority topics detected."
    )}

    ---

    # Topic Authority Summary

    ## Weakest Topic Authority Areas

    {table(
        topic_authority_df,
        columns=[
            "dominant_label",
            "topic_authority_score",
            "authority_tier",
            "strategic_status",
            "page_count",
            "product_pages",
            "category_pages",
            "landing_pages",
            "authority_content_pages",
            "cluster_health",
            "gap_type",
        ],
        limit=15,
        empty="No topic authority map available."
    )}

    ## Core Topic Strengths

    {table(
        core_strength_df,
        columns=[
            "dominant_label",
            "topic_authority_score",
            "authority_tier",
            "strategic_status",
            "page_count",
            "product_pages",
            "landing_pages",
            "authority_content_pages",
        ],
        limit=15,
        empty="No core topic strengths detected."
    )}

    ---

    # Content Gap Priorities

    {table(
        content_gap_df,
        columns=[
            "dominant_label",
            "gap_type",
            "gap_score",
            "page_count",
            "product_pages",
            "category_pages",
            "landing_pages",
            "authority_content_pages",
            "total_impressions",
            "recommended_action",
        ],
        limit=20,
        empty="No content gaps detected."
    )}

    ---

    # Semantic Cannibalization / Overlap Risks

    {table(
        cannibalization_df,
        columns=[
            "url_a",
            "role_a",
            "label_a",
            "url_b",
            "role_b",
            "label_b",
            "similarity_score",
            "risk_type",
        ],
        limit=20,
        empty="No semantic cannibalization or overlap risks detected."
    )}

    ---

    # Structural SEO Risks

    ## Top Crawl Issues

    {table(
        issue_df,
        columns=["issue", "count"],
        limit=15,
        empty="No crawl issues detected."
    )}

    ## Highest Priority Commercial Pages

    {table(
        priority_pages,
        columns=[
            "url",
            "commercial_seo_score",
            "issue_count",
            "issues",
        ],
        limit=20,
        empty="No priority commercial pages available."
    )}

    ---

    # Immediate Actions

    {action_list(immediate_actions)}

    ---

    # Strategic Mid-Term Actions

    {action_list(mid_term_actions)}

    ---

    # Source Files

    {source_line("Crawl", crawl_file)}
    {source_line("Search Console Merge", merge_file)}
    {source_line("Semantic Clusters", semantic_clusters_file)}
    {source_line("Semantic Pages", semantic_pages_file)}
    {source_line("Cannibalization", cannibalization_file)}
    {source_line("Orphan Topics", orphan_topics_file)}
    {source_line("Content Gaps", content_gap_file)}
    {source_line("Authority Gaps", authority_gap_file)}
    {source_line("Pillar Gaps", pillar_gap_file)}
    {source_line("Topic Authority Map", topic_authority_file)}
    {source_line("High Commercial / Low Authority", high_commercial_file)}
    {source_line("Topic Risks", topic_risk_file)}
    {source_line("Core Strengths", core_strength_file)}
    {source_line("Contextual Links", contextual_link_file)}
    {source_line("Implementation Plan", implementation_file)}

    ---

    # Notes

    This report is deterministic. It does not use AI generation.

    It synthesizes current outputs from the MORFRAC SEO pipeline into an executive-level view of:

    - crawl health
    - commercial SEO opportunity
    - semantic structure
    - content gaps
    - topic authority
    - internal linking opportunity
    - implementation priorities
    """

    write_markdown_report(
        output_file,
        md,
        report_type=REPORT_TYPE,
        source_agent=SOURCE_AGENT,
    )
    write_markdown_report(
        stable_output_file,
        md,
        report_type=REPORT_TYPE,
        source_agent=SOURCE_AGENT,
    )

    print("")
    print("================================================")
    print("SEO EXECUTIVE REVIEW COMPLETE")
    print("================================================")
    print(f"Output file: {output_file}")
    print(f"Stable file: {stable_output_file}")
    print("================================================")


if __name__ == "__main__":
    main()
