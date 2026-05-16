# ============================================================
# MORFRAC SEO EXECUTIVE REVIEW
# ============================================================

from pathlib import Path
from datetime import datetime
import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(
    r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC"
)

SEO_AGENT_PATH = (
    BASE_PATH
    / r"06_MARKETING\SEO_Agent"
)

CRAWL_PATH = (
    SEO_AGENT_PATH
    / "Crawls"
)

CONTEXTUAL_LINK_PATH = (
    SEO_AGENT_PATH
    / "Contextual_Links"
)

IMPLEMENTATION_PATH = (
    SEO_AGENT_PATH
    / "Implementation_Plans"
)

OUTPUT_PATH = (
    SEO_AGENT_PATH
    / "Executive_Reviews"
)

# ============================================================
# FIND LATEST FILES
# ============================================================

def latest_file(folder, pattern):

    files = sorted(
        folder.glob(pattern),
        reverse=True
    )

    if not files:
        return None

    return files[0]


def main():
    OUTPUT_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    crawl_file = latest_file(
        CRAWL_PATH,
        "*_site_crawl.csv"
    )

    link_file = latest_file(
        CONTEXTUAL_LINK_PATH,
        "*_contextual_link_recommendations_filtered.csv"
    )

    implementation_file = latest_file(
        IMPLEMENTATION_PATH,
        "*_seo_link_implementation_plan.csv"
    )

    # ============================================================
    # LOAD DATA
    # ============================================================

    print("Loading datasets...")

    if not crawl_file:
        raise Exception(
            "No crawl file found."
        )

    crawl_df = pd.read_csv(crawl_file)

    link_df = (
        pd.read_csv(link_file)
        if link_file
        else pd.DataFrame()
    )

    implementation_df = (
        pd.read_csv(implementation_file)
        if implementation_file
        else pd.DataFrame()
    )

    crawl_df = crawl_df.fillna("")

    # ============================================================
    # SUMMARY METRICS
    # ============================================================

    print("Calculating metrics...")

    total_pages = len(crawl_df)

    indexable_pages = int(
        crawl_df["indexable"].sum()
    ) if "indexable" in crawl_df.columns else 0

    high_priority_pages = len(
        crawl_df[
            crawl_df["business_priority"] == "high"
        ]
    ) if "business_priority" in crawl_df.columns else 0

    pages_with_issues = len(
        crawl_df[
            crawl_df["issue_count"] > 0
        ]
    ) if "issue_count" in crawl_df.columns else 0

    avg_word_count = int(
        crawl_df["word_count"].mean()
    ) if "word_count" in crawl_df.columns else 0

    # ============================================================
    # ISSUE ANALYSIS
    # ============================================================

    issue_counts = {}

    if "issues" in crawl_df.columns:

        for issues in crawl_df["issues"]:

            if not issues:
                continue

            split_issues = str(issues).split("; ")

            for issue in split_issues:

                issue_counts[issue] = (
                    issue_counts.get(issue, 0) + 1
                )

    top_issues = sorted(
        issue_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # ============================================================
    # HIGH PRIORITY PAGES
    # ============================================================

    priority_pages = pd.DataFrame()

    if (
        "commercial_seo_score"
        in crawl_df.columns
    ):

        priority_pages = (
            crawl_df[
                crawl_df["business_priority"] == "high"
            ]
            .sort_values(
                "commercial_seo_score",
                ascending=False
            )
            .head(20)
        )

    # ============================================================
    # LINK METRICS
    # ============================================================

    link_recommendations = len(link_df)

    implementation_links = len(
        implementation_df
    )

    # ============================================================
    # STRATEGIC OBSERVATIONS
    # ============================================================

    observations = []

    if pages_with_issues > (
        total_pages * 0.5
    ):
        observations.append(
            "- More than 50% of crawled pages contain SEO issues."
        )

    if avg_word_count < 400:
        observations.append(
            "- Average content depth is low. Thin content likely limits rankings."
        )

    if link_recommendations > 500:
        observations.append(
            "- Internal linking opportunities remain significantly underdeveloped."
        )

    if implementation_links < 50:
        observations.append(
            "- Internal linking implementation shortlist is still limited."
        )

    if high_priority_pages < 20:
        observations.append(
            "- Commercially valuable page count appears limited."
        )

    # ============================================================
    # BUILD MARKDOWN REPORT
    # ============================================================

    print("Generating executive review...")

    today = datetime.today().strftime(
        "%Y-%m-%d"
    )

    output_file = (
        OUTPUT_PATH
        / f"{today}_SEO_Executive_Review.md"
    )

    md = f"""# MORFRAC SEO Executive Review

    ## Generated

    {today}

    ---

    # Executive Summary

    - Total pages crawled: {total_pages}
    - Indexable pages: {indexable_pages}
    - High-priority pages: {high_priority_pages}
    - Pages with issues: {pages_with_issues}
    - Average word count: {avg_word_count}
    - Contextual link recommendations: {link_recommendations}
    - Implementation-ready links: {implementation_links}

    ---

    # Strategic Observations

    """

    if observations:

        for obs in observations:
            md += f"{obs}\n"

    else:

        md += (
            "- No major structural SEO risks detected.\n"
        )

    md += "\n---\n"
    md += "\n# Top SEO Issues\n\n"
    md += "| Issue | Count |\n"
    md += "|---|---:|\n"

    for issue, count in top_issues[:15]:

        md += f"| {issue} | {count} |\n"

    md += "\n---\n"
    md += "\n# Highest Priority Commercial Pages\n\n"
    md += "| URL | SEO Score | Issues |\n"
    md += "|---|---:|---|\n"

    for _, row in priority_pages.iterrows():

        md += (
            f"| {row['url']} "
            f"| {row['commercial_seo_score']} "
            f"| {row['issues']} |\n"
        )

    md += "\n---\n"
    md += "\n# Recommended Immediate Actions\n\n"

    actions = [
        "Improve metadata on high-priority commercial pages.",
        "Strengthen internal linking toward product/category pages.",
        "Expand thin technical/product content.",
        "Reduce duplicate or weak archive/tag pages.",
        "Improve semantic topical clustering.",
    ]

    for action in actions:
        md += f"- {action}\n"

    md += "\n---\n"
    md += "\n# Source Files\n\n"

    md += f"- Crawl: {crawl_file.name}\n"

    if link_file:
        md += (
            f"- Contextual Links: "
            f"{link_file.name}\n"
        )

    if implementation_file:
        md += (
            f"- Implementation Plan: "
            f"{implementation_file.name}\n"
        )

    # ============================================================
    # SAVE
    # ============================================================

    output_file.write_text(
        md,
        encoding="utf-8"
    )

    # ============================================================
    # COMPLETE
    # ============================================================

    print("")
    print("================================================")
    print("SEO EXECUTIVE REVIEW COMPLETE")
    print("================================================")
    print(f"Output file:")
    print(output_file)
    print("================================================")

if __name__ == "__main__":
    main()
