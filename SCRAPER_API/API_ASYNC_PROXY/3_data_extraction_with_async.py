import requests
from bs4 import BeautifulSoup
import time
import json

class ASIN:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.urls = [] 
        self.max_pages = 4
        self.asins = []
        self.product_data = []

    def wait_for_job(self, url, retries=10, delay=3):
        for _ in range(retries):
            res = requests.get(url).json()
            if res.get("response", {}).get("statusCode") == 200:
                return res
            time.sleep(delay)
        return None
        
    def fetch_asin(self):
        for x in range(1, self.max_pages + 1):
            url = f"https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A13896617011%2Cp_123%3A42439&dc&ds=v1%3Aj6g6JgDFcRxlPePvarmYkZr12vDwij2BKg9nZFwA%2FiU&qid=1750333845&rnid=85457740011&ref=sr_nr_p_123_8&page={x}"

            self.urls.append(url)

        scraping_jobs = requests.post(
            url = 'https://async.scraperapi.com/batchjobs',
            json={
                'apiKey': self.api_key, 
                'urls': self.urls,
                'premium': 'true',
                'ultra_premium': 'true',
                'follow_redirect': 'false',
                'retry_404': 'true',
                'render': 'true',
                'keep_headers': 'true'
                })
        
        jobs = scraping_jobs.json()

        status_urls = [job["statusUrl"] for job in jobs]

        print("Waiting for jobs to complete...")
        
        for status_url in status_urls:
            pass
            # DM for full code
                    
                     
    def fetch_product_data(self, asin):
        payload = { 'api_key': self.api_key, 'asin': asin }
        r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
        data = r.json()
        self.product_data.append(data)
    
    def fetch_and_save_all_data(self):
        # DM for full code
        
        filename = 'microsoft_computers.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.product_data, json_file, ensure_ascii=False, indent=4)
            print(f"✅ Data saved as JSON: {filename}")
    
    def run(self):
        self.fetch_asin()
        self.fetch_and_save_all_data()

if __name__ == '__main__':
    ASIN().run()

    

