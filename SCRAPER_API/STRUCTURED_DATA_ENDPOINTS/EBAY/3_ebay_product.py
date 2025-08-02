import requests
import json

class EbayProduct:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'sneakers'
        self.pages = 2
        self.urls = []
        self.product_id = []
        
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
        pass
        # DM for full code
        
    def operation_3(self):
        for url in self.urls:
            pass
        # DM for full code

        filename = 'ebay_product_id.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_id, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")

    def run(self):
        self.operation_2()
        self.operation_3()
        
if __name__ == '__main__':
    EbayProduct().run()
    

