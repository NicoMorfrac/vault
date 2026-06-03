import re
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

REPORT_TYPE = "seo_search_console_merge"
SOURCE_AGENT = "SEO_Agent"


CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
SEARCH_CONSOLE_PATH = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Merged_Analysis"

TODAY = datetime.today().strftime("%Y-%m-%d")

# =========================================
# HELPERS
# =========================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def clean_url(url):
    if pd.isna(url):
        return ""

    url = str(url).strip().lower()

    url = url.replace("https://www.morfrac.com", "")
    url = url.replace("http://www.morfrac.com", "")
    url = url.replace("https://morfrac.com", "")
    url = url.replace("http://morfrac.com", "")

    if url.endswith("/") and url != "/":
        url = url[:-1]

    return url


def parse_search_console_md(md_file):
    text = md_file.read_text(encoding="utf-8", errors="ignore")

    start_marker = "## Query Page Mapping"
    start_index = text.find(start_marker)

    if start_index == -1:
        raise Exception("No '## Query Page Mapping' section found in Search Console report.")

    section = text[start_index + len(start_marker):]

    next_section = section.find("\n## ")

    if next_section != -1:
        section = section[:next_section]

    pattern = re.compile(
        r"\|\s*(?!-+)(.*?)\s*\|\s*(https?://[^\|]+)\s*\|\s*([0-9]+)\s*\|\s*([0-9]+)\s*\|\s*([0-9\.]+)%\s*\|\s*([0-9\.]+)\s*\|\s*(Branded|Non-branded)\s*\|"
    )

    rows = []

    for match in pattern.findall(section):
        query = match[0].strip()

        if query.lower() == "query":
            continue

        rows.append({
            "query": query,
            "page": match[1].strip(),
            "clicks": float(match[2]),
            "impressions": float(match[3]),
            "ctr_percent": float(match[4]),
            "position": float(match[5]),
            "query_type": match[6].strip(),
        })

    df = pd.DataFrame(rows)

    if df.empty:
        raise Exception("No Search Console query-page rows parsed from markdown.")

    return df


def opportunity_type(row):
    impressions = row["impressions"]
    ctr = row["ctr_percent"]
    position = row["position"]
    issues = str(row.get("issues", ""))

    if impressions > 100 and ctr < 1:
        return "Low CTR Opportunity"

    if impressions > 100 and 8 < position < 25:
        return "Ranking Improvement Opportunity"

    if impressions > 50 and "Weak internal linking" in issues:
        return "Internal Linking Opportunity"

    if impressions > 50 and "Thin content" in issues:
        return "Content Expansion Opportunity"

    if impressions > 50 and "Missing meta description" in issues:
        return "Metadata Optimization Opportunity"

    return ""


def priority_score(row):
    score = 0

    impressions = row["impressions"]
    clicks = row["clicks"]
    ctr = row["ctr_percent"]
    position = row["position"]

    business_priority = str(row.get("business_priority", ""))
    issue_count = row.get("issue_count", 0)

    score += min(impressions / 10, 50)
    score += min(clicks / 5, 20)

    if ctr < 1:
        score += 20

    if 5 <= position <= 20:
        score += 25

    if business_priority == "high":
        score += 30
    elif business_priority == "medium":
        score += 15

    score += issue_count * 3

    return round(score, 2)


# =========================================
# LOAD FILES
# =========================================


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    print("Loading crawl data...")

    crawl_file = latest_file(CRAWL_PATH, "*_site_crawl.csv")

    if not crawl_file:
        raise FileNotFoundError("No *_site_crawl.csv crawl file found.")

    crawl_df = pd.read_csv(crawl_file).fillna("")

    print(f"Crawl file: {crawl_file}")

    if "url" not in crawl_df.columns:
        raise Exception(f"Crawl file missing 'url' column: {crawl_file}")

    print("\nLoading Search Console markdown data...")

    sc_file = latest_file(SEARCH_CONSOLE_PATH, "*_SEO_Query_Analysis.md")

    if not sc_file:
        raise FileNotFoundError("No Search Console markdown report found.")

    print(f"Search Console file: {sc_file}")

    sc_df = parse_search_console_md(sc_file)

    parsed_debug = OUTPUT_PATH / f"{TODAY}_parsed_search_console_rows.csv"
    sc_df.to_csv(parsed_debug, index=False, encoding="utf-8-sig")

    print(f"Parsed Search Console rows: {len(sc_df)}")
    print(f"Parsed debug CSV: {parsed_debug}")

    # =========================================
    # STANDARDIZE URLS
    # =========================================

    crawl_df["url_clean"] = crawl_df["url"].apply(clean_url)
    sc_df["url_clean"] = sc_df["page"].apply(clean_url)

    # =========================================
    # AGGREGATE SEARCH CONSOLE BY PAGE
    # =========================================

    print("\nAggregating Search Console data...")

    sc_agg = (
        sc_df
        .groupby("url_clean", as_index=False)
        .agg({
            "clicks": "sum",
            "impressions": "sum",
            "ctr_percent": "mean",
            "position": "mean",
        })
    )

    # =========================================
    # MERGE
    # =========================================

    print("\nMerging datasets...")

    merged = crawl_df.merge(
        sc_agg,
        on="url_clean",
        how="left"
    )

    merged["clicks"] = merged["clicks"].fillna(0)
    merged["impressions"] = merged["impressions"].fillna(0)
    merged["ctr_percent"] = merged["ctr_percent"].fillna(0)
    merged["position"] = merged["position"].fillna(999)

    # =========================================
    # OPPORTUNITY LOGIC
    # =========================================

    merged["seo_opportunity"] = merged.apply(opportunity_type, axis=1)
    merged["seo_priority_score"] = merged.apply(priority_score, axis=1)

    priority_df = merged[
        merged["seo_opportunity"] != ""
    ].copy()

    priority_df = priority_df.sort_values(
        "seo_priority_score",
        ascending=False
    )

    # =========================================
    # EXPORT
    # =========================================

    csv_output = OUTPUT_PATH / f"{TODAY}_search_console_merge.csv"
    stable_csv = OUTPUT_PATH / "search_console_merge.csv"

    priority_df.to_csv(csv_output, index=False, encoding="utf-8-sig")
    priority_df.to_csv(stable_csv, index=False, encoding="utf-8-sig")

    top_rows = priority_df.head(50)

    table = "| Opportunity | Priority Score | Impressions | CTR % | Position | URL |\n"
    table += "|---|---:|---:|---:|---:|---|\n"

    for _, row in top_rows.iterrows():
        table += (
            f"| {row['seo_opportunity']} "
            f"| {row['seo_priority_score']} "
            f"| {int(row['impressions'])} "
            f"| {round(row['ctr_percent'], 2)} "
            f"| {round(row['position'], 1)} "
            f"| {row['url']} |\n"
        )

    report = f"""# Search Console Merge Analysis

    ## Generated

    {TODAY}

    ---

    # Summary

    - Crawl pages: {len(crawl_df)}
    - Search Console URLs parsed: {len(sc_agg)}
    - Opportunity pages: {len(priority_df)}

    ---

    # Top SEO Opportunities

    {table}

    ---

    # Opportunity Types

    - Low CTR Opportunity
    - Ranking Improvement Opportunity
    - Internal Linking Opportunity
    - Content Expansion Opportunity
    - Metadata Optimization Opportunity

    ---

    # Source Files

    - Crawl file: `{crawl_file}`
    - Search Console markdown: `{sc_file}`

    ---

    # Notes

    This report merges crawl quality, commercial priority, structural SEO issues, and Search Console page performance.

    It reads the existing Search Console markdown report directly, so no Search Console CSV export is required.
    """

    md_output = OUTPUT_PATH / f"{TODAY}_search_console_merge.md"
    stable_md = OUTPUT_PATH / "search_console_merge.md"

    write_markdown_report(md_output, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)
    write_markdown_report(stable_md, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    # =========================================
    # COMPLETE
    # =========================================

    print("\n================================================")
    print("SEARCH CONSOLE MERGE COMPLETE")
    print("================================================")
    print(f"Opportunity pages: {len(priority_df)}")
    print(f"CSV: {csv_output}")
    print(f"Markdown: {md_output}")
    print("================================================")

if __name__ == "__main__":
    main()
