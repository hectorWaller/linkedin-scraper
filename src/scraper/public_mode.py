thonimport requests
from bs4 import BeautifulSoup
from extractors.job_parser import parse_job_card
from extractors.company_parser import parse_company_block

class PublicScraper:
    BASE_URL = "https://www.linkedin.com/jobs/search"

    def __init__(self, filters: dict):
        self.filters = filters

    def build_url(self, start=0):
        keyword = self.filters.get("keyword", "")
        location = self.filters.get("location", "")
        return f"{self.BASE_URL}?keywords={keyword}&location={location}&start={start}"

    def scrape(self):
        results = []
        limit = self.filters.get("limit", 25)

        for page in range(0, limit, 25):
            url = self.build_url(start=page)
            resp = requests.get(url, timeout=15)
            if resp.status_code != 200:
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            cards = soup.select(".base-card")

            for card in cards:
                job = parse_job_card(card)
                company_block = card.select_one(".base-search-card__subtitle")
                if company_block:
                    job["company"] = parse_company_block(company_block)
                results.append(job)

                if len(results) >= limit:
                    return results

        return results