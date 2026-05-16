# ============================================================
# MORFRAC SEO HISTORICAL COMPARISON
# Compares latest crawl against previous crawl
# ============================================================

from pathlib import Path
from datetime import datetime
import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

CRAWL_PATH = SEO_AGENT_PATH / "Crawls"

OUTPUT_PATH = SEO_AGENT_PATH / "Historical_Comparisons"

TODAY = datetime.today().strftime("%Y-%m-%d")

# ============================================================
# HELPERS
# ============================================================

def get_dated_crawl_files():
    files = sorted(CRAWL_PATH.glob("*_site_crawl.csv"))

    # Avoid stable/non-dated files if ever added.
    files = [
        f for f in files
        if f.name[:4].isdigit()
    ]

    return files


def safe_numeric(df, column):
    if column not in df.columns:
        return pd.Series([0] * len(df))

    return pd.to_numeric(df[column], errors="coerce").fillna(0)


def safe_text(df, column):
    if column not in df.columns:
        return pd.Series([""] * len(df))

    return df[column].fillna("").astype(str)


def issue_counts(df):
    counts = {}

    if "issues" not in df.columns:
        return counts

    for value in df["issues"].fillna(""):
        if not value:
            continue

        for issue in str(value).split("; "):
            issue = issue.strip()

            if not issue:
                continue

            counts[issue] = counts.get(issue, 0) + 1

    return counts


def metric_summary(df):
    summary = {}

    summary["total_pages"] = len(df)

    summary["indexable_pages"] = int(
        safe_numeric(df, "indexable").sum()
    )

    summary["high_priority_pages"] = int(
        (safe_text(df, "business_priority") == "high").sum()
    )

    summary["ignored_pages"] = int(
        (safe_text(df, "business_priority") == "ignore").sum()
    )

    summary["pages_with_issues"] = int(
        (safe_numeric(df, "issue_count") > 0).sum()
    )

    summary["avg_word_count"] = round(
        safe_numeric(df, "word_count").mean(),
        1
    )

    summary["avg_internal_links"] = round(
        safe_numeric(df, "internal_link_count").mean(),
        1
    )

    summary["avg_commercial_seo_score"] = round(
        safe_numeric(df, "commercial_seo_score").mean(),
        1
    )

    summary["missing_meta_pages"] = int(
        safe_text(df, "issues").str.contains("Missing meta description", regex=False).sum()
    )

    summary["short_title_pages"] = int(
        safe_text(df, "issues").str.contains("Short title", regex=False).sum()
    )

    summary["multiple_h1_pages"] = int(
        safe_text(df, "issues").str.contains("Multiple H1", regex=False).sum()
    )

    summary["thin_content_pages"] = int(
        safe_text(df, "issues").str.contains("Thin content", regex=False).sum()
    )

    summary["weak_internal_linking_pages"] = int(
        safe_text(df, "issues").str.contains("Weak internal linking", regex=False).sum()
    )

    return summary


def delta_row(metric, previous, latest):
    delta = latest - previous

    if delta > 0:
        direction = "UP"
    elif delta < 0:
        direction = "DOWN"
    else:
        direction = "NO CHANGE"

    return {
        "metric": metric,
        "previous": previous,
        "latest": latest,
        "delta": delta,
        "direction": direction,
    }


def classify_delta(metric, delta):
    # Positive/negative interpretation depends on metric type.
    bad_when_up = {
        "pages_with_issues",
        "ignored_pages",
        "missing_meta_pages",
        "short_title_pages",
        "multiple_h1_pages",
        "thin_content_pages",
        "weak_internal_linking_pages",
    }

    good_when_up = {
        "total_pages",
        "indexable_pages",
        "high_priority_pages",
        "avg_word_count",
        "avg_internal_links",
        "avg_commercial_seo_score",
    }

    if delta == 0:
        return "neutral"

    if metric in bad_when_up:
        return "worse" if delta > 0 else "better"

    if metric in good_when_up:
        return "better" if delta > 0 else "worse"

    return "neutral"


# ============================================================
# LOAD FILES
# ============================================================


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    crawl_files = get_dated_crawl_files()

    if len(crawl_files) < 2:
        raise Exception(
            "Need at least two dated crawl files to run historical comparison."
        )

    previous_file = crawl_files[-2]
    latest_file = crawl_files[-1]

    print("Using previous crawl:")
    print(previous_file)

    print("")
    print("Using latest crawl:")
    print(latest_file)

    previous_df = pd.read_csv(previous_file).fillna("")
    latest_df = pd.read_csv(latest_file).fillna("")

    # ============================================================
    # SUMMARY COMPARISON
    # ============================================================

    previous_summary = metric_summary(previous_df)
    latest_summary = metric_summary(latest_df)

    rows = []

    for metric in latest_summary.keys():
        rows.append(
            delta_row(
                metric,
                previous_summary.get(metric, 0),
                latest_summary.get(metric, 0),
            )
        )

    comparison_df = pd.DataFrame(rows)

    comparison_df["interpretation"] = comparison_df.apply(
        lambda row: classify_delta(row["metric"], row["delta"]),
        axis=1
    )

    # ============================================================
    # PAGE-LEVEL CHANGES
    # ============================================================

    previous_urls = set(previous_df["url"]) if "url" in previous_df.columns else set()
    latest_urls = set(latest_df["url"]) if "url" in latest_df.columns else set()

    new_urls = sorted(latest_urls - previous_urls)
    removed_urls = sorted(previous_urls - latest_urls)

    common_urls = sorted(previous_urls.intersection(latest_urls))

    previous_by_url = previous_df.set_index("url") if "url" in previous_df.columns else pd.DataFrame()
    latest_by_url = latest_df.set_index("url") if "url" in latest_df.columns else pd.DataFrame()

    page_changes = []

    for url in common_urls:
        prev = previous_by_url.loc[url]
        curr = latest_by_url.loc[url]

        prev_issues = str(prev.get("issues", ""))
        curr_issues = str(curr.get("issues", ""))

        prev_score = pd.to_numeric(prev.get("commercial_seo_score", 0), errors="coerce")
        curr_score = pd.to_numeric(curr.get("commercial_seo_score", 0), errors="coerce")

        prev_words = pd.to_numeric(prev.get("word_count", 0), errors="coerce")
        curr_words = pd.to_numeric(curr.get("word_count", 0), errors="coerce")

        prev_links = pd.to_numeric(prev.get("internal_link_count", 0), errors="coerce")
        curr_links = pd.to_numeric(curr.get("internal_link_count", 0), errors="coerce")

        score_delta = curr_score - prev_score
        word_delta = curr_words - prev_words
        link_delta = curr_links - prev_links

        if (
            prev_issues != curr_issues
            or abs(score_delta) > 0
            or abs(word_delta) >= 50
            or abs(link_delta) >= 3
        ):
            page_changes.append({
                "url": url,
                "previous_issues": prev_issues,
                "latest_issues": curr_issues,
                "score_delta": score_delta,
                "word_delta": word_delta,
                "internal_link_delta": link_delta,
            })

    page_changes_df = pd.DataFrame(page_changes)

    if not page_changes_df.empty:
        page_changes_df = page_changes_df.sort_values(
            ["score_delta", "word_delta", "internal_link_delta"],
            ascending=[False, False, False]
        )

    # ============================================================
    # ISSUE DELTAS
    # ============================================================

    previous_issue_counts = issue_counts(previous_df)
    latest_issue_counts = issue_counts(latest_df)

    all_issues = sorted(
        set(previous_issue_counts.keys()).union(set(latest_issue_counts.keys()))
    )

    issue_delta_rows = []

    for issue in all_issues:
        prev_count = previous_issue_counts.get(issue, 0)
        latest_count = latest_issue_counts.get(issue, 0)

        issue_delta_rows.append({
            "issue": issue,
            "previous": prev_count,
            "latest": latest_count,
            "delta": latest_count - prev_count,
        })

    issue_delta_df = pd.DataFrame(issue_delta_rows)

    if not issue_delta_df.empty:
        issue_delta_df = issue_delta_df.sort_values(
            "delta",
            ascending=False
        )

    # ============================================================
    # OUTPUT FILES
    # ============================================================

    comparison_csv = OUTPUT_PATH / f"{TODAY}_seo_historical_metric_comparison.csv"
    page_changes_csv = OUTPUT_PATH / f"{TODAY}_seo_page_level_changes.csv"
    issue_delta_csv = OUTPUT_PATH / f"{TODAY}_seo_issue_delta.csv"
    report_file = OUTPUT_PATH / f"{TODAY}_SEO_Historical_Comparison.md"

    comparison_df.to_csv(comparison_csv, index=False, encoding="utf-8-sig")

    if not page_changes_df.empty:
        page_changes_df.to_csv(page_changes_csv, index=False, encoding="utf-8-sig")
    else:
        pd.DataFrame().to_csv(page_changes_csv, index=False, encoding="utf-8-sig")

    if not issue_delta_df.empty:
        issue_delta_df.to_csv(issue_delta_csv, index=False, encoding="utf-8-sig")
    else:
        pd.DataFrame().to_csv(issue_delta_csv, index=False, encoding="utf-8-sig")

    # ============================================================
    # MARKDOWN REPORT
    # ============================================================

    comparison_table = comparison_df.to_markdown(index=False)

    issue_table = (
        issue_delta_df.head(20).to_markdown(index=False)
        if not issue_delta_df.empty
        else "No issue changes detected."
    )

    page_change_table = (
        page_changes_df.head(30).to_markdown(index=False)
        if not page_changes_df.empty
        else "No material page-level changes detected."
    )

    new_url_table = "\n".join([f"- {url}" for url in new_urls[:50]]) if new_urls else "- None"
    removed_url_table = "\n".join([f"- {url}" for url in removed_urls[:50]]) if removed_urls else "- None"

    better_count = int((comparison_df["interpretation"] == "better").sum())
    worse_count = int((comparison_df["interpretation"] == "worse").sum())
    neutral_count = int((comparison_df["interpretation"] == "neutral").sum())

    if worse_count > better_count:
        overall_direction = "SEO crawl health appears to have worsened compared with the previous crawl."
    elif better_count > worse_count:
        overall_direction = "SEO crawl health appears to have improved compared with the previous crawl."
    else:
        overall_direction = "SEO crawl health is broadly stable compared with the previous crawl."

    md = f"""# MORFRAC SEO Historical Comparison

    ## Generated

    {TODAY}

    ---

    # Compared Files

    Previous crawl:

    `{previous_file.name}`

    Latest crawl:

    `{latest_file.name}`

    ---

    # Executive Interpretation

    {overall_direction}

    - Metrics improved: {better_count}
    - Metrics worsened: {worse_count}
    - Metrics stable/neutral: {neutral_count}

    ---

    # Metric Comparison

    {comparison_table}

    ---

    # Issue Delta

    Positive delta means the issue appeared on more pages.
    Negative delta means the issue appeared on fewer pages.

    {issue_table}

    ---

    # New URLs Detected

    {new_url_table}

    ---

    # Removed URLs Detected

    {removed_url_table}

    ---

    # Material Page-Level Changes

    {page_change_table}

    ---

    # Recommended Review Actions

    - Check whether worsened issue counts are caused by real SEO degradation or crawl expansion.
    - Prioritize pages where commercial SEO score increased because of new issues.
    - Review new URLs for duplicate, thin, or orphan risks.
    - Review removed URLs for broken internal links or lost search value.
    - Track whether metadata, H1, content depth, and internal linking improve over repeated runs.

    ---

    # Output Files

    - Metric comparison CSV: `{comparison_csv}`
    - Page-level changes CSV: `{page_changes_csv}`
    - Issue delta CSV: `{issue_delta_csv}`
    """

    report_file.write_text(md, encoding="utf-8")

    # ============================================================
    # COMPLETE
    # ============================================================

    print("")
    print("================================================")
    print("SEO HISTORICAL COMPARISON COMPLETE")
    print("================================================")
    print(f"Previous crawl: {previous_file.name}")
    print(f"Latest crawl: {latest_file.name}")
    print(f"Metric CSV: {comparison_csv}")
    print(f"Page changes CSV: {page_changes_csv}")
    print(f"Issue delta CSV: {issue_delta_csv}")
    print(f"Report: {report_file}")
    print("================================================")

if __name__ == "__main__":
    main()
