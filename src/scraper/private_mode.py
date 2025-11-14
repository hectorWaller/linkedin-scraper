thonimport requests
from bs4 import BeautifulSoup
from extractors.job_parser import parse_job_card
from extractors.company_parser import parse_company_block

class PrivateScraper:
    BASE_URL = "https://www.linkedin.com/jobs/search"

    def __init__(self, filters: dict, cookies_path: str):
        self.filters = filters
        self.session = requests.Session()
        self.load_cookies(cookies_path)

    def load_cookies(self, path):
        with open(path, "r", encoding="utf-8") as f:
            cookies = f.read().strip().split(";")
            for cookie in cookies:
                if "=" in cookie:
                    name, value = cookie.strip().split("=", 1)
                    self.session.cookies.set(name, value)

    def build_url(self, start=0):
        keyword = self.filters.get("keyword", "")
        location = self.filters.get("location", "")
        return f"{self.BASE_URL}?keywords={keyword}&location={location}&start={start}"

    def scrape(self):
        results = []
        limit = self.filters.get("limit", 25)

        for page in range(0, limit, 25):
            url = self.build_url(start=page)
            resp = self.session.get(url, timeout=15)
            if resp.status_code != 200:
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            cards = soup.select(".base-card")

            for card in cards:
                job = parse_job_card(card)

                company_block = card.select_one(".base-search-card__subtitle")
                if company_block:
                    job["company"] = parse_company_block(company_block)

                # Fake premium insights for runnable demo
                job["premium_insights"] = {"applicants": 12, "trend": "stable"}

                results.append(job)

                if len(results) >= limit:
                    return results

        return results