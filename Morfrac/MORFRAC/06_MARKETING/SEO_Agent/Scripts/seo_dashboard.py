from pathlib import Path
from datetime import datetime
import csv
import html
import re


BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")
MARKETING_PATH = BASE_PATH / "06_MARKETING"
SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"
OUTPUT_PATH = SEO_AGENT_PATH / "Dashboard"
REPORT_HTML_PATH = OUTPUT_PATH / "Reports"
RUNNERS_PATH = OUTPUT_PATH / "Run_Scripts"
MARKETING_DASHBOARD_PATH = OUTPUT_PATH / "Marketing"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
REPORT_HTML_PATH.mkdir(parents=True, exist_ok=True)
RUNNERS_PATH.mkdir(parents=True, exist_ok=True)
MARKETING_DASHBOARD_PATH.mkdir(parents=True, exist_ok=True)

TODAY = datetime.today().strftime("%Y-%m-%d")


def latest_file(folder, pattern):
    folder = Path(folder)
    files = list(folder.glob(pattern)) if folder.exists() else []
    if not files:
        return None
    return max(files, key=lambda path: path.stat().st_mtime)


def read_csv_rows(path):
    if not path or not Path(path).exists():
        return []

    with open(path, "r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def file_count(folder, pattern):
    folder = Path(folder)
    return len(list(folder.glob(pattern))) if folder.exists() else 0


def latest_marketing_cards(path):
    if not path or not Path(path).exists():
        return []

    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    pattern = re.compile(
        r'<div class="card-title">(.*?)</div>\s*'
        r'<div class="card-value">(.*?)</div>\s*'
        r'<div class="card-sub">(.*?)</div>',
        re.S,
    )

    cards = []
    for title, value, note in pattern.findall(text):
        cards.append({
            "metric": html.unescape(re.sub(r"<.*?>", "", title)).strip(),
            "value": html.unescape(re.sub(r"<.*?>", "", value)).strip(),
            "note": html.unescape(re.sub(r"<.*?>", "", note)).strip(),
        })

    return cards


def to_float(value):
    try:
        if value in (None, ""):
            return 0.0
        return float(str(value).replace(",", ""))
    except ValueError:
        return 0.0


def to_int(value):
    return int(round(to_float(value)))


def fmt_number(value):
    return f"{to_int(value):,}"


def fmt_score(value):
    return f"{to_float(value):.2f}"


def rel_path(path):
    if not path:
        return ""
    try:
        return Path(path).relative_to(SEO_AGENT_PATH).as_posix()
    except ValueError:
        return Path(path).as_uri()


def file_link(path, label=None):
    if not path:
        return '<span class="muted">Not available</span>'
    label = label or Path(path).name
    href = html.escape(rel_path(path), quote=True)
    return f'<a href="{href}">{html.escape(label)}</a>'


def report_html_filename(path):
    if not path:
        return None
    path = Path(path)
    folder = path.parent.name
    safe_name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", f"{folder}__{path.stem}.html")
    return REPORT_HTML_PATH / safe_name


def inline_markdown(text):
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def markdown_table_to_html(lines):
    rows = []

    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)

    if not rows:
        return ""

    headers = rows[0]
    body_rows = rows[2:] if len(rows) > 1 and all(set(cell) <= {"-", ":", " "} for cell in rows[1]) else rows[1:]
    thead = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
    body = []

    for row in body_rows:
        if len(row) < len(headers):
            row += [""] * (len(headers) - len(row))
        cells = "".join(f"<td>{inline_markdown(cell)}</td>" for cell in row[:len(headers)])
        body.append(f"<tr>{cells}</tr>")

    return f"""
    <div class="report-table-wrap">
      <table>
        <thead><tr>{thead}</tr></thead>
        <tbody>{''.join(body)}</tbody>
      </table>
    </div>
    """


def markdown_to_html(markdown):
    output = []
    lines = markdown.splitlines()
    index = 0
    in_code = False
    code_lines = []
    list_open = False
    ordered_open = False

    def close_lists():
        nonlocal list_open, ordered_open
        if list_open:
            output.append("</ul>")
            list_open = False
        if ordered_open:
            output.append("</ol>")
            ordered_open = False

    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                close_lists()
                in_code = True
            index += 1
            continue

        if in_code:
            code_lines.append(line)
            index += 1
            continue

        if not stripped:
            close_lists()
            index += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            close_lists()
            table_lines = []
            while index < len(lines):
                table_line = lines[index].strip()
                if not (table_line.startswith("|") and table_line.endswith("|")):
                    break
                table_lines.append(table_line)
                index += 1
            output.append(markdown_table_to_html(table_lines))
            continue

        if stripped == "---":
            close_lists()
            output.append("<hr>")
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            close_lists()
            level = min(len(heading.group(1)), 4)
            output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            index += 1
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        if bullet:
            if ordered_open:
                output.append("</ol>")
                ordered_open = False
            if not list_open:
                output.append("<ul>")
                list_open = True
            output.append(f"<li>{inline_markdown(bullet.group(1))}</li>")
            index += 1
            continue

        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if ordered:
            if list_open:
                output.append("</ul>")
                list_open = False
            if not ordered_open:
                output.append("<ol>")
                ordered_open = True
            output.append(f"<li>{inline_markdown(ordered.group(1))}</li>")
            index += 1
            continue

        close_lists()
        output.append(f"<p>{inline_markdown(stripped)}</p>")
        index += 1

    close_lists()

    if in_code:
        output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")

    return "\n".join(output)


def render_markdown_report(source_path, title):
    if not source_path or not Path(source_path).exists():
        return None

    source_path = Path(source_path)
    output_path = report_html_filename(source_path)
    markdown = source_path.read_text(encoding="utf-8-sig")
    body = markdown_to_html(markdown)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    report_html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #090d12;
      --surface: #101722;
      --surface-2: #151f2d;
      --line: #243244;
      --text: #e6edf5;
      --muted: #96a3b5;
      --accent: #5eead4;
      --accent-2: #93c5fd;
      --code: #dbeafe;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Segoe UI, Arial, sans-serif;
      line-height: 1.58;
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 1;
      padding: 18px 28px;
      background: rgba(9, 13, 18, 0.94);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(8px);
    }}
    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px;
    }}
    h1 {{ margin: 0; font-size: 24px; letter-spacing: 0; }}
    h2 {{ margin: 32px 0 12px; font-size: 20px; letter-spacing: 0; color: #f8fbff; }}
    h3 {{ margin: 24px 0 10px; font-size: 17px; letter-spacing: 0; }}
    h4 {{ margin: 18px 0 8px; font-size: 15px; letter-spacing: 0; color: var(--accent); }}
    p {{ margin: 10px 0; color: #d7e1ee; }}
    a {{ color: var(--accent-2); text-decoration: none; font-weight: 650; }}
    a:hover {{ text-decoration: underline; }}
    .meta {{ margin-top: 6px; color: var(--muted); font-size: 13px; }}
    .actions {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; }}
    .button {{
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 7px 11px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--surface-2);
      color: var(--text);
    }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 26px 0; }}
    ul, ol {{ margin: 10px 0 14px 24px; padding: 0; }}
    li {{ margin: 6px 0; }}
    code {{
      color: var(--code);
      background: #172033;
      border: 1px solid #26364d;
      border-radius: 4px;
      padding: 1px 5px;
      font-size: 0.92em;
    }}
    pre {{
      overflow-x: auto;
      background: #0d1420;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 14px;
    }}
    pre code {{ border: 0; background: transparent; padding: 0; }}
    .report-table-wrap {{
      overflow-x: auto;
      margin: 14px 0 22px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--surface);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      padding: 9px 10px;
      text-align: left;
      vertical-align: top;
      border-bottom: 1px solid var(--line);
    }}
    th {{
      position: sticky;
      top: 72px;
      background: #182334;
      color: #dbeafe;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0;
    }}
    tr:nth-child(even) td {{ background: rgba(255, 255, 255, 0.018); }}
    tr:last-child td {{ border-bottom: 0; }}
    @media (max-width: 800px) {{
      header, main {{ padding-left: 16px; padding-right: 16px; }}
      th {{ position: static; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>{html.escape(title)}</h1>
    <div class="meta">Formatted view generated {html.escape(generated_at)} from {html.escape(rel_path(source_path))}</div>
    <div class="actions">
      <a class="button" href="../../seo_dashboard.html">Dashboard</a>
      <a class="button" href="../../{html.escape(rel_path(source_path), quote=True)}">Source Markdown</a>
      <a class="button" href="../../{html.escape(rel_path(source_path.parent), quote=True)}/">Report Folder</a>
    </div>
  </header>
  <main>
    {body}
  </main>
</body>
</html>
"""

    output_path.write_text(report_html, encoding="utf-8")
    return output_path


def folder_link(folder, label="History"):
    folder = Path(folder)
    try:
        href = folder.relative_to(SEO_AGENT_PATH).as_posix() + "/"
    except ValueError:
        href = folder.as_uri() + "/"
    href = html.escape(href, quote=True)
    return f'<a class="secondary-link" href="{href}">{html.escape(label)}</a>'


def count_where(rows, column, value):
    return sum(1 for row in rows if str(row.get(column, "")).strip() == value)


def count_in(rows, column, values):
    values = set(values)
    return sum(1 for row in rows if str(row.get(column, "")).strip() in values)


def sum_column(rows, column):
    return sum(to_float(row.get(column)) for row in rows)


def avg_column(rows, column):
    values = [to_float(row.get(column)) for row in rows if str(row.get(column, "")).strip() != ""]
    return sum(values) / len(values) if values else 0.0


def table(rows, columns, limit=10):
    if not rows:
        return '<div class="empty">No data available.</div>'

    rows = rows[:limit]
    header = "".join(f"<th>{html.escape(label)}</th>" for _, label in columns)
    body = []

    for row in rows:
        cells = []
        for key, _ in columns:
            value = row.get(key, "")
            cells.append(f"<td>{html.escape(str(value))}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")

    return f"""
    <div class="table-wrap">
      <table>
        <thead><tr>{header}</tr></thead>
        <tbody>{''.join(body)}</tbody>
      </table>
    </div>
    """


def metric_card(label, value, note=""):
    return f"""
    <section class="metric">
      <div class="metric-label">{html.escape(label)}</div>
      <div class="metric-value">{html.escape(str(value))}</div>
      <div class="metric-note">{html.escape(note)}</div>
    </section>
    """


def write_runner(filename, title, command_lines):
    runner_path = RUNNERS_PATH / filename
    body = [
        "@echo off",
        f"echo ==============================",
        f"echo {title}",
        f"echo ==============================",
        "echo.",
        *command_lines,
        "if errorlevel 1 (",
        "    echo.",
        "    echo Script failed.",
        "    pause",
        "    exit /b %errorlevel%",
        ")",
        "echo.",
        "echo Complete.",
        "echo.",
        "pause",
        "",
    ]
    runner_path.write_text("\n".join(body), encoding="utf-8")
    return runner_path


def script_runner(script_name, title):
    return write_runner(
        f"run_{Path(script_name).stem}.bat",
        title,
        [
            rf"cd /d {SEO_AGENT_PATH}\Scripts",
            f"py {script_name}",
            "if errorlevel 1 exit /b %errorlevel%",
            "py seo_dashboard.py",
        ],
    )


def run_button(path, label, primary=False):
    klass = "button primary" if primary else "button"
    return f'<a class="{klass}" href="{html.escape(rel_path(path), quote=True)}">{html.escape(label)}</a>'


def server_run_button(task_id, label, primary=False):
    klass = "button primary run-script-button" if primary else "button run-script-button"
    return (
        f'<button class="{klass}" type="button" data-task="{html.escape(task_id, quote=True)}">'
        f'{html.escape(label)}</button>'
    )


def report_row(title, folder, latest_pattern, stable_name=None, note=""):
    folder_path = SEO_AGENT_PATH / folder
    latest = latest_file(folder_path, latest_pattern)
    stable = folder_path / stable_name if stable_name else None
    latest_html = render_markdown_report(latest, title) if latest and latest.suffix.lower() == ".md" else None
    stable_html = render_markdown_report(stable, f"{title} Stable") if stable and stable.exists() and stable.suffix.lower() == ".md" else None
    stable_link = file_link(stable_html or stable, "Stable") if stable and stable.exists() else '<span class="muted">No stable file</span>'
    latest_link = file_link(latest_html or latest, "Latest") if latest else '<span class="muted">No latest file</span>'
    modified = latest.stat().st_mtime if latest else None
    modified_text = datetime.fromtimestamp(modified).strftime("%Y-%m-%d %H:%M") if modified else "Not available"

    return f"""
    <tr>
      <td><strong>{html.escape(title)}</strong><div class="row-note">{html.escape(note)}</div></td>
      <td>{latest_link}</td>
      <td>{stable_link}</td>
      <td>{folder_link(folder_path)}</td>
      <td>{html.escape(modified_text)}</td>
    </tr>
    """


def sort_by_number(rows, column, reverse=True):
    return sorted(rows, key=lambda row: to_float(row.get(column)), reverse=reverse)


def main():
    files = {
        "merged": latest_file(SEO_AGENT_PATH / "Merged_Analysis", "*_search_console_merge.csv")
        or SEO_AGENT_PATH / "Merged_Analysis" / "search_console_merge.csv",
        "semantic_clusters": latest_file(SEO_AGENT_PATH / "Semantic_Clusters", "*_semantic_clusters.csv")
        or SEO_AGENT_PATH / "Semantic_Clusters" / "semantic_clusters.csv",
        "semantic_cannibalization": latest_file(SEO_AGENT_PATH / "Semantic_Clusters", "*_semantic_cannibalization.csv")
        or SEO_AGENT_PATH / "Semantic_Clusters" / "semantic_cannibalization.csv",
        "semantic_orphans": latest_file(SEO_AGENT_PATH / "Semantic_Clusters", "*_semantic_orphan_topics.csv"),
        "content_gaps": latest_file(SEO_AGENT_PATH / "Content_Gap_Analysis", "*_content_gap_analysis.csv")
        or SEO_AGENT_PATH / "Content_Gap_Analysis" / "content_gap_analysis.csv",
        "topic_authority": latest_file(SEO_AGENT_PATH / "Topic_Authority_Map", "*_topic_authority_map.csv")
        or SEO_AGENT_PATH / "Topic_Authority_Map" / "topic_authority_map.csv",
        "contextual_links": latest_file(SEO_AGENT_PATH / "Contextual_Links", "*_contextual_link_recommendations_filtered.csv")
        or SEO_AGENT_PATH / "Contextual_Links" / "contextual_link_recommendations_filtered.csv",
        "entity_opportunities": latest_file(SEO_AGENT_PATH / "Entity_Relationship_Map", "*_entity_opportunities.csv")
        or SEO_AGENT_PATH / "Entity_Relationship_Map" / "entity_opportunities.csv",
        "pipeline_health": latest_file(SEO_AGENT_PATH / "Pipeline_Health", "*_pipeline_health_check.csv")
        or SEO_AGENT_PATH / "Pipeline_Health" / "pipeline_health_check.csv",
        "marketing_dashboard": latest_file(MARKETING_PATH / "Dashboards", "*_Marketing_Dashboard.html"),
        "marketing_executive_report": latest_file(MARKETING_PATH / "Executive_Reports", "*_Executive_Marketing_Report.md"),
        "marketing_review": latest_file(MARKETING_PATH / "Reviews", "*_Marketing_Review.md"),
        "competitor_summary": latest_file(MARKETING_PATH / r"Competitors\Notes", "*_Competitor_Summary.md"),
        "search_console_raw": latest_file(MARKETING_PATH / r"Analytics\Raw_Data\SearchConsole", "*_SearchConsole_Raw_Data.md"),
        "ga4_raw": latest_file(MARKETING_PATH / r"Analytics\Raw_Data\GA4", "*_GA4_Raw_Data.md"),
        "weekly_report": latest_file(MARKETING_PATH / r"Analytics\Weekly_Reports", "*_Weekly_Marketing_Report.md"),
    }

    merged_rows = read_csv_rows(files["merged"])
    cluster_rows = read_csv_rows(files["semantic_clusters"])
    cannibal_rows = read_csv_rows(files["semantic_cannibalization"])
    orphan_rows = read_csv_rows(files["semantic_orphans"])
    gap_rows = read_csv_rows(files["content_gaps"])
    authority_rows = read_csv_rows(files["topic_authority"])
    contextual_rows = read_csv_rows(files["contextual_links"])
    entity_rows = read_csv_rows(files["entity_opportunities"])
    health_rows = read_csv_rows(files["pipeline_health"])
    competitor_history_rows = read_csv_rows(MARKETING_PATH / r"Competitors\History\competitor_history.csv")
    marketing_cards = latest_marketing_cards(files["marketing_dashboard"])

    total_impressions = sum_column(merged_rows, "impressions")
    total_clicks = sum_column(merged_rows, "clicks")
    avg_position = avg_column(merged_rows, "position")
    avg_authority = avg_column(authority_rows, "topic_authority_score")
    top_topics = sort_by_number(authority_rows, "topic_authority_score", reverse=True)
    weak_topics = [row for row in authority_rows if row.get("authority_tier") in ("VERY_WEAK", "WEAK")]
    at_risk_topics = [row for row in authority_rows if row.get("strategic_status") == "TOPIC_AT_RISK"]
    commercial_gaps = [
        row for row in authority_rows
        if row.get("strategic_status") == "HIGH_COMMERCIAL_LOW_AUTHORITY"
    ]
    dominant_topics = [row for row in authority_rows if row.get("authority_tier") == "DOMINANT"]
    top_entities = sort_by_number(entity_rows, "entity_opportunity_score", reverse=True)
    health_fail = count_where(health_rows, "status", "FAIL")
    health_warn = count_where(health_rows, "status", "WARN")
    health_pass = count_where(health_rows, "status", "PASS")
    indexed_pages = count_where(merged_rows, "indexable", "True") + count_where(merged_rows, "indexable", "TRUE")
    search_console_exports = file_count(MARKETING_PATH / r"Analytics\Raw_Data\SearchConsole", "*_SearchConsole_Raw_Data.md")
    ga4_exports = file_count(MARKETING_PATH / r"Analytics\Raw_Data\GA4", "*_GA4_Raw_Data.md")
    marketing_dashboards = file_count(MARKETING_PATH / "Dashboards", "*_Marketing_Dashboard.html")
    blog_assets = file_count(MARKETING_PATH / r"Content\Blog", "*.md")
    landing_assets = file_count(MARKETING_PATH / r"Content\Landing_Pages", "*.md")
    linkedin_assets = file_count(MARKETING_PATH / r"Content\Social\LinkedIn", "*.md")

    report_rows = [
        report_row("Executive SEO Review", "Executive_Reviews", "*_SEO_Executive_Review.md", "SEO_Executive_Review.md", "Main executive intelligence report."),
        report_row("Pipeline Health", "Pipeline_Health", "*_pipeline_health_report.md", "pipeline_health_report.md", "Pass, warn, fail checks for latest outputs."),
        report_row("Topic Authority Map", "Topic_Authority_Map", "*_topic_authority_report.md", None, "Authority tiers, commercial gaps, topic risks."),
        report_row("Entity Relationship Map", "Entity_Relationship_Map", "*_entity_relationship_report.md", None, "Entity opportunities and crawl-derived relationship graph."),
        report_row("Content Gap Analysis", "Content_Gap_Analysis", "*_content_gap_report.md", None, "Missing pillars, authority gaps, orphan commercial topics."),
        report_row("Semantic Cluster Analysis", "Semantic_Clusters", "*_semantic_cluster_report.md", None, "Clusters, cannibalization and orphan topic risks."),
        report_row("Search Console Merge", "Merged_Analysis", "*_search_console_merge.md", "search_console_merge.md", "Crawl data merged with Search Console visibility."),
        report_row("Contextual Links", "Contextual_Links", "*_contextual_link_recommendations.md", None, "Filtered internal link recommendations."),
        report_row("Historical Comparison", "Historical_Comparisons", "*_SEO_Historical_Comparison.md", None, "Trend and change report across pipeline runs."),
        report_row("Action Plan", "Action_Plans", "*_seo_action_plan.md", None, "Prioritized implementation actions."),
    ]

    metrics = [
        metric_card("Pipeline Status", f"{health_fail} fail / {health_warn} warn", f"{health_pass} checks passing"),
        metric_card("Pages In Merge", fmt_number(len(merged_rows)), f"{fmt_number(indexed_pages)} indexable"),
        metric_card("Search Visibility", fmt_number(total_impressions), f"{fmt_number(total_clicks)} clicks"),
        metric_card("Average Position", fmt_score(avg_position), "Search Console merged pages"),
        metric_card("Semantic Clusters", fmt_number(len(cluster_rows)), f"{fmt_number(len(orphan_rows))} orphan topics"),
        metric_card("Cannibalization Pairs", fmt_number(len(cannibal_rows)), "Semantic risk pairs"),
        metric_card("Content Gaps", fmt_number(len(gap_rows)), "Detected gap rows"),
        metric_card("Avg Authority Score", fmt_score(avg_authority), f"{fmt_number(len(authority_rows))} topics scored"),
        metric_card("Commercial Authority Gaps", fmt_number(len(commercial_gaps)), "High commercial / low authority"),
        metric_card("Weak Topics", fmt_number(len(weak_topics)), f"{fmt_number(len(at_risk_topics))} at risk"),
        metric_card("Dominant Topics", fmt_number(len(dominant_topics)), "Authority tier DOMINANT"),
        metric_card("Contextual Links", fmt_number(len(contextual_rows)), "Filtered recommendations"),
        metric_card("Entity Opportunities", fmt_number(len(entity_rows)), "Entity relationship layer"),
        metric_card("SC Base Exports", fmt_number(search_console_exports), "Marketing Search Console raw files"),
        metric_card("GA4 Base Exports", fmt_number(ga4_exports), "Marketing analytics raw files"),
        metric_card("Competitor Snapshots", fmt_number(len(competitor_history_rows)), "Rows in competitor history"),
        metric_card("Generated Content Assets", fmt_number(blog_assets + landing_assets + linkedin_assets), f"{fmt_number(blog_assets)} blog / {fmt_number(landing_assets)} landing / {fmt_number(linkedin_assets)} LinkedIn"),
        metric_card("Marketing Dashboards", fmt_number(marketing_dashboards), "Historical dashboard files"),
    ]

    dashboard_runner = write_runner(
        "run_dashboard_refresh.bat",
        "MORFRAC SEO DASHBOARD REFRESH",
        [
            rf"cd /d {SEO_AGENT_PATH}\Scripts",
            "py seo_dashboard.py",
        ],
    )
    full_pipeline_runner = write_runner(
        "run_full_seo_pipeline.bat",
        "MORFRAC FULL SEO PIPELINE",
        [
            rf"cd /d {BASE_PATH}\02_AGENTS\SEO",
            "call run_seo_pipeline.bat",
        ],
    )
    marketing_reports_runner = write_runner(
        "run_marketing_reports.bat",
        "MORFRAC MARKETING REPORTS",
        [
            rf"cd /d {BASE_PATH}\02_AGENTS\Marketing",
            "call run_marketing_reports.bat",
        ],
    )
    competitor_monitoring_runner = write_runner(
        "run_competitor_monitoring.bat",
        "MORFRAC COMPETITOR MONITORING",
        [
            rf"cd /d {BASE_PATH}\02_AGENTS\Marketing",
            "call run_competitor_monitoring.bat",
        ],
    )
    runner_buttons = [
        server_run_button("dashboard", "Refresh Dashboard", primary=True),
        server_run_button("pipeline", "Run Full SEO Pipeline", primary=True),
        server_run_button("marketing_reports", "Run Marketing Reports", primary=True),
        server_run_button("competitor_monitoring", "Run Competitor Monitoring"),
        server_run_button("health", "Run Health Check"),
        server_run_button("executive", "Run Executive Review"),
        server_run_button("topic_authority", "Run Topic Authority"),
        server_run_button("content_gaps", "Run Content Gaps"),
        server_run_button("entity_map", "Run Entity Map"),
    ]

    marketing_source_rows = [
        {
            "source": "Marketing Dashboard",
            "latest": file_link(files["marketing_dashboard"], "Latest dashboard"),
            "folder": folder_link(MARKETING_PATH / "Dashboards"),
            "note": "Executive marketing KPIs and commentary.",
        },
        {
            "source": "Marketing Executive Report",
            "latest": file_link(files["marketing_executive_report"], "Latest report"),
            "folder": folder_link(MARKETING_PATH / "Executive_Reports"),
            "note": "Executive marketing report generated by marketing pipeline.",
        },
        {
            "source": "Marketing Review",
            "latest": file_link(files["marketing_review"], "Latest review"),
            "folder": folder_link(MARKETING_PATH / "Reviews"),
            "note": "Base marketing review input.",
        },
        {
            "source": "Competitor Summary",
            "latest": file_link(files["competitor_summary"], "Latest summary"),
            "folder": folder_link(MARKETING_PATH / r"Competitors\Notes"),
            "note": "Competitor monitoring output.",
        },
        {
            "source": "Search Console Raw Data",
            "latest": file_link(files["search_console_raw"], "Latest raw export"),
            "folder": folder_link(MARKETING_PATH / r"Analytics\Raw_Data\SearchConsole"),
            "note": "Upstream base file for SEO pipeline visibility.",
        },
        {
            "source": "GA4 Raw Data",
            "latest": file_link(files["ga4_raw"], "Latest raw export"),
            "folder": folder_link(MARKETING_PATH / r"Analytics\Raw_Data\GA4"),
            "note": "Upstream analytics base file.",
        },
        {
            "source": "Weekly Marketing Report",
            "latest": file_link(files["weekly_report"], "Latest report"),
            "folder": folder_link(MARKETING_PATH / r"Analytics\Weekly_Reports"),
            "note": "Weekly analytics summary.",
        },
    ]

    marketing_card_rows = [
        {
            "metric": card["metric"],
            "value": card["value"],
            "note": card["note"],
        }
        for card in marketing_cards[:8]
    ]
    marketing_source_table = "".join(
        f"""
        <tr>
          <td><strong>{html.escape(row["source"])}</strong><div class="row-note">{html.escape(row["note"])}</div></td>
          <td>{row["latest"]}</td>
          <td>{row["folder"]}</td>
        </tr>
        """
        for row in marketing_source_rows
    )
    marketing_dashboard_copy = None
    if files["marketing_dashboard"] and Path(files["marketing_dashboard"]).exists():
        marketing_dashboard_copy = MARKETING_DASHBOARD_PATH / "latest_marketing_dashboard.html"
        marketing_dashboard_copy.write_text(
            Path(files["marketing_dashboard"]).read_text(encoding="utf-8", errors="ignore"),
            encoding="utf-8",
        )

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    dashboard = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MORFRAC SEO Dashboard</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #090d12;
      --surface: #101722;
      --surface-2: #151f2d;
      --surface-3: #1a2635;
      --line: #243244;
      --text: #e6edf5;
      --muted: #96a3b5;
      --accent: #5eead4;
      --accent-2: #93c5fd;
      --risk: #fca5a5;
      --warn: #fcd34d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Segoe UI, Arial, sans-serif;
      background: radial-gradient(circle at 20% -10%, rgba(94, 234, 212, 0.08), transparent 32%), var(--bg);
      color: var(--text);
      line-height: 1.45;
    }}
    header {{
      padding: 28px 32px 20px;
      background: rgba(16, 23, 34, 0.96);
      border-bottom: 1px solid var(--line);
      box-shadow: 0 16px 44px rgba(0, 0, 0, 0.24);
    }}
    main {{
      padding: 24px 32px 40px;
      max-width: 1500px;
      margin: 0 auto;
    }}
    h1, h2, h3 {{ margin: 0; letter-spacing: 0; }}
    h1 {{ font-size: 28px; font-weight: 700; }}
    h2 {{ font-size: 18px; margin: 28px 0 12px; }}
    h3 {{ font-size: 15px; margin: 0 0 10px; }}
    a {{
      color: var(--accent-2);
      text-decoration: none;
      font-weight: 600;
    }}
    a:hover {{ text-decoration: underline; }}
    .subhead {{
      margin-top: 6px;
      color: var(--muted);
      font-size: 14px;
    }}
    .quick-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }}
    .run-panel {{
      margin-top: 18px;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: rgba(21, 31, 45, 0.72);
    }}
    .run-panel-title {{
      color: #f8fbff;
      font-size: 14px;
      font-weight: 750;
      margin-bottom: 4px;
    }}
    .run-panel-note {{
      color: var(--muted);
      font-size: 12px;
      margin-bottom: 10px;
    }}
    .button {{
      display: inline-flex;
      align-items: center;
      min-height: 36px;
      padding: 8px 12px;
      border: 1px solid var(--line);
      background: var(--surface-2);
      border-radius: 6px;
      color: var(--text);
      font-size: 13px;
      font-weight: 650;
      cursor: pointer;
      font-family: inherit;
    }}
    .button.primary {{
      border-color: rgba(94, 234, 212, 0.55);
      background: #10302d;
      color: #ccfbf1;
    }}
    .button:disabled {{
      cursor: wait;
      opacity: 0.6;
    }}
    .server-status {{
      margin-top: 12px;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #0d1420;
      color: var(--muted);
      font-size: 13px;
      white-space: pre-wrap;
    }}
    .tabs {{
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--line);
    }}
    .tab-button {{
      min-height: 40px;
      padding: 9px 13px;
      border: 1px solid transparent;
      border-bottom: 0;
      border-radius: 6px 6px 0 0;
      background: transparent;
      color: var(--muted);
      font-family: inherit;
      font-size: 14px;
      font-weight: 750;
      cursor: pointer;
    }}
    .tab-button.active {{
      background: var(--surface);
      border-color: var(--line);
      color: #f8fbff;
    }}
    .tab-panel {{
      display: none;
    }}
    .tab-panel.active {{
      display: block;
    }}
    .marketing-frame {{
      width: 100%;
      min-height: 76vh;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #0d1420;
    }}
    .metrics {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
    }}
    .metric {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 14px;
      min-height: 106px;
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
    }}
    .metric-label {{
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      font-weight: 700;
    }}
    .metric-value {{
      margin-top: 8px;
      font-size: 25px;
      font-weight: 750;
      white-space: nowrap;
      color: #f8fbff;
    }}
    .metric-note {{
      margin-top: 5px;
      color: var(--muted);
      font-size: 13px;
    }}
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .panel {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 16px;
    }}
    .table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--surface);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      padding: 9px 10px;
      text-align: left;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
    }}
    th {{
      background: var(--surface-3);
      font-size: 12px;
      text-transform: uppercase;
      color: #dbeafe;
    }}
    tr:nth-child(even) td {{ background: rgba(255, 255, 255, 0.018); }}
    tr:last-child td {{ border-bottom: 0; }}
    .row-note, .muted, .secondary-link {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 500;
    }}
    .empty {{
      color: var(--muted);
      padding: 12px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--surface);
    }}
    footer {{
      color: var(--muted);
      font-size: 12px;
      padding: 0 32px 26px;
      max-width: 1500px;
      margin: 0 auto;
    }}
    @media (max-width: 900px) {{
      header, main, footer {{ padding-left: 16px; padding-right: 16px; }}
      .grid-2 {{ grid-template-columns: 1fr; }}
      .metric-value {{ font-size: 22px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>MORFRAC SEO Dashboard</h1>
    <div class="subhead">Generated {html.escape(generated_at)}. Opens latest files directly and keeps folder access for historical reports.</div>
    <nav class="quick-actions">
      <a class="button" href="Dashboard/Reports/Executive_Reviews__SEO_Executive_Review.html">Executive Review</a>
      <a class="button" href="Dashboard/Reports/Pipeline_Health__pipeline_health_report.html">Pipeline Health</a>
      <a class="button" href="Topic_Authority_Map/topic_authority_map.csv">Topic Authority CSV</a>
      <a class="button" href="Entity_Relationship_Map/entity_opportunities.csv">Entity Opportunities CSV</a>
      <a class="button" href="Dashboard/">Dashboard Folder</a>
    </nav>
    <section class="run-panel">
      <div class="run-panel-title">Run Scripts</div>
      <div class="run-panel-note">To run scripts from buttons, open this dashboard through the local server: <code>start_seo_dashboard_server.bat</code>, then use <code>http://127.0.0.1:8765/</code>.</div>
      <nav class="quick-actions">
        {''.join(runner_buttons)}
      </nav>
      <div id="server-status" class="server-status">Checking dashboard server...</div>
    </section>
  </header>

  <main>
    <nav class="tabs" aria-label="Dashboard tabs">
      <button class="tab-button active" type="button" data-tab="seo-tab">SEO Dashboard</button>
      <button class="tab-button" type="button" data-tab="marketing-tab">Marketing Dashboard</button>
    </nav>

    <section id="seo-tab" class="tab-panel active">
    <h2>Metrics</h2>
    <section class="metrics">
      {''.join(metrics)}
    </section>

    <h2>Main Reports And History</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Area</th>
            <th>Latest</th>
            <th>Stable</th>
            <th>Folder</th>
            <th>Latest Modified</th>
          </tr>
        </thead>
        <tbody>
          {''.join(report_rows)}
        </tbody>
      </table>
    </div>

    <h2>Marketing Base Files</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Source</th>
            <th>Latest</th>
            <th>Folder</th>
          </tr>
        </thead>
        <tbody>
          {marketing_source_table}
        </tbody>
      </table>
    </div>

    <section class="grid-2">
      <div class="panel">
        <h2>Latest Marketing Dashboard Metrics</h2>
        {table(
            marketing_card_rows,
            [
                ("metric", "Metric"),
                ("value", "Value"),
                ("note", "Note"),
            ],
            limit=8,
        )}
      </div>
      <div class="panel">
        <h2>Competitor Base Signals</h2>
        {table(
            competitor_history_rows[:10],
            [
                ("date", "Date"),
                ("company", "Company"),
                ("website", "Website"),
                ("status", "Status"),
            ],
            limit=10,
        )}
      </div>
    </section>

    <section class="grid-2">
      <div class="panel">
        <h2>Highest Topic Authority</h2>
        {table(
            top_topics,
            [
                ("dominant_label", "Topic"),
                ("topic_authority_score", "Score"),
                ("authority_tier", "Tier"),
                ("strategic_status", "Status"),
                ("total_impressions", "Impressions"),
                ("total_clicks", "Clicks"),
            ],
            limit=10,
        )}
      </div>
      <div class="panel">
        <h2>Commercial Authority Gaps</h2>
        {table(
            commercial_gaps,
            [
                ("dominant_label", "Topic"),
                ("topic_authority_score", "Score"),
                ("commercial_strength", "Commercial"),
                ("authority_strength", "Authority"),
                ("recommended_action", "Action"),
            ],
            limit=10,
        )}
      </div>
    </section>

    <section class="grid-2">
      <div class="panel">
        <h2>Content Gap Priorities</h2>
        {table(
            sort_by_number(gap_rows, "gap_score", reverse=True),
            [
                ("dominant_label", "Topic"),
                ("gap_type", "Gap Type"),
                ("gap_score", "Score"),
                ("recommended_action", "Action"),
            ],
            limit=10,
        )}
      </div>
      <div class="panel">
        <h2>Entity Opportunities</h2>
        {table(
            top_entities,
            [
                ("entity_type", "Type"),
                ("entity_name", "Entity"),
                ("entity_opportunity_score", "Score"),
                ("entity_opportunity_type", "Opportunity"),
                ("total_impressions", "Impressions"),
            ],
            limit=10,
        )}
      </div>
    </section>

    <section class="grid-2">
      <div class="panel">
        <h2>Pipeline Health Checks</h2>
        {table(
            health_rows,
            [
                ("check_name", "Check"),
                ("status", "Status"),
                ("severity", "Severity"),
                ("row_count", "Rows"),
                ("notes", "Notes"),
            ],
            limit=14,
        )}
      </div>
      <div class="panel">
        <h2>Semantic Cannibalization Risks</h2>
        {table(
            sort_by_number(cannibal_rows, "similarity_score", reverse=True),
            [
                ("risk_type", "Risk"),
                ("label_a", "Label A"),
                ("label_b", "Label B"),
                ("similarity_score", "Similarity"),
                ("url_a", "URL A"),
                ("url_b", "URL B"),
            ],
            limit=8,
        )}
      </div>
    </section>
    </section>

    <section id="marketing-tab" class="tab-panel">
      <h2>Marketing Dashboard</h2>
      <div class="panel">
        <div class="quick-actions" style="margin-top: 0; margin-bottom: 12px;">
          {file_link(marketing_dashboard_copy, "Open embedded marketing dashboard") if marketing_dashboard_copy else '<span class="muted">No marketing dashboard available.</span>'}
          {file_link(files["marketing_dashboard"], "Open original latest marketing dashboard") if files["marketing_dashboard"] else ''}
          {folder_link(MARKETING_PATH / "Dashboards", "Marketing dashboard history")}
        </div>
        <iframe class="marketing-frame" src="{html.escape(rel_path(marketing_dashboard_copy), quote=True) if marketing_dashboard_copy else 'about:blank'}" title="Marketing Dashboard"></iframe>
      </div>
    </section>
  </main>

  <footer>
    Dashboard source: Scripts/seo_dashboard.py. Re-run the script after pipeline output changes to refresh this file.
  </footer>
  <script>
    const statusBox = document.getElementById("server-status");
    const runButtons = Array.from(document.querySelectorAll(".run-script-button"));
    const tabButtons = Array.from(document.querySelectorAll(".tab-button"));
    const tabPanels = Array.from(document.querySelectorAll(".tab-panel"));

    function setStatus(message) {{
      statusBox.textContent = message;
    }}

    function isServerMode() {{
      return location.protocol === "http:" && location.hostname === "127.0.0.1" && location.port === "8765";
    }}

    async function refreshStatus() {{
      if (!isServerMode()) {{
        runButtons.forEach((button) => button.disabled = true);
        setStatus("Script buttons are disabled in file mode. Open start_seo_dashboard_server.bat, then use http://127.0.0.1:8765/ to run scripts from the dashboard.");
        return;
      }}

      try {{
        const response = await fetch("/api/tasks");
        const data = await response.json();
        const running = Object.values(data.running || {{}});
        const latest = (data.history || [])[0];

        runButtons.forEach((button) => {{
          button.disabled = running.length > 0;
        }});

        if (running.length > 0) {{
          setStatus("Running: " + running.map((item) => item.label).join(", "));
        }} else if (latest) {{
          setStatus("Last run: " + latest.label + " - " + latest.status + ". Reload the page to see refreshed metrics after dashboard generation completes.");
        }} else {{
          setStatus("Server connected. Choose a script to run.");
        }}
      }} catch (error) {{
        runButtons.forEach((button) => button.disabled = true);
        setStatus("Dashboard server is not reachable. Start it with start_seo_dashboard_server.bat.");
      }}
    }}

    runButtons.forEach((button) => {{
      button.addEventListener("click", async () => {{
        if (!isServerMode()) {{
          setStatus("Open start_seo_dashboard_server.bat first, then use http://127.0.0.1:8765/.");
          return;
        }}

        const taskId = button.dataset.task;
        button.disabled = true;
        setStatus("Starting: " + button.textContent);

        try {{
          const response = await fetch("/api/run/" + encodeURIComponent(taskId), {{ method: "POST" }});
          const data = await response.json();
          setStatus(data.label + ": " + data.status);
          setTimeout(refreshStatus, 1000);
        }} catch (error) {{
          setStatus("Could not start script. Check the dashboard server window.");
        }}
      }});
    }});

    tabButtons.forEach((button) => {{
      button.addEventListener("click", () => {{
        const target = button.dataset.tab;
        tabButtons.forEach((item) => item.classList.toggle("active", item === button));
        tabPanels.forEach((panel) => panel.classList.toggle("active", panel.id === target));
      }});
    }});

    refreshStatus();
    setInterval(refreshStatus, 3000);
  </script>
</body>
</html>
"""

    dashboard_path = SEO_AGENT_PATH / "seo_dashboard.html"
    dashboard_copy_path = OUTPUT_PATH / "seo_dashboard.html"
    dashboard_index_path = OUTPUT_PATH / "index.html"
    redirect_dashboard = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=../seo_dashboard.html">
  <title>MORFRAC SEO Dashboard</title>
</head>
<body>
  <p><a href="../seo_dashboard.html">Open MORFRAC SEO Dashboard</a></p>
</body>
</html>
"""
    dashboard_path.write_text(dashboard, encoding="utf-8")
    dashboard_copy_path.write_text(redirect_dashboard, encoding="utf-8")
    dashboard_index_path.write_text(redirect_dashboard, encoding="utf-8")

    print("")
    print("================================================")
    print("SEO DASHBOARD COMPLETE")
    print("================================================")
    print(f"Dashboard: {dashboard_path}")
    print(f"Dashboard folder redirect: {dashboard_copy_path}")
    print(f"Dashboard folder index: {dashboard_index_path}")
    print(f"Metrics source date: {TODAY}")
    print("================================================")


if __name__ == "__main__":
    main()
