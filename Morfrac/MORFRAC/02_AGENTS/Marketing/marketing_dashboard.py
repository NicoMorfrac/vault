import re
import pandas as pd
from pathlib import Path
from datetime import datetime
import plotly.express as px
from plotly.offline import plot

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

TREND_FILE = BASE_PATH / r"06_MARKETING\Trend_Data\marketing_trends.csv"

STRATEGIC_INTELLIGENCE = BASE_PATH / r"06_MARKETING\Strategic_Intelligence"
TRAFFIC_QUALITY = BASE_PATH / r"06_MARKETING\Analytics\Traffic_Quality"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Dashboards"

# =========================================
# HELPERS
# =========================================

def latest_file(path, pattern="*.md"):
    files = list(path.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def latest_csv(path, pattern="*.csv"):
    files = list(path.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def read_text(path):
    if not path or not path.exists():
        return ""

    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


def clean_md(text):
    if not text:
        return "No data available."

    text = re.sub(r"#{1,6}\s*", "", text)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def extract_section(text, heading):
    patterns = [
        rf"# {re.escape(heading)}\s+(.*?)(?:\n# |\Z)",
        rf"## {re.escape(heading)}\s+(.*?)(?:\n## |\Z)"
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if match:
            return clean_md(match.group(1))

    return "No data available."


def style_chart(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1117",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        margin=dict(l=30, r=20, t=55, b=30),
        height=340
    )

    fig.update_xaxes(type="category")

    return fig


def classify_metric(value, inverse=False):
    try:
        value = float(value)
    except Exception:
        return "UNKNOWN", "#6b7280"

    if not inverse:
        if value <= -20:
            return "CRITICAL", "#991b1b"
        if value <= -10:
            return "WARNING", "#b45309"
        if value >= 10:
            return "POSITIVE", "#166534"
        return "STABLE", "#2563eb"

    if value >= 5:
        return "CRITICAL", "#991b1b"
    if value >= 2:
        return "WARNING", "#b45309"
    if value <= -2:
        return "POSITIVE", "#166534"
    return "STABLE", "#2563eb"


def format_value(value, decimals=1):
    try:
        return f"{float(value):.{decimals}f}"
    except Exception:
        return "N/A"


def metric_card(title, value, subtitle, status, color):
    return f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <div class="card-value">{value}</div>
        <div class="card-sub">{subtitle}</div>
        <div class="status-badge" style="background:{color};">{status}</div>
    </div>
    """


def pct(part, total):
    if total == 0:
        return 0

    return round((part / total) * 100, 1)


# =========================================
# LOAD TREND DATA
# =========================================


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    if not TREND_FILE.exists():
        print("Trend file missing.")
        exit()

    df = pd.read_csv(TREND_FILE)

    if df.empty:
        print("Trend file empty.")
        exit()

    df["date"] = df["date"].astype(str)

    for col in df.columns:
        if col != "date":
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    latest = df.iloc[-1]

    # =========================================
    # LOAD STRATEGIC INTELLIGENCE
    # =========================================

    strategic_file = latest_file(STRATEGIC_INTELLIGENCE)
    strategic_text = read_text(strategic_file)

    executive_summary = extract_section(
        strategic_text,
        "Executive Intelligence Summary"
    )

    key_risks = extract_section(
        strategic_text,
        "Key Risks"
    )

    key_opportunities = extract_section(
        strategic_text,
        "Key Opportunities"
    )

    recommended_actions = extract_section(
        strategic_text,
        "Recommended Executive Actions"
    )

    # =========================================
    # LOAD TRAFFIC QUALITY
    # =========================================

    traffic_quality_csv = latest_csv(TRAFFIC_QUALITY)
    traffic_df = pd.DataFrame()

    if traffic_quality_csv:
        traffic_df = pd.read_csv(traffic_quality_csv)

    high_sessions = 0
    medium_sessions = 0
    us_sessions = 0
    low_sessions = 0

    if not traffic_df.empty:
        traffic_df["sessions"] = pd.to_numeric(
            traffic_df["sessions"],
            errors="coerce"
        )

        high_sessions = traffic_df[
            traffic_df["tier"] == "HIGH"
        ]["sessions"].sum()

        medium_sessions = traffic_df[
            traffic_df["tier"] == "MEDIUM"
        ]["sessions"].sum()

        us_sessions = traffic_df[
            traffic_df["tier"] == "US_MONITORING"
        ]["sessions"].sum()

        low_sessions = traffic_df[
            traffic_df["tier"] == "LOW"
        ]["sessions"].sum()

    total_sessions = (
        high_sessions
        + medium_sessions
        + us_sessions
        + low_sessions
    )

    high_pct = pct(high_sessions, total_sessions)
    medium_pct = pct(medium_sessions, total_sessions)
    us_pct = pct(us_sessions, total_sessions)
    low_pct = pct(low_sessions, total_sessions)

    # =========================================
    # KPI STATUS
    # =========================================

    sessions_status, sessions_color = classify_metric(
        latest["sessions_28_change"]
    )

    click_status, click_color = classify_metric(
        latest["organic_click_change"]
    )

    ctr_status, ctr_color = classify_metric(
        latest["organic_ctr_change"]
    )

    position_status, position_color = classify_metric(
        latest["avg_position_change"],
        inverse=True
    )

    traffic_quality_status = "STABLE"
    traffic_quality_color = "#2563eb"

    if low_pct >= 45:
        traffic_quality_status = "WEAK"
        traffic_quality_color = "#991b1b"
    elif low_pct >= 30:
        traffic_quality_status = "CAUTION"
        traffic_quality_color = "#b45309"
    elif high_pct >= 50:
        traffic_quality_status = "GOOD"
        traffic_quality_color = "#166534"

    low_conf_status = "STABLE"
    low_conf_color = "#2563eb"

    if low_pct >= 45:
        low_conf_status = "WEAK"
        low_conf_color = "#991b1b"
    elif low_pct >= 30:
        low_conf_status = "CAUTION"
        low_conf_color = "#b45309"

    # =========================================
    # CHARTS
    # =========================================

    charts = {}

    fig_sessions = px.line(
        df,
        x="date",
        y="sessions_28",
        title="28-Day Sessions",
        markers=True
    )

    charts["sessions"] = plot(
        style_chart(fig_sessions),
        output_type="div",
        include_plotlyjs=False
    )

    fig_clicks = px.line(
        df,
        x="date",
        y="organic_clicks",
        title="Organic Clicks",
        markers=True
    )

    charts["clicks"] = plot(
        style_chart(fig_clicks),
        output_type="div",
        include_plotlyjs=False
    )

    fig_ctr = px.line(
        df,
        x="date",
        y="organic_ctr",
        title="Organic CTR",
        markers=True
    )

    charts["ctr"] = plot(
        style_chart(fig_ctr),
        output_type="div",
        include_plotlyjs=False
    )

    fig_position = px.line(
        df,
        x="date",
        y="avg_position",
        title="Average Position",
        markers=True
    )

    charts["position"] = plot(
        style_chart(fig_position),
        output_type="div",
        include_plotlyjs=False
    )

    confidence_df = pd.DataFrame({
        "segment": [
            "High",
            "Medium",
            "USA",
            "Low"
        ],
        "sessions": [
            high_sessions,
            medium_sessions,
            us_sessions,
            low_sessions
        ]
    })

    fig_confidence = px.bar(
        confidence_df,
        x="segment",
        y="sessions",
        title="Traffic Confidence Distribution"
    )

    charts["confidence"] = plot(
        style_chart(fig_confidence),
        output_type="div",
        include_plotlyjs="cdn"
    )

    if not traffic_df.empty:
        territory_df = (
            traffic_df
            .groupby("territory", as_index=False)
            .agg({"sessions": "sum"})
            .sort_values(
                "sessions",
                ascending=False
            )
        )

        fig_territory = px.bar(
            territory_df,
            x="territory",
            y="sessions",
            title="Territory Distribution"
        )

        charts["territory"] = plot(
            style_chart(fig_territory),
            output_type="div",
            include_plotlyjs=False
        )
    else:
        charts["territory"] = "<div class='panel'>No territory data available.</div>"

    # =========================================
    # BUILD DASHBOARD
    # =========================================

    run_date = datetime.today().strftime("%Y-%m-%d")

    dashboard_file = (
        OUTPUT_PATH
        / f"{run_date}_Marketing_Dashboard.html"
    )

    html = f"""
    <html>

    <head>

    <title>MORFRAC Marketing Intelligence Dashboard</title>

    <style>

    body {{
        background:#0d1117;
        color:white;
        font-family:Arial,sans-serif;
        margin:0;
    }}

    .page {{
        max-width:1280px;
        margin:auto;
        padding:44px;
    }}

    h1 {{
        font-size:42px;
        margin-bottom:8px;
    }}

    h2 {{
        margin-top:60px;
        margin-bottom:24px;
        border-bottom:1px solid #2d333b;
        padding-bottom:10px;
    }}

    .note {{
        color:#9ca3af;
        margin-bottom:40px;
    }}

    .summary-grid {{
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:18px;
    }}

    .grid-2 {{
        display:grid;
        grid-template-columns:repeat(2,1fr);
        gap:22px;
    }}

    .card {{
        background:#161b22;
        border:1px solid #2d333b;
        border-radius:14px;
        padding:22px;
    }}

    .card-title {{
        color:#9ca3af;
        font-size:13px;
        margin-bottom:10px;
    }}

    .card-value {{
        font-size:30px;
        font-weight:bold;
        margin-bottom:8px;
    }}

    .card-sub {{
        color:#cbd5e1;
        font-size:13px;
        margin-bottom:10px;
    }}

    .status-badge {{
        display:inline-block;
        padding:6px 10px;
        border-radius:999px;
        font-size:11px;
        font-weight:bold;
    }}

    .panel {{
        background:#161b22;
        border:1px solid #2d333b;
        border-radius:14px;
        padding:28px;
        line-height:1.65;
        overflow:hidden;
    }}

    .panel pre {{
        white-space:pre-wrap;
        font-family:Arial,sans-serif;
    }}

    .chart {{
        background:#111827;
        border:1px solid #2d333b;
        border-radius:14px;
        padding:14px;
        min-height:360px;
        overflow:hidden;
    }}

    .table-wrap {{
        overflow-x:auto;
    }}

    table {{
        border-collapse:collapse;
        width:100%;
        margin-top:20px;
        font-size:13px;
    }}

    th, td {{
        border:1px solid #374151;
        padding:8px;
        text-align:left;
    }}

    th {{
        background:#1f2937;
    }}

    td {{
        background:#111827;
    }}

    .footer {{
        margin-top:60px;
        color:#9ca3af;
        font-size:13px;
    }}

    </style>

    </head>

    <body>

    <div class="page">

    <h1>MORFRAC Marketing Intelligence Dashboard</h1>

    <p class="note">
    Generated: {run_date}
    </p>

    <h2>Executive Intelligence</h2>

    <div class="summary-grid">

    {metric_card(
        "Commercial Traffic Quality",
        f"{high_pct:.1f}%",
        "High relevance traffic",
        traffic_quality_status,
        traffic_quality_color
    )}

    {metric_card(
        "Low-Confidence Traffic",
        f"{low_pct:.1f}%",
        "Low-tier traffic",
        low_conf_status,
        low_conf_color
    )}

    {metric_card(
        "Organic CTR",
        f"{format_value(latest['organic_ctr'],2)}%",
        f"{format_value(latest['organic_ctr_change'])}% change",
        ctr_status,
        ctr_color
    )}

    {metric_card(
        "Average Position",
        format_value(latest["avg_position"],2),
        f"Change: {format_value(latest['avg_position_change'],2)}",
        position_status,
        position_color
    )}

    </div>

    <h2>Executive Commentary</h2>

    <div class="panel">
    <pre>{executive_summary}</pre>
    </div>

    <h2>Strategic Risks & Opportunities</h2>

    <div class="grid-2">

    <div class="panel">
    <h3>Key Risks</h3>
    <pre>{key_risks}</pre>
    </div>

    <div class="panel">
    <h3>Key Opportunities</h3>
    <pre>{key_opportunities}</pre>
    </div>

    </div>

    <h2>Traffic Confidence</h2>

    <div class="grid-2">

    <div class="chart">
    {charts["confidence"]}
    </div>

    <div class="chart">
    {charts["territory"]}
    </div>

    </div>

    <h2>Performance Trends</h2>

    <div class="grid-2">

    <div class="chart">{charts["sessions"]}</div>

    <div class="chart">{charts["clicks"]}</div>

    <div class="chart">{charts["ctr"]}</div>

    <div class="chart">{charts["position"]}</div>

    </div>

    <h2>Recommended Executive Actions</h2>

    <div class="panel">
    <pre>{recommended_actions}</pre>
    </div>

    <h2>Trend Data</h2>

    <div class="table-wrap">
    {df.to_html(index=False)}
    </div>

    <div class="footer">

    Strategic Intelligence Source:<br>
    {strategic_file}

    <br><br>

    Traffic Quality Source:<br>
    {traffic_quality_csv}

    </div>

    </div>

    </body>

    </html>
    """

    dashboard_file.write_text(
        html,
        encoding="utf-8"
    )

    print("\nMARKETING DASHBOARD CREATED\n")
    print(dashboard_file)

if __name__ == "__main__":
    main()
