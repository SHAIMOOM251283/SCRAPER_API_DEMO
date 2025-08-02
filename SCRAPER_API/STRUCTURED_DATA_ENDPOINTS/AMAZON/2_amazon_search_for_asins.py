import requests
import json

class AmazonSearch:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'lenovo'
        self.tld = 'com'
        self.pages = 2
        self.asins = []
        
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
    
    def extract_and_save(self):
        # DM for full code
        
        filename = 'lenovo_asins.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.asins, json_file, ensure_ascii=False, indent=4)
            print(f"✅ ASINs saved as JSON: {filename}")


    def run(self):
        self.extract_and_save()

if __name__ == '__main__':
    AmazonSearch().run()
