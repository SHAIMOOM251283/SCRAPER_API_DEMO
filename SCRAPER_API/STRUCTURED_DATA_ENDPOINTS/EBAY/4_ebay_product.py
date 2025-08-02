import requests
import json

class EbayProduct:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'sneakers'
        self.pages = 2
        self.urls = []
        self.product_id = []
        self.product_data = []
    
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

    def operation_4(self, product_id):
        payload = { 'api_key': self.api_key, 'product_id': product_id }
        r = requests.get('https://api.scraperapi.com/structured/ebay/product', params=payload)
        data = r.json()
        self.product_data.append(data)

    def operation_5(self):
        # DM for full code
        
        filename = 'ebay_products.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"Data saved as JSON: {filename}")
    
    def run(self):
        self.operation_2()
        self.operation_3()
        self.operation_5()

if __name__ == '__main__':
    EbayProduct().run()
    

