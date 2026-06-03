from pathlib import Path
import sys
from datetime import datetime

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_duplicate_content_report"
SOURCE_AGENT = "SEO_Agent"


CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Duplicate_Content"

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


def normalize_text(value):
    return safe_text(value).lower()


def classify_duplicate_severity(count):
    if count >= 20:
        return "CRITICAL"

    if count >= 10:
        return "HIGH"

    if count >= 5:
        return "MEDIUM"

    if count >= 2:
        return "LOW"

    return "NONE"


def duplicate_group_report(df, field_name):
    if df.empty or field_name not in df.columns:
        return pd.DataFrame()

    temp = df.copy()
    temp[f"{field_name}_clean"] = temp[field_name].apply(normalize_text)

    temp = temp[temp[f"{field_name}_clean"] != ""]

    grouped = (
        temp.groupby(f"{field_name}_clean", as_index=False)
        .agg(
            duplicate_count=("url", "count"),
            urls=("url", lambda x: " | ".join(sorted(set(map(str, x)))[:20])),
            page_types=("page_type", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            business_priorities=("business_priority", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
        )
    )

    grouped = grouped[grouped["duplicate_count"] > 1].copy()

    if grouped.empty:
        return grouped

    grouped["severity"] = grouped["duplicate_count"].apply(classify_duplicate_severity)

    grouped = grouped.sort_values(
        ["duplicate_count"],
        ascending=False
    )

    grouped = grouped.rename(columns={
        f"{field_name}_clean": field_name
    })

    return grouped


def detect_query_cannibalization(leverage_df):
    if leverage_df.empty:
        return pd.DataFrame()

    required = ["query", "page", "impressions", "clicks", "position", "intent", "page_type"]

    for col in required:
        if col not in leverage_df.columns:
            leverage_df[col] = ""

    grouped = (
        leverage_df.groupby("query", as_index=False)
        .agg(
            ranking_pages=("page", lambda x: " | ".join(sorted(set(map(str, x)))[:20])),
            page_count=("page", lambda x: len(set(map(str, x)))),
            total_impressions=("impressions", "sum"),
            total_clicks=("clicks", "sum"),
            best_position=("position", "min"),
            intents=("intent", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            page_types=("page_type", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
        )
    )

    grouped = grouped[grouped["page_count"] > 1].copy()

    if grouped.empty:
        return grouped

    grouped["severity"] = grouped["page_count"].apply(classify_duplicate_severity)

    grouped = grouped.sort_values(
        ["total_impressions", "page_count"],
        ascending=False
    )

    return grouped


def detect_product_category_overlap(leverage_df):
    if leverage_df.empty:
        return pd.DataFrame()

    required = ["query", "page", "page_type", "impressions", "position", "intent"]

    for col in required:
        if col not in leverage_df.columns:
            leverage_df[col] = ""

    temp = leverage_df.copy()

    grouped = (
        temp.groupby("query", as_index=False)
        .agg(
            pages=("page", lambda x: " | ".join(sorted(set(map(str, x)))[:20])),
            page_types=("page_type", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
            page_count=("page", lambda x: len(set(map(str, x)))),
            impressions=("impressions", "sum"),
            best_position=("position", "min"),
            intent=("intent", lambda x: " | ".join(sorted(set(map(str, x)))[:10])),
        )
    )

    def has_overlap(types):
        types = str(types).lower()
        return (
            ("product" in types and "category" in types)
            or ("product" in types and "landing" in types)
            or ("category" in types and "landing" in types)
            or ("blog" in types and "product" in types)
        )

    grouped = grouped[grouped["page_types"].apply(has_overlap)].copy()

    grouped = grouped.sort_values(
        ["impressions", "page_count"],
        ascending=False
    )

    return grouped


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
        print("No crawl CSV found.")
        return

    print("\nUsing crawl file:")
    print(crawl_file)

    crawl_df = pd.read_csv(crawl_file)

    if crawl_df.empty:
        print("Crawl CSV is empty.")
        return

    if leverage_file:
        print("\nUsing leverage file:")
        print(leverage_file)
        leverage_df = pd.read_csv(leverage_file)
    else:
        print("\nNo leverage file found. Cannibalization analysis skipped.")
        leverage_df = pd.DataFrame()

    for col in ["url", "title", "meta_description", "h1", "page_type", "business_priority"]:
        if col not in crawl_df.columns:
            crawl_df[col] = ""

    duplicate_titles = duplicate_group_report(crawl_df, "title")
    duplicate_meta = duplicate_group_report(crawl_df, "meta_description")
    duplicate_h1 = duplicate_group_report(crawl_df, "h1")

    cannibalization_candidates = detect_query_cannibalization(leverage_df)
    product_category_overlap = detect_product_category_overlap(leverage_df)

    output_titles_csv = OUTPUT_PATH / f"{run_date}_duplicate_titles.csv"
    output_meta_csv = OUTPUT_PATH / f"{run_date}_duplicate_meta_descriptions.csv"
    output_h1_csv = OUTPUT_PATH / f"{run_date}_duplicate_h1.csv"
    output_cannibal_csv = OUTPUT_PATH / f"{run_date}_cannibalization_candidates.csv"
    output_overlap_csv = OUTPUT_PATH / f"{run_date}_product_category_overlap.csv"
    output_md = OUTPUT_PATH / f"{run_date}_duplicate_content_report.md"

    duplicate_titles.to_csv(output_titles_csv, index=False)
    duplicate_meta.to_csv(output_meta_csv, index=False)
    duplicate_h1.to_csv(output_h1_csv, index=False)
    cannibalization_candidates.to_csv(output_cannibal_csv, index=False)
    product_category_overlap.to_csv(output_overlap_csv, index=False)

    duplicate_titles_table = (
        duplicate_titles.head(20).to_markdown(index=False)
        if not duplicate_titles.empty
        else "_No duplicate title groups detected._"
    )

    duplicate_meta_table = (
        duplicate_meta.head(20).to_markdown(index=False)
        if not duplicate_meta.empty
        else "_No duplicate meta description groups detected._"
    )

    duplicate_h1_table = (
        duplicate_h1.head(20).to_markdown(index=False)
        if not duplicate_h1.empty
        else "_No duplicate H1 groups detected._"
    )

    cannibal_table = (
        cannibalization_candidates.head(20).to_markdown(index=False)
        if not cannibalization_candidates.empty
        else "_No query cannibalization candidates detected._"
    )

    overlap_table = (
        product_category_overlap.head(20).to_markdown(index=False)
        if not product_category_overlap.empty
        else "_No product/category overlap candidates detected._"
    )

    report = f"""# SEO Duplicate Content Analysis

## Generated

{run_date}

## Purpose

This report identifies duplicate and overlapping SEO signals that may weaken search clarity.

It detects:

- duplicate title groups
- duplicate meta description groups
- duplicate H1 groups
- query cannibalization candidates
- product/category/landing overlap candidates

---

# Input Files

Crawl file:

{crawl_file}

Leverage file:

{leverage_file if leverage_file else "No leverage file used."}

---

# Duplicate Title Groups

{duplicate_titles_table}

---

# Duplicate Meta Description Groups

{duplicate_meta_table}

---

# Duplicate H1 Groups

{duplicate_h1_table}

---

# Query Cannibalization Candidates

{cannibal_table}

---

# Product / Category / Landing Overlap Candidates

{overlap_table}

---

# Interpretation Notes

Duplicate metadata is not automatically a critical issue.

Priority should be assigned when duplicate signals affect:

- commercial product pages
- category pages
- high-impression pages
- pages ranking for the same query
- multilingual equivalents without clear intent separation
- product/category/landing page overlap

Focus first on duplicates that reduce search intent clarity or split authority across competing URLs.

---

# Output Files

- Duplicate titles: {output_titles_csv}
- Duplicate meta descriptions: {output_meta_csv}
- Duplicate H1: {output_h1_csv}
- Cannibalization candidates: {output_cannibal_csv}
- Product/category overlap: {output_overlap_csv}
- Report: {output_md}
"""

    write_markdown_report(output_md, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nSEO DUPLICATE CONTENT ANALYSIS COMPLETE\n")
    print(output_titles_csv)
    print(output_meta_csv)
    print(output_h1_csv)
    print(output_cannibal_csv)
    print(output_overlap_csv)
    print(output_md)


if __name__ == "__main__":
    main()