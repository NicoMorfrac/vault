from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Indexation_Audit"

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
    return safe_text(url).rstrip("/").lower()


def classify_indexation_risk(row):
    url = normalize_url(row.get("url", ""))
    canonical = normalize_url(row.get("canonical", ""))
    robots = safe_text(row.get("robots", "")).lower()
    status_code = row.get("status_code", "")
    page_type = safe_text(row.get("page_type", "")).lower()

    risks = []

    # =========================================
    # URL PATTERN RISKS
    # =========================================

    low_value_patterns = [
        "/blog/tag/",
        "/page/",
        "/wishlist",
        "/document/",
        "/website/social/",
        "/cookie",
        "/privacy",
        "/terms",
        "/returns",
        "/shop/page/",
    ]

    for pattern in low_value_patterns:
        if pattern in url:
            risks.append("likely_low_value_indexable")

    # =========================================
    # CANONICAL RISKS
    # =========================================

    if not canonical:
        risks.append("missing_canonical")

    elif canonical != url:
        risks.append("canonical_mismatch")

    if canonical and canonical == url:
        risks.append("self_canonical")

    # =========================================
    # ROBOTS RISKS
    # =========================================

    if "noindex" in robots:
        risks.append("noindex")

    if "nofollow" in robots:
        risks.append("nofollow")

    # =========================================
    # STATUS RISKS
    # =========================================

    if status_code != 200:
        risks.append("non_200")

    # =========================================
    # DUPLICATE STRUCTURE RISKS
    # =========================================

    if "/shop/category/" in url and "/shop/" in url:
        risks.append("category_product_overlap")

    if "/es/" in url:
        risks.append("multilingual_duplicate_candidate")

    # =========================================
    # PAGINATION RISKS
    # =========================================

    if "/page/" in url:
        risks.append("pagination_indexation")

    # =========================================
    # DOCUMENT RISKS
    # =========================================

    if "/document/" in url or "/documents/" in url:
        risks.append("document_indexation")

    return "; ".join(sorted(set(risks)))


def classify_priority(risk_string):
    risk_string = safe_text(risk_string)

    critical_terms = [
        "canonical_mismatch",
        "document_indexation",
        "category_product_overlap",
    ]

    high_terms = [
        "pagination_indexation",
        "likely_low_value_indexable",
        "missing_canonical",
    ]

    for term in critical_terms:
        if term in risk_string:
            return "CRITICAL"

    for term in high_terms:
        if term in risk_string:
            return "HIGH"

    return "MEDIUM"


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    crawl_file = latest_csv(CRAWL_PATH, "*_site_crawl.csv")

    if not crawl_file:
        print("No crawl CSV found.")
        return

    print("\nUsing crawl file:")
    print(crawl_file)

    df = pd.read_csv(crawl_file)

    if df.empty:
        print("Crawl CSV is empty.")
        return

    required_cols = [
        "url",
        "canonical",
        "robots",
        "status_code",
        "page_type",
        "business_priority",
        "indexable",
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    df["indexation_risks"] = df.apply(classify_indexation_risk, axis=1)

    audit_df = df[
        df["indexation_risks"] != ""
    ].copy()

    if audit_df.empty:
        print("No indexation risks detected.")
        return

    audit_df["priority"] = audit_df["indexation_risks"].apply(classify_priority)

    audit_df = audit_df.sort_values(
        ["priority", "business_priority"],
        ascending=[True, False]
    )

    export_columns = [
        "priority",
        "url",
        "page_type",
        "business_priority",
        "indexable",
        "status_code",
        "canonical",
        "robots",
        "indexation_risks",
    ]

    export_columns = [
        c for c in export_columns
        if c in audit_df.columns
    ]

    final_df = audit_df[export_columns].copy()

    output_csv = OUTPUT_PATH / f"{run_date}_indexation_audit.csv"
    output_md = OUTPUT_PATH / f"{run_date}_indexation_audit.md"

    final_df.to_csv(output_csv, index=False)

    summary = (
        final_df.groupby("priority", as_index=False)
        .agg(
            affected_urls=("url", "count")
        )
        .sort_values("affected_urls", ascending=False)
    )

    summary_table = summary.to_markdown(index=False)

    top_rows = final_df.head(50).to_markdown(index=False)

    report = f"""# SEO Indexation Audit

## Generated

{run_date}

## Purpose

This report identifies likely indexation inefficiencies and crawl waste.

It detects:

- likely low-value indexable URLs
- canonical inconsistencies
- pagination indexation
- document URL indexation
- multilingual duplicate candidates
- category/product overlap
- missing canonical signals

---

# Input Crawl

{crawl_file}

---

# Risk Summary

{summary_table}

---

# Highest Priority Indexation Risks

{top_rows}

---

# Interpretation Notes

This report does not automatically mean URLs should be deindexed.

Priority should focus on URLs that:

- dilute authority
- compete with stronger canonical targets
- create crawl waste
- expose duplicate paths
- reduce query clarity
- create unnecessary index bloat

Common Odoo SEO risks include:

- category/product duplicate routing
- paginated archives
- tag archives
- document share URLs
- duplicated multilingual structures
- weak canonical consistency

---

# Output Files

- CSV: {output_csv}
- Markdown: {output_md}
"""

    output_md.write_text(report, encoding="utf-8")

    print("\nSEO INDEXATION AUDIT COMPLETE\n")
    print(output_csv)
    print(output_md)


if __name__ == "__main__":
    main()