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

REPORT_TYPE = "seo_leverage_report"
SOURCE_AGENT = "SEO_Agent"


SEARCH_CONSOLE_PATH = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"
CRAWL_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"

# =========================================
# HELPERS
# =========================================

def latest_md(path):
    files = list(path.glob("*.md"))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def latest_site_crawl(path):
    files = list(path.glob("*_site_crawl.csv"))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def normalize_url(url):
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


def classify_opportunity(score):
    if score >= 100:
        return "VERY HIGH"
    if score >= 75:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"
    return "LOW"


def clean_query(query):
    return str(query).strip().lower()


def clean_page(page):
    return str(page).strip().lower()


def is_junk_query(query):
    query = str(query).lower()

    junk_patterns = [
        "inurl:",
        "bart ",
        "como se llama",
        "ahora ",
    ]

    for pattern in junk_patterns:
        if pattern in query:
            return True

    return False


def classify_intent(query):
    query = str(query).lower().strip()

    product_brand_keywords = [
        "morfblock",
        "morf block",
        "powerfurl",
        "mreel",
        "m reel",
        "morfring",
        "morfwing",
    ]

    commercial_keywords = [
        "shackle",
        "padeye",
        "pad eye",
        "dogbone",
        "dogbones",
        "dog bone",
        "dog bones",
        "rigging",
        "torlon",
        "farr",
        "cancamo",
        "cáncamo",
        "mloop",
        "m loop",
    ]

    product_code_patterns = [
        r"^\d{2}-\d{2}$",
        r"^\d{2}xl$",
        r"^mor[-\s]?\d{3}$",
    ]

    for keyword in product_brand_keywords:
        if keyword in query:
            return "product_brand"

    for keyword in commercial_keywords:
        if keyword in query:
            return "commercial"

    for pattern in product_code_patterns:
        if re.match(pattern, query):
            return "product_code"

    return "unknown"


def classify_page_type(page):
    page = str(page).lower()

    if "/shop/category/" in page:
        return "category"

    if "/shop/" in page:
        return "product"

    if "/blog/" in page:
        return "blog"

    if (
        "/dogbone" in page
        or "/padeye" in page
        or "/shackle" in page
        or "/powerfurl" in page
    ):
        return "landing"

    if page.endswith("/shop"):
        return "shop"

    if page.endswith("/"):
        return "home"

    return "other"


def expected_ctr(position):
    if position <= 1:
        return 28
    elif position <= 2:
        return 15
    elif position <= 3:
        return 10
    elif position <= 4:
        return 7
    elif position <= 5:
        return 5
    elif position <= 6:
        return 4
    elif position <= 7:
        return 3.5
    elif position <= 8:
        return 3
    elif position <= 9:
        return 2.5
    elif position <= 10:
        return 2
    elif position <= 15:
        return 1
    elif position <= 20:
        return 0.8
    elif position <= 30:
        return 0.6
    elif position <= 40:
        return 0.4
    return 0.2


# =========================================
# LOAD FILES
# =========================================


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    seo_md = latest_md(SEARCH_CONSOLE_PATH)

    if not seo_md:
        print("No Search Console report found.")
        raise SystemExit

    seo_text = seo_md.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    print("\nUsing Search Console file:")
    print(seo_md)

    crawl_csv = latest_site_crawl(CRAWL_PATH)

    if not crawl_csv:
        print("No *_site_crawl.csv file found.")
        raise SystemExit

    print("\nUsing crawl file:")
    print(crawl_csv)

    crawl_df = pd.read_csv(crawl_csv)

    if "url" not in crawl_df.columns:
        raise Exception(
            f"Crawl file does not contain required 'url' column:\n{crawl_csv}\n\n"
            f"Columns found:\n{list(crawl_df.columns)}"
        )

    # =========================================
    # ISOLATE QUERY PAGE MAPPING SECTION ONLY
    # =========================================

    start_marker = "## Query Page Mapping"
    end_marker = "##"

    start_index = seo_text.find(start_marker)

    if start_index == -1:
        print("No Query Page Mapping section found.")
        raise SystemExit

    section_text = seo_text[start_index + len(start_marker):]

    next_section_index = section_text.find(end_marker)

    if next_section_index != -1:
        section_text = section_text[:next_section_index]

    # =========================================
    # PARSE QUERY PAGE DATA
    # =========================================

    rows = []

    pattern = re.compile(
        r"\|\s*(?!-+)(.*?)\s*\|\s*(https?://[^\|]+)\s*\|\s*([0-9]+)\s*\|\s*([0-9]+)\s*\|\s*([0-9\.]+)%\s*\|\s*([0-9\.]+)\s*\|\s*(Branded|Non-branded)\s*\|"
    )

    matches = pattern.findall(section_text)

    for match in matches:
        query = match[0].strip()
        page = match[1].strip()

        if query.lower() == "query":
            continue

        rows.append({
            "query": query,
            "query_clean": clean_query(query),
            "page": page,
            "page_clean": clean_page(page),
            "clicks": float(match[2]),
            "impressions": float(match[3]),
            "ctr_percent": float(match[4]),
            "position": float(match[5]),
            "query_type": match[6].strip(),
        })

    seo_df = pd.DataFrame(rows)

    if seo_df.empty:
        print("No Query Page Mapping rows parsed.")
        raise SystemExit

    # =========================================
    # NORMALIZE URLS + MERGE CRAWL DATA
    # =========================================

    seo_df["normalized_url"] = seo_df["page"].apply(normalize_url)
    crawl_df["normalized_url"] = crawl_df["url"].apply(normalize_url)

    seo_df = seo_df.drop_duplicates(
        subset=["query_clean", "page_clean"],
        keep="first"
    )

    seo_df = pd.merge(
        seo_df,
        crawl_df,
        on="normalized_url",
        how="left"
    )

    # =========================================
    # DEBUG UNMATCHED CRAWL URLS
    # =========================================

    debug_unmatched = seo_df[
        seo_df["url"].isna()
    ][[
        "query",
        "page",
        "normalized_url"
    ]].copy()

    debug_file = OUTPUT_PATH / f"{datetime.today().strftime('%Y-%m-%d')}_unmatched_query_pages.csv"

    debug_unmatched.to_csv(
        debug_file,
        index=False
    )

    print("\nUnmatched query-page URLs:")
    print(len(debug_unmatched))
    print(debug_file)

    # =========================================
    # FILTER NON-BRANDED ONLY
    # =========================================

    seo_df = seo_df[
        seo_df["query_type"].str.lower() == "non-branded"
    ].copy()

    if seo_df.empty:
        print("No non-branded query-page rows found.")
        raise SystemExit

    # =========================================
    # FILTER JUNK QUERIES
    # =========================================

    seo_df = seo_df[
        ~seo_df["query"].apply(is_junk_query)
    ].copy()

    if seo_df.empty:
        print("No non-branded non-junk query-page rows found.")
        raise SystemExit

    # =========================================
    # FILTER LOW IMPRESSION NOISE
    # =========================================

    seo_df = seo_df[
        seo_df["impressions"] >= 5
    ].copy()

    if seo_df.empty:
        print("No query-page rows remaining after impression filtering.")
        raise SystemExit

    # =========================================
    # CLASSIFY INTENT + PAGE TYPE
    # =========================================

    seo_df["intent"] = seo_df["query"].apply(classify_intent)
    seo_df["page_type"] = seo_df["page"].apply(classify_page_type)

    # =========================================
    # EXPECTED CTR + CTR GAP
    # =========================================

    seo_df["expected_ctr"] = seo_df["position"].apply(expected_ctr)

    seo_df["ctr_gap"] = (
        seo_df["expected_ctr"] -
        seo_df["ctr_percent"]
    )

    # =========================================
    # FILL MISSING CRAWL VALUES
    # =========================================

    for col in [
        "issue_count",
        "title_length",
        "meta_description_length",
    ]:
        if col not in seo_df.columns:
            seo_df[col] = 0

    seo_df["issue_count"] = seo_df["issue_count"].fillna(0)
    seo_df["title_length"] = seo_df["title_length"].fillna(0)
    seo_df["meta_description_length"] = seo_df["meta_description_length"].fillna(0)

    if "issues" not in seo_df.columns:
        seo_df["issues"] = ""

    seo_df["issues"] = seo_df["issues"].fillna("")

    # =========================================
    # OPPORTUNITY SCORING
    # =========================================

    scores = []

    for _, row in seo_df.iterrows():
        score = 0

        impressions = row.get("impressions", 0)
        position = row.get("position", 100)
        intent = row.get("intent", "unknown")
        page_type = row.get("page_type", "other")
        ctr_gap = row.get("ctr_gap", 0)

        issue_count = row.get("issue_count", 0)
        title_length = row.get("title_length", 0)
        meta_length = row.get("meta_description_length", 0)

        # Visibility
        if impressions >= 25:
            score += 10

        if impressions >= 100:
            score += 20

        if impressions >= 500:
            score += 20

        # CTR gap opportunity
        if ctr_gap >= 3:
            score += 30
        elif ctr_gap >= 2:
            score += 20
        elif ctr_gap >= 1:
            score += 10

        # Ranking opportunity
        if 4 <= position <= 15:
            score += 25
        elif 15 < position <= 25:
            score += 15
        elif 25 < position <= 40:
            score += 5

        # Intent weighting
        if intent == "commercial":
            score += 30
        elif intent == "product_code":
            score += 20
        elif intent == "product_brand":
            score += 15

        # Page type weighting
        if page_type == "product":
            score += 15
        elif page_type == "category":
            score += 12
        elif page_type == "landing":
            score += 10
        elif page_type == "shop":
            score += 5
        elif page_type == "blog":
            score -= 5

        # Crawl weakness
        score += min(issue_count * 2, 20)

        if title_length < 30:
            score += 10

        if meta_length < 80:
            score += 10

        scores.append(score)

    seo_df["opportunity_score"] = scores

    seo_df["opportunity_level"] = seo_df[
        "opportunity_score"
    ].apply(classify_opportunity)

    # =========================================
    # SORT
    # =========================================

    seo_df = seo_df.sort_values(
        "opportunity_score",
        ascending=False
    )

    # =========================================
    # OUTPUT
    # =========================================

    run_date = datetime.today().strftime("%Y-%m-%d")

    output_csv = OUTPUT_PATH / f"{run_date}_seo_query_page_crawl_leverage_opportunities.csv"
    output_md = OUTPUT_PATH / f"{run_date}_seo_query_page_crawl_leverage_opportunities.md"

    export_columns = [
        "query",
        "page",
        "clicks",
        "impressions",
        "ctr_percent",
        "expected_ctr",
        "ctr_gap",
        "position",
        "query_type",
        "intent",
        "page_type",
        "issue_count",
        "title_length",
        "meta_description_length",
        "issues",
        "opportunity_score",
        "opportunity_level",
    ]

    final_df = seo_df[export_columns].copy()

    final_df.to_csv(
        output_csv,
        index=False,
        encoding="utf-8-sig"
    )

    # =========================================
    # MARKDOWN REPORT
    # =========================================

    top_df = final_df.head(30)

    table = top_df.to_markdown(index=False)

    summary = f"""# SEO Query-Page-Crawl Leverage Opportunity Report

    ## Generated

    {run_date}

    ## Summary

    This report correlates:

    - Search Console query-page performance
    - crawl metadata
    - CTR gap
    - ranking opportunity
    - commercial intent
    - page type relevance

    Current filters applied:

    - non-branded query-page rows only
    - duplicate query-page removal
    - obvious junk-query filtering
    - minimum impression threshold
    - deterministic intent classification
    - page-type classification
    - expected CTR and CTR gap scoring
    - crawl metadata correlation

    This report connects:

    query → ranking page → crawl issues → opportunity score

    ---

    # Highest Leverage Query-Page-Crawl Opportunities

    {table}

    ---

    # Interpretation Notes

    Higher opportunity scores indicate:

    - existing search visibility
    - CTR below expected for current ranking position
    - near-page-one ranking potential
    - commercial/product intent
    - relevant page type
    - metadata or crawl weakness
    - non-branded discovery potential

    CTR gap means:

    expected CTR minus actual CTR.

    Intent categories:

    - commercial = generic high-intent product/service discovery
    - product_code = MORFRAC/product-size code discovery
    - product_brand = MORFRAC product-brand discovery
    - unknown = insufficient deterministic intent signal

    Page types:

    - product = direct product page
    - category = product category page
    - landing = commercial landing page
    - shop = generic shop page
    - blog = article/news content
    - other = uncategorized

    This is the Search Console + crawl correlation leverage report.

    ---

    # Source Files

    - Search Console report: `{seo_md}`
    - Crawl file: `{crawl_csv}`
    - Unmatched query-page debug file: `{debug_file}`
    """

    write_markdown_report(output_md, summary, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nSEO QUERY-PAGE-CRAWL LEVERAGE ANALYSIS COMPLETE\n")
    print(output_csv)
    print(output_md)

if __name__ == "__main__":
    main()
