import os
from pathlib import Path
from datetime import datetime

from openai import OpenAI

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

WEEKLY_REPORTS = BASE_PATH / r"06_MARKETING\Analytics\Weekly_Reports"
SEO_REPORTS = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"
MARKETING_REVIEWS = BASE_PATH / r"06_MARKETING\Reviews"
TRAFFIC_QUALITY = BASE_PATH / r"06_MARKETING\Analytics\Traffic_Quality"
CONTENT_OPPORTUNITIES = BASE_PATH / r"06_MARKETING\SEO\Content_Opportunities"
CONTENT_STRATEGY = BASE_PATH / r"06_MARKETING\Content\Strategy"
LINKEDIN_PROPOSALS = BASE_PATH / r"06_MARKETING\Content\Social\LinkedIn_Topic_Proposals"
COMPETITOR_CHANGES = BASE_PATH / r"06_MARKETING\Competitors\Change_Reports"
TREND_FILE = BASE_PATH / r"06_MARKETING\Trend_Data\marketing_trends.csv"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Strategic_Intelligence"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

MODEL = "gpt-5.4-mini"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# =========================================
# HELPERS
# =========================================

def latest_file(path, pattern="*.md"):

    files = list(path.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def read_text(path, max_chars=12000):

    if not path or not path.exists():
        return ""

    text = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    return text[-max_chars:]


def source_line(label, path):

    if not path:
        return f"- {label}: Not found"

    return f"- {label}: {path}"


# =========================================
# PROMPT
# =========================================

SYSTEM_PROMPT = """
You are MORFRAC's senior executive marketing strategist.

You analyze marketing, SEO, traffic quality, competitor, and editorial opportunity data.

MORFRAC is a premium engineering-driven marine hardware company focused on:
- high-performance sailing hardware
- furling systems
- textile interfaces
- friction rings
- lightweight structural systems
- custom engineering solutions
- performance sailing and offshore reliability

Your job is not to summarize files mechanically.

Your job is to produce executive intelligence:
- what changed
- why it matters
- what risks exist
- where the leverage is
- what should be prioritized
- what should not be overreacted to
- what commercial/positioning implications exist
- whether traffic is commercially meaningful or likely polluted by low-confidence signals

Rules:
- Use only the supplied data.
- Do not invent metrics.
- Do not invent competitors.
- Do not invent campaigns.
- Be direct.
- Be critical.
- Be commercially realistic.
- Prioritize engineering authority and technical differentiation.
- Treat low-confidence traffic separately from commercially relevant traffic.
- Do not overvalue traffic volume if traffic quality is weak.
- Do not write generic marketing advice.
- Do not produce final publishing content.
"""

USER_PROMPT_TEMPLATE = """
Create an executive strategic intelligence report for MORFRAC.

Use the data below.

Required output structure:

# Executive Intelligence Summary

A concise senior-level summary.

# What Changed

Identify the most important changes in traffic, SEO, visibility, engagement, traffic quality, content opportunities, and competitor signals.

# Traffic Quality Interpretation

Explain whether the traffic appears commercially meaningful.
Separate:
- high commercial relevance traffic
- United States monitoring traffic
- medium relevance traffic
- low-tier / low-confidence traffic
- suspicious or low-engagement signals

Do not treat all traffic volume as equally valuable.

# Why It Matters

Explain commercial and strategic implications.

# Key Risks

Rank the risks by importance.

# Key Opportunities

Rank the opportunities by leverage.

# SEO / Content Interpretation

Explain what the Search Console and content opportunity data imply.

# Editorial Direction

Recommend which editorial angles are worth developing and why.
Do not create final posts.

# Recommended Executive Actions

Give prioritized actions:
- High priority
- Medium priority
- Low priority

Each action must include:
- action
- reason
- expected impact
- evidence/source signal

# What Not To Do

Identify actions that would be premature, low value, or misleading.

# Final Assessment

Positive / Neutral / Negative / Mixed.
Explain why.

---

# INPUT DATA

## Weekly Marketing Report

{weekly_report}

---

## Traffic Quality Analysis

{traffic_quality}

---

## SEO Query Analysis

{seo_report}

---

## Rule-Based Marketing Review

{marketing_review}

---

## Content Opportunities

{content_opportunities}

---

## Content Strategy

{content_strategy}

---

## LinkedIn Topic Proposals

{linkedin_proposals}

---

## Competitor Changes

{competitor_changes}

---

## Trend Memory CSV

{trend_memory}
"""

# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    weekly_file = latest_file(WEEKLY_REPORTS)
    traffic_quality_file = latest_file(TRAFFIC_QUALITY)
    seo_file = latest_file(SEO_REPORTS)
    marketing_review_file = latest_file(MARKETING_REVIEWS)
    content_opportunities_file = latest_file(CONTENT_OPPORTUNITIES)
    content_strategy_file = latest_file(CONTENT_STRATEGY)
    linkedin_file = latest_file(LINKEDIN_PROPOSALS)
    competitor_file = latest_file(COMPETITOR_CHANGES)

    weekly_report = read_text(weekly_file)
    traffic_quality = read_text(traffic_quality_file)
    seo_report = read_text(seo_file)
    marketing_review = read_text(marketing_review_file)
    content_opportunities = read_text(content_opportunities_file)
    content_strategy = read_text(content_strategy_file)
    linkedin_proposals = read_text(linkedin_file)
    competitor_changes = read_text(competitor_file)
    trend_memory = read_text(TREND_FILE, max_chars=8000)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        weekly_report=weekly_report,
        traffic_quality=traffic_quality,
        seo_report=seo_report,
        marketing_review=marketing_review,
        content_opportunities=content_opportunities,
        content_strategy=content_strategy,
        linkedin_proposals=linkedin_proposals,
        competitor_changes=competitor_changes,
        trend_memory=trend_memory
    )

    print("\nRUNNING OPENAI EXECUTIVE STRATEGIC INTELLIGENCE...\n")

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    output_text = response.output_text.strip()

    output_file = OUTPUT_PATH / f"{run_date}_OpenAI_Executive_Intelligence.md"

    content = f"""# OpenAI Executive Intelligence

## Generated

{run_date}

## Model

{MODEL}

## Source Files

{source_line("Weekly Marketing Report", weekly_file)}
{source_line("Traffic Quality Analysis", traffic_quality_file)}
{source_line("SEO Query Analysis", seo_file)}
{source_line("Marketing Review", marketing_review_file)}
{source_line("Content Opportunities", content_opportunities_file)}
{source_line("Content Strategy", content_strategy_file)}
{source_line("LinkedIn Topic Proposals", linkedin_file)}
{source_line("Competitor Changes", competitor_file)}
{source_line("Trend Memory", TREND_FILE)}

---

{output_text}
"""

    output_file.write_text(
        content,
        encoding="utf-8"
    )

    print("\nOPENAI EXECUTIVE INTELLIGENCE CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()