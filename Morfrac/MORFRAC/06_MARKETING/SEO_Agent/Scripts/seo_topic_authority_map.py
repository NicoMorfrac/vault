# ============================================================
# MORFRAC SEO TOPIC AUTHORITY MAP
# Deterministic scoring from existing SEO pipeline outputs
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

SEMANTIC_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
CONTENT_GAP_PATH = SEO_AGENT_PATH / "Content_Gap_Analysis"
CONTEXTUAL_LINK_PATH = SEO_AGENT_PATH / "Contextual_Links"

OUTPUT_PATH = SEO_AGENT_PATH / "Topic_Authority_Map"

TODAY = datetime.today().strftime("%Y-%m-%d")


# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = [
        f for f in folder.glob(pattern)
        if re.match(r"^\d{4}-\d{2}-\d{2}_", f.name)
    ]

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def safe_read_csv(path):
    if path and path.exists():
        return pd.read_csv(path).fillna("")
    return pd.DataFrame()


def to_numeric(df, column):
    if column not in df.columns:
        return pd.Series([0] * len(df))
    return pd.to_numeric(df[column], errors="coerce").fillna(0)


def normalize_url(url):
    if pd.isna(url):
        return ""

    url = str(url).strip().lower()

    for prefix in [
        "https://www.morfrac.com",
        "http://www.morfrac.com",
        "https://morfrac.com",
        "http://morfrac.com",
    ]:
        url = url.replace(prefix, "")

    if url.endswith("/") and url != "/":
        url = url[:-1]

    return url


def authority_tier(score):
    if score >= 85:
        return "DOMINANT"
    if score >= 65:
        return "STRONG"
    if score >= 45:
        return "MODERATE"
    if score >= 25:
        return "WEAK"
    return "VERY_WEAK"


def strategic_status(row):
    score = row["topic_authority_score"]
    commercial = row.get("commercial_strength", 0)
    authority = row.get("authority_strength", 0)
    product_pages = row.get("product_pages", 0)
    category_pages = row.get("category_pages", 0)
    landing_pages = row.get("landing_pages", 0)
    gap_type = str(row.get("gap_type", ""))
    health = str(row.get("cluster_health", ""))

    commercial_pages = product_pages + category_pages + landing_pages

    if commercial >= 45 and authority < 35 and score < 50:
        return "HIGH_COMMERCIAL_LOW_AUTHORITY"

    if commercial_pages >= 5 and authority < 25 and score < 45:
        return "HIGH_COMMERCIAL_LOW_AUTHORITY"

    if authority >= 55 and commercial < 30:
        return "AUTHORITY_WITHOUT_COMMERCIAL_CAPTURE"

    if score >= 75:
        return "CORE_TOPIC_STRENGTH"

    if (
        score < 25
        or gap_type not in ("", "No major gap")
        or health in ("ORPHAN_TOPIC", "FRAGMENTED_TOPIC", "PRODUCT_HEAVY_NO_PILLAR")
    ):
        return "TOPIC_AT_RISK"

    return "STABLE"


def commercial_strength(row):
    product_pages = float(row.get("product_pages", 0))
    category_pages = float(row.get("category_pages", 0))
    landing_pages = float(row.get("landing_pages", 0))
    priority = float(row.get("avg_seo_priority_score", 0))

    score = 0
    score += min(product_pages * 4, 35)
    score += min(category_pages * 10, 25)
    score += min(landing_pages * 12, 25)
    score += min(priority, 15)

    return round(max(0, min(100, score)), 2)


def authority_strength(row):
    authority_pages = float(row.get("authority_content_pages", 0))
    impressions = float(row.get("total_impressions", 0))
    clicks = float(row.get("total_clicks", 0))
    contextual_links = float(row.get("contextual_link_recommendations", 0))

    score = 0
    score += min(authority_pages * 8, 40)
    score += min(contextual_links / 2, 20)
    score += min(impressions / 50, 20)
    score += min(clicks / 10, 20)

    return round(max(0, min(100, score)), 2)


def structural_health(row):
    category_pages = float(row.get("category_pages", 0))
    landing_pages = float(row.get("landing_pages", 0))
    health = str(row.get("cluster_health", ""))

    score = 50

    if health == "CORE_TOPIC":
        score += 20
    elif health == "BALANCED_TOPIC":
        score += 15
    elif health == "FRAGMENTED_TOPIC":
        score -= 20
    elif health == "PRODUCT_HEAVY_NO_PILLAR":
        score -= 25
    elif health == "CONTENT_WITHOUT_COMMERCIAL_TARGET":
        score -= 20
    elif health == "ORPHAN_TOPIC":
        score -= 15

    if landing_pages > 0:
        score += 10

    if category_pages > 0:
        score += 10

    return round(max(0, min(100, score)), 2)


def gap_penalty(row):
    gap_type = str(row.get("gap_type", ""))
    gap_score = float(row.get("gap_score", 0))

    if not gap_type or gap_type == "No major gap":
        return 0

    return round(min(25, 15 + gap_score / 10), 2)


def score_topic(row):
    final_score = (
        float(row.get("commercial_strength", 0)) * 0.35
        + float(row.get("authority_strength", 0)) * 0.35
        + float(row.get("structural_health", 0)) * 0.30
    )

    final_score -= float(row.get("gap_penalty", 0))

    return round(max(0, min(100, final_score)), 2)


def build_content_gap_lookup(gap_df):
    if gap_df.empty:
        return {}

    lookup = {}

    for _, row in gap_df.iterrows():
        cluster_id = str(row.get("semantic_cluster_id", "")).strip()
        label = str(row.get("dominant_label", "")).strip().lower()
        payload = {
            "gap_type": row.get("gap_type", ""),
            "gap_score": row.get("gap_score", 0),
            "recommended_action": row.get("recommended_action", ""),
        }

        if cluster_id:
            lookup[("id", cluster_id)] = payload

        if label:
            lookup[("label", label)] = payload

    return lookup


def build_contextual_link_metrics(pages_df, links_df):
    if pages_df.empty or links_df.empty:
        return pd.DataFrame(columns=[
            "semantic_cluster_id",
            "contextual_link_recommendations",
            "contextual_link_density",
        ])

    required_page_cols = {"url", "semantic_cluster_id"}
    required_link_cols = {"source_url", "target_url"}

    if not required_page_cols.issubset(pages_df.columns):
        return pd.DataFrame(columns=[
            "semantic_cluster_id",
            "contextual_link_recommendations",
            "contextual_link_density",
        ])

    if not required_link_cols.issubset(links_df.columns):
        return pd.DataFrame(columns=[
            "semantic_cluster_id",
            "contextual_link_recommendations",
            "contextual_link_density",
        ])

    page_map = pages_df[["url", "semantic_cluster_id"]].copy()
    page_map["url_key"] = page_map["url"].apply(normalize_url)
    url_to_cluster = dict(zip(
        page_map["url_key"],
        page_map["semantic_cluster_id"].astype(str),
    ))

    records = []

    for _, row in links_df.iterrows():
        for col in ["source_url", "target_url"]:
            cluster_id = url_to_cluster.get(normalize_url(row.get(col, "")))

            if cluster_id:
                records.append({
                    "semantic_cluster_id": cluster_id,
                    "link_role": col,
                })

    if not records:
        return pd.DataFrame(columns=[
            "semantic_cluster_id",
            "contextual_link_recommendations",
            "contextual_link_density",
        ])

    link_counts = (
        pd.DataFrame(records)
        .groupby("semantic_cluster_id", as_index=False)
        .agg(contextual_link_recommendations=("link_role", "count"))
    )

    page_counts = (
        pages_df
        .assign(semantic_cluster_id=pages_df["semantic_cluster_id"].astype(str))
        .groupby("semantic_cluster_id", as_index=False)
        .agg(topic_page_count=("url", "count"))
    )

    link_counts = link_counts.merge(
        page_counts,
        on="semantic_cluster_id",
        how="left",
    )

    link_counts["topic_page_count"] = to_numeric(link_counts, "topic_page_count").replace(0, 1)
    link_counts["contextual_link_density"] = (
        link_counts["contextual_link_recommendations"]
        / link_counts["topic_page_count"]
    ).round(2)

    return link_counts[[
        "semantic_cluster_id",
        "contextual_link_recommendations",
        "contextual_link_density",
    ]]


def table_or_message(df, columns, message, limit=30):
    if df.empty:
        return message

    existing = [col for col in columns if col in df.columns]

    if not existing:
        return message

    return dataframe_to_markdown(df[existing].head(limit))


def markdown_cell(value):
    text = str(value)
    text = text.replace("\n", " ").replace("|", "\\|")
    return text


def dataframe_to_markdown(df):
    if df.empty:
        return ""

    headers = [markdown_cell(col) for col in df.columns]
    separator = ["---"] * len(headers)
    rows = []

    for _, row in df.iterrows():
        rows.append([markdown_cell(row[col]) for col in df.columns])

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(separator) + " |",
    ]

    for row in rows:
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    clusters_file = latest_file(SEMANTIC_PATH, "*_semantic_clusters.csv")
    pages_file = latest_file(SEMANTIC_PATH, "*_semantic_cluster_pages.csv")
    content_gap_file = latest_file(CONTENT_GAP_PATH, "*_content_gap_analysis.csv")
    contextual_links_file = latest_file(
        CONTEXTUAL_LINK_PATH,
        "*_contextual_link_recommendations_filtered.csv",
    )

    if not clusters_file:
        raise FileNotFoundError("No dated semantic cluster summary CSV found.")

    clusters_df = safe_read_csv(clusters_file)
    pages_df = safe_read_csv(pages_file)
    gap_df = safe_read_csv(content_gap_file)
    links_df = safe_read_csv(contextual_links_file)

    if clusters_df.empty:
        raise ValueError("Semantic cluster summary CSV is empty.")

    for col in [
        "page_count",
        "product_pages",
        "category_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "total_clicks",
        "avg_seo_priority_score",
    ]:
        clusters_df[col] = to_numeric(clusters_df, col)

    clusters_df["semantic_cluster_id"] = clusters_df.get(
        "semantic_cluster_id",
        pd.Series(range(len(clusters_df))),
    ).astype(str)

    clusters_df["dominant_label"] = clusters_df.get(
        "dominant_label",
        pd.Series(["Unknown"] * len(clusters_df)),
    ).astype(str)

    clusters_df["cluster_health"] = clusters_df.get(
        "cluster_health",
        pd.Series([""] * len(clusters_df)),
    ).astype(str)

    gap_lookup = build_content_gap_lookup(gap_df)

    gap_payloads = []

    for _, row in clusters_df.iterrows():
        cluster_id = str(row.get("semantic_cluster_id", "")).strip()
        label = str(row.get("dominant_label", "")).strip().lower()
        payload = (
            gap_lookup.get(("id", cluster_id))
            or gap_lookup.get(("label", label))
            or {
                "gap_type": "",
                "gap_score": 0,
                "recommended_action": "",
            }
        )
        gap_payloads.append(payload)

    gap_payload_df = pd.DataFrame(gap_payloads)
    clusters_df = pd.concat(
        [clusters_df.reset_index(drop=True), gap_payload_df.reset_index(drop=True)],
        axis=1,
    )

    clusters_df["gap_score"] = to_numeric(clusters_df, "gap_score")

    link_metrics_df = build_contextual_link_metrics(pages_df, links_df)

    if not link_metrics_df.empty:
        clusters_df = clusters_df.merge(
            link_metrics_df,
            on="semantic_cluster_id",
            how="left",
        )
    else:
        clusters_df["contextual_link_recommendations"] = 0
        clusters_df["contextual_link_density"] = 0

    clusters_df["contextual_link_recommendations"] = to_numeric(
        clusters_df,
        "contextual_link_recommendations",
    )
    clusters_df["contextual_link_density"] = to_numeric(
        clusters_df,
        "contextual_link_density",
    )

    clusters_df["commercial_strength"] = clusters_df.apply(commercial_strength, axis=1)
    clusters_df["authority_strength"] = clusters_df.apply(authority_strength, axis=1)
    clusters_df["structural_health"] = clusters_df.apply(structural_health, axis=1)
    clusters_df["gap_penalty"] = clusters_df.apply(gap_penalty, axis=1)
    clusters_df["topic_authority_score"] = clusters_df.apply(score_topic, axis=1)
    clusters_df["authority_tier"] = clusters_df["topic_authority_score"].apply(authority_tier)
    clusters_df["strategic_status"] = clusters_df.apply(strategic_status, axis=1)

    output_columns = [
        "semantic_cluster_id",
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
        "category_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "total_clicks",
        "avg_seo_priority_score",
        "cluster_health",
        "gap_type",
        "gap_score",
        "contextual_link_recommendations",
        "contextual_link_density",
        "recommended_action",
    ]

    output_columns = [col for col in output_columns if col in clusters_df.columns]

    topic_df = (
        clusters_df[output_columns]
        .sort_values(
            ["topic_authority_score", "total_impressions", "page_count"],
            ascending=[False, False, False],
        )
        .reset_index(drop=True)
    )

    high_commercial_low_authority_df = topic_df[
        topic_df["strategic_status"] == "HIGH_COMMERCIAL_LOW_AUTHORITY"
    ].copy()

    risk_df = topic_df[
        topic_df["strategic_status"].isin([
            "TOPIC_AT_RISK",
            "HIGH_COMMERCIAL_LOW_AUTHORITY",
        ])
        | topic_df["authority_tier"].isin(["VERY_WEAK", "WEAK"])
    ].copy()

    core_df = topic_df[
        topic_df["strategic_status"] == "CORE_TOPIC_STRENGTH"
    ].copy()

    dated_topic_csv = OUTPUT_PATH / f"{TODAY}_topic_authority_map.csv"
    stable_topic_csv = OUTPUT_PATH / "topic_authority_map.csv"
    high_commercial_csv = OUTPUT_PATH / f"{TODAY}_high_commercial_low_authority.csv"
    risk_csv = OUTPUT_PATH / f"{TODAY}_topic_risk_topics.csv"
    core_csv = OUTPUT_PATH / f"{TODAY}_core_topic_strengths.csv"
    report_md = OUTPUT_PATH / f"{TODAY}_topic_authority_report.md"

    topic_df.to_csv(dated_topic_csv, index=False, encoding="utf-8-sig")
    topic_df.to_csv(stable_topic_csv, index=False, encoding="utf-8-sig")
    high_commercial_low_authority_df.to_csv(high_commercial_csv, index=False, encoding="utf-8-sig")
    risk_df.to_csv(risk_csv, index=False, encoding="utf-8-sig")
    core_df.to_csv(core_csv, index=False, encoding="utf-8-sig")

    report_columns = [
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
        "contextual_link_density",
    ]

    authority_table = table_or_message(
        topic_df,
        report_columns,
        "No topic authority data available.",
        40,
    )

    high_commercial_table = table_or_message(
        high_commercial_low_authority_df,
        report_columns,
        "No high-commercial / low-authority topics detected.",
        25,
    )

    risk_table = table_or_message(
        risk_df,
        report_columns,
        "No weak or at-risk topics detected.",
        25,
    )

    core_table = table_or_message(
        core_df,
        report_columns,
        "No core topic strengths detected.",
        25,
    )

    report = f"""# MORFRAC SEO Topic Authority Map

## Generated

{TODAY}

---

# Source Files Used

- Semantic cluster summary: `{clusters_file}`
- Semantic cluster pages: `{pages_file if pages_file else "Not available"}`
- Content gap analysis: `{content_gap_file if content_gap_file else "Not available"}`
- Contextual link recommendations: `{contextual_links_file if contextual_links_file else "Not available"}`

---

# Summary

- Topics scored: {len(topic_df)}
- High commercial / low authority topics: {len(high_commercial_low_authority_df)}
- Weak or at-risk topics: {len(risk_df)}
- Core topic strengths: {len(core_df)}
- Average topic authority score: {round(topic_df["topic_authority_score"].mean(), 2) if not topic_df.empty else 0}

---

# Overall Topic Authority Map

{authority_table}

---

# High Commercial / Low Authority Topics

{high_commercial_table}

---

# Weak / At-Risk Topics

{risk_table}

---

# Core Topic Strengths

{core_table}

---

# Interpretation Notes

Authority scoring is deterministic and capped from 0 to 100.

Positive authority signals:

- broad page coverage
- product, category, and landing-page coverage
- technical or educational authority content
- Search Console demand through impressions and clicks
- existing SEO priority
- contextual link density
- healthy semantic cluster status

Negative authority signals:

- content gap presence
- missing authority content
- missing commercial pillar pages
- orphan or fragmented topic status
- authority content without commercial capture

Authority tiers:

- `VERY_WEAK`: topic has little authority footprint.
- `WEAK`: topic exists but lacks depth, structure, or support.
- `MODERATE`: topic has a usable base but needs reinforcement.
- `STRONG`: topic has solid commercial and authority support.
- `DOMINANT`: topic is a mature authority area.

Strategic statuses:

- `HIGH_COMMERCIAL_LOW_AUTHORITY`: commercial footprint or demand exists, but authority is weak.
- `AUTHORITY_WITHOUT_COMMERCIAL_CAPTURE`: authority content exists without product/category capture.
- `CORE_TOPIC_STRENGTH`: strong topic with commercial and authority support.
- `TOPIC_AT_RISK`: weak, fragmented, orphaned, or gap-affected topic.
- `STABLE`: no immediate structural issue detected.

---

# Recommended Actions

1. Prioritize `HIGH_COMMERCIAL_LOW_AUTHORITY` topics for technical guides, comparison pages, and stronger internal linking.
2. Build or improve pillar pages for product-heavy topics without landing-page support.
3. Route authority content toward relevant commercial pages when status is `AUTHORITY_WITHOUT_COMMERCIAL_CAPTURE`.
4. Consolidate fragmented or orphan topics before creating more content.
5. Defend `CORE_TOPIC_STRENGTH` clusters with regular updates, internal links, and refreshed metadata.

---

# Output Files

- Topic authority map: `{dated_topic_csv}`
- Stable topic authority map: `{stable_topic_csv}`
- High commercial / low authority topics: `{high_commercial_csv}`
- Topic risk topics: `{risk_csv}`
- Core topic strengths: `{core_csv}`
"""

    report_md.write_text(report, encoding="utf-8")

    print("")
    print("================================================")
    print("SEO TOPIC AUTHORITY MAP COMPLETE")
    print("================================================")
    print(f"Topics scored: {len(topic_df)}")
    print(f"High commercial / low authority topics: {len(high_commercial_low_authority_df)}")
    print(f"Weak or at-risk topics: {len(risk_df)}")
    print(f"Core topic strengths: {len(core_df)}")
    print(f"Report: {report_md}")
    print("================================================")


if __name__ == "__main__":
    main()
