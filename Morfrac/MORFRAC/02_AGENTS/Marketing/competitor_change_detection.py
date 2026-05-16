import pandas as pd
from pathlib import Path
from datetime import datetime

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

HISTORY_FILE = BASE_PATH / r"06_MARKETING\Competitors\History\competitor_history.csv"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Competitors\Change_Reports"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def clean(value):

    if pd.isna(value):
        return ""

    return str(value).strip()


# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    if not HISTORY_FILE.exists():
        print("Missing competitor_history.csv")
        return

    df = pd.read_csv(HISTORY_FILE)

    if df.empty:
        print("History file is empty.")
        return

    df["date"] = df["date"].astype(str)

    companies = sorted(df["company"].dropna().unique())

    changes = []

    for company in companies:

        company_df = df[df["company"] == company].copy()

        company_df = company_df.sort_values("date")

        if len(company_df) < 2:
            continue

        latest = company_df.iloc[-1]
        previous = company_df.iloc[-2]

        latest_title = clean(latest["title"])
        previous_title = clean(previous["title"])

        latest_description = clean(latest["description"])
        previous_description = clean(previous["description"])

        latest_status = clean(latest["status"])
        previous_status = clean(previous["status"])

        company_changes = []

        # =====================================
        # STATUS CHANGE
        # =====================================

        if latest_status != previous_status:

            company_changes.append(
                f"Website status changed from {previous_status} to {latest_status}"
            )

        # =====================================
        # TITLE CHANGE
        # =====================================

        if latest_title != previous_title:

            company_changes.append(
                "Homepage title changed"
            )

        # =====================================
        # DESCRIPTION CHANGE
        # =====================================

        if latest_description != previous_description:

            company_changes.append(
                "Meta description changed"
            )

        if company_changes:

            changes.append({
                "company": company,
                "changes": company_changes
            })

    # =========================================
    # BUILD REPORT
    # =========================================

    output_file = OUTPUT_PATH / f"{run_date}_Competitor_Changes.md"

    content = f"""# Competitor Change Detection

## Date

{run_date}

## Source

{HISTORY_FILE}

## Detected Changes

"""

    if changes:

        for item in changes:

            content += f"### {item['company']}\n\n"

            for change in item["changes"]:
                content += f"- {change}\n"

            content += "\n"

    else:

        content += "No competitor changes detected.\n"

    content += """

## Notes

This report compares:
- latest competitor snapshot
vs
- previous historical snapshot

Current checks:
- website status changes
- homepage title changes
- meta description changes

Future checks may include:
- keyword analysis
- homepage content shifts
- product terminology changes
- SEO direction changes
- campaign detection
"""

    output_file.write_text(content, encoding="utf-8")

    print("\nCOMPETITOR CHANGE REPORT CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()