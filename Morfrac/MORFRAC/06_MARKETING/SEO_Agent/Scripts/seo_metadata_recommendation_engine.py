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

REPORT_TYPE = "seo_metadata_recommendations"
SOURCE_AGENT = "SEO_Agent"


METADATA_TARGETS_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Metadata_Targets"
LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Metadata_Recommendations"

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


def title_case_query(query):
    query = safe_text(query)
    return " ".join(word.capitalize() for word in query.split())


def classify_product_family(row):
    text = f"{row.get('query', '')} {row.get('page', '')}".lower()

    if "dogbone" in text or "dog bone" in text:
        return "dogbone"

    if "mloop" in text or "m loop" in text:
        return "mloop"

    if "shackle" in text:
        return "shackle"

    if "padeye" in text or "pad eye" in text or "cancamo" in text or "cáncamo" in text:
        return "padeye"

    if "powerfurl" in text or "furler" in text or "furling" in text:
        return "powerfurl"

    if "morfblock" in text or "morf block" in text:
        return "morfblock"

    if "morfring" in text or "friction ring" in text:
        return "morfring"

    if "mreel" in text:
        return "mreel"

    if "hoistlock" in text or "gaff lock" in text:
        return "hoistlock"

    return "general"


def generate_title(row):
    query = safe_text(row.get("query", ""))
    page_type = safe_text(row.get("page_type", "")).lower()
    family = classify_product_family(row)

    q = title_case_query(query)

    if family == "dogbone":
        return "Dogbone Connectors for Sailing Rigging | MORFRAC"

    if family == "mloop":
        return "Mloop Dyneema Loops for Sailing Hardware | MORFRAC"

    if family == "shackle":
        return "Titanium Shackles for High-Load Sailing Hardware | MORFRAC"

    if family == "padeye":
        return "Padeyes for High-Performance Sailing Hardware | MORFRAC"

    if family == "powerfurl":
        return "Powerfurl Furling Systems for Performance Sailing | MORFRAC"

    if family == "morfblock":
        return "Morfblock Lightweight Sailing Blocks | MORFRAC"

    if family == "morfring":
        return "Morfring Friction Rings for Sailing Systems | MORFRAC"

    if family == "mreel":
        return "Mreel Rope Management Systems for Sailing | MORFRAC"

    if family == "hoistlock":
        return "Hoistlock Halyard Lock Systems for Sailing | MORFRAC"

    if page_type == "blog":
        return f"{q} Technical Guide | MORFRAC"

    if page_type == "product":
        return f"{q} for Sailing Hardware | MORFRAC"

    if page_type == "landing":
        return f"{q} for Performance Sailing | MORFRAC"

    return f"{q} | MORFRAC"


def generate_meta(row):
    query = safe_text(row.get("query", ""))
    family = classify_product_family(row)
    page_type = safe_text(row.get("page_type", "")).lower()

    if family == "dogbone":
        return "Discover MORFRAC dogbone connectors for soft shackles, textile rigging and high-performance sailing hardware. Lightweight, reliable and engineered for demanding marine use."

    if family == "mloop":
        return "Explore MORFRAC Mloop Dyneema loops for clean, strong and lightweight sailing hardware connections. Designed for performance rigging and simple onboard integration."

    if family == "shackle":
        return "High-load MORFRAC shackles for sailing hardware applications. Engineered for strength, corrosion resistance and reliable performance in demanding marine systems."

    if family == "padeye":
        return "MORFRAC padeyes for performance sailing applications, including lightweight deck hardware solutions engineered for strength, reliability and clean integration."

    if family == "powerfurl":
        return "MORFRAC Powerfurl systems deliver simple, reliable and lightweight furling solutions for performance sailing, offshore use and modern sail handling."

    if family == "morfblock":
        return "MORFRAC Morfblock sailing blocks combine lightweight construction, high-load capability and clean textile integration for performance marine hardware systems."

    if family == "morfring":
        return "MORFRAC Morfring friction rings provide lightweight, low-maintenance solutions for textile rigging, control lines and high-performance sailing systems."

    if family == "mreel":
        return "MORFRAC Mreel rope management systems help organize lines cleanly and efficiently on performance sailing boats and custom deck layouts."

    if family == "hoistlock":
        return "MORFRAC Hoistlock systems provide high-load sail locking solutions for performance mainsail handling, halyard load reduction and reliable offshore use."

    if page_type == "blog":
        return f"Technical information from MORFRAC about {query}, with engineering context, marine applications and practical performance sailing insights."

    return f"Explore MORFRAC solutions for {query}, engineered for high-performance sailing hardware, technical reliability and clean marine system integration."


def confidence_score(row):
    score = 0

    if float(row.get("opportunity_score", 0)) >= 100:
        score += 35
    elif float(row.get("opportunity_score", 0)) >= 75:
        score += 25

    if float(row.get("impressions", 0)) >= 100:
        score += 25
    elif float(row.get("impressions", 0)) >= 25:
        score += 15

    if float(row.get("ctr_gap", 0)) >= 2:
        score += 20

    if safe_text(row.get("intent", "")).lower() in ["commercial", "product_code", "product_brand"]:
        score += 20

    return min(score, 100)


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    metadata_file = latest_csv(
        METADATA_TARGETS_PATH,
        "*_seo_metadata_targets.csv"
    )

    if not metadata_file:
        print("No metadata targets CSV found.")
        return

    print("\nUsing metadata targets file:")
    print(metadata_file)

    df = pd.read_csv(metadata_file)

    if df.empty:
        print("Metadata targets file is empty.")
        return

    df["recommended_title"] = df.apply(generate_title, axis=1)
    df["recommended_meta_description"] = df.apply(generate_meta, axis=1)
    df["product_family"] = df.apply(classify_product_family, axis=1)
    df["recommendation_confidence"] = df.apply(confidence_score, axis=1)

    df["title_length_recommended"] = df["recommended_title"].apply(len)
    df["meta_length_recommended"] = df["recommended_meta_description"].apply(len)

    output_csv = OUTPUT_PATH / f"{run_date}_seo_metadata_recommendations.csv"
    output_md = OUTPUT_PATH / f"{run_date}_seo_metadata_recommendations.md"

    export_columns = [
        "priority",
        "product_family",
        "query",
        "page",
        "impressions",
        "ctr_percent",
        "expected_ctr",
        "ctr_gap",
        "position",
        "intent",
        "page_type",
        "metadata_need",
        "recommended_title",
        "title_length_recommended",
        "recommended_meta_description",
        "meta_length_recommended",
        "recommendation_confidence",
        "opportunity_score",
    ]

    export_columns = [c for c in export_columns if c in df.columns]

    final_df = df[export_columns].sort_values(
        ["recommendation_confidence", "opportunity_score", "impressions"],
        ascending=False
    )

    final_df.to_csv(output_csv, index=False)

    table = final_df.head(30).to_markdown(index=False)

    report = f"""# SEO Metadata Recommendations

## Generated

{run_date}

## Purpose

This report generates review-ready SEO metadata recommendations.

It uses deterministic metadata targets and converts them into proposed:

- title tags
- meta descriptions
- product-family positioning
- confidence scores

These recommendations are not automatically published.

They should be reviewed before implementation.

---

# Metadata Recommendations

{table}

---

# Review Rules

Before implementation, verify:

- title is accurate for the actual page
- title is not keyword-stuffed
- meta description matches the product/page content
- technical claims are true
- product family is correctly classified
- Spanish pages may require Spanish-language metadata

---

# Output Files

- CSV: {output_csv}
- Markdown: {output_md}
"""

    write_markdown_report(output_md, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nSEO METADATA RECOMMENDATIONS COMPLETE\n")
    print(output_csv)
    print(output_md)


if __name__ == "__main__":
    main()