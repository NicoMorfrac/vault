import re
from pathlib import Path
from datetime import datetime

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

INPUT_PATH = BASE_PATH / r"06_MARKETING\SEO\Content_Opportunities"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Content\Strategy"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def latest_file(path, pattern="*.md"):

    files = list(path.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def read_text(path):

    return path.read_text(encoding="utf-8")


# =========================================
# EXTRACT OPPORTUNITIES
# =========================================

def extract_queries(text):

    rows = []

    for line in text.splitlines():

        if not line.startswith("|"):
            continue

        if "---" in line:
            continue

        cols = [c.strip() for c in line.split("|")]

        if len(cols) < 9:
            continue

        query = cols[1]

        if query.lower() == "query":
            continue

        rows.append(query)

    return rows

# =========================================
# STRATEGY CLASSIFICATION
# =========================================

def classify_archetype(query):

    q = query.lower()

    # =====================================
    # COMPARISON
    # =====================================

    if "vs" in q:
        return {
            "archetype": "Comparison",
            "audience": "Buyers evaluating alternatives",
            "style": "Analytical",
            "cta": "Discuss tradeoffs and engineering choices"
        }

    # =====================================
    # EDUCATIONAL
    # =====================================

    if "how" in q or "what" in q:
        return {
            "archetype": "Educational",
            "audience": "Sailors researching solutions",
            "style": "Technical explanation",
            "cta": "Learn more about engineering implications"
        }

    # =====================================
    # MATERIAL / ENGINEERING
    # =====================================

    engineering_terms = [
        "friction",
        "load",
        "padeye",
        "dogbone",
        "rigging",
        "furling",
        "ring",
        "soft shackle",
        "textile"
    ]

    for term in engineering_terms:

        if term in q:
            return {
                "archetype": "Technical Authority",
                "audience": "Performance sailing audience",
                "style": "Engineering-focused",
                "cta": "Discuss engineering and optimization"
            }

    # =====================================
    # COMMERCIAL
    # =====================================

    if "price" in q or "cost" in q:
        return {
            "archetype": "Commercial Intent",
            "audience": "Purchase-oriented visitors",
            "style": "Commercial technical",
            "cta": "Request project consultation"
        }

    # =====================================
    # DEFAULT
    # =====================================

    return {
        "archetype": "Industry Insight",
        "audience": "General sailing audience",
        "style": "Professional insight",
        "cta": "Encourage discussion"
    }

# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    latest_input = latest_file(INPUT_PATH)

    if not latest_input:
        print("No Content Opportunities file found.")
        return

    text = read_text(latest_input)

    queries = extract_queries(text)

    if not queries:
        print("No queries detected.")
        return

    output_file = OUTPUT_PATH / (
        f"{run_date}_Content_Strategy.md"
    )

    content = f"""# Content Strategy Classification

## Generated

{run_date}

## Source

{latest_input.name}

## Strategic Content Archetypes

"""

    for query in queries[:25]:

        strategy = classify_archetype(query)

        content += f"""
### Query

{query}

### Archetype

{strategy['archetype']}

### Target Audience

{strategy['audience']}

### Communication Style

{strategy['style']}

### Suggested CTA

{strategy['cta']}

---

"""

    output_file.write_text(
        content,
        encoding="utf-8"
    )

    print("\nCONTENT STRATEGY CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()