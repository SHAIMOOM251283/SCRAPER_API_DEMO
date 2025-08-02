import requests
from bs4 import BeautifulSoup
import json, csv
import pandas as pd

class AmazonScraper:
    def __init__(self):
        self.api_key = 'API_KEY'
        self.base_url = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A13896617011%2Cp_123%3A42439&dc&ds=v1%3Aj6g6JgDFcRxlPePvarmYkZr12vDwij2BKg9nZFwA%2FiU&qid=1750333845&rnid=85457740011&ref=sr_nr_p_123_8'
        self.product_data = []
        self.max_pages = 4  # set this to desired number of pages

    def fetch_page(self, page_num):
        url = f"{self.base_url}&page={page_num}"
        params = {
            'api_key': self.api_key,
            'url': url,
            'premium': 'true',
            'ultra_premium': 'true',
            'follow_redirect': 'false',
            'retry_404': 'true',
            'render': 'true',
            'keep_headers': 'true'
        }

        try:
            response = requests.get('http://api.scraperapi.com', params=params, timeout=90)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"❌ Failed to fetch page {page_num}: {e}")
            return None

    def extract_product_data(self, soup):
        pass
        # DM for full code

    def save_data(self):
        format_choice = input("Enter output format (json, csv, excel, all): ").strip().lower()

        if format_choice not in {"json", "csv", "excel", "all"}:
            print("❌ Invalid format selected. Please choose from: json, csv, excel, all.")
            return

        if not self.product_data:
            print("⚠️ No data to save.")
            return

        if format_choice in {"json", "all"}:
            with open("amazon_products.json", "w", encoding="utf-8") as f:
                json.dump(self.product_data, f, ensure_ascii=False, indent=4)
            print(f"✅ Saved {len(self.product_data)} products to 'amazon_products.json'")

        if format_choice in {"csv", "all"}:
            keys = self.product_data[0].keys()
            with open("amazon_products.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.product_data)
            print(f"✅ Saved {len(self.product_data)} products to 'amazon_products.csv'")

        if format_choice in {"excel", "all"}:
            try:
                df = pd.DataFrame(self.product_data)
                df.to_excel("amazon_products.xlsx", index=False)
                print(f"✅ Saved {len(self.product_data)} products to 'amazon_products.xlsx'")
            except ImportError:
                print("❌ 'openpyxl' is required for Excel output. Please install it using 'pip install openpyxl'")

    def run(self):
        pass
        # DM for full code

if __name__ == '__main__':
    AmazonScraper().run()
