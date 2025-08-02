import requests
import json

class GoogleJobs:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.query = 'full stack developer'
        self.country_code = 'us'
        self.all_data = []

    def operation_1(self):
        payload = { 'api_key': self.api_key, 'query': self.query, 'country_code': self.country_code }
        r = requests.get('https://api.scraperapi.com/structured/google/jobs', params=payload)
        
        data = r.json()

        result = data.get("jobs_results", [])
        self.all_data.append(result)
    
    def operation_2(self):
        filename = 'google_jobs.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")
    
    def run(self):
        self.operation_1()
        self.operation_2()

if __name__ == '__main__':
    GoogleJobs().run()