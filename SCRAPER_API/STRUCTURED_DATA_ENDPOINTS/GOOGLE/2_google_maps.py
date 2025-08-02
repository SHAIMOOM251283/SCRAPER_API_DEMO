import requests
import json

class GoogleMapsSearch:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = '3d rendering'
        self.country_code = 'us'
        self.urls = []
        self.all_data = []
        
    def operation_1(self):
        payload = { 'api_key': self.api_key, 'query': self.query, 'country_code': self.country_code }
        r = requests.get('https://api.scraperapi.com/structured/google/mapssearch', params=payload)
        data = r.json()

        result = data.get("results", [])
        self.all_data.extend(result)

        next_page_url = data.get("next_page_url")
        self.urls.append(next_page_url)

    def operation_2(self, url):
        payload = { 'api_key': self.api_key }
        r = requests.get(url, params=payload)
        data = r.json()
        
        result = data.get("results", [])
        self.all_data.extend(result)
    
    def operation_3(self):
        pass
        # DM for full code
    
    def operation_4(self):
        filename = "google_maps_search.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")
    
    def run(self):
        self.operation_1()
        self.operation_3()
        self.operation_4()
        
if __name__ == '__main__':
    GoogleMapsSearch().run()
