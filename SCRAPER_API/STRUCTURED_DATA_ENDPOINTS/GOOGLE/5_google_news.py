import requests
import json

class GoogleNews:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'war'
        self.country_code = 'us'
        self.urls = []
        self.all_data = []
        
    def operation_1(self):
        payload = { 'api_key': self.api_key, 'query': self.query, 'country_code': self.country_code }
        r = requests.get('https://api.scraperapi.com/structured/google/news', params=payload)
        data = r.json()

        result = data.get("articles", [])
        self.all_data.extend(result)

        pages = data.get("pagination", {}).get("pages", [])
        for page in pages:
            self.urls.append(page.get("url"))
    
    def operation_2(self):
        last_url = self.urls[-1]
        payload = { 'api_key': self.api_key, 'url': last_url, 'autoparse': 'true' }
        r = requests.get('http://api.scraperapi.com', params=payload)
        data = r.json()
        pages = data.get("pagination", {}).get("pages", [])
        new_urls = [page.get("url") for page in pages if page.get("url")]
        self.urls.extend(new_urls)
    
    def operation_3(self):
        pass
        # DM for full code
    
    def operation_4(self, url):
        payload = { 'api_key': self.api_key, 'url': url, 'autoparse': 'true' }
        r = requests.get('http://api.scraperapi.com', params=payload)
        data = r.json()
        
        result = data.get("articles", [])
        self.all_data.extend(result)
    
    def operation_5(self):
        pass
        # DM for full code

    def operation_6(self):
        filename = "google_news.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")
    
    def run(self):
        self.operation_1()
        self.operation_3()
        self.operation_5()
        self.operation_6()

if __name__ == '__main__':
    GoogleNews().run()

        
        
