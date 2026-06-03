import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import sys
from datetime import datetime

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "competitor_summary"
SOURCE_AGENT = "Marketing"


WATCHLIST = BASE_PATH / r"06_MARKETING\Competitors\competitor_watchlist.csv"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Competitors\Notes"
HISTORY_PATH = BASE_PATH / r"06_MARKETING\Competitors\History"

HISTORY_FILE = HISTORY_PATH / "competitor_history.csv"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
HISTORY_PATH.mkdir(parents=True, exist_ok=True)


# =========================================
# HELPERS
# =========================================

def fetch_page(url):

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0 MORFRAC competitor research bot"
            }
        )

        return response.status_code, response.text

    except Exception as e:
        return None, str(e)


def extract_metadata(html):

    soup = BeautifulSoup(html, "html.parser")

    title = ""

    if soup.title and soup.title.string:
        title = soup.title.string.strip()

    description = ""

    desc_tag = soup.find("meta", attrs={"name": "description"})

    if desc_tag and desc_tag.get("content"):
        description = desc_tag.get("content").strip()

    return title, description


def clean_table_text(value):

    if value is None:
        return ""

    return str(value).replace("|", "-").replace("\n", " ").replace("\r", " ").strip()


# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    if not WATCHLIST.exists():
        print("Missing competitor_watchlist.csv")
        return

    df = pd.read_csv(WATCHLIST)

    rows = []

    for _, row in df.iterrows():

        company = row.get("company", "")
        website = row.get("website", "")
        notes = row.get("notes", "")
        priority = row.get("priority", "")

        print(f"Checking {company}: {website}")

        status, html = fetch_page(website)

        title = ""
        description = ""

        if status == 200:
            title, description = extract_metadata(html)

        rows.append({
            "company": company,
            "website": website,
            "priority": priority,
            "status": status,
            "title": title,
            "description": description,
            "notes": notes,
        })

    # =====================================
    # WRITE MARKDOWN REPORT
    # =====================================

    output_file = OUTPUT_PATH / f"{run_date}_Competitor_Summary.md"

    content = f"""# Competitor Summary

## Date

{run_date}

## Source

{WATCHLIST}

## Summary Table

| Company | Priority | Status | Website | Title | Meta Description |
|---|---|---:|---|---|---|
"""

    for item in rows:

        content += (
            f"| {clean_table_text(item['company'])} "
            f"| {clean_table_text(item['priority'])} "
            f"| {clean_table_text(item['status'])} "
            f"| {clean_table_text(item['website'])} "
            f"| {clean_table_text(item['title'])} "
            f"| {clean_table_text(item['description'])} |\n"
        )

    content += """

## Notes

This is a lightweight homepage metadata scan.

Use this report for:
- competitor positioning review
- messaging comparison
- future SEO/content monitoring

This does not yet perform:
- deep crawling
- keyword ranking tracking
- ad monitoring
- LinkedIn monitoring
- backlink analysis
"""

    write_markdown_report(output_file, content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    # =====================================
    # UPDATE HISTORY CSV
    # =====================================

    history_rows = []

    for item in rows:

        history_rows.append({
            "date": run_date,
            "company": item["company"],
            "website": item["website"],
            "title": item["title"],
            "description": item["description"],
            "status": item["status"],
        })

    history_df = pd.DataFrame(history_rows)

    if HISTORY_FILE.exists():

        existing_df = pd.read_csv(HISTORY_FILE)

        combined_df = pd.concat(
            [existing_df, history_df],
            ignore_index=True
        )

        combined_df.to_csv(HISTORY_FILE, index=False)

    else:

        history_df.to_csv(HISTORY_FILE, index=False)

    print("\nCOMPETITOR SUMMARY CREATED\n")
    print(output_file)

    print("\nCOMPETITOR HISTORY UPDATED\n")
    print(HISTORY_FILE)


if __name__ == "__main__":
    main()