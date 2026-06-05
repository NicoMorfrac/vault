# MORFRAC SEO CONTEXTUAL LINK RECOMMENDER
# FILTERED + STRATEGIC VERSION
# ============================================================

from pathlib import Path
import sys
from datetime import datetime
from urllib.parse import urlparse
from collections import defaultdict
import pandas as pd
import re

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(
    r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC"
)

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_contextual_link_report"
SOURCE_AGENT = "SEO_Agent"

CRAWL_FOLDER = (
    BASE_PATH
    / r"06_MARKETING\SEO_Agent\Crawls"
)

OUTPUT_FOLDER = (
    BASE_PATH
    / r"06_MARKETING\SEO_Agent\Contextual_Links"
)

# ============================================================
# AUTO-DETECT LATEST CRAWL
# ============================================================


def main():
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    crawl_files = sorted(
        CRAWL_FOLDER.glob("*_site_crawl.csv"),
        reverse=True
    )

    if not crawl_files:
        raise Exception(
            f"No crawl files found in:\n{CRAWL_FOLDER}"
        )

    CRAWL_FILE = crawl_files[0]

    # ============================================================
    # SETTINGS
    # ============================================================

    MIN_WORDS = 250
    MAX_RECOMMENDATIONS_PER_PAGE = 5
    MIN_SHARED_KEYWORDS = 3

    # ============================================================
    # LOAD CRAWL
    # ============================================================

    print("Loading crawl data...")

    df = pd.read_csv(CRAWL_FILE)

    required_columns = [
        "url",
        "title",
        "h1",
        "word_count",
        "page_type",
        "business_priority",
    ]

    missing = [
        c for c in required_columns
        if c not in df.columns
    ]

    if missing:
        raise Exception(
            f"Missing columns in crawl:\n{missing}"
        )

    # ============================================================
    # CLEAN
    # ============================================================

    df = df.fillna("")

    # ============================================================
    # HELPERS
    # ============================================================

    STOPWORDS = {
        "with","this","that","from","your","have",
        "will","into","about","more","than","their",
        "they","them","been","being","also","using",
        "used","while","there","where","which","would",
        "could","should","under","between","through",
        "product","products","shop","category",
        "morfrac","system","systems","page",
        "click","view","read","sale","best",
        "high","performance"
    }

    def clean_text(text):

        text = str(text).lower()

        text = re.sub(r"[^a-z0-9\s\-]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def tokenize(text):

        text = clean_text(text)

        words = text.split()

        words = [
            w for w in words
            if len(w) > 3
            and w not in STOPWORDS
            and not w.isdigit()
        ]

        return words

    def extract_keywords(title, h1, url):

        slug = (
            urlparse(url)
            .path
            .replace("/", " ")
            .replace("-", " ")
        )

        combined = f"{title} {h1} {slug}"

        words = tokenize(combined)

        freq = defaultdict(int)

        for w in words:
            freq[w] += 1

        sorted_words = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            w[0]
            for w in sorted_words[:15]
        ]

    def is_spanish(url):

        return "/es/" in url.lower()

    def is_noise_page(row):

        url = str(row["url"]).lower()

        noise_patterns = [
            "/tag/",
            "/author/",
            "/page/",
            "/search",
            "/cart",
            "/checkout",
            "/privacy",
            "/terms",
            "/cookie",
            "/wishlist",
            "/web/",
            "/login",
        ]

        for p in noise_patterns:
            if p in url:
                return True

        if row["business_priority"] == "ignore":
            return True

        return False

    def page_similarity(source, target):

        s = set(source["keywords"])
        t = set(target["keywords"])

        overlap = s.intersection(t)

        return overlap

    # ============================================================
    # PREPARE PAGES
    # ============================================================

    print("Processing pages...")

    pages = []

    for _, row in df.iterrows():

        if is_noise_page(row):
            continue

        if int(row["word_count"]) < MIN_WORDS:
            continue

        url = row["url"]

        keywords = extract_keywords(
            row["title"],
            row["h1"],
            url
        )

        pages.append({
            "url": url,
            "title": row["title"],
            "h1": row["h1"],
            "page_type": row["page_type"],
            "business_priority": row["business_priority"],
            "keywords": keywords,
            "is_spanish": is_spanish(url),
        })

    print(f"Eligible pages: {len(pages)}")

    # ============================================================
    # GENERATE RECOMMENDATIONS
    # ============================================================

    print("Generating recommendations...")

    recommendations = []

    for source in pages:

        candidates = []

        for target in pages:

            # ------------------------------------
            # skip self
            # ------------------------------------

            if source["url"] == target["url"]:
                continue

            # ------------------------------------
            # language consistency
            # ------------------------------------

            if source["is_spanish"] != target["is_spanish"]:
                continue

            # ------------------------------------
            # avoid same product duplication
            # ------------------------------------

            source_slug = urlparse(source["url"]).path
            target_slug = urlparse(target["url"]).path

            source_parts = set(source_slug.split("-"))
            target_parts = set(target_slug.split("-"))

            slug_overlap = (
                source_parts
                .intersection(target_parts)
            )

            if len(slug_overlap) >= 4:
                continue

            # ------------------------------------
            # keyword similarity
            # ------------------------------------

            overlap = page_similarity(
                source,
                target
            )

            if len(overlap) < MIN_SHARED_KEYWORDS:
                continue

            # ------------------------------------
            # scoring
            # ------------------------------------

            score = len(overlap)

            # prioritize product/category links

            if target["page_type"] == "product":
                score += 3

            if target["business_priority"] == "high":
                score += 3

            if source["page_type"] == "technical_blog":
                score += 2

            candidates.append({
                "target_url": target["url"],
                "target_title": target["title"],
                "score": score,
                "anchors": ", ".join(
                    list(overlap)[:8]
                )
            })

        # ----------------------------------------
        # sort best candidates
        # ----------------------------------------

        candidates = sorted(
            candidates,
            key=lambda x: x["score"],
            reverse=True
        )

        candidates = (
            candidates[
                :MAX_RECOMMENDATIONS_PER_PAGE
            ]
        )

        # ----------------------------------------
        # export recommendations
        # ----------------------------------------

        for c in candidates:

            recommendations.append({
                "source_url": source["url"],
                "source_title": source["title"],
                "target_url": c["target_url"],
                "target_title": c["target_title"],
                "relevance_score": c["score"],
                "suggested_anchor_keywords": c["anchors"]
            })

    # ============================================================
    # EXPORT
    # ============================================================

    print("Exporting files...")

    today = datetime.today().strftime("%Y-%m-%d")

    out_df = pd.DataFrame(recommendations)

    # --------------------------------------------
    # remove duplicate recommendations
    # --------------------------------------------

    out_df = out_df.drop_duplicates(
        subset=[
            "source_url",
            "target_url"
        ]
    )

    # --------------------------------------------
    # export CSV
    # --------------------------------------------

    csv_file = (
        OUTPUT_FOLDER
        / f"{today}_contextual_link_recommendations_filtered.csv"
    )

    stable_csv = (
        OUTPUT_FOLDER
        / "contextual_link_recommendations_filtered.csv"
    )

    out_df.to_csv(csv_file, index=False)
    out_df.to_csv(stable_csv, index=False)

    # --------------------------------------------
    # markdown summary
    # --------------------------------------------

    summary_file = (
        OUTPUT_FOLDER
        / f"{today}_contextual_link_recommendations_filtered.md"
    )

    top_examples = out_df.sort_values(
        "relevance_score",
        ascending=False
    ).head(50)

    md = f"""# Contextual Link Recommendations

    ## Generated

    {today}

    ## Crawl Source

    {CRAWL_FILE.name}

    ---

    # Summary

    - Eligible pages: {len(pages)}
    - Recommendations: {len(out_df)}

    ---

    # Top Recommendations

    | Source | Target | Score |
    |---|---|---|
    """

    for _, row in top_examples.iterrows():

        md += (
            f"| {row['source_url']} "
            f"| {row['target_url']} "
            f"| {row['relevance_score']} |\n"
        )

    write_markdown_report(summary_file, md, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    # ============================================================
    # COMPLETE
    # ============================================================

    print("")
    print("================================================")
    print("CONTEXTUAL LINK ANALYSIS COMPLETE")
    print("================================================")
    print(f"Eligible pages: {len(pages)}")
    print(f"Recommendations: {len(out_df)}")
    print(f"CSV: {csv_file}")
    print(f"Stable CSV: {stable_csv}")
    print(f"Markdown: {summary_file}")
    print("================================================")

if __name__ == "__main__":
    main()
