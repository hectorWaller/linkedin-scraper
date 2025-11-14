thonimport json
import argparse
from scraper.public_mode import PublicScraper
from scraper.private_mode import PrivateScraper
from outputs.writer_json import JSONWriter
from outputs.writer_csv import CSVWriter

def load_filters(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="LinkedIn Job Scraper")
    parser.add_argument("--mode", choices=["public", "private"], required=True)
    parser.add_argument("--filters", required=True, help="Path to filter JSON file")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--format", choices=["json", "csv"], default="json")
    parser.add_argument("--cookies", default=None, help="Path to LinkedIn cookies (private mode only)")
    args = parser.parse_args()

    filters = load_filters(args.filters)

    if args.mode == "public":
        scraper = PublicScraper(filters)
    else:
        scraper = PrivateScraper(filters, args.cookies)

    results = scraper.scrape()

    if args.format == "json":
        JSONWriter.write(args.output, results)
    else:
        CSVWriter.write(args.output, results)

    print(f"Scraping complete. Saved {len(results)} records to {args.output}")

if __name__ == "__main__":
    main()