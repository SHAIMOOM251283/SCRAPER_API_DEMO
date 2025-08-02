import requests
import json

class RedfinListings:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.pages = 2  # total pages to scrape
        self.property_data = []

    def get_url_for_page(self, page):
        pass
        # DM for full code

    def fetch_page_listings(self, page):
        url = self.get_url_for_page(page)
        payload = {
            'api_key': self.api_key,
            'url': url
        }
        r = requests.get('https://api.scraperapi.com/structured/redfin/search', params=payload)

        if r.status_code == 200:
            data = r.json()
            results = data.get("listing", [])
            if results:
                self.property_data.extend(results)
                print(f"✅ Page {page} fetched with {len(results)} results")
            else:
                print(f"⚠️ No results found on page {page}")
        else:
            print(f"❌ Request for page {page} failed with status code {r.status_code}")

    def scrape_all_pages(self):
        # DM for full code

        filename = 'redfin_nyc_sale.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.property_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved to JSON: {filename}")

if __name__ == '__main__':
    RedfinListings().scrape_all_pages()
