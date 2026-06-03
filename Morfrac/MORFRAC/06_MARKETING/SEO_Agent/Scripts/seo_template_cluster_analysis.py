from pathlib import Path
import sys
from datetime import datetime

import pandas as pd

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_template_cluster_analysis"
SOURCE_AGENT = "SEO_Agent"


CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Template_Analysis"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def latest_csv(path):
    files = list(path.glob("*_site_crawl.csv"))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def classify_template(url):
    url = str(url).lower()

    if "/shop/category/" in url:
        return "shop_category"

    if "/shop/" in url:
        if "mloop" in url:
            return "product_mloop"
        if "dogbone" in url:
            return "product_dogbone"
        if "morfblock" in url:
            return "product_morfblock"
        if "shackle" in url:
            return "product_shackle"
        if "morfring" in url:
            return "product_morfring"
        if "powerfurl" in url:
            return "product_powerfurl"
        return "product_other"

    if "/blog/" in url:
        return "blog"

    if "dogbone" in url:
        return "landing_dogbone"

    if "padeye" in url:
        return "landing_padeye"

    if "powerfurl" in url:
        return "landing_powerfurl"

    if "morfblock" in url:
        return "landing_morfblock"

    if url.endswith("/shop"):
        return "shop_home"

    if url.endswith("/"):
        return "home"

    return "other"


def has_issue(issue_text, issue_name):
    return issue_name.lower() in str(issue_text).lower()


def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    crawl_file = latest_csv(CRAWL_PATH)

    if not crawl_file:
        print("No crawl CSV found.")
        return

    print("\nUsing crawl file:")
    print(crawl_file)

    df = pd.read_csv(crawl_file)

    if df.empty:
        print("Crawl CSV is empty.")
        return

    df["template_cluster"] = df["url"].apply(classify_template)

    required_cols = [
        "issue_count",
        "commercial_seo_score",
        "title_length",
        "meta_description_length",
        "word_count",
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = 0

    if "issues" not in df.columns:
        df["issues"] = ""

    df["issues"] = df["issues"].fillna("")

    df["missing_title"] = df["issues"].apply(lambda x: has_issue(x, "Missing title"))
    df["short_title"] = df["issues"].apply(lambda x: has_issue(x, "Short title"))
    df["long_title"] = df["issues"].apply(lambda x: has_issue(x, "Long title"))

    df["missing_meta"] = df["issues"].apply(lambda x: has_issue(x, "Missing meta description"))
    df["short_meta"] = df["issues"].apply(lambda x: has_issue(x, "Short meta description"))
    df["long_meta"] = df["issues"].apply(lambda x: has_issue(x, "Long meta description"))

    df["missing_h1"] = df["issues"].apply(lambda x: has_issue(x, "Missing H1"))
    df["multiple_h1"] = df["issues"].apply(lambda x: has_issue(x, "Multiple H1"))

    df["thin_content"] = df["issues"].apply(lambda x: has_issue(x, "Thin content"))
    df["missing_alt"] = df["issues"].apply(lambda x: has_issue(x, "Images missing alt text"))
    df["weak_internal_linking"] = df["issues"].apply(lambda x: has_issue(x, "Weak internal linking"))

    grouped = (
        df.groupby("template_cluster", as_index=False)
        .agg(
            pages=("url", "count"),
            avg_issue_count=("issue_count", "mean"),
            total_issues=("issue_count", "sum"),
            avg_commercial_seo_score=("commercial_seo_score", "mean"),
            avg_title_length=("title_length", "mean"),
            avg_meta_length=("meta_description_length", "mean"),
            avg_word_count=("word_count", "mean"),
            missing_title_count=("missing_title", "sum"),
            short_title_count=("short_title", "sum"),
            long_title_count=("long_title", "sum"),
            missing_meta_count=("missing_meta", "sum"),
            short_meta_count=("short_meta", "sum"),
            long_meta_count=("long_meta", "sum"),
            missing_h1_count=("missing_h1", "sum"),
            multiple_h1_count=("multiple_h1", "sum"),
            thin_content_count=("thin_content", "sum"),
            missing_alt_count=("missing_alt", "sum"),
            weak_internal_linking_count=("weak_internal_linking", "sum"),
        )
    )

    grouped["structural_risk_score"] = (
        grouped["total_issues"]
        + grouped["multiple_h1_count"] * 2
        + grouped["missing_meta_count"] * 3
        + grouped["short_title_count"] * 2
        + grouped["missing_alt_count"]
    )

    grouped = grouped.sort_values(
        ["structural_risk_score", "pages"],
        ascending=False
    )

    output_csv = OUTPUT_PATH / f"{run_date}_template_cluster_analysis.csv"
    output_md = OUTPUT_PATH / f"{run_date}_template_cluster_analysis.md"

    grouped.to_csv(output_csv, index=False)

    top_table = grouped.head(25).to_markdown(index=False)

    summary = f"""# SEO Template Cluster Analysis

## Generated

{run_date}

## Input

{crawl_file}

## Purpose

This report identifies structural SEO issues by template/page family.

It is designed to detect repeated template-level weaknesses rather than individual page defects.

---

# Template Cluster Summary

{top_table}

---

# Interpretation Notes

Higher structural risk scores indicate repeated SEO defects across a page family.

Primary template-level signals include:

- repeated short or missing titles
- repeated missing or weak meta descriptions
- repeated multiple H1 issues
- repeated missing image alt text
- repeated thin content
- weak internal linking

This report should be used to prioritize structural fixes before page-by-page edits.
"""

    write_markdown_report(output_md, summary, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nSEO TEMPLATE CLUSTER ANALYSIS COMPLETE\n")
    print(output_csv)
    print(output_md)


if __name__ == "__main__":
    main()