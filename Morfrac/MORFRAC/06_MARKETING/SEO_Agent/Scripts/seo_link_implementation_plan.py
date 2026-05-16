# ============================================================
# MORFRAC SEO LINK IMPLEMENTATION PLAN
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

INPUT_FOLDER = (
    BASE_PATH
    / r"06_MARKETING\SEO_Agent\Contextual_Links"
)

OUTPUT_FOLDER = (
    BASE_PATH
    / r"06_MARKETING\SEO_Agent\Implementation_Plans"
)

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# ============================================================
# FIND FILTERED RECOMMENDATION FILE
# ============================================================

input_file = (
    INPUT_FOLDER
    / "contextual_link_recommendations_filtered.csv"
)

if not input_file.exists():
    raise Exception(
        f"Missing input file:\n{input_file}"
    )

# ============================================================
# SETTINGS
# ============================================================

MAX_LINKS_PER_SOURCE = 3
MAX_TOTAL_RECOMMENDATIONS = 100
MIN_RELEVANCE_SCORE = 6

# ============================================================
# LOAD DATA
# ============================================================

print("Loading recommendation data...")

df = pd.read_csv(input_file)

required_columns = [
    "source_url",
    "source_title",
    "target_url",
    "target_title",
    "relevance_score",
    "suggested_anchor_keywords"
]

missing = [
    c for c in required_columns
    if c not in df.columns
]

if missing:
    raise Exception(
        f"Missing columns:\n{missing}"
    )

# ============================================================
# CLEAN
# ============================================================

df = df.fillna("")

# ============================================================
# FILTER LOW VALUE LINKS
# ============================================================

print("Filtering recommendations...")

df = df[
    df["relevance_score"] >= MIN_RELEVANCE_SCORE
]

# ============================================================
# SORT
# ============================================================

df = df.sort_values(
    "relevance_score",
    ascending=False
)

# ============================================================
# LIMIT LINKS PER SOURCE PAGE
# ============================================================

print("Limiting links per source page...")

limited_rows = []

source_counter = {}

for _, row in df.iterrows():

    source = row["source_url"]

    current = source_counter.get(source, 0)

    if current >= MAX_LINKS_PER_SOURCE:
        continue

    limited_rows.append(row)

    source_counter[source] = current + 1

limited_df = pd.DataFrame(limited_rows)

# ============================================================
# LIMIT TOTAL LINKS
# ============================================================

limited_df = limited_df.head(
    MAX_TOTAL_RECOMMENDATIONS
)

# ============================================================
# EXPORT CSV
# ============================================================

today = datetime.today().strftime("%Y-%m-%d")

csv_file = (
    OUTPUT_FOLDER
    / f"{today}_seo_link_implementation_plan.csv"
)

stable_csv = (
    OUTPUT_FOLDER
    / "seo_link_implementation_plan.csv"
)

limited_df.to_csv(csv_file, index=False)
limited_df.to_csv(stable_csv, index=False)

# ============================================================
# GENERATE MARKDOWN PLAN
# ============================================================

print("Generating markdown report...")

md_file = (
    OUTPUT_FOLDER
    / f"{today}_seo_link_implementation_plan.md"
)

md = f"""# SEO Internal Link Implementation Plan

## Generated

{today}

---

# Summary

- Total implementation links: {len(limited_df)}
- Maximum links per source page: {MAX_LINKS_PER_SOURCE}
- Minimum relevance score: {MIN_RELEVANCE_SCORE}

---

# Recommended Internal Links

"""

grouped = limited_df.groupby("source_url")

for source_url, group in grouped:

    source_title = (
        group.iloc[0]["source_title"]
    )

    md += f"\n## Source Page\n\n"
    md += f"### {source_title}\n\n"
    md += f"{source_url}\n\n"

    md += "| Target Page | Relevance | Suggested Anchors |\n"
    md += "|---|---:|---|\n"

    for _, row in group.iterrows():

        md += (
            f"| {row['target_url']} "
            f"| {row['relevance_score']} "
            f"| {row['suggested_anchor_keywords']} |\n"
        )

    md += "\n---\n"

md_file.write_text(
    md,
    encoding="utf-8"
)

# ============================================================
# COMPLETE
# ============================================================

print("")
print("================================================")
print("SEO LINK IMPLEMENTATION PLAN COMPLETE")
print("================================================")
print(f"Implementation links: {len(limited_df)}")
print(f"CSV: {csv_file}")
print(f"Stable CSV: {stable_csv}")
print(f"Markdown: {md_file}")
print("================================================")