from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse, urldefrag
from collections import deque
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

CRAWL_OUTPUT = BASE_PATH / r"06_MARKETING\SEO_Agent\Crawls"
AUDIT_OUTPUT = BASE_PATH / r"06_MARKETING\SEO_Agent\Audits"

CRAWL_OUTPUT.mkdir(parents=True, exist_ok=True)
AUDIT_OUTPUT.mkdir(parents=True, exist_ok=True)

START_URL = "https://www.morfrac.com/"
ALLOWED_DOMAIN = "www.morfrac.com"

MAX_PAGES = 500
REQUEST_DELAY_SECONDS = 0.5
TIMEOUT = 15

SEED_URLS = [
    "https://www.morfrac.com/shop/mloop-dyneema-loop-12675",
    "https://www.morfrac.com/es/shop/mloop-dyneema-loop-12675",
    "https://www.morfrac.com/shop/dogbone60-23-12467",
    "https://www.morfrac.com/es/shop/dogbone60-23-12467",
    "https://www.morfrac.com/es/shop/shackle-17-4ph-12827",
    "https://www.morfrac.com/shop/morfblock-light-4-p-12338",
    "https://www.morfrac.com/shop/morfblock-light-4-hl-12823",
    "https://www.morfrac.com/es/shop/category/mloop-34",
    "https://www.morfrac.com/es/shop/category/morfblock-17",
]

EXCLUDED_PATH_CONTAINS = [
    "/web/login",
    "/shop/cart",
    "/my/",
    "/payment",
    "/checkout",
    "/account",
    "/admin",
    "/web/",
]

HEADERS = {
    "User-Agent": "MORFRAC SEO audit crawler; contact: info@morfrac.com"
}

# =========================================
# HELPERS
# =========================================

def normalize_url(url):
    url, _ = urldefrag(url)

    parsed = urlparse(url)

    if parsed.scheme not in ["http", "https"]:
        return None

    if parsed.netloc == "morfrac.com":
        url = url.replace(
            "https://morfrac.com",
            "https://www.morfrac.com"
        )

        url = url.replace(
            "http://morfrac.com",
            "https://www.morfrac.com"
        )

    parsed = urlparse(url)

    if parsed.netloc != ALLOWED_DOMAIN:
        return None

    clean_url = parsed._replace(query="").geturl()

    if clean_url.endswith("/") and clean_url != START_URL:
        clean_url = clean_url.rstrip("/")

    return clean_url


def should_exclude(url):
    parsed = urlparse(url)

    path = parsed.path.lower()

    for item in EXCLUDED_PATH_CONTAINS:
        if item in path:
            return True

    return False


def fetch(url):
    start = time.time()

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            allow_redirects=True,
        )

        elapsed = round(time.time() - start, 2)

        return {
            "status_code": response.status_code,
            "final_url": response.url,
            "html": response.text,
            "elapsed": elapsed,
            "error": "",
        }

    except Exception as e:
        elapsed = round(time.time() - start, 2)

        return {
            "status_code": None,
            "final_url": url,
            "html": "",
            "elapsed": elapsed,
            "error": str(e),
        }


def get_text_or_empty(tag):
    if not tag:
        return ""

    return tag.get_text(" ", strip=True)


# =========================================
# PAGE CLASSIFICATION
# =========================================

def classify_page(url):
    url_lower = url.lower()

    system_patterns = [
        "/cookie",
        "/privacy",
        "/terms",
        "/returns",
        "/wishlist",
        "/web/",
        "/login",
        "/partner",
        "/disclaimer",
        "/website/social/",
    ]

    for pattern in system_patterns:
        if pattern in url_lower:
            return {
                "page_type": "system",
                "business_priority": "ignore",
                "authority_value": "low",
                "commercial_relevance": "low",
                "likely_noise": "high",
            }

    if "/blog/tag/" in url_lower:
        return {
            "page_type": "archive",
            "business_priority": "low",
            "authority_value": "low",
            "commercial_relevance": "low",
            "likely_noise": "high",
        }

    if "/blog/" in url_lower:
        return {
            "page_type": "technical_blog",
            "business_priority": "medium",
            "authority_value": "high",
            "commercial_relevance": "medium",
            "likely_noise": "low",
        }

    high_value_patterns = [
        "dogbone",
        "padeye",
        "morfwing",
        "powerfurl",
        "morfblock",
        "mloop",
        "friction-ring",
        "soft-shackle",
        "/shop/",
    ]

    for pattern in high_value_patterns:
        if pattern in url_lower:
            return {
                "page_type": "product",
                "business_priority": "high",
                "authority_value": "high",
                "commercial_relevance": "high",
                "likely_noise": "low",
            }

    return {
        "page_type": "general",
        "business_priority": "medium",
        "authority_value": "medium",
        "commercial_relevance": "medium",
        "likely_noise": "low",
    }


def extract_page_data(url, fetch_result):
    html = fetch_result["html"]

    status_code = fetch_result["status_code"]
    final_url = fetch_result["final_url"]
    elapsed = fetch_result["elapsed"]
    error = fetch_result["error"]

    soup = BeautifulSoup(
        html,
        "lxml"
    ) if html else BeautifulSoup("", "lxml")

    title = ""

    if soup.title and soup.title.string:
        title = soup.title.string.strip()

    meta_description = ""

    desc_tag = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if desc_tag and desc_tag.get("content"):
        meta_description = desc_tag.get("content").strip()

    canonical = ""

    canonical_tag = soup.find("link", rel="canonical")

    if canonical_tag and canonical_tag.get("href"):
        canonical = canonical_tag.get("href").strip()

    robots = ""

    robots_tag = soup.find(
        "meta",
        attrs={"name": "robots"}
    )

    if robots_tag and robots_tag.get("content"):
        robots = robots_tag.get("content").strip()

    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")

    h1_texts = [
        get_text_or_empty(h)
        for h in h1_tags
        if get_text_or_empty(h)
    ]

    body_text = ""

    if soup.body:
        body_text = soup.body.get_text(
            " ",
            strip=True
        )

    word_count = len(body_text.split())

    images = soup.find_all("img")

    image_count = len(images)

    images_missing_alt = sum(
        1 for img in images
        if not img.get("alt")
    )

    links = soup.find_all("a", href=True)

    internal_links = []

    for link in links:
        href = link.get("href")

        absolute = urljoin(final_url, href)

        normalized = normalize_url(absolute)

        if normalized:
            internal_links.append(normalized)

    noindex = "noindex" in robots.lower()

    indexable = (
        status_code == 200
        and not noindex
    )

    classification = classify_page(url)

    return {
        "url": url,
        "final_url": final_url,
        "status_code": status_code,
        "load_time_seconds": elapsed,
        "error": error,
        "title": title,
        "title_length": len(title),
        "meta_description": meta_description,
        "meta_description_length": len(meta_description),
        "canonical": canonical,
        "robots": robots,
        "indexable": indexable,
        "page_type": classification["page_type"],
        "business_priority": classification["business_priority"],
        "authority_value": classification["authority_value"],
        "commercial_relevance": classification["commercial_relevance"],
        "likely_noise": classification["likely_noise"],
        "h1_count": len(h1_tags),
        "h1": " | ".join(h1_texts[:3]),
        "word_count": word_count,
        "image_count": image_count,
        "images_missing_alt": images_missing_alt,
        "internal_link_count": len(set(internal_links)),
        "internal_links": sorted(set(internal_links)),
    }


# =========================================
# MAIN
# =========================================

def main():
    run_date = datetime.today().strftime("%Y-%m-%d")

    queue = deque()

    visited = set()

    results = []

    start = normalize_url(START_URL)

    queue.append(start)

    for seed_url in SEED_URLS:
        normalized_seed = normalize_url(seed_url)

        if normalized_seed:
            queue.append(normalized_seed)

    while queue and len(visited) < MAX_PAGES:
        url = queue.popleft()

        if not url:
            continue

        if url in visited:
            continue

        if should_exclude(url):
            continue

        print(f"Crawling {len(visited)+1}: {url}")

        visited.add(url)

        fetch_result = fetch(url)

        page_data = extract_page_data(
            url,
            fetch_result
        )

        results.append(page_data)

        for link in page_data["internal_links"]:
            if (
                link not in visited
                and not should_exclude(link)
            ):
                queue.append(link)

        time.sleep(REQUEST_DELAY_SECONDS)

    df = pd.DataFrame(results)

    crawl_file = CRAWL_OUTPUT / f"{run_date}_site_crawl.csv"

    export_df = df.copy()

    export_df["internal_links"] = export_df[
        "internal_links"
    ].apply(
        lambda links: str(links)
    )

    export_df.to_csv(
        crawl_file,
        index=False
    )

    print("")
    print("================================================")
    print("SEO CRAWL COMPLETE")
    print("================================================")
    print(f"Pages crawled: {len(df)}")
    print(f"Crawl CSV: {crawl_file}")
    print("================================================")


if __name__ == "__main__":
    main()