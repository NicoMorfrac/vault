# ============================================================
# MORFRAC SEO EXECUTIVE REVIEW
# Deterministic executive intelligence report
# ============================================================

from pathlib import Path
from datetime import datetime
import re

import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

CRAWL_PATH = SEO_AGENT_PATH / "Crawls"
CONTEXTUAL_LINK_PATH = SEO_AGENT_PATH / "Contextual_Links"
IMPLEMENTATION_PATH = SEO_AGENT_PATH / "Implementation_Plans"
MERGED_PATH = SEO_AGENT_PATH / "Merged_Analysis"
SEMANTIC_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
CONTENT_GAP_PATH = SEO_AGENT_PATH / "Content_Gap_Analysis"
TOPIC_AUTHORITY_PATH = SEO_AGENT_PATH / "Topic_Authority_Map"

OUTPUT_PATH = SEO_AGENT_PATH / "Executive_Reviews"

TODAY = datetime.today().strftime("%Y-%m-%d")


# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    dated_files = [
        f for f in files
        if re.match(r"^\d{4}-\d{2}-\d{2}_", f.name)
    ]

    candidates = dated_files if dated_files else files

    if not candidates:
        return None

    return max(candidates, key=lambda f: f.stat().st_mtime)


def safe_read_csv(path):
    if path and path.exists():
        return pd.read_csv(path).fillna("")
    return pd.DataFrame()


def to_numeric(df, column):
    if column not in df.columns:
        return pd.Series([0] * len(df))
    return pd.to_numeric(df[column], errors="coerce").fillna(0)


def safe_count(df):
    return 0 if df.empty else len(df)


def markdown_cell(value):
    text = str(value)
    text = text.replace("\n", " ").replace("|", "\\|")
    return text


def dataframe_to_markdown(df, columns=None, limit=20, empty_message="No data available."):
    if df.empty:
        return empty_message

    if columns:
        columns = [col for col in columns if col in df.columns]

        if not columns:
            return empty_message

        df = df[columns]

    df = df.head(limit)

    headers = [markdown_cell(col) for col in df.columns]
    rows = []

    for _, row in df.iterrows():
        rows.append([markdown_cell(row[col]) for col in df.columns])

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in rows:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def issue_counts(crawl_df):
    counts = {}

    if crawl_df.empty or "issues" not in crawl_df.columns:
        return counts

    for value in crawl_df["issues"].fillna(""):
        if not value:
            continue

        for issue in str(value).split("; "):
            issue = issue.strip()

            if issue:
                counts[issue] = counts.get(issue, 0) + 1

    return counts


def top_issue_table(crawl_df):
    counts = issue_counts(crawl_df)

    if not counts:
        return pd.DataFrame(columns=["issue", "count"])

    return (
        pd.DataFrame(
            [{"issue": issue, "count": count} for issue, count in counts.items()]
        )
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )


def metric_value(df, column, fallback=0):
    if df.empty or column not in df.columns:
        return fallback
    return to_numeric(df, column).sum()


def average_value(df, column, fallback=0):
    if df.empty or column not in df.columns:
        return fallback
    series = to_numeric(df, column)
    return round(float(series.mean()), 2) if len(series) else fallback


def source_line(label, path):
    return f"- {label}: `{path if path else 'Not available'}`"


def build_immediate_actions(metrics):
    actions = []

    if metrics["high_commercial_low_authority_topics"] > 0:
        actions.append(
            "Prioritize high-commercial / low-authority topics with technical authority pages and stronger pillar-page routing."
        )

    if metrics["content_gaps_detected"] > 0:
        actions.append(
            "Turn the highest scoring content gaps into briefs for technical guides, commercial pillars, or category support pages."
        )

    if metrics["cannibalization_pair_count"] > 0:
        actions.append(
            "Review semantic cannibalization pairs and choose consolidate, differentiate, or canonicalize actions for overlapping pages."
        )

    if metrics["orphan_topic_count"] > 0:
        actions.append(
            "Connect orphan topics into commercial clusters with internal links or retire them if they have no strategic demand."
        )

    if metrics["pages_with_issues"] > 0:
        actions.append(
            "Fix crawl-level technical issues on high-priority commercial and indexable pages first."
        )

    if not actions:
        actions.append(
            "Maintain the current SEO base and monitor topic authority movement after the next crawl."
        )

    return actions


def build_mid_term_actions(metrics):
    actions = [
        "Build topic ecosystems around product families with product pages, category support, commercial landing pages, and technical authority content.",
        "Use topic authority score movement as the primary executive KPI for SEO strategy, not only page-level crawl errors.",
        "Create a recurring review loop between content gaps, contextual links, and topic authority outputs.",
    ]

    if metrics["average_authority_score"] < 45:
        actions.append(
            "Raise average topic authority by strengthening authority content depth and commercial capture paths for weak clusters."
        )

    if metrics["dominant_topics"] == 0:
        actions.append(
            "Select one or two commercially important topics to develop into defensible dominant authority areas."
        )

    if metrics["total_impressions"] > 0 and metrics["total_clicks"] == 0:
        actions.append(
            "Audit high-impression pages for title, meta, intent match, and internal-link support to convert visibility into clicks."
        )

    return actions


# ============================================================
# MAIN
# ============================================================

def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # ============================================================
    # LATEST INPUTS
    # ============================================================

    crawl_file = latest_file(CRAWL_PATH, "*_site_crawl.csv")
    contextual_link_file = latest_file(
        CONTEXTUAL_LINK_PATH,
        "*_contextual_link_recommendations_filtered.csv",
    )
    implementation_file = latest_file(
        IMPLEMENTATION_PATH,
        "*_seo_link_implementation_plan.csv",
    )
    merge_file = latest_file(MERGED_PATH, "*_search_console_merge.csv")
    semantic_clusters_file = latest_file(SEMANTIC_PATH, "*_semantic_clusters.csv")
    semantic_pages_file = latest_file(SEMANTIC_PATH, "*_semantic_cluster_pages.csv")
    cannibalization_file = latest_file(SEMANTIC_PATH, "*_semantic_cannibalization.csv")
    orphan_topics_file = latest_file(SEMANTIC_PATH, "*_semantic_orphan_topics.csv")
    content_gap_file = latest_file(CONTENT_GAP_PATH, "*_content_gap_analysis.csv")
    authority_gap_file = latest_file(CONTENT_GAP_PATH, "*_authority_gap_analysis.csv")
    topic_authority_file = latest_file(TOPIC_AUTHORITY_PATH, "*_topic_authority_map.csv")
    high_commercial_file = latest_file(
        TOPIC_AUTHORITY_PATH,
        "*_high_commercial_low_authority.csv",
    )
    topic_risk_file = latest_file(TOPIC_AUTHORITY_PATH, "*_topic_risk_topics.csv")
    core_strength_file = latest_file(TOPIC_AUTHORITY_PATH, "*_core_topic_strengths.csv")

    # ============================================================
    # LOAD DATA
    # ============================================================

    print("Loading executive SEO datasets...")

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
    topic_authority_df = safe_read_csv(topic_authority_file)
    high_commercial_df = safe_read_csv(high_commercial_file)
    topic_risk_df = safe_read_csv(topic_risk_file)
    core_strength_df = safe_read_csv(core_strength_file)

    # ============================================================
    # EXECUTIVE METRICS
    # ============================================================

    print("Calculating executive SEO metrics...")

    total_pages = safe_count(crawl_df)
    indexable_pages = int(metric_value(crawl_df, "indexable"))
    pages_with_issues = int((to_numeric(crawl_df, "issue_count") > 0).sum()) if not crawl_df.empty else 0
    avg_word_count = int(average_value(crawl_df, "word_count")) if not crawl_df.empty else 0
    contextual_link_recommendations = safe_count(contextual_link_df)
    implementation_links = safe_count(implementation_df)

    total_impressions = int(
        metric_value(merge_df, "impressions")
        or metric_value(topic_authority_df, "total_impressions")
        or metric_value(semantic_clusters_df, "total_impressions")
    )
    total_clicks = int(
        metric_value(merge_df, "clicks")
        or metric_value(topic_authority_df, "total_clicks")
        or metric_value(semantic_clusters_df, "total_clicks")
    )

    semantic_cluster_count = safe_count(semantic_clusters_df)
    cannibalization_pair_count = safe_count(cannibalization_df)
    orphan_topic_count = safe_count(orphan_topics_df)
    content_gaps_detected = safe_count(content_gap_df)
    authority_gaps_detected = safe_count(authority_gap_df)
    high_commercial_low_authority_topics = safe_count(high_commercial_df)

    dominant_topics = 0

    if not topic_authority_df.empty and "authority_tier" in topic_authority_df.columns:
        dominant_topics = int((topic_authority_df["authority_tier"] == "DOMINANT").sum())

    if dominant_topics == 0 and not core_strength_df.empty:
        dominant_topics = safe_count(core_strength_df)

    at_risk_topics = safe_count(topic_risk_df)
    average_authority_score = average_value(topic_authority_df, "topic_authority_score")

    metrics = {
        "total_pages": total_pages,
        "indexable_pages": indexable_pages,
        "pages_with_issues": pages_with_issues,
        "avg_word_count": avg_word_count,
        "contextual_link_recommendations": contextual_link_recommendations,
        "implementation_links": implementation_links,
        "semantic_cluster_count": semantic_cluster_count,
        "cannibalization_pair_count": cannibalization_pair_count,
        "orphan_topic_count": orphan_topic_count,
        "content_gaps_detected": content_gaps_detected,
        "authority_gaps_detected": authority_gaps_detected,
        "high_commercial_low_authority_topics": high_commercial_low_authority_topics,
        "dominant_topics": dominant_topics,
        "at_risk_topics": at_risk_topics,
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "average_authority_score": average_authority_score,
    }

    # ============================================================
    # REPORT DATA SLICES
    # ============================================================

    issue_df = top_issue_table(crawl_df)

    topic_authority_columns = [
        "dominant_label",
        "topic_authority_score",
        "authority_tier",
        "strategic_status",
        "commercial_strength",
        "authority_strength",
        "structural_health",
        "gap_penalty",
        "page_count",
        "product_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "cluster_health",
        "gap_type",
    ]

    high_commercial_columns = topic_authority_columns

    content_gap_columns = [
        "dominant_label",
        "gap_type",
        "gap_score",
        "recommended_action",
        "product_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "cluster_health",
    ]

    cannibalization_columns = [
        "url_a",
        "role_a",
        "label_a",
        "url_b",
        "role_b",
        "label_b",
        "similarity_score",
        "risk_type",
    ]

    structural_risk_columns = [
        "issue",
        "count",
    ]

    # ============================================================
    # STRATEGIC SUMMARIES
    # ============================================================

    health_summary = []

    if average_authority_score < 25:
        health_summary.append(
            "Topic authority is materially weak. The SEO system has visibility assets, but topic ecosystems are not yet structurally strong."
        )
    elif average_authority_score < 45:
        health_summary.append(
            "Topic authority is underdeveloped. Several commercial clusters need authority content, pillar pages, or consolidation."
        )
    elif average_authority_score < 65:
        health_summary.append(
            "Topic authority is moderate. The SEO base is usable, but dominant topic ownership is not yet established."
        )
    else:
        health_summary.append(
            "Topic authority is strong. The main task is defending dominant clusters and improving weaker commercial edges."
        )

    if high_commercial_low_authority_topics > 0:
        health_summary.append(
            f"{high_commercial_low_authority_topics} topics show commercial value without enough authority support."
        )

    if cannibalization_pair_count > 0:
        health_summary.append(
            f"{cannibalization_pair_count} semantic cannibalization pairs require differentiation or consolidation review."
        )

    commercial_summary = []

    if total_impressions or total_clicks:
        commercial_summary.append(
            f"Current merged Search Console footprint shows {total_impressions} impressions and {total_clicks} clicks across analyzed pages."
        )

    if high_commercial_low_authority_topics:
        commercial_summary.append(
            "The primary growth opportunity is not more raw crawling; it is converting commercial clusters into authoritative topic systems."
        )

    if not commercial_summary:
        commercial_summary.append(
            "No Search Console demand data was available in the current merge output. Commercial opportunity is inferred from semantic and product-page structure."
        )

    topic_summary = []
    topic_summary.append(
        f"{semantic_cluster_count} semantic clusters are currently tracked, with an average topic authority score of {average_authority_score}."
    )
    topic_summary.append(
        f"{dominant_topics} dominant/core topics and {at_risk_topics} at-risk topics were identified."
    )

    immediate_actions = build_immediate_actions(metrics)
    mid_term_actions = build_mid_term_actions(metrics)

    # ============================================================
    # BUILD MARKDOWN REPORT
    # ============================================================

    print("Generating executive intelligence report...")

    output_file = OUTPUT_PATH / f"{TODAY}_SEO_Executive_Review.md"
    stable_output_file = OUTPUT_PATH / "SEO_Executive_Review.md"

    source_lines = [
        source_line("Crawl audit", crawl_file),
        source_line("Contextual links", contextual_link_file),
        source_line("Implementation plan", implementation_file),
        source_line("Search Console merge", merge_file),
        source_line("Semantic clusters", semantic_clusters_file),
        source_line("Semantic cluster pages", semantic_pages_file),
        source_line("Semantic cannibalization", cannibalization_file),
        source_line("Semantic orphan topics", orphan_topics_file),
        source_line("Content gap analysis", content_gap_file),
        source_line("Authority gap analysis", authority_gap_file),
        source_line("Topic authority map", topic_authority_file),
        source_line("High commercial / low authority topics", high_commercial_file),
        source_line("Topic risk topics", topic_risk_file),
        source_line("Core topic strengths", core_strength_file),
    ]

    md = f"""# MORFRAC SEO Executive Intelligence Review

## Generated

{TODAY}

---

# Executive SEO Health Summary

{"".join(f"- {item}\n" for item in health_summary)}

## Executive Metrics

| Metric | Value |
|---|---:|
| Crawled pages | {total_pages} |
| Indexable pages | {indexable_pages} |
| Pages with crawl issues | {pages_with_issues} |
| Average word count | {avg_word_count} |
| Contextual link recommendations | {contextual_link_recommendations} |
| Implementation-ready links | {implementation_links} |
| Semantic clusters | {semantic_cluster_count} |
| Cannibalization pairs | {cannibalization_pair_count} |
| Orphan topics | {orphan_topic_count} |
| Content gaps detected | {content_gaps_detected} |
| Authority gaps detected | {authority_gaps_detected} |
| High commercial / low authority topics | {high_commercial_low_authority_topics} |
| Dominant/core topics | {dominant_topics} |
| At-risk topics | {at_risk_topics} |
| Total impressions | {total_impressions} |
| Total clicks | {total_clicks} |
| Average authority score | {average_authority_score} |

---

# Commercial Opportunity Summary

{"".join(f"- {item}\n" for item in commercial_summary)}

---

# Topic Authority Summary

{"".join(f"- {item}\n" for item in topic_summary)}

{dataframe_to_markdown(topic_authority_df, topic_authority_columns, 20, "No topic authority map available.")}

---

# Semantic Cannibalization Risks

{dataframe_to_markdown(cannibalization_df, cannibalization_columns, 20, "No semantic cannibalization file available or no risks detected.")}

---

# High Commercial / Low Authority Topics

{dataframe_to_markdown(high_commercial_df, high_commercial_columns, 20, "No high commercial / low authority topics detected.")}

---

# Content Gap Priorities

{dataframe_to_markdown(content_gap_df.sort_values("gap_score", ascending=False) if "gap_score" in content_gap_df.columns else content_gap_df, content_gap_columns, 20, "No content gap priorities available.")}

---

# Structural SEO Risks

## Crawl Issue Concentration

{dataframe_to_markdown(issue_df, structural_risk_columns, 15, "No crawl issue data available.")}

## Orphan Topics

{dataframe_to_markdown(orphan_topics_df, content_gap_columns, 15, "No orphan topic file available or no orphan topics detected.")}

---

# Immediate Actions

{"".join(f"{i + 1}. {action}\n" for i, action in enumerate(immediate_actions))}

---

# Strategic Mid-Term Actions

{"".join(f"{i + 1}. {action}\n" for i, action in enumerate(mid_term_actions))}

---

# Source Files

{chr(10).join(source_lines)}
"""

    output_file.write_text(md, encoding="utf-8")
    stable_output_file.write_text(md, encoding="utf-8")

    print("")
    print("================================================")
    print("SEO EXECUTIVE REVIEW COMPLETE")
    print("================================================")
    print(f"Output file: {output_file}")
    print(f"Stable file: {stable_output_file}")
    print("================================================")


if __name__ == "__main__":
    main()
