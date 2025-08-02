import requests
import json

class EbayProduct:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'sneakers'
        self.pages = 2
        self.urls = []
        
    def operation_1(self, page):
        payload = { 'api_key': self.api_key, 'query': self.query, 'page': page }
        r = requests.get('https://api.scraperapi.com/structured/ebay/search', params=payload)
        data = r.json()

        results = data
        
        if results:
            for product in results:
                pass
        # DM for full code

    def operation_2(self):
        # DM for full code
        
        filename = 'ebay_product_urls.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.urls, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved to JSON: {filename}")

if __name__ == '__main__':
    EbayProduct().operation_2()