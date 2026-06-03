# ============================================================
# MORFRAC SEO PIPELINE HEALTH CHECK
# Verifies freshness, file existence, row counts, and key columns
# ============================================================

from pathlib import Path
import sys
from datetime import datetime
import re

import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_pipeline_health_report"
SOURCE_AGENT = "SEO_Agent"

SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

TODAY = datetime.today().strftime("%Y-%m-%d")

OUTPUT_PATH = SEO_AGENT_PATH / "Pipeline_Health"

CHECKS = [
    {
        "name": "Crawl CSV",
        "folder": SEO_AGENT_PATH / "Crawls",
        "pattern": "*_site_crawl.csv",
        "required": True,
        "min_rows": 50,
        "required_columns": [
            "url",
            "title",
            "h1",
            "meta_description",
            "word_count",
            "page_type",
            "business_priority",
        ],
    },
    {
        "name": "Search Console Merge",
        "folder": SEO_AGENT_PATH / "Merged_Analysis",
        "pattern": "*_search_console_merge.csv",
        "required": True,
        "min_rows": 1,
        "required_columns": [
            "url",
            "impressions",
            "clicks",
            "seo_opportunity",
            "seo_priority_score",
        ],
    },
    {
        "name": "Internal Link Graph Pages",
        "folder": SEO_AGENT_PATH / "Internal_Linking",
        "pattern": "*_internal_link_graph_pages.csv",
        "required": True,
        "min_rows": 50,
        "required_columns": [
            "url",
            "inbound_internal_links",
            "outbound_internal_links",
            "internal_link_graph_score",
        ],
    },
    {
        "name": "Contextual Link Recommendations",
        "folder": SEO_AGENT_PATH / "Contextual_Links",
        "pattern": "*_contextual_link_recommendations_filtered.csv",
        "required": True,
        "min_rows": 10,
        "required_columns": [
            "source_url",
            "target_url",
            "relevance_score",
        ],
    },
    {
        "name": "Semantic Cluster Summary",
        "folder": SEO_AGENT_PATH / "Semantic_Clusters",
        "pattern": "*_semantic_clusters.csv",
        "required": True,
        "min_rows": 3,
        "required_columns": [
            "semantic_cluster_id",
            "dominant_label",
            "page_count",
            "cluster_health",
        ],
    },
    {
        "name": "Semantic Cluster Pages",
        "folder": SEO_AGENT_PATH / "Semantic_Clusters",
        "pattern": "*_semantic_cluster_pages.csv",
        "required": True,
        "min_rows": 50,
        "required_columns": [
            "url",
            "manual_topic_label",
            "semantic_cluster_id",
        ],
    },
    {
        "name": "Content Gap Analysis",
        "folder": SEO_AGENT_PATH / "Content_Gap_Analysis",
        "pattern": "*_content_gap_analysis.csv",
        "required": True,
        "min_rows": 1,
        "required_columns": [
            "dominant_label",
            "gap_type",
            "gap_score",
            "recommended_action",
        ],
    },
    {
        "name": "Topic Authority Map",
        "folder": SEO_AGENT_PATH / "Topic_Authority_Map",
        "pattern": "*_topic_authority_map.csv",
        "required": True,
        "min_rows": 3,
        "required_columns": [
            "dominant_label",
            "topic_authority_score",
            "authority_tier",
            "strategic_status",
        ],
    },
    {
        "name": "Executive Review",
        "folder": SEO_AGENT_PATH / "Executive_Reviews",
        "pattern": "*_SEO_Executive_Review.md",
        "required": True,
        "min_rows": 0,
        "required_columns": [],
    },
    {
        "name": "Historical Comparison",
        "folder": SEO_AGENT_PATH / "Historical_Comparisons",
        "pattern": "*_SEO_Historical_Comparison.md",
        "required": False,
        "min_rows": 0,
        "required_columns": [],
    },
]

# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    if not files:
        return None

    dated_files = [
        f for f in files
        if re.match(r"^\d{4}-\d{2}-\d{2}_", f.name)
    ]

    candidates = dated_files if dated_files else files

    return max(candidates, key=lambda f: f.stat().st_mtime)


def is_from_today(path):
    if not path:
        return False

    return path.name.startswith(f"{TODAY}_")


def safe_read_csv(path):
    try:
        return pd.read_csv(path).fillna("")
    except Exception:
        return pd.DataFrame()


def check_markdown_file(path):
    if not path or not path.exists():
        return 0, False

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        return len(text.splitlines()), len(text.strip()) > 100
    except Exception:
        return 0, False


def evaluate_check(config):
    name = config["name"]
    folder = config["folder"]
    pattern = config["pattern"]
    required = config["required"]
    min_rows = config["min_rows"]
    required_columns = config["required_columns"]

    path = latest_file(folder, pattern)

    row_count = 0
    missing_columns = []
    is_fresh = False
    exists = path is not None and path.exists()
    readable = False

    status = "PASS"
    severity = "OK"
    notes = []

    if not exists:
        if required:
            status = "FAIL"
            severity = "CRITICAL"
            notes.append("Required output file is missing.")
        else:
            status = "WARN"
            severity = "OPTIONAL"
            notes.append("Optional output file is missing.")

        return {
            "check_name": name,
            "status": status,
            "severity": severity,
            "file_path": "",
            "fresh_today": False,
            "row_count": 0,
            "min_expected_rows": min_rows,
            "missing_columns": "",
            "notes": "; ".join(notes),
        }

    is_fresh = is_from_today(path)

    if not is_fresh:
        status = "WARN"
        severity = "STALE"
        notes.append("Latest file is not from today.")

    if path.suffix.lower() == ".csv":
        df = safe_read_csv(path)
        readable = not df.empty or min_rows == 0
        row_count = len(df)

        if min_rows > 0 and row_count < min_rows:
            status = "FAIL" if required else "WARN"
            severity = "LOW_ROWS"
            notes.append(
                f"Row count below expected minimum: {row_count} < {min_rows}."
            )

        for col in required_columns:
            if col not in df.columns:
                missing_columns.append(col)

        if missing_columns:
            status = "FAIL" if required else "WARN"
            severity = "MISSING_COLUMNS"
            notes.append(
                "Missing required columns: " + ", ".join(missing_columns)
            )

        if not readable and required:
            status = "FAIL"
            severity = "UNREADABLE"
            notes.append("CSV could not be read or is empty.")

    elif path.suffix.lower() == ".md":
        row_count, readable = check_markdown_file(path)

        if not readable and required:
            status = "FAIL"
            severity = "UNREADABLE"
            notes.append("Markdown file is missing content or unreadable.")

    else:
        notes.append("File type not specifically validated.")

    if not notes:
        notes.append("Output looks usable.")

    return {
        "check_name": name,
        "status": status,
        "severity": severity,
        "file_path": str(path),
        "fresh_today": is_fresh,
        "row_count": row_count,
        "min_expected_rows": min_rows,
        "missing_columns": ", ".join(missing_columns),
        "notes": "; ".join(notes),
    }


def status_summary(results_df):
    if results_df.empty:
        return {
            "pass_count": 0,
            "warn_count": 0,
            "fail_count": 0,
            "overall_status": "FAIL",
        }

    pass_count = int((results_df["status"] == "PASS").sum())
    warn_count = int((results_df["status"] == "WARN").sum())
    fail_count = int((results_df["status"] == "FAIL").sum())

    if fail_count > 0:
        overall_status = "FAIL"
    elif warn_count > 0:
        overall_status = "WARN"
    else:
        overall_status = "PASS"

    return {
        "pass_count": pass_count,
        "warn_count": warn_count,
        "fail_count": fail_count,
        "overall_status": overall_status,
    }


def escape_md(value):
    text = str(value)
    text = text.replace("\n", " ")
    text = text.replace("|", "\\|")
    return text


def markdown_table(df, columns=None, limit=None):
    if df.empty:
        return "No data available."

    if columns:
        columns = [c for c in columns if c in df.columns]

        if not columns:
            return "No data available."

        df = df[columns]

    if limit:
        df = df.head(limit)

    headers = [escape_md(col) for col in df.columns]

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for _, row in df.iterrows():
        values = [escape_md(row[col]) for col in df.columns]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    print("Running SEO pipeline health check...")

    results = []

    for check in CHECKS:
        results.append(evaluate_check(check))

    results_df = pd.DataFrame(results)

    summary = status_summary(results_df)

    csv_file = OUTPUT_PATH / f"{TODAY}_pipeline_health_check.csv"
    stable_csv = OUTPUT_PATH / "pipeline_health_check.csv"

    md_file = OUTPUT_PATH / f"{TODAY}_pipeline_health_report.md"
    stable_md = OUTPUT_PATH / "pipeline_health_report.md"

    results_df.to_csv(csv_file, index=False, encoding="utf-8-sig")
    results_df.to_csv(stable_csv, index=False, encoding="utf-8-sig")

    failures_df = results_df[results_df["status"] == "FAIL"].copy()
    warnings_df = results_df[results_df["status"] == "WARN"].copy()

    report = f"""# MORFRAC SEO Pipeline Health Check

## Generated

{TODAY}

---

# Overall Status

**{summary["overall_status"]}**

| Result | Count |
|---|---:|
| PASS | {summary["pass_count"]} |
| WARN | {summary["warn_count"]} |
| FAIL | {summary["fail_count"]} |

---

# Critical Failures

{markdown_table(
    failures_df,
    columns=[
        "check_name",
        "severity",
        "fresh_today",
        "row_count",
        "min_expected_rows",
        "missing_columns",
        "notes",
    ],
)}

---

# Warnings

{markdown_table(
    warnings_df,
    columns=[
        "check_name",
        "severity",
        "fresh_today",
        "row_count",
        "min_expected_rows",
        "missing_columns",
        "notes",
    ],
)}

---

# Full Pipeline Check

{markdown_table(
    results_df,
    columns=[
        "check_name",
        "status",
        "severity",
        "fresh_today",
        "row_count",
        "min_expected_rows",
        "missing_columns",
        "notes",
    ],
)}

---

# Interpretation

Use this report before trusting the SEO executive review.

- `FAIL` means a required output is missing, empty, stale in structure, or missing required columns.
- `WARN` means the pipeline likely ran but has stale or optional/marginal outputs.
- `PASS` means the output exists, is fresh, and has usable structure.

If this report fails, fix the failing upstream script before relying on executive conclusions.

---

# Output Files

- Health CSV: `{csv_file}`
- Stable health CSV: `{stable_csv}`
- Health report: `{md_file}`
- Stable health report: `{stable_md}`
"""

    write_markdown_report(md_file, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)
    write_markdown_report(stable_md, report, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("")
    print("================================================")
    print("SEO PIPELINE HEALTH CHECK COMPLETE")
    print("================================================")
    print(f"Overall status: {summary['overall_status']}")
    print(f"PASS: {summary['pass_count']}")
    print(f"WARN: {summary['warn_count']}")
    print(f"FAIL: {summary['fail_count']}")
    print(f"Report: {md_file}")
    print("================================================")

    if summary["fail_count"] > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
