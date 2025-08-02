import requests
import json

class ASIN:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.asins = [
            'B0CXKYTQS2',
            'B0CXKTL1SK',
            'B07YNHXX8D',
            'B07D3ZNX42',
            'B09VLJS222'
        ]
        self.product_data = []

    def operation_1(self, asin):
        payload = { 'api_key': self.api_key, 'asin': asin }
        r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
        data = r.json()
        self.product_data.append(data)
    
    def operation_2(self):
        pass
        # DM for full code

    def operation_3(self):
        filename = 'product_data.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved as JSON: {filename}")

    def run(self):
        self.operation_2()
        self.operation_3()

if __name__ == '__main__':
    ASIN().run()

