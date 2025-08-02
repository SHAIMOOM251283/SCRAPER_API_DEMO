import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class WalmartScraper:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'versace'
        self.pages = 2
        self.product_id = []
        self.product_data = []

    def operation_1(self, page):
        payload = { 'api_key': self.api_key, 'query': self.query, 'page': page }
        r = requests.get('https://api.scraperapi.com/structured/walmart/search', params=payload)
        data = r.json()
        results = data.get("items", [])
        if results:
            for product in results:
                product_id = product.get("id")
                if product_id:
                    self.product_id.append(product_id)
            print(f"✅ Page {page} fetched with {len(results)} results")
        else:
            print(f"⚠️ No results found on page {page}")
        
    def operation_2(self):
        pass
        # DM for full code
    
    def operation_3(self, product_id):
        print(f"Extracting Data from {product_id}")
        try:
            payload = { 'api_key': self.api_key, 'product_id': product_id }
            r = requests.get('https://api.scraperapi.com/structured/walmart/product', params=payload)
            data = r.json()
            self.product_data.append(data)
        except Exception as e:
            print(f"❌ Failed to extract {product_id}: {e}")

    def operation_4(self):
        # DM for full code
        
        filename = 'walmart_products.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")

    def run(self):
        self.operation_2()
        self.operation_4()

if __name__ == '__main__':
    WalmartScraper().run()
