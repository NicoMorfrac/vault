import subprocess
import re
from pathlib import Path
from datetime import datetime

# =========================================
# CONFIG
# =========================================

MODEL = "qwen2.5:7b"

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

GA4_REPORTS = BASE_PATH / r"06_MARKETING\Analytics\Weekly_Reports"
SEO_REPORTS = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"
MARKETING_REVIEWS = BASE_PATH / r"06_MARKETING\Reviews"

TREND_FILE = BASE_PATH / r"06_MARKETING\Trend_Data\marketing_trends.csv"

PROMPT_FILE = BASE_PATH / r"02_AGENTS\Marketing\prompts\executive_summary_prompt.md"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\LLM_Reviews"

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


def extract_signal(text, label):

    pattern = rf"{re.escape(label)}:\s*(-?\d+\.?\d*)"

    match = re.search(pattern, text)

    if match:
        return float(match.group(1))

    return None


def clean_llm_output(text):

    # Remove ANSI terminal escape sequences
    text = re.sub(
        r'\x1B\[[0-?]*[ -/]*[@-~]',
        '',
        text
    )

    # Remove carriage returns
    text = text.replace('\r', '')

    # Fix Ollama/Qwen streamed word-wrap duplication:
    # Example:
    # Opportunit
    # Opportunities  -> Opportunities
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:

        stripped = line.strip()

        if cleaned_lines:

            previous = cleaned_lines[-1].strip()

            if previous and stripped:

                previous_clean = re.sub(r'[^A-Za-z]', '', previous).lower()
                current_clean = re.sub(r'[^A-Za-z]', '', stripped).lower()

                # If previous line is a broken prefix of the current line, drop previous
                if (
                    len(previous_clean) >= 3
                    and current_clean.startswith(previous_clean)
                    and previous_clean != current_clean
                ):
                    cleaned_lines[-1] = line
                    continue

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Remove excessive blank lines
    text = re.sub(
        r'\n{3,}',
        '\n\n',
        text
    )

    return text.strip()


def run_ollama(prompt):

    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )

    if result.stderr.strip():
        print("OLLAMA STDERR:")
        print(result.stderr)

    return clean_llm_output(result.stdout)


# =========================================
# MAIN
# =========================================

def main():

    run_date = datetime.today().strftime("%Y-%m-%d")

    ga4_file = latest_file(GA4_REPORTS)
    seo_file = latest_file(SEO_REPORTS)
    review_file = latest_file(MARKETING_REVIEWS)

    if not ga4_file:
        print("Missing GA4 report.")
        return

    if not seo_file:
        print("Missing SEO report.")
        return

    if not review_file:
        print("Missing marketing review.")
        return

    if not PROMPT_FILE.exists():
        print("Missing prompt file.")
        return

    ga4_text = read_text(ga4_file)
    seo_text = read_text(seo_file)
    review_text = read_text(review_file)
    prompt_text = read_text(PROMPT_FILE)

    trend_text = ""

    if TREND_FILE.exists():
        trend_text = read_text(TREND_FILE)

    sessions_7_change = extract_signal(
        ga4_text,
        "7-day sessions change"
    )

    sessions_28_change = extract_signal(
        ga4_text,
        "28-day sessions change"
    )

    click_change = extract_signal(
        seo_text,
        "Click change"
    )

    impression_change = extract_signal(
        seo_text,
        "Impression change"
    )

    ctr_change = extract_signal(
        seo_text,
        "CTR change"
    )

    position_change = extract_signal(
        seo_text,
        "Position change"
    )

    seo_lower = seo_text.lower()

    detected_topics = []

    keywords = [
        "dogbone",
        "dogbones",
        "soft pad eye",
        "mreel",
        "farr x2",
        "pad eye",
        "rigging",
        "furling",
        "code zero",
        "friction ring"
    ]

    for keyword in keywords:
        if keyword in seo_lower:
            detected_topics.append(keyword)

    detected_topics = sorted(list(set(detected_topics)))

    structured_context = f"""
MARKETING SIGNALS

7-day sessions change: {sessions_7_change}
28-day sessions change: {sessions_28_change}

SEO SIGNALS

Organic click change: {click_change}
Organic impression change: {impression_change}
Organic CTR change: {ctr_change}
Position change: {position_change}

DETECTED SEO TOPICS

{chr(10).join("- " + topic for topic in detected_topics)}

TREND MEMORY

{trend_text[-3000:] if trend_text else "No trend history available."}

LATEST RULE-BASED MARKETING REVIEW

{review_text[-5000:]}
"""

    full_prompt = f"""
{prompt_text}

---

# STRUCTURED INPUT DATA

{structured_context}

---

# TASK

Generate:
- executive summary
- key risks
- key opportunities
- strategic priorities
- recommended actions

Requirements:

- Use only provided metrics.
- Do not invent data.
- Focus on marine/performance sailing context.
- Prioritize commercially relevant opportunities.
- Avoid generic marketing consultant language.
- Keep recommendations specific and actionable.
"""

    print("\nRUNNING LOCAL LLM MARKETING REVIEW...\n")

    llm_output = run_ollama(full_prompt)

    output_file = OUTPUT_PATH / f"{run_date}_LLM_Marketing_Review.md"

    output_content = f"""# LLM Marketing Review

## Generated

{run_date}

## Model

{MODEL}

## Source Files

GA4 Report:

{ga4_file}

SEO Report:

{seo_file}

Marketing Review:

{review_file}

Trend Memory:

{TREND_FILE}

Prompt File:

{PROMPT_FILE}

---

# Structured Input Summary

| Signal | Value |
|---|---:|
| 7-day sessions change | {sessions_7_change} |
| 28-day sessions change | {sessions_28_change} |
| Organic click change | {click_change} |
| Organic impression change | {impression_change} |
| Organic CTR change | {ctr_change} |
| Position change | {position_change} |

## Detected Topics

"""

    if detected_topics:
        for topic in detected_topics:
            output_content += f"- {topic}\n"
    else:
        output_content += "- None detected\n"

    output_content += f"""

---

# LLM Analysis

{llm_output}

---

## Traceability

- Generated by: marketing_llm_review.py
- Model used: {MODEL}
- Prompt used: {PROMPT_FILE}
"""

    output_file.write_text(output_content, encoding="utf-8")

    print("\nLLM MARKETING REVIEW CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()