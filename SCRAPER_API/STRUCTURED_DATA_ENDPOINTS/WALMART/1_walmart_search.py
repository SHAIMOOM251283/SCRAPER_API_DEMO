import requests
import json

class WalmartScraper:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'versace'
        self.pages = 2
        self.product_data = []

    def operation_1(self, page):
        payload = { 'api_key': self.api_key, 'query': self.query, 'page': page }
        r = requests.get('https://api.scraperapi.com/structured/walmart/search', params=payload)
        data = r.json()
        results = data.get("items", [])
        if results:
            self.product_data.extend(results)
            print(f"✅ Page {page} fetched with {len(results)} results")
        else:
            print(f"⚠️ No results found on page {page}")

    def operation_2(self):
        # DM for full code
        
        filename = 'walmart_search_results.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")

if __name__ == '__main__':
    WalmartScraper().operation_2()
