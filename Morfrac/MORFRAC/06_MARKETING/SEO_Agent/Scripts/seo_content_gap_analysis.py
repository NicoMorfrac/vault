# ============================================================
# MORFRAC SEO CONTENT GAP ANALYSIS
# Deterministic V1
# ============================================================

from pathlib import Path
import sys
from datetime import datetime
import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_content_gap_report"
SOURCE_AGENT = "SEO_Agent"


SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

SEMANTIC_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
MERGE_PATH = SEO_AGENT_PATH / "Merged_Analysis"
LINK_PATH = SEO_AGENT_PATH / "Contextual_Links"

OUTPUT_PATH = SEO_AGENT_PATH / "Content_Gap_Analysis"

TODAY = datetime.today().strftime("%Y-%m-%d")

# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))
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


def classify_gap(row):
    product_pages = row.get("product_pages", 0)
    category_pages = row.get("category_pages", 0)
    landing_pages = row.get("landing_pages", 0)
    authority_pages = row.get("authority_content_pages", 0)
    impressions = row.get("total_impressions", 0)
    health = str(row.get("cluster_health", ""))

    if product_pages >= 10 and authority_pages == 0:
        return "Missing technical authority content"

    if product_pages >= 10 and landing_pages == 0:
        return "Missing commercial pillar page"

    if product_pages >= 5 and category_pages == 0:
        return "Missing category support"

    if authority_pages >= 3 and product_pages == 0 and category_pages == 0:
        return "Authority content lacks commercial target"

    if health == "ORPHAN_TOPIC":
        return "Orphan topic"

    if impressions >= 100 and authority_pages == 0:
        return "Search demand without authority support"

    return "No major gap"


def recommended_action(row):
    gap = row.get("gap_type", "")
    label = row.get("dominant_label", "topic")

    if gap == "Missing technical authority content":
        return f"Create technical guide content supporting the {label} product family."

    if gap == "Missing commercial pillar page":
        return f"Create or strengthen a commercial landing/pillar page for {label}."

    if gap == "Missing category support":
        return f"Create or improve category structure for {label} pages."

    if gap == "Authority content lacks commercial target":
        return f"Link existing authority content toward relevant {label} product/category pages."

    if gap == "Orphan topic":
        return f"Add supporting pages or internal links if {label} has commercial value."

    if gap == "Search demand without authority support":
        return f"Build authority content around {label} queries and link to commercial pages."

    return "Monitor; no immediate content gap detected."


def gap_score(row):
    score = 0

    product_pages = float(row.get("product_pages", 0))
    category_pages = float(row.get("category_pages", 0))
    landing_pages = float(row.get("landing_pages", 0))
    authority_pages = float(row.get("authority_content_pages", 0))
    impressions = float(row.get("total_impressions", 0))
    clicks = float(row.get("total_clicks", 0))
    avg_priority = float(row.get("avg_seo_priority_score", 0))
    health = str(row.get("cluster_health", ""))

    score += min(product_pages * 3, 40)
    score += min(impressions / 10, 30)
    score += min(clicks, 20)
    score += min(avg_priority, 30)

    if product_pages >= 10 and authority_pages == 0:
        score += 35

    if product_pages >= 10 and landing_pages == 0:
        score += 30

    if product_pages >= 5 and category_pages == 0:
        score += 20

    if authority_pages >= 3 and product_pages == 0:
        score += 15

    if health == "FRAGMENTED_TOPIC":
        score += 20

    if health == "PRODUCT_HEAVY_NO_PILLAR":
        score += 30

    if health == "CONTENT_WITHOUT_COMMERCIAL_TARGET":
        score += 20

    if health == "ORPHAN_TOPIC":
        score += 10

    return round(score, 2)


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # ============================================================
    # LOAD FILES
    # ============================================================

    clusters_file = latest_file(SEMANTIC_PATH, "*_semantic_clusters.csv")
    pages_file = latest_file(SEMANTIC_PATH, "*_semantic_cluster_pages.csv")
    merge_file = latest_file(MERGE_PATH, "*_search_console_merge.csv")
    links_file = latest_file(LINK_PATH, "*_contextual_link_recommendations_filtered.csv")

    if not clusters_file:
        raise FileNotFoundError("No semantic cluster summary CSV found.")

    print("Using semantic cluster file:")
    print(clusters_file)

    clusters_df = safe_read_csv(clusters_file)
    pages_df = safe_read_csv(pages_file)
    merge_df = safe_read_csv(merge_file)
    links_df = safe_read_csv(links_file)

    # ============================================================
    # NORMALIZE NUMERIC COLUMNS
    # ============================================================

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

    # ============================================================
    # GAP ANALYSIS
    # ============================================================

    clusters_df["gap_type"] = clusters_df.apply(classify_gap, axis=1)
    clusters_df["gap_score"] = clusters_df.apply(gap_score, axis=1)
    clusters_df["recommended_action"] = clusters_df.apply(recommended_action, axis=1)

    gap_df = clusters_df[
        clusters_df["gap_type"] != "No major gap"
    ].copy()

    gap_df = gap_df.sort_values(
        "gap_score",
        ascending=False
    )

    # ============================================================
    # AUTHORITY GAP ANALYSIS
    # ============================================================

    authority_gap_df = clusters_df[
        (
            (clusters_df["product_pages"] >= 5)
            &
            (clusters_df["authority_content_pages"] == 0)
        )
        |
        (
            (clusters_df["total_impressions"] >= 50)
            &
            (clusters_df["authority_content_pages"] == 0)
        )
    ].copy()

    authority_gap_df = authority_gap_df.sort_values(
        "gap_score",
        ascending=False
    )

    # ============================================================
    # MISSING PILLAR PAGES
    # ============================================================

    pillar_gap_df = clusters_df[
        (
            (clusters_df["product_pages"] >= 5)
            &
            (clusters_df["landing_pages"] == 0)
        )
        |
        (
            clusters_df["cluster_health"] == "PRODUCT_HEAVY_NO_PILLAR"
        )
    ].copy()

    pillar_gap_df = pillar_gap_df.sort_values(
        "gap_score",
        ascending=False
    )

    # ============================================================
    # ORPHAN COMMERCIAL TOPICS
    # ============================================================

    orphan_commercial_df = clusters_df[
        (
            clusters_df["cluster_health"] == "ORPHAN_TOPIC"
        )
        &
        (
            (clusters_df["product_pages"] > 0)
            |
            (clusters_df["total_impressions"] > 0)
        )
    ].copy()

    orphan_commercial_df = orphan_commercial_df.sort_values(
        "gap_score",
        ascending=False
    )

    # ============================================================
    # PAGE-LEVEL SUPPORT SUMMARY
    # ============================================================

    page_support_df = pd.DataFrame()

    if not pages_df.empty:
        page_support_df = (
            pages_df
            .groupby(["manual_topic_label", "page_role"], as_index=False)
            .agg(
                pages=("url", "count"),
                total_impressions=("impressions", "sum"),
                total_clicks=("clicks", "sum"),
                avg_priority=("seo_priority_score", "mean"),
            )
            .sort_values(["manual_topic_label", "pages"], ascending=[True, False])
        )

    # ============================================================
    # OUTPUT FILES
    # ============================================================

    content_gap_csv = OUTPUT_PATH / f"{TODAY}_content_gap_analysis.csv"
    authority_gap_csv = OUTPUT_PATH / f"{TODAY}_authority_gap_analysis.csv"
    pillar_gap_csv = OUTPUT_PATH / f"{TODAY}_missing_pillar_pages.csv"
    orphan_csv = OUTPUT_PATH / f"{TODAY}_orphan_commercial_topics.csv"
    page_support_csv = OUTPUT_PATH / f"{TODAY}_page_support_summary.csv"
    report_md = OUTPUT_PATH / f"{TODAY}_content_gap_report.md"

    stable_content_gap_csv = OUTPUT_PATH / "content_gap_analysis.csv"
    stable_pillar_gap_csv = OUTPUT_PATH / "missing_pillar_pages.csv"

    gap_df.to_csv(content_gap_csv, index=False, encoding="utf-8-sig")
    gap_df.to_csv(stable_content_gap_csv, index=False, encoding="utf-8-sig")

    authority_gap_df.to_csv(authority_gap_csv, index=False, encoding="utf-8-sig")
    pillar_gap_df.to_csv(pillar_gap_csv, index=False, encoding="utf-8-sig")
    pillar_gap_df.to_csv(stable_pillar_gap_csv, index=False, encoding="utf-8-sig")

    orphan_commercial_df.to_csv(orphan_csv, index=False, encoding="utf-8-sig")

    if not page_support_df.empty:
        page_support_df.to_csv(page_support_csv, index=False, encoding="utf-8-sig")
    else:
        pd.DataFrame().to_csv(page_support_csv, index=False, encoding="utf-8-sig")

    # ============================================================
    # MARKDOWN REPORT
    # ============================================================

    gap_table = (
        gap_df.head(30).to_markdown(index=False)
        if not gap_df.empty
        else "No major content gaps detected."
    )

    authority_table = (
        authority_gap_df.head(20).to_markdown(index=False)
        if not authority_gap_df.empty
        else "No major authority-content gaps detected."
    )

    pillar_table = (
        pillar_gap_df.head(20).to_markdown(index=False)
        if not pillar_gap_df.empty
        else "No missing pillar-page gaps detected."
    )

    orphan_table = (
        orphan_commercial_df.head(20).to_markdown(index=False)
        if not orphan_commercial_df.empty
        else "No commercial orphan topics detected."
    )

    report = f"""# MORFRAC SEO Content Gap Analysis

## Generated

{TODAY}

---

# Purpose

This report identifies missing content and authority gaps across MORFRAC semantic SEO clusters.

It uses deterministic data from:

- semantic cluster analysis
- crawl data
- Search Console merge data
- contextual linking outputs

It detects:

- product-heavy clusters without technical authority content
- product-heavy clusters without pillar/landing pages
- authority content without commercial targets
- orphan commercial topics
- search-demand topics without supporting authority content

---

# Source Files

- Semantic clusters: `{clusters_file}`
- Semantic pages: `{pages_file if pages_file else "Not available"}`
- Search Console merge: `{merge_file if merge_file else "Not available"}`
- Contextual links: `{links_file if links_file else "Not available"}`

---

# Summary

- Semantic clusters reviewed: {len(clusters_df)}
- Content gaps detected: {len(gap_df)}
- Authority gaps detected: {len(authority_gap_df)}
- Missing pillar-page gaps: {len(pillar_gap_df)}
- Orphan commercial topics: {len(orphan_commercial_df)}

---

# Highest Priority Content Gaps

{gap_table}

---

# Authority Content Gaps

{authority_table}

---

# Missing Pillar / Landing Page Gaps

{pillar_table}

---

# Orphan Commercial Topics

{orphan_table}

---

# Interpretation Notes

Gap type meanings:

- `Missing technical authority content`: product cluster exists, but there are no supporting technical/educational pages.
- `Missing commercial pillar page`: many pages exist, but no central commercial landing page supports the cluster.
- `Missing category support`: product pages exist without enough category-level support.
- `Authority content lacks commercial target`: educational/blog content exists but does not clearly connect to products/categories.
- `Search demand without authority support`: impressions exist, but the topic lacks supporting authority content.
- `Orphan topic`: topic has only one semantic cluster/page path and may need support if commercially useful.

Recommended actions:

1. Build technical guides for product-heavy clusters.
2. Build commercial landing pages where product families lack a central pillar.
3. Link authority content toward product/category pages.
4. Avoid creating new content in fragmented topics before consolidation.
5. Prioritize gaps with impressions, product pages, and high gap scores.

---

# Output Files

- Content gap analysis: `{content_gap_csv}`
- Authority gap analysis: `{authority_gap_csv}`
- Missing pillar pages: `{pillar_gap_csv}`
- Orphan commercial topics: `{orphan_csv}`
- Page support summary: `{page_support_csv}`
"""

    write_markdown_report(report_md, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    # ============================================================
    # COMPLETE
    # ============================================================

    print("")
    print("================================================")
    print("SEO CONTENT GAP ANALYSIS COMPLETE")
    print("================================================")
    print(f"Semantic clusters reviewed: {len(clusters_df)}")
    print(f"Content gaps detected: {len(gap_df)}")
    print(f"Authority gaps detected: {len(authority_gap_df)}")
    print(f"Missing pillar-page gaps: {len(pillar_gap_df)}")
    print(f"Orphan commercial topics: {len(orphan_commercial_df)}")
    print(f"Report: {report_md}")
    print("================================================")


if __name__ == "__main__":
    main()
