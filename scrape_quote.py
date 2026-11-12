
"""
Practice scraper for https://quotes.toscrape.com/
Extracts quote text, author, tags, and source page URL into quotes.csv.
"""

import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

START_URL = "https://quotes.toscrape.com/"
OUTPUT_FILE = "quotes.csv"
REQUEST_DELAY_SECONDS = 1
TIMEOUT_SECONDS = 15
MAX_RETRIES = 3

HEADERS = {
    "User-Agent": "LearningQuotesScraper/1.0 (educational practice project)"
}


def fetch_page(url, session=None, retries=MAX_RETRIES):
    """Fetch one page with timeout and retry handling."""
    client = session or requests.Session()

    for attempt in range(1, retries + 1):
        try:
            response = client.get(
                url,
                headers=HEADERS,
                timeout=TIMEOUT_SECONDS
            )
            response.raise_for_status()
            return response

        except requests.RequestException as exc:
            print(f"Request attempt {attempt}/{retries} failed: {exc}")

            if attempt < retries:
                time.sleep(2 * attempt)

    return None


def parse_quotes(html, page_url):
    """Extract quote information from one page."""
    soup = BeautifulSoup(html, "html.parser")
    records = []

    for item in soup.select("div.quote"):
        quote_element = item.select_one("span.text")
        author_element = item.select_one("small.author")

        if quote_element is None or author_element is None:
            continue

        tags = [
            tag.get_text(strip=True)
            for tag in item.select("div.tags a.tag")
        ]

        records.append({
            "quote": quote_element.get_text(" ", strip=True),
            "author": author_element.get_text(strip=True),
            "tags": "; ".join(tags),
            "source_url": page_url
        })

    return records


def get_next_page_url(html, current_url):
    """Find the next page link."""
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")

    if next_link is None:
        return None

    return urljoin(current_url, next_link.get("href", ""))


def scrape_all_pages(start_url=START_URL):
    """Scrape all pages using the next-page links."""
    all_records = []
    current_url = start_url
    visited_urls = set()

    with requests.Session() as session:

        while current_url and current_url not in visited_urls:

            visited_urls.add(current_url)

            response = fetch_page(
                current_url,
                session=session
            )

            if response is None:
                print("Could not fetch:", current_url)
                break

            page_records = parse_quotes(
                response.text,
                current_url
            )

            all_records.extend(page_records)

            print(
                f"Fetched {current_url} | "
                f"{len(page_records)} quotes | "
                f"{len(all_records)} total"
            )

            current_url = get_next_page_url(
                response.text,
                current_url
            )

            if current_url:
                time.sleep(REQUEST_DELAY_SECONDS)

    return all_records


def save_to_csv(records, output_file=OUTPUT_FILE):
    """Save records to a CSV file."""
    fieldnames = [
        "quote",
        "author",
        "tags",
        "source_url"
    ]

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(records)


def main():
    records = scrape_all_pages()

    if not records:
        print("No records collected.")
        return

    save_to_csv(records)

    print(
        f"\nSaved {len(records)} records "
        f"to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
