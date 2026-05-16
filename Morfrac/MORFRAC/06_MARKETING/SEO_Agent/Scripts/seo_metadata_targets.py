from pathlib import Path
from datetime import datetime

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Metadata_Targets"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def latest_csv(path, pattern):
    files = list(path.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def classify_metadata_need(row):
    issues = str(row.get("issues", "")).lower()
    title_length = float(row.get("title_length", 0))
    meta_length = float(row.get("meta_description_length", 0))
    ctr_gap = float(row.get("ctr_gap", 0))

    needs = []

    if "missing title" in issues:
        needs.append("missing_title")

    if "short title" in issues or title_length < 30:
        needs.append("short_title")

    if "long title" in issues or title_length > 65:
        needs.append("long_title")

    if "missing meta description" in issues or meta_length == 0:
        needs.append("missing_meta")

    if "short meta description" in issues or (0 < meta_length < 80):
        needs.append("short_meta")

    if "long meta description" in issues or meta_length > 170:
        needs.append("long_meta")

    if ctr_gap >= 2:
        needs.append("serp_ctr_gap")

    return "; ".join(sorted(set(needs)))


def create_copy_brief(row):
    query = str(row.get("query", "")).strip()
    page = str(row.get("page", "")).strip()
    intent = str(row.get("intent", "")).strip()
    page_type = str(row.get("page_type", "")).strip()
    issues = str(row.get("issues", "")).strip()

    brief = []

    brief.append(f"Primary query: {query}")
    brief.append(f"Page type: {page_type}")
    brief.append(f"Intent: {intent}")

    if row.get("impressions", 0) >= 100:
        brief.append("High existing visibility; improve click capture.")

    if row.get("ctr_gap", 0) >= 2:
        brief.append("CTR is below expected for current ranking position.")

    if "short title" in issues.lower():
        brief.append("Title is too short; expand with commercial/search intent.")

    if "long title" in issues.lower():
        brief.append("Title is too long; shorten without losing product intent.")

    if "missing meta description" in issues.lower():
        brief.append("Meta description is missing; create a compelling commercial snippet.")

    if "short meta description" in issues.lower():
        brief.append("Meta description is too short; expand with value proposition.")

    if page_type == "product":
        brief.append("Emphasize product function, marine use case, and engineering reliability.")

    if page_type == "landing":
        brief.append("Position the page as an authority landing page and product gateway.")

    if page_type == "category":
        brief.append("Position as a product family/category discovery page.")

    if page_type == "blog":
        brief.append("If query is commercial, consider linking to or creating a commercial landing page.")

    return " ".join(brief)


def priority_label(score):
    score = float(score)

    if score >= 120:
        return "CRITICAL"

    if score >= 90:
        return "HIGH"

    if score >= 70:
        return "MEDIUM"

    return "LOW"


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    leverage_file = latest_csv(
        LEVERAGE_PATH,
        "*_seo_query_page_crawl_leverage_opportunities.csv"
    )

    if not leverage_file:
        print("No query-page-crawl leverage CSV found.")
        return

    print("\nUsing leverage file:")
    print(leverage_file)

    df = pd.read_csv(leverage_file)

    if df.empty:
        print("Leverage CSV is empty.")
        return

    required_cols = [
        "query",
        "page",
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
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # Select only meaningful metadata targets
    targets = df[
        (
            (df["opportunity_score"] >= 70)
            | (df["ctr_gap"] >= 2)
            | (df["impressions"] >= 25)
        )
    ].copy()

    if targets.empty:
        print("No metadata targets found.")
        return

    targets["metadata_need"] = targets.apply(classify_metadata_need, axis=1)
    targets["copy_brief"] = targets.apply(create_copy_brief, axis=1)
    targets["priority"] = targets["opportunity_score"].apply(priority_label)

    # Keep rows where metadata work is justified
    targets = targets[
        (targets["metadata_need"] != "")
        | (targets["ctr_gap"] >= 2)
        | (targets["opportunity_score"] >= 90)
    ].copy()

    targets = targets.sort_values(
        ["opportunity_score", "impressions", "ctr_gap"],
        ascending=False
    )

    output_csv = OUTPUT_PATH / f"{run_date}_seo_metadata_targets.csv"
    output_md = OUTPUT_PATH / f"{run_date}_seo_metadata_targets.md"

    export_columns = [
        "priority",
        "query",
        "page",
        "impressions",
        "ctr_percent",
        "expected_ctr",
        "ctr_gap",
        "position",
        "intent",
        "page_type",
        "title_length",
        "meta_description_length",
        "issues",
        "metadata_need",
        "copy_brief",
        "opportunity_score",
    ]

    export_columns = [col for col in export_columns if col in targets.columns]

    final_df = targets[export_columns].copy()

    final_df.to_csv(output_csv, index=False)

    table = final_df.head(30).to_markdown(index=False)

    report = f"""# SEO Metadata Targets

## Generated

{run_date}

## Purpose

This report identifies pages that should receive metadata rewrites or SERP snippet optimization.

It does not generate final SEO copy.

It prepares structured targets for the SEO Agent to write:

- optimized title tags
- meta descriptions
- H1 recommendations
- SERP positioning rationale

---

# Metadata Rewrite Targets

{table}

---

# Usage

Feed this report into the SEO Agent.

The agent should generate final metadata recommendations using:

- the primary query
- page type
- commercial intent
- CTR gap
- crawl issues
- MORFRAC positioning
- engineering authority context

---

# Output Files

- CSV: {output_csv}
- Markdown: {output_md}
"""

    output_md.write_text(report, encoding="utf-8")

    print("\nSEO METADATA TARGETS COMPLETE\n")
    print(output_csv)
    print(output_md)


if __name__ == "__main__":
    main()