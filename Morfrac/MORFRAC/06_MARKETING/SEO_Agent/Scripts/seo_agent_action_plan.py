from pathlib import Path
from datetime import datetime

import pandas as pd

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

LEVERAGE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Leverage_Reports"
TEMPLATE_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Template_Analysis"
FIX_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Fix_Recommendations"
LINK_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Internal_Linking"
METADATA_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Metadata_Targets"

OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent\Action_Plans"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =========================================
# HELPERS
# =========================================

def latest_csv(path, pattern):
    files = list(path.glob(pattern))

    if not files:
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def safe_read_csv(path):
    if not path or not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except:
        return pd.DataFrame()


def markdown_table(df, rows=15):
    if df.empty:
        return "_No data available._"

    return df.head(rows).to_markdown(index=False)


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    leverage_file = latest_csv(
        LEVERAGE_PATH,
        "*_seo_query_page_crawl_leverage_opportunities.csv"
    )

    template_file = latest_csv(
        TEMPLATE_PATH,
        "*_template_cluster_analysis.csv"
    )

    fix_file = latest_csv(
        FIX_PATH,
        "*_seo_fix_recommendations.csv"
    )

    link_file = latest_csv(
        LINK_PATH,
        "*_internal_link_opportunities.csv"
    )

    metadata_file = latest_csv(
        METADATA_PATH,
        "*_seo_metadata_targets.csv"
    )

    leverage_df = safe_read_csv(leverage_file)
    template_df = safe_read_csv(template_file)
    fix_df = safe_read_csv(fix_file)
    link_df = safe_read_csv(link_file)
    metadata_df = safe_read_csv(metadata_file)

    # =========================================
    # EXECUTIVE METRICS
    # =========================================

    high_leverage_pages = len(
        leverage_df[
            leverage_df.get("opportunity_level", "") == "VERY HIGH"
        ]
    ) if not leverage_df.empty else 0

    critical_metadata_targets = len(
        metadata_df[
            metadata_df.get("priority", "") == "CRITICAL"
        ]
    ) if not metadata_df.empty else 0

    high_risk_templates = len(
        template_df[
            template_df.get("structural_risk_score", 0) >= 300
        ]
    ) if not template_df.empty else 0

    total_fixes = len(fix_df) if not fix_df.empty else 0

    internal_link_targets = len(link_df) if not link_df.empty else 0

    # =========================================
    # TOP TABLES
    # =========================================

    top_leverage = pd.DataFrame()

    if not leverage_df.empty:
        top_leverage = leverage_df.sort_values(
            "opportunity_score",
            ascending=False
        )[
            [
                "query",
                "page",
                "opportunity_score",
                "ctr_gap",
                "position",
                "issues",
            ]
        ]

    top_templates = pd.DataFrame()

    if not template_df.empty:
        top_templates = template_df.sort_values(
            "structural_risk_score",
            ascending=False
        )[
            [
                "template_cluster",
                "pages",
                "total_issues",
                "multiple_h1_count",
                "missing_meta_count",
                "missing_alt_count",
                "structural_risk_score",
            ]
        ]

    top_metadata = pd.DataFrame()

    if not metadata_df.empty:
        top_metadata = metadata_df.sort_values(
            "opportunity_score",
            ascending=False
        )[
            [
                "priority",
                "query",
                "page",
                "metadata_need",
                "ctr_gap",
                "opportunity_score",
            ]
        ]

    top_fixes = pd.DataFrame()

    if not fix_df.empty:
        top_fixes = fix_df.copy()

    top_links = pd.DataFrame()

    if not link_df.empty:
        top_links = link_df.copy()

    # =========================================
    # STRATEGIC INTERPRETATION
    # =========================================

    interpretation = []

    if high_risk_templates > 0:
        interpretation.append(
            "- Major SEO leverage exists at template level rather than page-by-page fixes."
        )

    if critical_metadata_targets > 0:
        interpretation.append(
            "- SERP click-capture improvements are likely achievable through metadata rewrites."
        )

    if high_leverage_pages > 0:
        interpretation.append(
            "- Existing rankings indicate MORFRAC already has discoverability potential in multiple non-branded commercial searches."
        )

    if internal_link_targets > 0:
        interpretation.append(
            "- Internal authority distribution can likely be improved through contextual linking between products, landing pages, and engineering content."
        )

    if not interpretation:
        interpretation.append(
            "- No major strategic interpretation available."
        )

    interpretation_text = "\n".join(interpretation)

    # =========================================
    # IMPLEMENTATION PRIORITIES
    # =========================================

    implementation_order = """
1. Fix template-level metadata weaknesses
2. Fix repeated H1 structure problems
3. Improve product/category metadata
4. Improve internal linking to high-leverage pages
5. Strengthen authority landing pages
6. Expand technical engineering authority content
7. Improve CTR capture for near-page-one queries
8. Reduce crawl noise and duplicate paths
"""

    # =========================================
    # REPORT
    # =========================================

    report = f"""# MORFRAC SEO Action Plan

## Generated

{run_date}

---

# Executive Summary

- High leverage query opportunities: {high_leverage_pages}
- Critical metadata targets: {critical_metadata_targets}
- High-risk template clusters: {high_risk_templates}
- SEO fix recommendations: {total_fixes}
- Internal linking opportunities: {internal_link_targets}

---

# Strategic Interpretation

{interpretation_text}

---

# Top Query-Level Opportunities

{markdown_table(top_leverage)}

---

# Highest Risk Template Clusters

{markdown_table(top_templates)}

---

# Metadata Rewrite Priorities

{markdown_table(top_metadata)}

---

# SEO Fix Recommendations

{markdown_table(top_fixes)}

---

# Internal Linking Opportunities

{markdown_table(top_links)}

---

# Recommended Implementation Order

{implementation_order}

---

# Strategic Focus

Prioritize:

- non-branded discoverability
- engineering authority
- product/category visibility
- CTR improvement
- commercial intent alignment
- technical differentiation

Avoid prioritizing:

- vanity traffic
- low-intent content
- archive/tag pages
- low-commercial-value pages

---

# Output Sources

Leverage report:
{leverage_file}

Template analysis:
{template_file}

Fix recommendations:
{fix_file}

Internal linking:
{link_file}

Metadata targets:
{metadata_file}
"""

    output_md = OUTPUT_PATH / f"{run_date}_seo_action_plan.md"

    output_md.write_text(report, encoding="utf-8")

    print("\nSEO ACTION PLAN COMPLETE\n")
    print(output_md)


if __name__ == "__main__":
    main()