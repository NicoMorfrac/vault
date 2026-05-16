import re
import csv
from pathlib import Path
from datetime import datetime

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

GA4_REPORTS = BASE_PATH / r"06_MARKETING\Analytics\Weekly_Reports"
SEO_REPORTS = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Reviews"
TREND_PATH = BASE_PATH / r"06_MARKETING\Trend_Data"
TREND_FILE = TREND_PATH / "marketing_trends.csv"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
TREND_PATH.mkdir(parents=True, exist_ok=True)


# =========================================
# HELPERS
# =========================================

def latest_file(path, pattern="*.md"):
    files = list(path.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def read_file(filepath):
    return filepath.read_text(encoding="utf-8")


def find_percentage(text, label):
    pattern = rf"{re.escape(label)}:\s*(-?\d+\.?\d*)%"
    match = re.search(pattern, text)
    if match:
        return float(match.group(1))
    return None


def find_float(text, label):
    pattern = rf"{re.escape(label)}:\s*(-?\d+\.?\d*)"
    match = re.search(pattern, text)
    if match:
        return float(match.group(1))
    return None


def safe_value(value):
    if value is None:
        return ""
    return value


def add_unique(items, message):
    if message not in items:
        items.append(message)


def ensure_trend_file():
    if not TREND_FILE.exists():
        with open(TREND_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date",
                "sessions_7_change",
                "sessions_28_change",
                "click_change",
                "impression_change",
                "ctr_change",
                "position_change",
                "alerts",
                "opportunities",
                "campaigns"
            ])


def read_trends():
    ensure_trend_file()

    rows = []

    with open(TREND_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    return rows


def append_trend(row):
    ensure_trend_file()

    existing = read_trends()

    # Avoid duplicate same-date rows
    existing = [r for r in existing if r.get("date") != row["date"]]
    existing.append(row)

    with open(TREND_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "date",
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

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing)


def to_float(value):
    try:
        if value in ["", None]:
            return None
        return float(value)
    except ValueError:
        return None


def detect_persistent_trends(trends):
    if len(trends) < 3:
        return []

    recent = trends[-3:]
    findings = []

    sessions_28 = [to_float(r.get("sessions_28_change")) for r in recent]
    clicks = [to_float(r.get("click_change")) for r in recent]
    ctr = [to_float(r.get("ctr_change")) for r in recent]

    if all(v is not None and v < 0 for v in sessions_28):
        findings.append("Persistent issue: 28-day traffic has declined for the last 3 recorded reviews.")

    if all(v is not None and v < 0 for v in clicks):
        findings.append("Persistent issue: organic clicks have declined for the last 3 recorded reviews.")

    if all(v is not None and v < 0 for v in ctr):
        findings.append("Persistent issue: organic CTR has declined for the last 3 recorded reviews.")

    if all(v is not None and v > 0 for v in sessions_28):
        findings.append("Positive trend: 28-day traffic has improved for the last 3 recorded reviews.")

    if all(v is not None and v > 0 for v in clicks):
        findings.append("Positive trend: organic clicks have improved for the last 3 recorded reviews.")

    return findings


# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    ga4_file = latest_file(GA4_REPORTS)
    seo_file = latest_file(SEO_REPORTS)

    if not ga4_file or not seo_file:
        print("Missing reports.")
        return

    ga4_text = read_file(ga4_file)
    seo_text = read_file(seo_file)

    alerts = []
    opportunities = []
    campaigns = []

    # =====================================
    # GA4 SIGNALS
    # =====================================

    sessions_change_7 = find_percentage(ga4_text, "7-day sessions change")
    sessions_change_28 = find_percentage(ga4_text, "28-day sessions change")

    if sessions_change_7 is not None:
        if sessions_change_7 < -20:
            add_unique(alerts, f"CRITICAL: 7-day sessions dropped {sessions_change_7:.1f}%.")
        elif sessions_change_7 > 20:
            add_unique(opportunities, f"Traffic increased {sessions_change_7:.1f}% over 7 days.")

    if sessions_change_28 is not None:
        if sessions_change_28 < -20:
            add_unique(alerts, f"CRITICAL: 28-day sessions dropped {sessions_change_28:.1f}%.")
        elif sessions_change_28 > 20:
            add_unique(opportunities, f"Traffic increased {sessions_change_28:.1f}% over 28 days.")

    # =====================================
    # SEO SIGNALS
    # =====================================

    ctr_change = find_percentage(seo_text, "CTR change")
    impression_change = find_percentage(seo_text, "Impression change")
    click_change = find_percentage(seo_text, "Click change")
    position_change = find_float(seo_text, "Position change")

    if ctr_change is not None:
        if ctr_change < -15:
            add_unique(alerts, f"Organic CTR dropped {ctr_change:.1f}%.")
        elif ctr_change > 15:
            add_unique(opportunities, f"Organic CTR improved {ctr_change:.1f}%.")

    if impression_change is not None:
        if impression_change < -20:
            add_unique(alerts, f"Organic impressions dropped {impression_change:.1f}%.")
        elif impression_change > 20:
            add_unique(opportunities, f"Organic impressions increased {impression_change:.1f}%.")

    if click_change is not None:
        if click_change < -20:
            add_unique(alerts, f"Organic clicks dropped {click_change:.1f}%.")
        elif click_change > 20:
            add_unique(opportunities, f"Organic clicks increased {click_change:.1f}%.")

    if position_change is not None and position_change > 5:
        add_unique(alerts, f"Average ranking worsened by {position_change:.1f} positions.")

    # =====================================
    # OPPORTUNITY DETECTION
    # =====================================

    seo_lower = seo_text.lower()

    if "dogbones" in seo_lower or "dogbone" in seo_lower:
        add_unique(opportunities, "Dogbone-related queries detected with SEO visibility.")
        add_unique(campaigns, "Create SEO landing page and LinkedIn content focused on dogbone rigging systems.")

    if "soft pad eye" in seo_lower:
        add_unique(opportunities, "Soft pad eye keyword visibility detected.")
        add_unique(campaigns, "Create educational content around soft pad eyes and textile attachment systems.")

    if "mreel" in seo_lower:
        add_unique(opportunities, "mreel search visibility detected.")
        add_unique(campaigns, "Strengthen branded SEO content and product explanation pages for mreel.")

    if "farr x2" in seo_lower:
        add_unique(opportunities, "Farr X2 query visibility detected.")
        add_unique(campaigns, "Create Farr X2 related performance optimization content.")

    # =====================================
    # TREND MEMORY
    # =====================================

    trend_row = {
        "date": run_date,
        "sessions_7_change": safe_value(sessions_change_7),
        "sessions_28_change": safe_value(sessions_change_28),
        "click_change": safe_value(click_change),
        "impression_change": safe_value(impression_change),
        "ctr_change": safe_value(ctr_change),
        "position_change": safe_value(position_change),
        "alerts": len(alerts),
        "opportunities": len(opportunities),
        "campaigns": len(campaigns),
    }

    append_trend(trend_row)

    trends = read_trends()
    persistent_findings = detect_persistent_trends(trends)

    for finding in persistent_findings:
        if finding.startswith("Persistent issue"):
            add_unique(alerts, finding)
        else:
            add_unique(opportunities, finding)

    # =====================================
    # PRIORITY
    # =====================================

    priority = "Low"

    if len(alerts) >= 3:
        priority = "High"
    elif len(alerts) >= 1:
        priority = "Medium"
    elif len(opportunities) >= 3:
        priority = "Medium"

    # =====================================
    # BUILD REPORT
    # =====================================

    report_file = OUTPUT_PATH / f"{run_date}_Marketing_Review.md"

    report_content = f"""# Marketing Review

## Objective

Review latest marketing and SEO reports, detect anomalies, identify opportunities, and maintain trend memory.

## Source Reports

GA4 Report:

{ga4_file}

SEO Report:

{seo_file}

Trend File:

{TREND_FILE}

## Executive Summary

- Alerts detected: {len(alerts)}
- Opportunities detected: {len(opportunities)}
- Campaign ideas generated: {len(campaigns)}
- Overall priority: {priority}

## Current Signals

| Metric | Value |
|---|---:|
| 7-day sessions change | {safe_value(sessions_change_7)} |
| 28-day sessions change | {safe_value(sessions_change_28)} |
| Organic click change | {safe_value(click_change)} |
| Organic impression change | {safe_value(impression_change)} |
| Organic CTR change | {safe_value(ctr_change)} |
| Position change | {safe_value(position_change)} |

## Alerts

"""

    if alerts:
        for item in alerts:
            report_content += f"- {item}\n"
    else:
        report_content += "- No critical alerts detected.\n"

    report_content += "\n## Opportunities\n\n"

    if opportunities:
        for item in opportunities:
            report_content += f"- {item}\n"
    else:
        report_content += "- No major opportunities detected.\n"

    report_content += "\n## Campaign Ideas\n\n"

    if campaigns:
        for item in campaigns:
            report_content += f"- {item}\n"
    else:
        report_content += "- No campaign ideas generated.\n"

    report_content += "\n## Persistent Trend Findings\n\n"

    if persistent_findings:
        for item in persistent_findings:
            report_content += f"- {item}\n"
    else:
        report_content += "- Not enough recurring trend evidence yet, or no persistent trend detected.\n"

    report_content += f"""

## Recommended Actions

### High Priority

- Investigate major traffic or SEO drops immediately.
- Review ranking losses and CTR deterioration.
- Validate whether changes correlate with website changes, indexing changes, campaign activity, or external market factors.

### Medium Priority

- Improve low CTR queries with strong impressions.
- Strengthen non-branded SEO visibility.
- Expand content around rising search topics.

### Low Priority

- Continue monitoring current trends.
- Maintain reporting cadence.

## Traceability

- Generated: {run_date}
- Generated by: marketing_review.py
- Trend memory updated: {TREND_FILE}
"""

    report_file.write_text(report_content, encoding="utf-8")

    print("\nMARKETING REVIEW CREATED\n")
    print(report_file)
    print("\nTREND MEMORY UPDATED\n")
    print(TREND_FILE)


if __name__ == "__main__":
    main()