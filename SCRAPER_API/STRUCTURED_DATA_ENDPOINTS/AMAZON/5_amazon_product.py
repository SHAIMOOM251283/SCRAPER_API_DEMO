import requests
import json

class AmazonSearch:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'lenovo'
        self.tld = 'com'
        self.pages = 2
        self.asins = []
        self.product_data = []

    def fetch_product_data(self, page):
        payload = {
            'api_key': self.api_key,
            'query': self.query,
            'tld': self.tld,
            'page': page
        }
        r = requests.get('https://api.scraperapi.com/structured/amazon/search', params=payload)
        data = r.json()
        results = data.get("results", [])
        if results:
            for item in results:
                pass
        # DM for full code

    def store_asins(self):
        pass
        # DM for full code
    
    def fetch_data_from_asins(self, asin):
        payload = { 'api_key': self.api_key, 'asin': asin }
        r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
        data = r.json()
        self.product_data.append(data)
    
    def extract_and_save(self):
        # DM for full code
            
        filename = 'lenovo_2.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved as JSON: {filename}")

    def run(self):
        self.store_asins()
        self.extract_and_save()

if __name__ == '__main__':
    AmazonSearch().run()
