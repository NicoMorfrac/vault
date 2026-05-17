# ============================================================
# MORFRAC SEO ENTITY RELATIONSHIP MAP
# Deterministic knowledge-graph foundation for SEO intelligence
# ============================================================

from pathlib import Path
from datetime import datetime
import re
import ast

import pandas as pd

# ============================================================
# CONFIG
# ============================================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")
SEO_AGENT_PATH = BASE_PATH / r"06_MARKETING\SEO_Agent"

CRAWL_PATH = SEO_AGENT_PATH / "Crawls"
SEMANTIC_PATH = SEO_AGENT_PATH / "Semantic_Clusters"
CONTENT_GAP_PATH = SEO_AGENT_PATH / "Content_Gap_Analysis"
TOPIC_AUTHORITY_PATH = SEO_AGENT_PATH / "Topic_Authority_Map"
CONTEXTUAL_LINK_PATH = SEO_AGENT_PATH / "Contextual_Links"

OUTPUT_PATH = SEO_AGENT_PATH / "Entity_Relationship_Map"

TODAY = datetime.today().strftime("%Y-%m-%d")

# ============================================================
# ENTITY DICTIONARY
# ============================================================

ENTITY_RULES = {
    "product_family": {
        "powerfurl": ["powerfurl", "furler", "furling", "top down", "continuous line"],
        "morfblock": ["morfblock", "morf block", "sailing block", "snatch block"],
        "dogbone": ["dogbone", "dog bone"],
        "mloop": ["mloop", "m loop", "dyneema loop"],
        "morfring": ["morfring", "friction ring"],
        "padeye": ["padeye", "pad eye", "cancamo", "cáncamo"],
        "shackle": ["shackle", "soft shackle", "titanium shackle"],
        "mreel": ["mreel", "rope reeler", "line reeler"],
        "morfwing": ["morfwing", "wing sail", "semi rigid wing"],
        "hoistlock": ["hoistlock", "gaff lock", "halyard lock"],
    },
    "application": {
        "furling_systems": ["furling", "furler", "top down", "continuous line"],
        "sheet_handling": ["sheet", "sheeting", "block", "fairlead"],
        "deck_attachment": ["deck", "padeye", "attachment", "through deck"],
        "soft_connection": ["soft connection", "dyneema", "loop", "lashing"],
        "low_friction_rigging": ["low friction", "friction ring", "ring"],
        "custom_engineering": ["custom", "engineering", "manufacturing", "cnc", "3d printed"],
        "sail_handling": ["sail", "mainsail", "headsail", "gaff", "halyard"],
        "rope_management": ["rope", "line", "reeler", "management"],
    },
    "material": {
        "aluminium": ["aluminium", "aluminum", "7075", "6082", "6061", "hard anodized"],
        "titanium": ["titanium", "grade 5", "gr5", "ti"],
        "stainless_steel": ["stainless", "316", "17-4ph", "17 4ph"],
        "dyneema": ["dyneema", "hmpe"],
        "carbon": ["carbon", "composite"],
        "torlon": ["torlon"],
        "ptfe": ["ptfe"],
    },
    "engineering_concept": {
        "swl": ["swl", "safe working load", "working load"],
        "breaking_load": ["breaking load", "bl", "mbl"],
        "low_friction": ["low friction", "friction"],
        "lightweight": ["lightweight", "light weight"],
        "customizable": ["customizable", "custom"],
        "cnc_machining": ["cnc", "machined", "machining"],
        "high_load": ["high load", "load"],
        "marine_hardware": ["marine hardware", "sailing hardware"],
    },
    "intent": {
        "commercial": ["/shop/", "/category/", "buy", "online", "product"],
        "technical": ["guide", "engineering", "technical", "how", "design"],
        "brand": ["morfrac"],
        "support": ["shipping", "returns", "terms", "privacy"],
    },
}

LOW_VALUE_PATTERNS = [
    "/privacy",
    "/returns",
    "/shipping",
    "/terms",
    "/disclaimer",
    "/wishlist",
    "/cookie",
    "/login",
    "/web/",
    "/my/",
    "/payment",
    "/checkout",
    "/account",
    "/admin",
    "/blog/tag/",
    "/tag/",
    "/page/",
    "/outlet-",
]

# ============================================================
# HELPERS
# ============================================================

def latest_file(folder, pattern):
    files = list(folder.glob(pattern))

    if not files:
        return None

    dated = [
        f for f in files
        if re.match(r"^\d{4}-\d{2}-\d{2}_", f.name)
    ]

    candidates = dated if dated else files

    return max(candidates, key=lambda f: f.stat().st_mtime)


def safe_read_csv(path):
    if path and path.exists():
        return pd.read_csv(path).fillna("")
    return pd.DataFrame()


def to_numeric(df, column):
    if df.empty or column not in df.columns:
        return pd.Series([0] * len(df))

    return pd.to_numeric(df[column], errors="coerce").fillna(0)


def clean_text(value):
    if pd.isna(value):
        return ""

    text = str(value).lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z0-9áéíóúñüø\-/\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalize_url(url):
    if pd.isna(url):
        return ""

    value = str(url).strip().lower()

    for prefix in [
        "https://www.morfrac.com",
        "http://www.morfrac.com",
        "https://morfrac.com",
        "http://morfrac.com",
    ]:
        value = value.replace(prefix, "")

    if value.endswith("/") and value != "/":
        value = value[:-1]

    return value


def is_low_value_url(url):
    value = normalize_url(url)

    return any(pattern in value for pattern in LOW_VALUE_PATTERNS)


def detect_entities(text):
    clean = clean_text(text)

    found = []

    for entity_type, entities in ENTITY_RULES.items():
        for entity_name, keywords in entities.items():
            for keyword in keywords:
                keyword_clean = clean_text(keyword)

                if keyword_clean and keyword_clean in clean:
                    found.append({
                        "entity_type": entity_type,
                        "entity_name": entity_name,
                        "matched_keyword": keyword,
                    })
                    break

    return found


def classify_page_role(url, page_type):
    url_clean = normalize_url(url)
    page_type = clean_text(page_type)

    if "/shop/category/" in url_clean:
        return "category"

    if "/shop/" in url_clean:
        return "product"

    if "/blog/" in url_clean:
        return "authority_content"

    if page_type == "technical_blog":
        return "authority_content"

    if any(x in url_clean for x in [
        "/dogbone",
        "/padeye",
        "/powerfurl",
        "/morfblock",
        "/mloop",
        "/shackle",
        "/morfring",
        "/morfwing",
        "/mreel",
        "/hoistlock",
    ]):
        return "landing"

    return "general"


def parse_internal_links(value):
    if not value:
        return []

    if isinstance(value, list):
        return value

    text = str(value)

    try:
        parsed = ast.literal_eval(text)

        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass

    return []


def relationship_weight(source_role, target_role):
    if source_role == "authority_content" and target_role in ["product", "category", "landing"]:
        return 5

    if source_role == "landing" and target_role in ["category", "product"]:
        return 4

    if source_role == "category" and target_role == "product":
        return 4

    if source_role == "product" and target_role in ["category", "landing"]:
        return 2

    return 1


def relationship_type(source_role, target_role):
    if source_role == "authority_content" and target_role in ["product", "category", "landing"]:
        return "authority_supports_commercial"

    if source_role == "landing" and target_role in ["category", "product"]:
        return "pillar_routes_to_commercial"

    if source_role == "category" and target_role == "product":
        return "category_supports_product"

    if source_role == "product" and target_role == "product":
        return "product_related_to_product"

    if source_role == "product" and target_role in ["category", "landing"]:
        return "product_links_to_parent"

    return "general_internal_link"


def markdown_escape(value):
    return str(value).replace("\n", " ").replace("|", "\\|")


def markdown_table(df, columns=None, limit=25, empty_message="No data available."):
    if df.empty:
        return empty_message

    if columns:
        columns = [col for col in columns if col in df.columns]

        if not columns:
            return empty_message

        df = df[columns]

    df = df.head(limit)

    headers = [markdown_escape(col) for col in df.columns]

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for _, row in df.iterrows():
        values = [markdown_escape(row[col]) for col in df.columns]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    print("Loading SEO entity relationship inputs...")

    crawl_file = latest_file(CRAWL_PATH, "*_site_crawl.csv")
    semantic_pages_file = latest_file(SEMANTIC_PATH, "*_semantic_cluster_pages.csv")
    content_gap_file = latest_file(CONTENT_GAP_PATH, "*_content_gap_analysis.csv")
    topic_authority_file = latest_file(TOPIC_AUTHORITY_PATH, "*_topic_authority_map.csv")
    contextual_links_file = latest_file(
        CONTEXTUAL_LINK_PATH,
        "*_contextual_link_recommendations_filtered.csv"
    )

    crawl_df = safe_read_csv(crawl_file)
    semantic_pages_df = safe_read_csv(semantic_pages_file)
    content_gap_df = safe_read_csv(content_gap_file)
    topic_authority_df = safe_read_csv(topic_authority_file)
    contextual_links_df = safe_read_csv(contextual_links_file)

    if crawl_df.empty:
        raise FileNotFoundError("No crawl CSV found for entity relationship map.")

    required_cols = [
        "url",
        "title",
        "h1",
        "meta_description",
        "page_type",
        "business_priority",
        "commercial_relevance",
        "authority_value",
        "word_count",
        "internal_links",
    ]

    for col in required_cols:
        if col not in crawl_df.columns:
            crawl_df[col] = ""

    print("Preparing page entity map...")

    crawl_df["normalized_url"] = crawl_df["url"].apply(normalize_url)
    crawl_df["page_role"] = crawl_df.apply(
        lambda row: classify_page_role(row["url"], row["page_type"]),
        axis=1
    )
    crawl_df["is_low_value"] = crawl_df["url"].apply(is_low_value_url)

    useful_df = crawl_df[
        ~crawl_df["is_low_value"]
    ].copy()

    useful_df["entity_text"] = useful_df.apply(
        lambda row: " ".join([
            str(row.get("url", "")),
            str(row.get("title", "")),
            str(row.get("h1", "")),
            str(row.get("meta_description", "")),
            str(row.get("page_type", "")),
        ]),
        axis=1
    )

    if not semantic_pages_df.empty:
        semantic_cols = [
            col for col in [
                "url",
                "manual_topic_label",
                "semantic_cluster_id",
                "impressions",
                "clicks",
                "seo_priority_score",
            ]
            if col in semantic_pages_df.columns
        ]

        semantic_tmp = semantic_pages_df[semantic_cols].copy()

        if "url" in semantic_tmp.columns:
            semantic_tmp["normalized_url"] = semantic_tmp["url"].apply(normalize_url)

            useful_df = useful_df.merge(
                semantic_tmp.drop(columns=["url"]),
                on="normalized_url",
                how="left"
            )

    for col in ["impressions", "clicks", "seo_priority_score"]:
        if col not in useful_df.columns:
            useful_df[col] = 0

        useful_df[col] = pd.to_numeric(useful_df[col], errors="coerce").fillna(0)

    page_entities = []

    for _, row in useful_df.iterrows():
        entities = detect_entities(row["entity_text"])

        for entity in entities:
            page_entities.append({
                "url": row["url"],
                "normalized_url": row["normalized_url"],
                "page_role": row["page_role"],
                "page_type": row["page_type"],
                "business_priority": row["business_priority"],
                "commercial_relevance": row["commercial_relevance"],
                "authority_value": row["authority_value"],
                "manual_topic_label": row.get("manual_topic_label", ""),
                "semantic_cluster_id": row.get("semantic_cluster_id", ""),
                "impressions": row.get("impressions", 0),
                "clicks": row.get("clicks", 0),
                "seo_priority_score": row.get("seo_priority_score", 0),
                "entity_type": entity["entity_type"],
                "entity_name": entity["entity_name"],
                "matched_keyword": entity["matched_keyword"],
            })

    page_entity_df = pd.DataFrame(page_entities)

    if page_entity_df.empty:
        raise ValueError("No entities detected. Check ENTITY_RULES or crawl content.")

    print("Building entity summary...")

    entity_summary_df = (
        page_entity_df
        .groupby(["entity_type", "entity_name"], as_index=False)
        .agg(
            page_count=("url", "nunique"),
            product_pages=("page_role", lambda x: int((x == "product").sum())),
            category_pages=("page_role", lambda x: int((x == "category").sum())),
            landing_pages=("page_role", lambda x: int((x == "landing").sum())),
            authority_content_pages=("page_role", lambda x: int((x == "authority_content").sum())),
            total_impressions=("impressions", "sum"),
            total_clicks=("clicks", "sum"),
            avg_seo_priority_score=("seo_priority_score", "mean"),
        )
    )

    entity_summary_df["avg_seo_priority_score"] = (
        pd.to_numeric(entity_summary_df["avg_seo_priority_score"], errors="coerce")
        .fillna(0)
        .round(2)
    )

    entity_summary_df = entity_summary_df.sort_values(
        ["entity_type", "page_count"],
        ascending=[True, False]
    )

    print("Building page-to-page relationship edges...")

    url_role_map = dict(zip(useful_df["normalized_url"], useful_df["page_role"]))
    url_full_map = dict(zip(useful_df["normalized_url"], useful_df["url"]))

    edges = []

    for _, row in useful_df.iterrows():
        source_url = row["url"]
        source_key = row["normalized_url"]
        source_role = row["page_role"]

        links = parse_internal_links(row.get("internal_links", ""))

        for link in links:
            target_key = normalize_url(link)

            if not target_key:
                continue

            if target_key not in url_role_map:
                continue

            if target_key == source_key:
                continue

            target_role = url_role_map[target_key]

            edges.append({
                "source_url": source_url,
                "target_url": url_full_map[target_key],
                "source_role": source_role,
                "target_role": target_role,
                "relationship_type": relationship_type(source_role, target_role),
                "relationship_weight": relationship_weight(source_role, target_role),
                "relationship_source": "crawl_internal_link",
            })

    edge_df = pd.DataFrame(edges)

    if not edge_df.empty:
        edge_df = edge_df.drop_duplicates(
            subset=[
                "source_url",
                "target_url",
                "relationship_type",
                "relationship_source",
            ]
        )

    print("Building entity-to-entity relationships...")

    entity_relationships = []

    if not edge_df.empty:
        source_entities = page_entity_df[[
            "normalized_url",
            "entity_type",
            "entity_name",
        ]].rename(columns={
            "normalized_url": "source_key",
            "entity_type": "source_entity_type",
            "entity_name": "source_entity_name",
        })

        target_entities = page_entity_df[[
            "normalized_url",
            "entity_type",
            "entity_name",
        ]].rename(columns={
            "normalized_url": "target_key",
            "entity_type": "target_entity_type",
            "entity_name": "target_entity_name",
        })

        edge_tmp = edge_df.copy()
        edge_tmp["source_key"] = edge_tmp["source_url"].apply(normalize_url)
        edge_tmp["target_key"] = edge_tmp["target_url"].apply(normalize_url)

        joined = (
            edge_tmp
            .merge(source_entities, on="source_key", how="left")
            .merge(target_entities, on="target_key", how="left")
        )

        joined = joined.dropna(
            subset=[
                "source_entity_type",
                "source_entity_name",
                "target_entity_type",
                "target_entity_name",
            ]
        )

        joined = joined[
            ~(
                (joined["source_entity_type"] == joined["target_entity_type"])
                &
                (joined["source_entity_name"] == joined["target_entity_name"])
            )
        ].copy()

        if not joined.empty:
            entity_relationships_df = (
                joined
                .groupby([
                    "source_entity_type",
                    "source_entity_name",
                    "target_entity_type",
                    "target_entity_name",
                    "relationship_type",
                ], as_index=False)
                .agg(
                    relationship_count=("source_url", "count"),
                    total_relationship_weight=("relationship_weight", "sum"),
                )
                .sort_values(
                    ["total_relationship_weight", "relationship_count"],
                    ascending=False
                )
            )
        else:
            entity_relationships_df = pd.DataFrame()
    else:
        entity_relationships_df = pd.DataFrame()

    print("Building opportunity layer...")

    opportunity_rows = []

    gap_labels = set()

    if not content_gap_df.empty and "dominant_label" in content_gap_df.columns:
        gap_labels = set(
            content_gap_df["dominant_label"].astype(str).str.lower().tolist()
        )

    authority_lookup = {}

    if not topic_authority_df.empty:
        for _, row in topic_authority_df.iterrows():
            label = str(row.get("dominant_label", "")).lower()
            if label:
                authority_lookup[label] = {
                    "topic_authority_score": row.get("topic_authority_score", 0),
                    "authority_tier": row.get("authority_tier", ""),
                    "strategic_status": row.get("strategic_status", ""),
                }

    for _, row in entity_summary_df.iterrows():
        entity_name = str(row["entity_name"]).lower()
        entity_type = row["entity_type"]

        authority_data = authority_lookup.get(entity_name, {})

        product_pages = int(row["product_pages"])
        authority_pages = int(row["authority_content_pages"])
        landing_pages = int(row["landing_pages"])
        impressions = float(row["total_impressions"])

        gap_flag = entity_name in gap_labels

        opportunity_score = 0

        opportunity_score += min(product_pages * 5, 35)
        opportunity_score += min(impressions / 25, 25)

        if authority_pages == 0 and product_pages > 0:
            opportunity_score += 25

        if landing_pages == 0 and product_pages >= 5:
            opportunity_score += 20

        if gap_flag:
            opportunity_score += 20

        opportunity_score = round(min(opportunity_score, 100), 2)

        if product_pages > 0 and authority_pages == 0:
            opportunity_type = "COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT"
        elif product_pages >= 5 and landing_pages == 0:
            opportunity_type = "COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE"
        elif gap_flag:
            opportunity_type = "ENTITY_HAS_CONTENT_GAP"
        elif impressions > 100 and product_pages > 0:
            opportunity_type = "SEARCH_VISIBLE_COMMERCIAL_ENTITY"
        else:
            opportunity_type = "MONITOR"

        opportunity_rows.append({
            "entity_type": entity_type,
            "entity_name": row["entity_name"],
            "page_count": row["page_count"],
            "product_pages": product_pages,
            "landing_pages": landing_pages,
            "authority_content_pages": authority_pages,
            "total_impressions": int(impressions),
            "total_clicks": int(row["total_clicks"]),
            "topic_authority_score": authority_data.get("topic_authority_score", ""),
            "authority_tier": authority_data.get("authority_tier", ""),
            "strategic_status": authority_data.get("strategic_status", ""),
            "has_content_gap": gap_flag,
            "entity_opportunity_score": opportunity_score,
            "entity_opportunity_type": opportunity_type,
        })

    entity_opportunities_df = pd.DataFrame(opportunity_rows).sort_values(
        "entity_opportunity_score",
        ascending=False
    )

    print("Exporting entity relationship map...")

    page_entity_csv = OUTPUT_PATH / f"{TODAY}_page_entity_map.csv"
    entity_summary_csv = OUTPUT_PATH / f"{TODAY}_entity_summary.csv"
    page_edges_csv = OUTPUT_PATH / f"{TODAY}_page_relationship_edges.csv"
    entity_edges_csv = OUTPUT_PATH / f"{TODAY}_entity_relationship_edges.csv"
    opportunities_csv = OUTPUT_PATH / f"{TODAY}_entity_opportunities.csv"
    report_md = OUTPUT_PATH / f"{TODAY}_entity_relationship_report.md"

    stable_page_entity_csv = OUTPUT_PATH / "page_entity_map.csv"
    stable_entity_summary_csv = OUTPUT_PATH / "entity_summary.csv"
    stable_page_edges_csv = OUTPUT_PATH / "page_relationship_edges.csv"
    stable_entity_edges_csv = OUTPUT_PATH / "entity_relationship_edges.csv"
    stable_opportunities_csv = OUTPUT_PATH / "entity_opportunities.csv"

    page_entity_df.to_csv(page_entity_csv, index=False, encoding="utf-8-sig")
    page_entity_df.to_csv(stable_page_entity_csv, index=False, encoding="utf-8-sig")

    entity_summary_df.to_csv(entity_summary_csv, index=False, encoding="utf-8-sig")
    entity_summary_df.to_csv(stable_entity_summary_csv, index=False, encoding="utf-8-sig")

    if not edge_df.empty:
        edge_df.to_csv(page_edges_csv, index=False, encoding="utf-8-sig")
        edge_df.to_csv(stable_page_edges_csv, index=False, encoding="utf-8-sig")
    else:
        pd.DataFrame().to_csv(page_edges_csv, index=False, encoding="utf-8-sig")
        pd.DataFrame().to_csv(stable_page_edges_csv, index=False, encoding="utf-8-sig")

    if not entity_relationships_df.empty:
        entity_relationships_df.to_csv(entity_edges_csv, index=False, encoding="utf-8-sig")
        entity_relationships_df.to_csv(stable_entity_edges_csv, index=False, encoding="utf-8-sig")
    else:
        pd.DataFrame().to_csv(entity_edges_csv, index=False, encoding="utf-8-sig")
        pd.DataFrame().to_csv(stable_entity_edges_csv, index=False, encoding="utf-8-sig")

    entity_opportunities_df.to_csv(opportunities_csv, index=False, encoding="utf-8-sig")
    entity_opportunities_df.to_csv(stable_opportunities_csv, index=False, encoding="utf-8-sig")

    report = f"""# MORFRAC SEO Entity Relationship Map

## Generated

{TODAY}

---

# Purpose

This report creates a deterministic entity relationship layer for MORFRAC SEO intelligence.

It maps:

- product families
- applications
- materials
- engineering concepts
- search/content intent
- page-to-page relationships
- entity-to-entity relationships
- entity-level content and authority opportunities

This is the foundation for future SEO knowledge graph, content brief generation, competitor comparison, and AI-assisted planning.

---

# Source Files

- Crawl file: `{crawl_file}`
- Semantic pages: `{semantic_pages_file if semantic_pages_file else "Not available"}`
- Content gaps: `{content_gap_file if content_gap_file else "Not available"}`
- Topic authority map: `{topic_authority_file if topic_authority_file else "Not available"}`
- Contextual link recommendations loaded for future expansion: `{contextual_links_file if contextual_links_file else "Not available"}`

---

# Summary

- Useful pages analyzed: {len(useful_df)}
- Page-entity mappings: {len(page_entity_df)}
- Unique entities: {len(entity_summary_df)}
- Page relationship edges: {len(edge_df)}
- Entity relationship edges: {len(entity_relationships_df)}
- Entity opportunities: {len(entity_opportunities_df)}

---

# Highest Entity Opportunities

{markdown_table(
    entity_opportunities_df,
    columns=[
        "entity_type",
        "entity_name",
        "entity_opportunity_score",
        "entity_opportunity_type",
        "page_count",
        "product_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "authority_tier",
        "strategic_status",
        "has_content_gap",
    ],
    limit=25,
)}

---

# Entity Summary

{markdown_table(
    entity_summary_df,
    columns=[
        "entity_type",
        "entity_name",
        "page_count",
        "product_pages",
        "category_pages",
        "landing_pages",
        "authority_content_pages",
        "total_impressions",
        "total_clicks",
    ],
    limit=40,
)}

---

# Strongest Entity Relationships

{markdown_table(
    entity_relationships_df,
    columns=[
        "source_entity_type",
        "source_entity_name",
        "target_entity_type",
        "target_entity_name",
        "relationship_type",
        "relationship_count",
        "total_relationship_weight",
    ],
    limit=40,
)}

---

# Interpretation Notes

Entity opportunity types:

- `COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT`: commercial footprint exists but no supporting authority content.
- `COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE`: many commercial/product pages exist but no clear landing/pillar page.
- `ENTITY_HAS_CONTENT_GAP`: entity appears in the content gap layer.
- `SEARCH_VISIBLE_COMMERCIAL_ENTITY`: entity has visibility and commercial footprint.
- `MONITOR`: no immediate structural issue detected.

Recommended actions:

1. Prioritize product entities with high opportunity scores and no authority content.
2. Build technical guides around applications and engineering concepts, not only product families.
3. Use entity relationships to design internal links and content hubs.
4. Use this layer before generating content briefs or competitor gap reports.
5. Extend `ENTITY_RULES` over time as MORFRAC adds products, applications, materials, and engineering concepts.

---

# Output Files

- Page entity map: `{page_entity_csv}`
- Entity summary: `{entity_summary_csv}`
- Page relationship edges: `{page_edges_csv}`
- Stable page relationship edges: `{stable_page_edges_csv}`
- Entity relationship edges: `{entity_edges_csv}`
- Entity opportunities: `{opportunities_csv}`
"""

    report_md.write_text(report, encoding="utf-8")

    print("")
    print("================================================")
    print("SEO ENTITY RELATIONSHIP MAP COMPLETE")
    print("================================================")
    print(f"Useful pages analyzed: {len(useful_df)}")
    print(f"Page-entity mappings: {len(page_entity_df)}")
    print(f"Unique entities: {len(entity_summary_df)}")
    print(f"Page relationship edges: {len(edge_df)}")
    print(f"Entity relationship edges: {len(entity_relationships_df)}")
    print(f"Report: {report_md}")
    print("================================================")


if __name__ == "__main__":
    main()
