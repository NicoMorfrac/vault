import re
from pathlib import Path
from datetime import datetime

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

INPUT_PATH = BASE_PATH / r"06_MARKETING\SEO\Content_Opportunities"

BLOG_OUTPUT = BASE_PATH / r"06_MARKETING\Content\Blog"

LANDING_OUTPUT = BASE_PATH / r"06_MARKETING\Content\Landing_Pages"

SOCIAL_OUTPUT = BASE_PATH / r"06_MARKETING\Content\Social"

BLOG_OUTPUT.mkdir(parents=True, exist_ok=True)
LANDING_OUTPUT.mkdir(parents=True, exist_ok=True)
SOCIAL_OUTPUT.mkdir(parents=True, exist_ok=True)

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


def slugify(text):

    text = text.lower()

    text = re.sub(r"[^a-z0-9]+", "_", text)

    return text.strip("_")


# =========================================
# EXTRACT OPPORTUNITIES
# =========================================

def extract_opportunities(text):

    opportunities = []

    lines = text.splitlines()

    for line in lines:

        if not line.startswith("|"):
            continue

        if "---" in line:
            continue

        columns = [c.strip() for c in line.split("|")]

        if len(columns) < 9:
            continue

        query = columns[1]

        if query.lower() == "query":
            continue

        priority = columns[7]
        recommendation = columns[8]

        opportunities.append({
            "query": query,
            "priority": priority,
            "recommendation": recommendation,
        })

    return opportunities


# =========================================
# CONTENT IDEAS
# =========================================

def generate_blog_content(query):

    title = f"{query.title()} — Technical Guide"

    content = f"""# {title}

## Objective

Improve SEO visibility and technical authority
for the query:

{query}

## Suggested Article Structure

1. What is {query}?
2. Applications in performance sailing
3. Common engineering mistakes
4. Material selection
5. Load considerations
6. Comparison with alternatives
7. MORFRAC approach
8. FAQ

## SEO Notes

- Add technical diagrams
- Add internal links
- Add product references
- Add comparison terminology
- Use engineering-focused language

## Suggested CTA

Contact MORFRAC for engineering guidance
and custom hardware solutions.

"""

    return title, content


def generate_landing_page(query):

    title = f"{query.title()} Landing Page"

    content = f"""# {title}

## Goal

Create a focused SEO landing page targeting:

{query}

## Recommended Sections

- Product overview
- Engineering advantages
- Load capability
- Materials
- Typical applications
- Comparison vs alternatives
- FAQ
- Technical downloads

## SEO Focus

- Improve CTR
- Improve ranking
- Increase authority
- Capture commercial intent

## Suggested Assets

- Product renders
- Technical drawings
- Real applications
- Performance examples

"""

    return title, content


def generate_social_post(query):

    content = f"""# Social Content Idea

## Topic

{query}

## LinkedIn Post Direction

Explain:
- engineering problem
- typical industry mistake
- better engineering solution
- real-world sailing application

## Suggested Hook

"Most sailing hardware discussions focus on products.
Few focus on engineering consequences."

## Suggested CTA

Invite technical discussion or project consultation.

"""

    return content


# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    latest_opportunity_file = latest_file(INPUT_PATH)

    if not latest_opportunity_file:
        print("No Content Opportunities file found.")
        return

    text = read_text(latest_opportunity_file)

    opportunities = extract_opportunities(text)

    if not opportunities:
        print("No opportunities detected.")
        return

    generated = 0

    for item in opportunities[:10]:

        query = item["query"]

        priority = item["priority"]

        recommendation = item["recommendation"]

        slug = slugify(query)

        # =====================================
        # BLOG
        # =====================================

        blog_title, blog_content = generate_blog_content(query)

        blog_file = BLOG_OUTPUT / (
            f"{run_date}_{slug}_Blog.md"
        )

        blog_file.write_text(
            blog_content,
            encoding="utf-8"
        )

        # =====================================
        # LANDING PAGE
        # =====================================

        landing_title, landing_content = generate_landing_page(query)

        landing_file = LANDING_OUTPUT / (
            f"{run_date}_{slug}_LandingPage.md"
        )

        landing_file.write_text(
            landing_content,
            encoding="utf-8"
        )

        # =====================================
        # SOCIAL
        # =====================================

        social_content = generate_social_post(query)

        social_file = SOCIAL_OUTPUT / (
            f"{run_date}_{slug}_Social.md"
        )

        social_file.write_text(
            social_content,
            encoding="utf-8"
        )

        generated += 1

        print(f"Generated content set for: {query}")

    print("\nCONTENT GENERATION COMPLETE\n")
    print(f"Generated sets: {generated}")


if __name__ == "__main__":
    main()