import requests
import json

class AmazonSearch:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'lenovo'
        self.tld = 'com'
        self.pages = 2
        self.product_data = []

    def fetch_product_data(self, page):
        payload = { 'api_key': self.api_key, 'query': self.query, 'tld': self.tld, 'page': page }
        r = requests.get('https://api.scraperapi.com/structured/amazon/search', params=payload)
        data = r.json()
        results = data.get("results", [])
        if results:
            self.product_data.extend(results)
            print(f"✅ Page {page} fetched with {len(results)} results")
        else:
            print(f"⚠️ No results found on page {page}")
    
    def extract_and_save(self):
        # DM for full code 
        
        filename = 'lenovo_1.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved as JSON: {filename}")
    
if __name__ == '__main__':
    AmazonSearch().extract_and_save()    