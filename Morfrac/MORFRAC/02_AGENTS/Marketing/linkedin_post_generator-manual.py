import os
import re
from pathlib import Path
from datetime import datetime

from openai import OpenAI

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

INPUT_PATH = BASE_PATH / r"06_MARKETING\Content\Strategy"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Content\Social\LinkedIn"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

MODEL = "gpt-5.4-mini"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# =========================================
# HELPERS
# =========================================

def latest_files(path, limit=5):

    files = list(path.glob("*_Content_Strategy.md"))

    if not files:
        return []

    files = sorted(
        files,
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    return files[:limit]


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
You are a senior marine industry marketing strategist.

You write LinkedIn posts for MORFRAC.

MORFRAC specializes in:
- high-performance sailing hardware
- furling systems
- textile systems
- friction rings
- lightweight engineering
- custom marine hardware
- structural sailing systems

Writing style requirements:
- technically credible
- engineering-oriented
- concise
- commercially intelligent
- authoritative but not arrogant
- no emojis
- avoid generic marketing language
- avoid sounding AI-generated
- create strong hooks
- focus on engineering insight
- encourage discussion
- vary tone depending on strategic archetype

Post structure:
- strong opening hook
- technical insight
- industry observation
- MORFRAC positioning
- CTA or discussion point

Do not invent fake projects or fake customer stories.
"""

# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    strategy_files = latest_files(INPUT_PATH)

    if not strategy_files:
        print("No content strategy files found.")
        return

    generated = 0

    for strategy_file in strategy_files:

        source_text = read_text(strategy_file)

        sections = extract_sections(source_text)

        if not sections:
            print(f"No strategy sections found in {strategy_file.name}")
            continue

        for section in sections[:10]:

            query = section["query"]
            archetype = section["archetype"]
            audience = section["audience"]
            style = section["style"]
            cta = section["cta"]

            prompt = f"""
Generate a polished LinkedIn post for MORFRAC.

QUERY:
{query}

ARCHETYPE:
{archetype}

TARGET AUDIENCE:
{audience}

COMMUNICATION STYLE:
{style}

CTA DIRECTION:
{cta}

Requirements:
- 150 to 300 words
- professional LinkedIn style
- technically credible
- marine/performance sailing context
- create engagement
- no emojis
- no hashtags
- no excessive formatting
- vary tone depending on archetype
- avoid repetitive structure
- focus on engineering insight
"""

            print(f"\nGenerating LinkedIn post for: {query}")

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

            post_text = response.output_text.strip()

            safe_query = re.sub(
                r"[^a-zA-Z0-9]+",
                "_",
                query.lower()
            ).strip("_")

            output_file = OUTPUT_PATH / (
                f"{run_date}_{safe_query}_LinkedIn.md"
            )

            output_content = f"""# LinkedIn Post

## Generated

{run_date}

## Query

{query}

## Archetype

{archetype}

## Audience

{audience}

---

{post_text}
"""

            output_file.write_text(
                output_content,
                encoding="utf-8"
            )

            generated += 1

            print(f"Created: {output_file.name}")

    print("\nLINKEDIN POST GENERATION COMPLETE\n")
    print(f"Posts generated: {generated}")


if __name__ == "__main__":
    main()