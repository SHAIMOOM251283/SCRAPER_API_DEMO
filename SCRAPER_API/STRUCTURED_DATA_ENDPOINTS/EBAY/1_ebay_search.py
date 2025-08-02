import requests
import json

class EbayScraper:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'sneakers'
        self.pages = 2
        self.product_data = []

    def operation_1(self, page):
        payload = { 'api_key': self.api_key, 'query': self.query, 'page': page }
        r = requests.get('https://api.scraperapi.com/structured/ebay/search', params=payload)
        data = r.json()
        results = data
        if results: 
            pass
        # DM for full code

    def operation_2(self):
        # DM for full code
        
        filename = 'ebay_search_results.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")

if __name__ == '__main__':
    EbayScraper().operation_2()
