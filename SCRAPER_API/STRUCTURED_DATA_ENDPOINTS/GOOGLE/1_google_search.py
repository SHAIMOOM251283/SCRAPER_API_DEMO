import requests
import json

class GoogleSearch:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = '3d rendering'
        self.country_code = 'us'
        self.urls = []
        self.all_data = []
        
    def operation_1(self):
        payload = {
            'api_key': self.api_key,
            'query': self.query,
            'country_code': self.country_code
        }
        r = requests.get('https://api.scraperapi.com/structured/google/search', params=payload)

        if r.status_code != 200:
            print(f"[operation_1] Request failed with status {r.status_code}")
            print("Response:", r.text)
            return

        try:
            data = r.json()
        except json.JSONDecodeError:
            print("[operation_1] Failed to parse JSON.")
            print("Raw response:", r.text[:200])
            return

        result = data.get("organic_results", [])
        self.all_data.extend(result)

        pages = data.get("pagination", {}).get("pages", [])
        for page in pages:
            if page.get("url"):
                self.urls.append(page.get("url"))
    
    def operation_2(self, url):
        payload = { 'api_key': self.api_key }
        r = requests.get(url, params=payload)

        if r.status_code != 200:
            print(f"[operation_2] Failed to fetch {url} — Status Code: {r.status_code}")
            print("Response Text:", r.text[:200])
            return

        try:
            data = r.json()
        except json.JSONDecodeError:
            print(f"[operation_2] Invalid JSON returned from: {url}")
            print("Raw response:", r.text[:200])
            return

        pages = data.get("pagination", {}).get("pages", [])
        new_urls = [page.get("url") for page in pages if page.get("url")]
        self.urls.extend(new_urls)
    
    def operation_3(self, max_iterations=2):
        pass
        # DM for full code
    
    def operation_4(self, url):
        payload = { 'api_key': self.api_key }
        r = requests.get(url, params=payload)

        if r.status_code != 200:
            print(f"[operation_4] Failed to fetch {url} — Status Code: {r.status_code}")
            print("Response Text:", r.text[:200])
            return

        try:
            data = r.json()
        except json.JSONDecodeError:
            print(f"[operation_4] Invalid JSON from {url}")
            print("Raw response:", r.text[:200])
            return

        result = data.get("organic_results", [])
        self.all_data.extend(result)

    def operation_5(self):
        pass
        # DM for full code

    def operation_6(self):
        filename = "google_search_organic_results.json"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.all_data, f, ensure_ascii=False, indent=4)
            print(f"[operation_6] Data saved to {filename}")
        except Exception as e:
            print(f"[operation_6] Failed to save file: {e}")
    
    def run(self):
        self.operation_1()
        self.operation_3()
        self.operation_5()
        self.operation_6()
        
if __name__ == '__main__':
    GoogleSearch().run()
