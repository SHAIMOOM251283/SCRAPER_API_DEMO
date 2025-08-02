import requests
import json

class ASIN:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.asins = []
        self.product_data = []
    
    def operation_1(self):
        while True:
            asin = input("Enter ASIN (or enter blank to quit): ")
            if asin == '':
                break
            self.asins.append(asin)

    def operation_2(self, asin):
        payload = { 'api_key': self.api_key, 'asin': asin }
        r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
        data = r.json()
        self.product_data.append(data)
    
    def operation_3(self):
        pass
        # DM for full code

    def operation_4(self):
        filename = 'asin.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved as JSON: {filename}")

    def run(self):
        self.operation_1()
        self.operation_3()
        self.operation_4()

if __name__ == '__main__':
    ASIN().run()

