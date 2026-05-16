from pathlib import Path
from datetime import datetime
import re
import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

WEEKLY_REPORTS = BASE_PATH / r"06_MARKETING\Analytics\Weekly_Reports"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Analytics\Traffic_Quality"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# COMMERCIAL TERRITORY CLASSIFICATION
# =========================================

HIGH_RELEVANCE = {
    "Southern Europe": [
        "Spain",
        "Italy",
        "France",
        "Portugal",
    ],
    "Northern Europe": [
        "Germany",
        "Netherlands",
        "Denmark",
        "Sweden",
        "Norway",
        "Finland",
    ],
    "Oceania": [
        "Australia",
        "New Zealand",
    ],
}

US_MONITORING = [
    "United States",
]

MEDIUM_RELEVANCE = {
    "South America": [
        "Argentina",
        "Brazil",
        "Chile",
        "Uruguay",
    ],
}

LOW_TIER = [
    "Singapore",
    "Hong Kong",
    "United Arab Emirates",
    "UAE",
    "China",
    "India",
    "Vietnam",
    "Russia",
    "(not set)",
    "",
]

SUSPICIOUS_PAGES = [
    "/web/login",
    "(not set)",
    "",
]

# =========================================
# HELPERS
# =========================================

def latest_file(path, pattern="*.md"):
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


def extract_table(text, heading):
    pattern = rf"### {re.escape(heading)}\s+(.*?)(?:\n\n|## |\Z)"
    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return []

    table_text = match.group(1)
    lines = table_text.splitlines()

    rows = []

    for line in lines:
        if "|" not in line:
            continue

        if "---" in line:
            continue

        cols = [c.strip() for c in line.split("|")]
        cols = [c for c in cols if c != ""]

        if len(cols) < 3:
            continue

        first_col = cols[0].strip().lower()

        if first_col in [
            "country",
            "landingpage",
            "landing page",
            "sessions",
            "session sourcemedium",
            "sessionsourcemedium",
        ]:
            continue

        rows.append(cols)

    return rows


def classify_country(country):
    country = str(country).strip()

    for territory, countries in HIGH_RELEVANCE.items():
        if country in countries:
            return {
                "tier": "HIGH",
                "territory": territory,
                "confidence": "High commercial relevance",
            }

    if country in US_MONITORING:
        return {
            "tier": "US_MONITORING",
            "territory": "United States",
            "confidence": "Commercially relevant but crawler/noise prone",
        }

    for territory, countries in MEDIUM_RELEVANCE.items():
        if country in countries:
            return {
                "tier": "MEDIUM",
                "territory": territory,
                "confidence": "Medium commercial relevance",
            }

    if country in LOW_TIER:
        return {
            "tier": "LOW",
            "territory": "Low Tier / Low Confidence",
            "confidence": "Low confidence or high-noise geography",
        }

    return {
        "tier": "LOW",
        "territory": "Low Tier / Low Confidence",
        "confidence": "Unclassified geography treated as low confidence",
    }


def pct(part, total):
    if total == 0:
        return 0

    return round((part / total) * 100, 1)


def dataframe_to_markdown(df):
    if df.empty:
        return "No data available."

    headers = list(df.columns)

    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for _, row in df.iterrows():
        values = [str(row[col]) for col in headers]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    weekly_file = latest_file(WEEKLY_REPORTS)

    if not weekly_file:
        print("No weekly report found.")
        return

    text = read_text(weekly_file)

    geography_rows = extract_table(
        text,
        "Geography"
    )

    landing_rows = extract_table(
        text,
        "Top Landing Pages"
    )

    country_results = []
    suspicious_notes = []

    # =====================================
    # GEOGRAPHY ANALYSIS
    # =====================================

    for row in geography_rows:
        try:
            country = row[0]
            sessions = int(float(row[1]))
            users = int(float(row[2]))

        except Exception:
            continue

        classification = classify_country(country)

        tier = classification["tier"]
        territory = classification["territory"]
        confidence = classification["confidence"]

        notes = []

        if tier == "LOW":
            notes.append(
                "Low-tier or low-confidence geography"
            )

        if tier == "US_MONITORING":
            notes.append(
                "USA requires engagement validation due to crawler/datacenter noise risk"
            )

        if sessions > 20 and tier == "LOW":
            notes.append(
                "High session volume from low-confidence geography"
            )

        if sessions > 20 and tier == "US_MONITORING":
            notes.append(
                "High USA session volume should be checked for engagement quality"
            )

        country_results.append({
            "country": country,
            "territory": territory,
            "tier": tier,
            "sessions": sessions,
            "users": users,
            "confidence": confidence,
            "notes": "; ".join(notes)
        })

    df = pd.DataFrame(country_results)

    if df.empty:
        print("No geography rows found.")
        return

    # =====================================
    # LANDING PAGE ANALYSIS
    # =====================================

    for row in landing_rows:
        try:
            page = row[0]
            sessions = int(float(row[1]))
            users = int(float(row[2]))
            engaged = int(float(row[3]))

        except Exception:
            continue

        if page in SUSPICIOUS_PAGES:
            suspicious_notes.append(
                f"Suspicious landing page detected: {page or '[blank]'} "
                f"(sessions={sessions})"
            )

        if sessions > 5 and engaged == 0:
            suspicious_notes.append(
                f"Low engagement traffic detected on {page or '[blank]'} "
                f"(sessions={sessions}, engagedSessions=0)"
            )

    # =====================================
    # SUMMARY CALCULATIONS
    # =====================================

    total_sessions = int(df["sessions"].sum())

    high_sessions = int(
        df[df["tier"] == "HIGH"]["sessions"].sum()
    )

    medium_sessions = int(
        df[df["tier"] == "MEDIUM"]["sessions"].sum()
    )

    us_sessions = int(
        df[df["tier"] == "US_MONITORING"]["sessions"].sum()
    )

    low_sessions = int(
        df[df["tier"] == "LOW"]["sessions"].sum()
    )

    high_pct = pct(high_sessions, total_sessions)
    medium_pct = pct(medium_sessions, total_sessions)
    us_pct = pct(us_sessions, total_sessions)
    low_pct = pct(low_sessions, total_sessions)

    territory_summary = (
        df.groupby(["territory", "tier"], as_index=False)
        .agg({
            "sessions": "sum",
            "users": "sum"
        })
        .sort_values(
            "sessions",
            ascending=False
        )
    )

    # =====================================
    # INTERPRETATION
    # =====================================

    interpretation = []

    if high_pct >= 50:
        interpretation.append(
            "Most traffic is concentrated in high commercial relevance territories."
        )

    elif high_pct < 35:
        interpretation.append(
            "High commercial relevance traffic appears weak relative to total sessions."
        )

    if low_pct > 25:
        interpretation.append(
            "A significant share of traffic comes from low-tier or low-confidence territories."
        )

    if us_pct > 10:
        interpretation.append(
            "United States traffic is material and should be interpreted separately because it may include both commercial interest and crawler/datacenter noise."
        )

    if suspicious_notes:
        interpretation.append(
            "Suspicious or low-engagement landing page patterns were detected."
        )

    if not interpretation:
        interpretation.append(
            "No major traffic quality concerns detected from current rule set."
        )

    # =====================================
    # OUTPUT CSV
    # =====================================

    csv_file = OUTPUT_PATH / (
        f"{run_date}_Traffic_Quality_Data.csv"
    )

    df.to_csv(
        csv_file,
        index=False
    )

    # =====================================
    # OUTPUT MARKDOWN REPORT
    # =====================================

    report_file = OUTPUT_PATH / (
        f"{run_date}_Traffic_Quality_Report.md"
    )

    report = f"""# Traffic Quality Analysis

## Generated

{run_date}

## Source

{weekly_file}

---

# Executive Interpretation

{" ".join(interpretation)}

---

# Traffic Confidence Summary

| Segment | Sessions | Share |
|---|---:|---:|
| High commercial relevance | {high_sessions} | {high_pct}% |
| Medium commercial relevance | {medium_sessions} | {medium_pct}% |
| United States monitoring | {us_sessions} | {us_pct}% |
| Low tier / low confidence | {low_sessions} | {low_pct}% |
| Total analyzed | {total_sessions} | 100.0% |

---

# Territory Summary

{dataframe_to_markdown(territory_summary)}

---

# Country-Level Analysis

{dataframe_to_markdown(df)}

---

# Suspicious Signals

"""

    if suspicious_notes:
        for note in suspicious_notes:
            report += f"- {note}\n"

    else:
        report += "- No major suspicious signals detected.\n"

    report += """

---

# Interpretation Rules

High commercial relevance:
- Southern Europe
- Northern Europe
- Oceania

United States monitoring:
- commercially important
- interpreted separately because of crawler and datacenter traffic risk

Medium commercial relevance:
- South America

Low tier / low confidence:
- Singapore
- Hong Kong
- UAE
- China
- India
- Vietnam
- Russia
- unknown or unclassified regions

This report is a rule-based traffic qualification layer.
It does not prove whether traffic is human, bot, commercial, or non-commercial.
It provides a confidence filter for executive interpretation.
"""

    report_file.write_text(
        report,
        encoding="utf-8"
    )

    print("\nTRAFFIC QUALITY ANALYSIS COMPLETE\n")
    print(f"CSV: {csv_file}")
    print(f"REPORT: {report_file}")


if __name__ == "__main__":
    main()