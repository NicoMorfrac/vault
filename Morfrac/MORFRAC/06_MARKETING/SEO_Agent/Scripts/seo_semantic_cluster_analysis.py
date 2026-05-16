# ============================================================
# MORFRAC SEO SEMANTIC CLUSTER ANALYSIS
# Deterministic V1 - TF-IDF + cosine similarity
# ============================================================

from pathlib import Path
from datetime import datetime
import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

CRAWL_PATH = SEO_AGENT_PATH / "Crawls"
MERGE_PATH = SEO_AGENT_PATH / "Merged_Analysis"

OUTPUT_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

TODAY = datetime.today().strftime("%Y-%m-%d")

MIN_WORDS = 80
SIMILARITY_THRESHOLD = 0.65
MAX_CLUSTERS = 12

# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def clean_text(text):
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z0-9áéíóúñüø\s\-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


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


def classify_page_role(url, page_type):
    url = str(url).lower()
    page_type = str(page_type).lower()

    if "/shop/category/" in url:
        return "category"

    if "/shop/" in url:
        return "product"

    if "/blog/" in url:
        return "authority_content"

    if page_type == "technical_blog":
        return "authority_content"

    if any(x in url for x in [
        "/dogbone",
        "/padeye",
        "/powerfurl",
        "/morfblock",
        "/mloop",
        "/shackle",
        "/morfring",
        "/morfwing",
    ]):
        return "landing"

    return "general"


def detect_cluster_label(text):
    text = clean_text(text)

    labels = {
        "dogbone": ["dogbone", "dog bone"],
        "mloop": ["mloop", "m loop", "dyneema loop", "dyneema"],
        "shackle": ["shackle", "soft shackle"],
        "padeye": ["padeye", "pad eye", "cancamo", "cáncamo"],
        "powerfurl": ["powerfurl", "furler", "furling", "top down", "continuous line"],
        "morfblock": ["morfblock", "morf block", "block"],
        "morfring": ["morfring", "friction ring"],
        "morfwing": ["morfwing", "wing"],
        "mreel": ["mreel", "rope reeler", "reeler"],
        "hoistlock": ["hoistlock", "gaff lock", "halyard lock"],
        "custom_engineering": ["custom", "engineering", "manufacturing", "3d printed", "cnc"],
    }

    for label, keywords in labels.items():
        for keyword in keywords:
            if keyword in text:
                return label

    return "other"


def top_terms_for_cluster(vectorizer, matrix, indices, top_n=8):
    if len(indices) == 0:
        return ""

    terms = vectorizer.get_feature_names_out()

    cluster_matrix = matrix[indices]

    mean_scores = cluster_matrix.mean(axis=0).A1

    top_indices = mean_scores.argsort()[::-1][:top_n]

    return ", ".join([terms[i] for i in top_indices if mean_scores[i] > 0])


# ============================================================
# LOAD DATA
# ============================================================

print("Loading crawl data...")

crawl_file = latest_file(CRAWL_PATH, "*_site_crawl.csv")

if not crawl_file:
    raise FileNotFoundError("No *_site_crawl.csv file found.")

crawl_df = pd.read_csv(crawl_file).fillna("")

print(f"Crawl file: {crawl_file}")

merge_file = latest_file(MERGE_PATH, "*_search_console_merge.csv")

if merge_file:
    merge_df = pd.read_csv(merge_file).fillna("")
    print(f"Search Console merge file: {merge_file}")
else:
    merge_df = pd.DataFrame()
    print("No Search Console merge file found. Continuing without it.")

# ============================================================
# VALIDATE CRAWL
# ============================================================

required_cols = [
    "url",
    "title",
    "h1",
    "meta_description",
    "word_count",
    "page_type",
    "business_priority",
    "commercial_relevance",
    "authority_value",
]

for col in required_cols:
    if col not in crawl_df.columns:
        crawl_df[col] = ""

# ============================================================
# PREPARE PAGE DATA
# ============================================================

print("Preparing semantic text...")

crawl_df["word_count"] = pd.to_numeric(
    crawl_df["word_count"],
    errors="coerce"
).fillna(0)

df = crawl_df[
    crawl_df["word_count"] >= MIN_WORDS
].copy()

df["normalized_url"] = df["url"].apply(normalize_url)

df["page_role"] = df.apply(
    lambda row: classify_page_role(row["url"], row["page_type"]),
    axis=1
)

df["semantic_text"] = df.apply(
    lambda row: clean_text(
        f"{row['url']} {row['title']} {row['h1']} {row['meta_description']}"
    ),
    axis=1
)

df["manual_topic_label"] = df["semantic_text"].apply(detect_cluster_label)

df = df[
    df["semantic_text"].str.len() > 20
].copy()

if len(df) < 3:
    raise Exception("Not enough pages for semantic clustering.")

# ============================================================
# MERGE SEARCH CONSOLE DATA IF AVAILABLE
# ============================================================

if not merge_df.empty and "url_clean" in merge_df.columns:
    merge_cols = [
        col for col in [
            "url_clean",
            "clicks",
            "impressions",
            "ctr_percent",
            "position",
            "seo_opportunity",
            "seo_priority_score",
        ]
        if col in merge_df.columns
    ]

    df = df.merge(
        merge_df[merge_cols],
        left_on="normalized_url",
        right_on="url_clean",
        how="left"
    )

for col in [
    "clicks",
    "impressions",
    "ctr_percent",
    "position",
    "seo_priority_score",
]:
    if col not in df.columns:
        df[col] = 0

df["clicks"] = pd.to_numeric(df["clicks"], errors="coerce").fillna(0)
df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce").fillna(0)
df["seo_priority_score"] = pd.to_numeric(df["seo_priority_score"], errors="coerce").fillna(0)

# ============================================================
# TF-IDF
# ============================================================

print("Running TF-IDF...")

vectorizer = TfidfVectorizer(
    max_features=1200,
    stop_words="english",
    ngram_range=(1, 2),
    min_df=1,
)

tfidf_matrix = vectorizer.fit_transform(df["semantic_text"])

# ============================================================
# KMEANS CLUSTERING
# ============================================================

print("Clustering pages...")

n_pages = len(df)

n_clusters = min(
    MAX_CLUSTERS,
    max(2, int(n_pages ** 0.5))
)

kmeans = KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)

df["semantic_cluster_id"] = kmeans.fit_predict(tfidf_matrix)

# ============================================================
# COSINE SIMILARITY
# ============================================================

print("Calculating similarity...")

similarity_matrix = cosine_similarity(tfidf_matrix)

similar_pairs = []

urls = df["url"].tolist()
roles = df["page_role"].tolist()
labels = df["manual_topic_label"].tolist()
clusters = df["semantic_cluster_id"].tolist()

for i in range(len(df)):
    for j in range(i + 1, len(df)):
        score = similarity_matrix[i][j]

        if score >= SIMILARITY_THRESHOLD:
            similar_pairs.append({
                "url_a": urls[i],
                "role_a": roles[i],
                "label_a": labels[i],
                "cluster_a": clusters[i],
                "url_b": urls[j],
                "role_b": roles[j],
                "label_b": labels[j],
                "cluster_b": clusters[j],
                "similarity_score": round(score, 4),
                "risk_type": (
                    "likely_cannibalization"
                    if labels[i] == labels[j]
                    else "semantic_overlap"
                ),
            })

similar_df = pd.DataFrame(similar_pairs)

if not similar_df.empty:
    similar_df = similar_df.sort_values(
        "similarity_score",
        ascending=False
    )

# ============================================================
# CLUSTER SUMMARY
# ============================================================

print("Building cluster summary...")

cluster_rows = []

for cluster_id, group in df.groupby("semantic_cluster_id"):
    indices = list(group.index)

    index_positions = [
        df.index.get_loc(idx)
        for idx in indices
    ]

    role_counts = group["page_role"].value_counts().to_dict()
    label_counts = group["manual_topic_label"].value_counts().to_dict()

    dominant_label = group["manual_topic_label"].value_counts().idxmax()

    top_terms = top_terms_for_cluster(
        vectorizer,
        tfidf_matrix,
        index_positions,
        top_n=10
    )

    page_count = len(group)
    product_pages = role_counts.get("product", 0)
    category_pages = role_counts.get("category", 0)
    authority_pages = role_counts.get("authority_content", 0)
    landing_pages = role_counts.get("landing", 0)

    total_impressions = int(group["impressions"].sum())
    total_clicks = int(group["clicks"].sum())
    avg_priority = round(group["seo_priority_score"].mean(), 2)

    if page_count == 1:
        cluster_health = "ORPHAN_TOPIC"
    elif page_count > 12:
        cluster_health = "FRAGMENTED_TOPIC"
    elif product_pages > 5 and category_pages == 0 and landing_pages == 0:
        cluster_health = "PRODUCT_HEAVY_NO_PILLAR"
    elif authority_pages > 3 and product_pages == 0:
        cluster_health = "CONTENT_WITHOUT_COMMERCIAL_TARGET"
    else:
        cluster_health = "OK"

    cluster_rows.append({
        "semantic_cluster_id": cluster_id,
        "dominant_label": dominant_label,
        "page_count": page_count,
        "product_pages": product_pages,
        "category_pages": category_pages,
        "landing_pages": landing_pages,
        "authority_content_pages": authority_pages,
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "avg_seo_priority_score": avg_priority,
        "cluster_health": cluster_health,
        "top_terms": top_terms,
        "role_counts": str(role_counts),
        "label_counts": str(label_counts),
    })

cluster_summary_df = pd.DataFrame(cluster_rows)

cluster_summary_df = cluster_summary_df.sort_values(
    ["cluster_health", "page_count"],
    ascending=[True, False]
)

# ============================================================
# ORPHAN TOPICS
# ============================================================

orphan_topics_df = cluster_summary_df[
    cluster_summary_df["cluster_health"] == "ORPHAN_TOPIC"
].copy()

# ============================================================
# CANNIBALIZATION
# ============================================================

if not similar_df.empty:
    cannibalization_df = similar_df[
        similar_df["risk_type"] == "likely_cannibalization"
    ].copy()
else:
    cannibalization_df = pd.DataFrame()

# ============================================================
# PAGE EXPORT
# ============================================================

page_export_cols = [
    "url",
    "title",
    "h1",
    "page_type",
    "page_role",
    "business_priority",
    "commercial_relevance",
    "authority_value",
    "word_count",
    "manual_topic_label",
    "semantic_cluster_id",
    "clicks",
    "impressions",
    "seo_priority_score",
]

page_export_df = df[page_export_cols].copy()

# ============================================================
# OUTPUT FILES
# ============================================================

clusters_csv = OUTPUT_PATH / f"{TODAY}_semantic_clusters.csv"
pages_csv = OUTPUT_PATH / f"{TODAY}_semantic_cluster_pages.csv"
similarity_csv = OUTPUT_PATH / f"{TODAY}_semantic_similarity_pairs.csv"
cannibalization_csv = OUTPUT_PATH / f"{TODAY}_semantic_cannibalization.csv"
orphans_csv = OUTPUT_PATH / f"{TODAY}_semantic_orphan_topics.csv"
report_md = OUTPUT_PATH / f"{TODAY}_semantic_cluster_report.md"

stable_clusters_csv = OUTPUT_PATH / "semantic_clusters.csv"
stable_pages_csv = OUTPUT_PATH / "semantic_cluster_pages.csv"
stable_cannibalization_csv = OUTPUT_PATH / "semantic_cannibalization.csv"

cluster_summary_df.to_csv(clusters_csv, index=False, encoding="utf-8-sig")
cluster_summary_df.to_csv(stable_clusters_csv, index=False, encoding="utf-8-sig")

page_export_df.to_csv(pages_csv, index=False, encoding="utf-8-sig")
page_export_df.to_csv(stable_pages_csv, index=False, encoding="utf-8-sig")

if not similar_df.empty:
    similar_df.to_csv(similarity_csv, index=False, encoding="utf-8-sig")
else:
    pd.DataFrame().to_csv(similarity_csv, index=False, encoding="utf-8-sig")

if not cannibalization_df.empty:
    cannibalization_df.to_csv(cannibalization_csv, index=False, encoding="utf-8-sig")
    cannibalization_df.to_csv(stable_cannibalization_csv, index=False, encoding="utf-8-sig")
else:
    pd.DataFrame().to_csv(cannibalization_csv, index=False, encoding="utf-8-sig")
    pd.DataFrame().to_csv(stable_cannibalization_csv, index=False, encoding="utf-8-sig")

if not orphan_topics_df.empty:
    orphan_topics_df.to_csv(orphans_csv, index=False, encoding="utf-8-sig")
else:
    pd.DataFrame().to_csv(orphans_csv, index=False, encoding="utf-8-sig")

# ============================================================
# MARKDOWN REPORT
# ============================================================

top_clusters = cluster_summary_df.head(20).to_markdown(index=False)

if not cannibalization_df.empty:
    top_cannibalization = cannibalization_df.head(30).to_markdown(index=False)
else:
    top_cannibalization = "No high-confidence cannibalization pairs detected."

if not orphan_topics_df.empty:
    orphan_table = orphan_topics_df.head(30).to_markdown(index=False)
else:
    orphan_table = "No orphan topic clusters detected."

report = f"""# MORFRAC SEO Semantic Cluster Analysis

## Generated

{TODAY}

---

# Purpose

This report groups MORFRAC pages by deterministic semantic similarity using TF-IDF and cosine similarity.

It identifies:

- semantic clusters
- likely cannibalization pairs
- orphan topics
- fragmented clusters
- product-heavy clusters without clear pillar support
- authority content without commercial targets

---

# Source Files

- Crawl file: `{crawl_file}`
- Search Console merge file: `{merge_file if merge_file else "Not available"}`

---

# Summary

- Pages analyzed: {len(df)}
- Semantic clusters: {n_clusters}
- Similar page pairs above threshold: {len(similar_df)}
- Likely cannibalization pairs: {len(cannibalization_df)}
- Orphan topic clusters: {len(orphan_topics_df)}

Similarity threshold:

`{SIMILARITY_THRESHOLD}`

---

# Cluster Summary

{top_clusters}

---

# Likely Cannibalization / Duplicate Intent

{top_cannibalization}

---

# Orphan Topic Clusters

{orphan_table}

---

# Interpretation Notes

Cluster health meanings:

- `ORPHAN_TOPIC`: only one page in the cluster. It may lack supporting content.
- `FRAGMENTED_TOPIC`: too many pages in one cluster. This may indicate topic sprawl or cannibalization.
- `PRODUCT_HEAVY_NO_PILLAR`: many product pages but no clear category or landing page support.
- `CONTENT_WITHOUT_COMMERCIAL_TARGET`: content exists but does not clearly support product/category pages.
- `OK`: structurally acceptable cluster.

Recommended next actions:

1. Review cannibalization pairs before writing more content.
2. Build or strengthen pillar pages for product-heavy clusters.
3. Link authority content toward commercial category/product pages.
4. Expand orphan topics only if they support commercial search demand.
5. Avoid creating new pages inside already fragmented topics unless consolidation is planned.

---

# Output Files

- Cluster summary: `{clusters_csv}`
- Page cluster mapping: `{pages_csv}`
- Similarity pairs: `{similarity_csv}`
- Cannibalization: `{cannibalization_csv}`
- Orphan topics: `{orphans_csv}`
"""

report_md.write_text(report, encoding="utf-8")

# ============================================================
# COMPLETE
# ============================================================

print("")
print("================================================")
print("SEO SEMANTIC CLUSTER ANALYSIS COMPLETE")
print("================================================")
print(f"Pages analyzed: {len(df)}")
print(f"Clusters: {n_clusters}")
print(f"Similar pairs: {len(similar_df)}")
print(f"Cannibalization pairs: {len(cannibalization_df)}")
print(f"Orphan topic clusters: {len(orphan_topics_df)}")
print(f"Report: {report_md}")
print("================================================")