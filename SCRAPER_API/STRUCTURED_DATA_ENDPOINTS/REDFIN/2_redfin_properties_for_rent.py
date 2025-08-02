import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class RedfinListings:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.pages = 2  # total pages to scrape
        self.urls = []
        self.property_data = []

    def get_url_for_page(self, page):
        pass
        # DM for full code

    def fetch_page_listings(self, page):
        url = self.get_url_for_page(page)
        payload = { 'api_key': self.api_key, 'url': url }
        r = requests.get('https://api.scraperapi.com/structured/redfin/search', params=payload)

        if r.status_code == 200:
            data = r.json()
            results = data.get("listing", [])
            if results:
                for property in results:
                    property_url = property.get("url")
                    if property_url:
                        self.urls.append(property_url)
                print(f"✅ Page {page} fetched with {len(results)} results")
            else:
                print(f"⚠️ No results found on page {page}")
        else:
            print(f"❌ Request for page {page} failed with status code {r.status_code}")

    def extract_property_urls(self):
        pass
        # DM for full code

    def extract_property_data(self, property_url):
        print(f"Extracting Data from {property_url}")
        try:
            payload = { 'api_key': self.api_key, 'url': property_url }
            r = requests.get('https://api.scraperapi.com/structured/redfin/forrent', params=payload)
            data = r.json()
            self.property_data.append(data)
        except Exception as e:
            print(f"❌ Failed to extract {property_url}: {e}")

    def scrape_data_from_all_property_urls(self):
        # DM for full code
        
        filename = 'redfin_nyc_rental_data.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.property_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")
    
    def run(self):
        self.extract_property_urls()
        self.scrape_data_from_all_property_urls()

if __name__ == '__main__':
    RedfinListings().run()
