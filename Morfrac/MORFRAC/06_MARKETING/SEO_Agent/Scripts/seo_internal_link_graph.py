from pathlib import Path
from datetime import datetime
import ast

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
AUTHORITY_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Authority_Hubs"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Internal_Linking"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def latest_csv(path, pattern):
    files = list(path.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def safe_text(value):
    if pd.isna(value):
        return ""
    return str(value).strip()


def normalize_url(url):
    url = safe_text(url).lower()
    url = url.replace("https://www.morfrac.com", "")
    url = url.replace("http://www.morfrac.com", "")
    url = url.replace("https://morfrac.com", "")
    url = url.replace("http://morfrac.com", "")

    if url.endswith("/") and url != "/":
        url = url[:-1]

    return url


def parse_internal_links(value):
    if pd.isna(value):
        return []

    text = str(value).strip()

    if not text:
        return []

    try:
        parsed = ast.literal_eval(text)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass

    return []


def detect_cluster(text):
    text = safe_text(text).lower()

    clusters = {
        "dogbone": ["dogbone", "dog bone"],
        "mloop": ["mloop", "m loop", "dyneema loop"],
        "shackle": ["shackle"],
        "padeye": ["padeye", "pad eye", "cancamo", "cáncamo"],
        "powerfurl": ["powerfurl", "furler", "furling"],
        "morfblock": ["morfblock", "morf block", "block"],
        "morfring": ["morfring", "friction ring"],
        "morfwing": ["morfwing", "wing"],
        "mreel": ["mreel", "rope reeler"],
        "hoistlock": ["hoistlock", "gaff lock", "halyard lock"],
        "custom_engineering": ["custom", "engineering", "3d printed", "manufacturing"],
    }

    for cluster, keywords in clusters.items():
        for keyword in keywords:
            if keyword in text:
                return cluster

    return "other"


def page_importance_score(row):
    score = 0

    business_priority = safe_text(row.get("business_priority", "")).lower()
    page_type = safe_text(row.get("page_type", "")).lower()
    commercial_relevance = safe_text(row.get("commercial_relevance", "")).lower()
    authority_value = safe_text(row.get("authority_value", "")).lower()

    if business_priority == "high":
        score += 40
    elif business_priority == "medium":
        score += 20

    if page_type == "product":
        score += 25
    elif page_type in ["technical_blog", "blog"]:
        score += 15
    elif page_type == "general":
        score += 10

    if commercial_relevance == "high":
        score += 25
    elif commercial_relevance == "medium":
        score += 10

    if authority_value == "high":
        score += 20
    elif authority_value == "medium":
        score += 10

    return score


def classify_link_priority(score):
    if score >= 100:
        return "CRITICAL"
    if score >= 75:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"
    return "LOW"


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    crawl_file = latest_csv(CRAWL_PATH, "*_site_crawl.csv")
    leverage_file = latest_csv(
        LEVERAGE_PATH,
        "*_seo_query_page_crawl_leverage_opportunities.csv"
    )
    authority_file = latest_csv(
        AUTHORITY_PATH,
        "*_authority_hub_analysis.csv"
    )

    if not crawl_file:
        print("No crawl CSV found.")
        return

    print("\nUsing crawl file:")
    print(crawl_file)

    crawl_df = pd.read_csv(crawl_file)

    leverage_df = pd.DataFrame()
    authority_df = pd.DataFrame()

    if leverage_file:
        print("\nUsing leverage file:")
        print(leverage_file)
        leverage_df = pd.read_csv(leverage_file)

    if authority_file:
        print("\nUsing authority hub file:")
        print(authority_file)
        authority_df = pd.read_csv(authority_file)

    if crawl_df.empty:
        print("Crawl CSV is empty.")
        return

    for col in [
        "url",
        "page_type",
        "business_priority",
        "commercial_relevance",
        "authority_value",
        "internal_links",
        "issue_count",
        "title",
        "h1",
    ]:
        if col not in crawl_df.columns:
            crawl_df[col] = ""

    crawl_df["normalized_url"] = crawl_df["url"].apply(normalize_url)
    crawl_df["authority_cluster"] = crawl_df.apply(
        lambda row: detect_cluster(
            f"{row.get('url', '')} {row.get('title', '')} {row.get('h1', '')}"
        ),
        axis=1
    )

    crawl_df["page_importance_score"] = crawl_df.apply(
        page_importance_score,
        axis=1
    )

    # =========================================
    # BUILD LINK GRAPH
    # =========================================

    edges = []

    for _, row in crawl_df.iterrows():
        source_url = row.get("url", "")
        source_norm = row.get("normalized_url", "")
        source_cluster = row.get("authority_cluster", "other")
        source_type = row.get("page_type", "")

        links = parse_internal_links(row.get("internal_links", ""))

        for target in links:
            target_norm = normalize_url(target)

            if not target_norm:
                continue

            edges.append({
                "source_url": source_url,
                "source_normalized": source_norm,
                "source_page_type": source_type,
                "source_cluster": source_cluster,
                "target_url": target,
                "target_normalized": target_norm,
            })

    edge_df = pd.DataFrame(edges)

    if edge_df.empty:
        print("No internal links found.")
        return

    target_summary = (
        edge_df.groupby("target_normalized", as_index=False)
        .agg(
            inbound_internal_links=("source_normalized", "count"),
            unique_linking_pages=("source_normalized", lambda x: len(set(x))),
            linking_clusters=("source_cluster", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            linking_page_types=("source_page_type", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
        )
    )

    source_summary = (
        edge_df.groupby("source_normalized", as_index=False)
        .agg(
            outbound_internal_links=("target_normalized", "count"),
            unique_target_pages=("target_normalized", lambda x: len(set(x))),
        )
    )

    page_df = crawl_df.merge(
        target_summary,
        left_on="normalized_url",
        right_on="target_normalized",
        how="left"
    )

    page_df = page_df.merge(
        source_summary,
        left_on="normalized_url",
        right_on="source_normalized",
        how="left"
    )

    for col in [
        "inbound_internal_links",
        "unique_linking_pages",
        "outbound_internal_links",
        "unique_target_pages",
    ]:
        page_df[col] = page_df[col].fillna(0)

    # =========================================
    # MERGE LEVERAGE DATA
    # =========================================

    if not leverage_df.empty:
        if "page" not in leverage_df.columns:
            leverage_df["page"] = ""

        leverage_df["normalized_url"] = leverage_df["page"].apply(normalize_url)

        leverage_summary = (
            leverage_df.groupby("normalized_url", as_index=False)
            .agg(
                total_search_impressions=("impressions", "sum"),
                total_search_clicks=("clicks", "sum"),
                avg_opportunity_score=("opportunity_score", "mean"),
                max_opportunity_score=("opportunity_score", "max"),
                primary_queries=("query", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
                search_intents=("intent", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            )
        )

        page_df = page_df.merge(
            leverage_summary,
            on="normalized_url",
            how="left"
        )

    for col in [
        "total_search_impressions",
        "total_search_clicks",
        "avg_opportunity_score",
        "max_opportunity_score",
    ]:
        if col not in page_df.columns:
            page_df[col] = 0
        page_df[col] = page_df[col].fillna(0)

    if "primary_queries" not in page_df.columns:
        page_df["primary_queries"] = ""

    if "search_intents" not in page_df.columns:
        page_df["search_intents"] = ""

    # =========================================
    # SCORING
    # =========================================

    scores = []

    for _, row in page_df.iterrows():
        score = 0

        page_importance = float(row.get("page_importance_score", 0))
        inbound_links = float(row.get("inbound_internal_links", 0))
        search_impressions = float(row.get("total_search_impressions", 0))
        opportunity = float(row.get("max_opportunity_score", 0))
        page_type = safe_text(row.get("page_type", "")).lower()
        business_priority = safe_text(row.get("business_priority", "")).lower()

        score += page_importance

        if search_impressions >= 100:
            score += 30
        elif search_impressions >= 25:
            score += 15
        elif search_impressions >= 5:
            score += 8

        if opportunity >= 100:
            score += 30
        elif opportunity >= 75:
            score += 20
        elif opportunity >= 50:
            score += 10

        if inbound_links == 0:
            score += 40
        elif inbound_links < 3:
            score += 25
        elif inbound_links < 5:
            score += 15
        elif inbound_links < 10:
            score += 5

        if page_type in ["product", "general"] and business_priority == "high":
            score += 10

        scores.append(score)

    page_df["internal_link_graph_score"] = scores
    page_df["internal_link_priority"] = page_df["internal_link_graph_score"].apply(
        classify_link_priority
    )

    # =========================================
    # ORPHANS / WEAK SUPPORT
    # =========================================

    orphan_df = page_df[
        page_df["inbound_internal_links"] == 0
    ].copy()

    weak_support_df = page_df[
        (
            page_df["inbound_internal_links"] < 5
        )
        & (
            (page_df["business_priority"].astype(str).str.lower() == "high")
            | (page_df["total_search_impressions"] >= 5)
            | (page_df["max_opportunity_score"] >= 50)
        )
    ].copy()

    authority_summary = (
        page_df.groupby("authority_cluster", as_index=False)
        .agg(
            pages=("url", "count"),
            avg_inbound_links=("inbound_internal_links", "mean"),
            total_inbound_links=("inbound_internal_links", "sum"),
            avg_graph_score=("internal_link_graph_score", "mean"),
            high_priority_pages=("internal_link_priority", lambda x: sum(v in ["CRITICAL", "HIGH"] for v in x)),
            total_search_impressions=("total_search_impressions", "sum"),
            max_opportunity_score=("max_opportunity_score", "max"),
        )
        .sort_values(
            ["high_priority_pages", "total_search_impressions"],
            ascending=False
        )
    )

    # =========================================
    # EXPORTS
    # =========================================

    output_edges = OUTPUT_PATH / f"{run_date}_internal_link_graph_edges.csv"
    output_pages = OUTPUT_PATH / f"{run_date}_internal_link_graph_pages.csv"
    output_orphans = OUTPUT_PATH / f"{run_date}_orphan_pages.csv"
    output_weak = OUTPUT_PATH / f"{run_date}_weak_internal_support_pages.csv"
    output_authority = OUTPUT_PATH / f"{run_date}_authority_flow_summary.csv"
    output_md = OUTPUT_PATH / f"{run_date}_internal_link_graph_analysis.md"

    edge_df.to_csv(output_edges, index=False)

    page_export_cols = [
        "url",
        "page_type",
        "business_priority",
        "commercial_relevance",
        "authority_value",
        "authority_cluster",
        "inbound_internal_links",
        "unique_linking_pages",
        "outbound_internal_links",
        "unique_target_pages",
        "total_search_impressions",
        "max_opportunity_score",
        "primary_queries",
        "search_intents",
        "internal_link_graph_score",
        "internal_link_priority",
    ]

    page_export_cols = [c for c in page_export_cols if c in page_df.columns]

    page_df[page_export_cols].sort_values(
        "internal_link_graph_score",
        ascending=False
    ).to_csv(output_pages, index=False)

    orphan_df[page_export_cols].sort_values(
        "internal_link_graph_score",
        ascending=False
    ).to_csv(output_orphans, index=False)

    weak_support_df[page_export_cols].sort_values(
        "internal_link_graph_score",
        ascending=False
    ).to_csv(output_weak, index=False)

    authority_summary.to_csv(output_authority, index=False)

    # =========================================
    # MARKDOWN REPORT
    # =========================================

    top_pages = (
        page_df[page_export_cols]
        .sort_values("internal_link_graph_score", ascending=False)
        .head(30)
        .to_markdown(index=False)
    )

    top_weak = (
        weak_support_df[page_export_cols]
        .sort_values("internal_link_graph_score", ascending=False)
        .head(30)
        .to_markdown(index=False)
        if not weak_support_df.empty
        else "_No weak internal support pages detected._"
    )

    top_orphans = (
        orphan_df[page_export_cols]
        .sort_values("internal_link_graph_score", ascending=False)
        .head(30)
        .to_markdown(index=False)
        if not orphan_df.empty
        else "_No orphan pages detected._"
    )

    authority_table = (
        authority_summary.head(20).to_markdown(index=False)
        if not authority_summary.empty
        else "_No authority flow summary available._"
    )

    report = f"""# SEO Internal Link Graph Analysis

## Generated

{run_date}

## Purpose

This report analyzes internal authority flow across the MORFRAC website.

It identifies:

- weakly supported commercial pages
- orphan pages
- high-opportunity pages with low internal links
- authority cluster reinforcement gaps
- internal link concentration issues

---

# Input Files

Crawl file:

{crawl_file}

Leverage file:

{leverage_file if leverage_file else "No leverage file used."}

Authority hub file:

{authority_file if authority_file else "No authority hub file used."}

---

# Highest Internal Link Graph Priorities

{top_pages}

---

# Weak Internal Support Pages

{top_weak}

---

# Orphan Pages

{top_orphans}

---

# Authority Flow Summary

{authority_table}

---

# Interpretation Notes

High internal link graph scores indicate pages that are:

- commercially important
- weakly supported internally
- already visible in search
- part of important authority clusters
- suitable for stronger contextual linking

Priority should focus on:

- product pages with search impressions but weak internal support
- authority hubs with fragmented support
- landing pages that should distribute authority to products
- blog articles that should link toward commercial pages
- category pages that should reinforce product families

Avoid prioritizing:

- legal pages
- utility pages
- tag archives
- low-commercial-value pages

---

# Output Files

- Link graph edges: {output_edges}
- Page-level graph summary: {output_pages}
- Orphan pages: {output_orphans}
- Weak support pages: {output_weak}
- Authority flow summary: {output_authority}
- Report: {output_md}
"""

    output_md.write_text(report, encoding="utf-8")

    print("\nSEO INTERNAL LINK GRAPH ANALYSIS COMPLETE\n")
    print(output_edges)
    print(output_pages)
    print(output_orphans)
    print(output_weak)
    print(output_authority)
    print(output_md)


if __name__ == "__main__":
    main()