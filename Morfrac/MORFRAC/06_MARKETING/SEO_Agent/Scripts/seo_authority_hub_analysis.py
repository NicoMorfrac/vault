from pathlib import Path
from datetime import datetime

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Authority_Hubs"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# AUTHORITY CLUSTERS
# =========================================
AUTHORITY_CLUSTERS = {
    "dogbone": [
        "dogbone",
        "soft shackle",
        "connection",
        "joint",
    ],

    "mloop": [
        "mloop",
        "dyneema loop",
        "soft loop",
        "loop",
    ],

    "shackle": [
        "shackle",
        "soft shackle",
        "titanium shackle",
    ],

    "padeye": [
        "padeye",
        "through deck",
        "stick on",
    ],

    "powerfurl": [
        "powerfurl",
        "furler",
        "furling",
        "top down",
        "continuous line",
    ],

    "morfblock": [
        "morfblock",
        "sailing block",
        "snatch block",
        "block",
    ],

    "morfring": [
        "morfring",
        "friction ring",
        "ring",
    ],

    "morfwing": [
        "morfwing",
        "wing sail",
        "wing",
    ],

    "mreel": [
        "mreel",
        "rope reeler",
        "line reeler",
        "rope management",
    ],

    "hoistlock": [
        "hoistlock",
        "gaff lock",
        "mainsail lock",
        "halyard lock",
    ],

    "custom_engineering": [
        "custom",
        "engineering",
        "manufacturing",
        "3d printed",
    ],
}

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


def normalize(value):
    return safe_text(value).lower()


def detect_cluster(text):
    text = normalize(text)

    for cluster, keywords in AUTHORITY_CLUSTERS.items():
        for keyword in keywords:
            if keyword in text:
                return cluster

    return "other"


def classify_hub_strength(row):
    impressions = float(row.get("total_impressions", 0))
    urls = float(row.get("supporting_urls", 0))
    opportunity = float(row.get("avg_opportunity_score", 0))

    score = 0

    score += impressions * 0.1
    score += urls * 3
    score += opportunity * 0.5

    if score >= 150:
        return "VERY STRONG"

    if score >= 80:
        return "STRONG"

    if score >= 40:
        return "MEDIUM"

    return "WEAK"


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

    if not crawl_file:
        print("No crawl file found.")
        return

    if not leverage_file:
        print("No leverage file found.")
        return

    print("\nUsing crawl file:")
    print(crawl_file)

    print("\nUsing leverage file:")
    print(leverage_file)

    crawl_df = pd.read_csv(crawl_file)
    leverage_df = pd.read_csv(leverage_file)

    if crawl_df.empty or leverage_df.empty:
        print("Required data is empty.")
        return

    for col in [
        "query",
        "page",
        "impressions",
        "clicks",
        "page_type",
        "intent",
        "opportunity_score",
    ]:
        if col not in leverage_df.columns:
            leverage_df[col] = ""

    leverage_df["authority_cluster"] = leverage_df.apply(
        lambda row: detect_cluster(
            f"{row.get('query', '')} {row.get('page', '')}"
        ),
        axis=1
    )

    grouped = (
        leverage_df.groupby("authority_cluster", as_index=False)
        .agg(
            supporting_urls=("page", lambda x: len(set(map(str, x)))),
            total_impressions=("impressions", "sum"),
            total_clicks=("clicks", "sum"),
            avg_opportunity_score=("opportunity_score", "mean"),
            page_types=("page_type", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            intents=("intent", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            example_queries=("query", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            example_pages=("page", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
        )
    )

    grouped = grouped[grouped["authority_cluster"] != "other"].copy()

    grouped["hub_strength"] = grouped.apply(classify_hub_strength, axis=1)

    grouped = grouped.sort_values(
        ["total_impressions", "avg_opportunity_score"],
        ascending=False
    )

    # =========================================
    # STRATEGIC RECOMMENDATIONS
    # =========================================

    recommendations = []

    for _, row in grouped.iterrows():
        cluster = row["authority_cluster"]

        recommendation = {
            "authority_cluster": cluster,
            "hub_strength": row["hub_strength"],
            "supporting_urls": row["supporting_urls"],
            "recommended_hub_action": "",
            "recommended_supporting_content": "",
        }

        if row["hub_strength"] in ["VERY STRONG", "STRONG"]:
            recommendation["recommended_hub_action"] = (
                "Build or strengthen dedicated authority landing page."
            )

        else:
            recommendation["recommended_hub_action"] = (
                "Expand supporting authority content before scaling hub."
            )

        recommendation["recommended_supporting_content"] = (
            "Technical guides | comparisons | application pages | engineering explanations | integration examples"
        )

        recommendations.append(recommendation)

    recommendations_df = pd.DataFrame(recommendations)

    # =========================================
    # OUTPUTS
    # =========================================

    output_csv = OUTPUT_PATH / f"{run_date}_authority_hub_analysis.csv"
    output_recommendations = OUTPUT_PATH / f"{run_date}_authority_hub_recommendations.csv"
    output_md = OUTPUT_PATH / f"{run_date}_authority_hub_analysis.md"

    grouped.to_csv(output_csv, index=False)
    recommendations_df.to_csv(output_recommendations, index=False)

    grouped_table = grouped.head(20).to_markdown(index=False)
    recommendations_table = recommendations_df.head(20).to_markdown(index=False)

    report = f"""# SEO Authority Hub Analysis

## Generated

{run_date}

## Purpose

This report identifies MORFRAC authority hub opportunities.

The goal is not broad content production.

The goal is:

- engineering authority concentration
- commercial search capture
- technical differentiation
- internal authority consolidation
- product ecosystem discoverability

---

# Authority Hub Summary

{grouped_table}

---

# Strategic Recommendations

{recommendations_table}

---

# Interpretation Notes

Authority hubs should:

- consolidate related product families
- support internal linking
- target commercial + technical intent
- support engineering authority
- capture non-branded discovery
- reduce fragmented topical authority

Recommended hub structure:

Hub page
→ technical guides
→ supporting product pages
→ integration pages
→ application examples
→ comparison content

Avoid:

- generic sailing blogs
- high-volume low-intent content
- disconnected articles
- vanity traffic strategies

---

# Output Files

- Hub analysis: {output_csv}
- Recommendations: {output_recommendations}
- Report: {output_md}
"""

    output_md.write_text(report, encoding="utf-8")

    print("\nSEO AUTHORITY HUB ANALYSIS COMPLETE\n")
    print(output_csv)
    print(output_recommendations)
    print(output_md)


if __name__ == "__main__":
    main()