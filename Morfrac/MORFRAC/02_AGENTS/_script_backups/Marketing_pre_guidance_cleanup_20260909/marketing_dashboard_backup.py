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

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Dashboards"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# LOAD DATA
# =========================================

if not TREND_FILE.exists():
    print("Trend file missing.")
    exit()

df = pd.read_csv(TREND_FILE)

if df.empty:
    print("Trend file is empty.")
    exit()

# =========================================
# CLEAN DATA
# =========================================

numeric_columns = [
    "sessions_7_change",
    "sessions_28_change",
    "click_change",
    "impression_change",
    "ctr_change",
    "position_change",
    "alerts",
    "opportunities",
    "campaigns"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df["date"] = df["date"].astype(str)

# =========================================
# CHART HELPER
# =========================================

def style_chart(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111111",
        plot_bgcolor="#1a1a1a",
        font=dict(color="white"),
        margin=dict(l=40, r=40, t=70, b=40)
    )

    fig.update_xaxes(type="category")

    return fig


charts = []

# =========================================
# GENERATE CHARTS
# =========================================

fig_sessions_28 = px.line(
    df,
    x="date",
    y="sessions_28_change",
    title="28-Day Sessions Change Trend",
    markers=True
)

charts.append(
    plot(style_chart(fig_sessions_28), output_type="div", include_plotlyjs="cdn")
)

fig_sessions_7 = px.line(
    df,
    x="date",
    y="sessions_7_change",
    title="7-Day Sessions Change Trend",
    markers=True
)

charts.append(
    plot(style_chart(fig_sessions_7), output_type="div", include_plotlyjs=False)
)

fig_clicks = px.line(
    df,
    x="date",
    y="click_change",
    title="Organic Click Change Trend",
    markers=True
)

charts.append(
    plot(style_chart(fig_clicks), output_type="div", include_plotlyjs=False)
)

fig_impressions = px.line(
    df,
    x="date",
    y="impression_change",
    title="Organic Impression Change Trend",
    markers=True
)

charts.append(
    plot(style_chart(fig_impressions), output_type="div", include_plotlyjs=False)
)

fig_ctr = px.line(
    df,
    x="date",
    y="ctr_change",
    title="Organic CTR Change Trend",
    markers=True
)

charts.append(
    plot(style_chart(fig_ctr), output_type="div", include_plotlyjs=False)
)

fig_alerts = px.bar(
    df,
    x="date",
    y=["alerts", "opportunities", "campaigns"],
    title="Alerts / Opportunities / Campaign Ideas",
    barmode="group"
)

charts.append(
    plot(style_chart(fig_alerts), output_type="div", include_plotlyjs=False)
)

# =========================================
# SUMMARY VALUES
# =========================================

latest = df.iloc[-1]

latest_date = latest.get("date", "")
latest_sessions_7 = latest.get("sessions_7_change", "")
latest_sessions_28 = latest.get("sessions_28_change", "")
latest_click_change = latest.get("click_change", "")
latest_impression_change = latest.get("impression_change", "")
latest_ctr_change = latest.get("ctr_change", "")
latest_position_change = latest.get("position_change", "")
latest_alerts = latest.get("alerts", "")
latest_opportunities = latest.get("opportunities", "")
latest_campaigns = latest.get("campaigns", "")

# =========================================
# HTML DASHBOARD
# =========================================

run_date = datetime.today().strftime("%Y-%m-%d")

dashboard_file = OUTPUT_PATH / f"{run_date}_Marketing_Dashboard.html"

html = f"""
<html>
<head>
    <title>MORFRAC Marketing Dashboard</title>

    <style>
        body {{
            background-color: #111111;
            color: white;
            font-family: Arial, sans-serif;
            margin: 40px;
        }}

        h1, h2 {{
            color: white;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            margin-bottom: 40px;
        }}

        .card {{
            background-color: #1c1c1c;
            border: 1px solid #333;
            padding: 18px;
            border-radius: 10px;
        }}

        .card-title {{
            color: #aaa;
            font-size: 13px;
            margin-bottom: 8px;
        }}

        .card-value {{
            font-size: 26px;
            font-weight: bold;
        }}

        .chart {{
            margin-bottom: 60px;
            background-color: #111111;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 40px;
            color: white;
        }}

        th, td {{
            border: 1px solid #444;
            padding: 10px;
            text-align: left;
        }}

        th {{
            background-color: #222;
        }}

        td {{
            background-color: #161616;
        }}

        .note {{
            color: #bbb;
            margin-bottom: 30px;
        }}
    </style>
</head>

<body>

<h1>MORFRAC Marketing Dashboard</h1>

<p class="note">Generated: {run_date}</p>

<h2>Latest Signals</h2>

<div class="summary-grid">

    <div class="card">
        <div class="card-title">Latest Data Point</div>
        <div class="card-value">{latest_date}</div>
    </div>

    <div class="card">
        <div class="card-title">7-Day Sessions Change</div>
        <div class="card-value">{latest_sessions_7}</div>
    </div>

    <div class="card">
        <div class="card-title">28-Day Sessions Change</div>
        <div class="card-value">{latest_sessions_28}</div>
    </div>

    <div class="card">
        <div class="card-title">Organic Click Change</div>
        <div class="card-value">{latest_click_change}</div>
    </div>

    <div class="card">
        <div class="card-title">Organic Impression Change</div>
        <div class="card-value">{latest_impression_change}</div>
    </div>

    <div class="card">
        <div class="card-title">Organic CTR Change</div>
        <div class="card-value">{latest_ctr_change}</div>
    </div>

    <div class="card">
        <div class="card-title">Position Change</div>
        <div class="card-value">{latest_position_change}</div>
    </div>

    <div class="card">
        <div class="card-title">Alerts</div>
        <div class="card-value">{latest_alerts}</div>
    </div>

    <div class="card">
        <div class="card-title">Opportunities / Campaigns</div>
        <div class="card-value">{latest_opportunities} / {latest_campaigns}</div>
    </div>

</div>

<h2>Trend Charts</h2>

<div class="chart">{charts[0]}</div>
<div class="chart">{charts[1]}</div>
<div class="chart">{charts[2]}</div>
<div class="chart">{charts[3]}</div>
<div class="chart">{charts[4]}</div>
<div class="chart">{charts[5]}</div>

<h2>Trend Data</h2>

{df.to_html(index=False)}

</body>
</html>
"""

dashboard_file.write_text(html, encoding="utf-8")

print("\nMARKETING DASHBOARD CREATED\n")
print(dashboard_file)