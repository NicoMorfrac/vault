from pathlib import Path
from datetime import datetime

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
TEMPLATE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Template_Analysis"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Fix_Recommendations"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def latest_csv(path, pattern="*.csv"):
    files = list(path.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def classify_fix_type(row):
    issues = str(row.get("issues", "")).lower()
    page_type = str(row.get("page_type", "")).lower()
    intent = str(row.get("intent", "")).lower()
    ctr_gap = float(row.get("ctr_gap", 0))
    impressions = float(row.get("impressions", 0))

    fixes = []

    if "short title" in issues or "long title" in issues or row.get("title_length", 0) < 30:
        fixes.append("title_rewrite")

    if "missing meta description" in issues or "short meta description" in issues or row.get("meta_description_length", 0) < 80:
        fixes.append("meta_rewrite")

    if "multiple h1" in issues:
        fixes.append("h1_template_fix")

    if "images missing alt text" in issues:
        fixes.append("image_alt_template_fix")

    if ctr_gap >= 2 and impressions >= 5:
        fixes.append("serp_ctr_improvement")

    if page_type == "blog" and intent == "commercial":
        fixes.append("commercial_landing_page_needed")

    if page_type in ["product", "landing", "category"]:
        fixes.append("internal_linking_review")

    return "; ".join(sorted(set(fixes)))


def priority_reason(row):
    reasons = []

    if row.get("impressions", 0) >= 100:
        reasons.append("high existing visibility")

    if row.get("ctr_gap", 0) >= 2:
        reasons.append("CTR below expected")

    if row.get("position", 100) <= 10:
        reasons.append("already ranking on page 1")

    if row.get("intent", "") in ["commercial", "product_code", "product_brand"]:
        reasons.append("commercial/product intent")

    if row.get("issue_count", 0) > 0:
        reasons.append("crawl issues detected")

    return "; ".join(reasons)


def suggested_action(row):
    page_type = str(row.get("page_type", "")).lower()
    issues = str(row.get("issues", "")).lower()
    query = str(row.get("query", ""))
    page = str(row.get("page", ""))

    actions = []

    if "multiple h1" in issues:
        actions.append("Fix template so the page has one primary H1 only.")

    if "short title" in issues:
        actions.append("Rewrite title to include product/category term, sailing use case, and MORFRAC brand.")

    if "long title" in issues:
        actions.append("Shorten title while keeping main product term and commercial intent.")

    if "missing meta description" in issues or "short meta description" in issues:
        actions.append("Add a commercial meta description focused on use case, material/engineering advantage, and click intent.")

    if "images missing alt text" in issues:
        actions.append("Add descriptive alt text to product/category images at template level.")

    if page_type == "product":
        actions.append("Add internal links from related landing/category pages to this product page.")

    if page_type == "landing":
        actions.append("Strengthen landing page copy around the query cluster and link to relevant products.")

    if page_type == "blog":
        actions.append("Consider creating or linking to a commercial landing page if the query has buying intent.")

    if not actions:
        actions.append("Review manually; no obvious deterministic fix found.")

    return " ".join(actions)


def generate_title_hint(row):
    query = str(row.get("query", "")).strip()
    page_type = str(row.get("page_type", "")).lower()

    if not query:
        return ""

    if page_type == "product":
        return f"{query.title()} for Sailing Hardware | MORFRAC"

    if page_type == "landing":
        return f"{query.title()} for High-Performance Sailing | MORFRAC"

    if page_type == "category":
        return f"{query.title()} Marine Hardware | MORFRAC"

    if page_type == "blog":
        return f"{query.title()} - Technical Guide | MORFRAC"

    return f"{query.title()} | MORFRAC"


def generate_meta_hint(row):
    query = str(row.get("query", "")).strip()
    intent = str(row.get("intent", "")).lower()

    if intent == "product_code":
        return f"Explore MORFRAC {query} sailing hardware with technical specifications, product details, and high-performance marine applications."

    if intent == "commercial":
        return f"Discover MORFRAC {query} solutions for high-performance sailing hardware, engineered for strength, reliability, and simple integration."

    if intent == "product_brand":
        return f"Learn about MORFRAC {query} products, technical features, applications, and available configurations for sailing systems."

    return f"Technical information and MORFRAC solutions related to {query}."


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    leverage_file = latest_csv(
        LEVERAGE_PATH,
        "*_seo_query_page_crawl_leverage_opportunities.csv"
    )

    template_file = latest_csv(
        TEMPLATE_PATH,
        "*_template_cluster_analysis.csv"
    )

    if not leverage_file:
        print("No leverage CSV found.")
        return

    print("\nUsing leverage file:")
    print(leverage_file)

    leverage_df = pd.read_csv(leverage_file)

    if leverage_df.empty:
        print("Leverage file is empty.")
        return

    if template_file:
        print("\nUsing template file:")
        print(template_file)
        template_df = pd.read_csv(template_file)
    else:
        print("\nNo template analysis file found. Continuing without template data.")
        template_df = pd.DataFrame()

    # Keep only meaningful opportunities
    df = leverage_df[
        leverage_df["opportunity_score"] >= 75
    ].copy()

    if df.empty:
        print("No high-priority opportunities found.")
        return

    df["fix_types"] = df.apply(classify_fix_type, axis=1)
    df["priority_reason"] = df.apply(priority_reason, axis=1)
    df["recommended_action"] = df.apply(suggested_action, axis=1)
    df["suggested_title_direction"] = df.apply(generate_title_hint, axis=1)
    df["suggested_meta_direction"] = df.apply(generate_meta_hint, axis=1)

    output_csv = OUTPUT_PATH / f"{run_date}_seo_fix_recommendations.csv"
    output_md = OUTPUT_PATH / f"{run_date}_seo_fix_recommendations.md"

    export_columns = [
        "query",
        "page",
        "clicks",
        "impressions",
        "ctr_percent",
        "expected_ctr",
        "ctr_gap",
        "position",
        "intent",
        "page_type",
        "issue_count",
        "title_length",
        "meta_description_length",
        "issues",
        "opportunity_score",
        "opportunity_level",
        "fix_types",
        "priority_reason",
        "recommended_action",
        "suggested_title_direction",
        "suggested_meta_direction",
    ]

    export_columns = [col for col in export_columns if col in df.columns]

    final_df = df[export_columns].copy()
    final_df.to_csv(output_csv, index=False)

    top_fixes_table = final_df.head(30).to_markdown(index=False)

    template_summary = ""

    if not template_df.empty:
        template_summary = template_df.head(10).to_markdown(index=False)

    summary = f"""# SEO Fix Recommendations

## Generated

{run_date}

## Purpose

This report converts SEO leverage intelligence into practical fix recommendations.

It uses:

- Search Console query-page opportunity data
- crawl metadata
- template cluster analysis
- deterministic commercial intent classification

---

# Highest Priority Fixes

{top_fixes_table}

---

# Template-Level Risk Summary

{template_summary if template_summary else "No template summary available."}

---

# Recommended Execution Order

## 1. Fix template-level H1 duplication

Multiple H1 issues appear repeatedly across product, category, landing, and blog templates.

This should be corrected at template level before individual page edits.

## 2. Rewrite high-leverage SERP titles

Prioritize pages with:

- high impressions
- page 1 rankings
- CTR below expected
- commercial/product intent

## 3. Improve meta descriptions

Focus first on pages with:

- missing meta descriptions
- short meta descriptions
- commercial query visibility
- product/category intent

## 4. Add image alt text at template level

Missing alt text appears structurally across product and category templates.

Fixing this at template level is more efficient than page-by-page edits.

## 5. Strengthen internal linking

Use high-authority landing pages to support:

- mloop products
- dogbone products
- shackle products
- padeye pages
- morfblock product families

---

# Notes

This report is deterministic.

It does not publish or edit website content.

It generates fix recommendations for review before implementation.
"""

    output_md.write_text(summary, encoding="utf-8")

    print("\nSEO FIX RECOMMENDATIONS COMPLETE\n")
    print(output_csv)
    print(output_md)


if __name__ == "__main__":
    main()