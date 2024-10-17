import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(url, base_domain):
    parsed_url = urlparse(url)
    return parsed_url.netloc == base_domain or not parsed_url.netloc

# Web crawler function
def web_crawler(start_url, depth):
    visited_urls = set()

    def crawl(url, current_depth):
        if current_depth > depth or url in visited_urls:
            return
        visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Visited: {url} at depth {current_depth}")

        base_domain = urlparse(start_url).netloc

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)  # Build absolute URL
            if is_valid_url(full_url, base_domain):
                crawl(full_url, current_depth + 1)

    # Start crawling from the start URL at depth 0
    crawl(start_url, 0)

# Starting URL and depth limit
start_url = "https://prathameshks.github.io/"
depth = 3  # Set crawling depth limit
web_crawler(start_url, depth)
