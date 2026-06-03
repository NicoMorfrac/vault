import os
import re
from pathlib import Path
import sys
from datetime import datetime

from openai import OpenAI

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "linkedin_topic_proposals"
SOURCE_AGENT = "Marketing"


INPUT_PATH = BASE_PATH / r"06_MARKETING\Content\Strategy"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Content\Social\LinkedIn_Topic_Proposals"

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

    return max(
        files,
        key=lambda f: f.stat().st_mtime
    )


def read_text(path):

    return path.read_text(encoding="utf-8")


def extract_sections(text):

    sections = []

    pattern = r"### Query\s+(.*?)\s+### Archetype\s+(.*?)\s+### Target Audience\s+(.*?)\s+### Communication Style\s+(.*?)\s+### Suggested CTA\s+(.*?)\s+---"

    matches = re.findall(
        pattern,
        text,
        re.DOTALL
    )

    for match in matches:

        sections.append({
            "query": match[0].strip(),
            "archetype": match[1].strip(),
            "audience": match[2].strip(),
            "style": match[3].strip(),
            "cta": match[4].strip(),
        })

    return sections

# =========================================
# PROMPT
# =========================================

SYSTEM_PROMPT = """
You are a senior B2B marine industry editorial strategist.

Your task is NOT to write full LinkedIn posts.

Your task is to propose:
- strategically valuable LinkedIn topics
- engineering positioning angles
- discussion opportunities
- authority-building content

MORFRAC specializes in:
- performance sailing hardware
- furling systems
- textile systems
- friction rings
- lightweight structural systems
- engineering-driven marine hardware

Avoid:
- generic marketing ideas
- repetitive themes
- vague content
- AI-sounding phrasing

Focus on:
- technical authority
- commercial relevance
- engineering insight
- discussion potential
- differentiated positioning
"""

# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    strategy_file = latest_file(INPUT_PATH)

    if not strategy_file:
        print("No strategy file found.")
        return

    strategy_text = read_text(strategy_file)

    sections = extract_sections(strategy_text)

    if not sections:
        print("No strategy sections found.")
        return

    proposals = []

    for section in sections[:15]:

        prompt = f"""
Create a concise LinkedIn topic proposal.

INPUT:

Query:
{section['query']}

Archetype:
{section['archetype']}

Audience:
{section['audience']}

Communication Style:
{section['style']}

CTA:
{section['cta']}

Generate:

1. Topic Title
2. Why This Matters
3. Strategic Angle
4. Discussion Potential
5. Recommended Tone
6. Priority Score (1-10)

Keep concise and commercially intelligent.
"""

        print(f"Generating proposal: {section['query']}")

        response = client.responses.create(
            model=MODEL,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        proposal_text = response.output_text.strip()

        proposals.append(proposal_text)

    output_file = OUTPUT_PATH / (
        f"{run_date}_LinkedIn_Topic_Proposals.md"
    )

    content = f"""# LinkedIn Topic Proposals

## Generated

{run_date}

## Source Strategy File

{strategy_file.name}

---

"""

    for i, proposal in enumerate(proposals, start=1):

        content += f"""
# Proposal {i}

{proposal}

---

"""

    write_markdown_report(output_file, content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nLINKEDIN TOPIC PROPOSALS CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()