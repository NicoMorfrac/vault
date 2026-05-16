from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

CRAWL_DIR = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
LEVERAGE_DIR = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"

OUTPUT_DIR = BASE_PATH / r"06_MARKETING\SEO_Agent\Internal_Linking"

# =========================================
# LOAD FILES
# =========================================


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    crawl_files = sorted(CRAWL_DIR.glob("*_site_crawl.csv"))

    if not crawl_files:
        raise FileNotFoundError("No crawl CSV found.")

    crawl_file = crawl_files[-1]

    print(f"\nUsing crawl file:\n{crawl_file}\n")

    crawl_df = pd.read_csv(crawl_file)

    # =========================================
    # HELPERS
    # =========================================

    def classify_priority(row):
        page_type = str(row.get("page_type", "")).lower()
        business_priority = str(row.get("business_priority", "")).lower()

        if business_priority == "high":
            return "high"

        if page_type in ["product", "landing", "category"]:
            return "high"

        if page_type == "blog":
            return "medium"

        return "low"


    def estimate_link_score(row):
        score = 0

        internal_links = row.get("internal_link_count", 0)
        issue_count = row.get("issue_count", 0)
        page_type = str(row.get("page_type", "")).lower()
        business_priority = str(row.get("business_priority", "")).lower()

        if business_priority == "high":
            score += 40

        if page_type == "product":
            score += 25

        if page_type == "landing":
            score += 20

        if internal_links < 3:
            score += 35
        elif internal_links < 5:
            score += 20
        elif internal_links < 10:
            score += 10

        score += issue_count * 3

        return score


    def detect_missing_crosslinks(url):
        url_lower = str(url).lower()

        opportunities = []

        if "morfblock" in url_lower:
            opportunities.append(
                "Cross-link related morfblock size families"
            )

        if "powerfurl" in url_lower:
            opportunities.append(
                "Cross-link compatible furling components"
            )

        if "dogbone" in url_lower:
            opportunities.append(
                "Cross-link aluminium/titanium variants"
            )

        if "morfring" in url_lower:
            opportunities.append(
                "Cross-link related ring sizes"
            )

        if "mloop" in url_lower:
            opportunities.append(
                "Cross-link loop sizing/configuration pages"
            )

        return "; ".join(opportunities)


    def detect_authority_gaps(row):
        gaps = []

        page_type = str(row.get("page_type", "")).lower()
        internal_links = row.get("internal_link_count", 0)
        word_count = row.get("word_count", 0)

        if page_type in ["product", "landing"] and internal_links < 5:
            gaps.append("Weak internal authority support")

        if page_type == "blog" and word_count > 600:
            gaps.append("Potential authority article")

        return "; ".join(gaps)


    # =========================================
    # BUILD ANALYSIS
    # =========================================

    records = []

    for _, row in crawl_df.iterrows():

        url = row.get("url", "")
        page_type = row.get("page_type", "")
        internal_links = row.get("internal_link_count", 0)
        issue_count = row.get("issue_count", 0)

        priority = classify_priority(row)

        link_score = estimate_link_score(row)

        opportunities = []

        if internal_links < 3:
            opportunities.append(
                "Increase internal links"
            )

        if page_type == "blog":
            opportunities.append(
                "Add contextual product links"
            )

        if page_type == "product":
            opportunities.append(
                "Add related product links"
            )

        if page_type == "landing":
            opportunities.append(
                "Strengthen category/product reinforcement"
            )

        crosslinks = detect_missing_crosslinks(url)

        authority_gaps = detect_authority_gaps(row)

        records.append({
            "url": url,
            "page_type": page_type,
            "business_priority": row.get("business_priority", ""),
            "internal_link_count": internal_links,
            "issue_count": issue_count,
            "word_count": row.get("word_count", 0),
            "priority": priority,
            "authority_gap": authority_gaps,
            "crosslink_opportunities": crosslinks,
            "recommended_actions": "; ".join(opportunities),
            "internal_link_opportunity_score": link_score,
        })

    # =========================================
    # EXPORT
    # =========================================

    df = pd.DataFrame(records)

    df = df.sort_values(
        "internal_link_opportunity_score",
        ascending=False
    )

    run_date = datetime.today().strftime("%Y-%m-%d")

    csv_file = (
        OUTPUT_DIR /
        f"{run_date}_internal_link_opportunities.csv"
    )

    md_file = (
        OUTPUT_DIR /
        f"{run_date}_internal_link_opportunities.md"
    )

    df.to_csv(csv_file, index=False)

    # =========================================
    # SUMMARY TABLE
    # =========================================

    top_df = df.head(50)

    table = (
        "| URL | Type | Links | Authority Gap | "
        "Crosslink Opportunities | Actions | Score |\n"
    )

    table += "|---|---|---:|---|---|---|---:|\n"

    for _, row in top_df.iterrows():

        table += (
            f"| {row['url']} "
            f"| {row['page_type']} "
            f"| {row['internal_link_count']} "
            f"| {row['authority_gap']} "
            f"| {row['crosslink_opportunities']} "
            f"| {row['recommended_actions']} "
            f"| {row['internal_link_opportunity_score']} |\n"
        )

    # =========================================
    # MARKDOWN REPORT
    # =========================================

    report = f"""# SEO Internal Linking Opportunities

    ## Generated

    {run_date}

    ## Input

    {crawl_file}

    ---

    # Purpose

    This report identifies:

    - weak internal authority support
    - weak product reinforcement
    - contextual linking opportunities
    - authority dead-ends
    - related product linking opportunities
    - high-value pages lacking support

    ---

    # Highest Internal Linking Opportunities

    {table}

    ---

    # Interpretation Notes

    Higher scores indicate:

    - commercially important pages
    - weak internal authority reinforcement
    - insufficient contextual linking
    - missing product relationships
    - weak discoverability reinforcement

    Priority should focus on:

    - product pages
    - landing pages
    - authority blog articles
    - category reinforcement
    - cross-product navigation

    Avoid prioritizing:

    - legal pages
    - utility pages
    - archives
    - low-commercial-value pages

    ---

    # Output Files

    - CSV:
    {csv_file}

    - Markdown:
    {md_file}
    """

    md_file.write_text(report, encoding="utf-8")

    print("\nSEO INTERNAL LINK OPPORTUNITY ANALYSIS COMPLETE\n")

    print(csv_file)
    print(md_file)

if __name__ == "__main__":
    main()
