import requests

class AmazonScraper:

    def __init__(self):
        self.api_key = 'API_KEY'
        self.output_format = 'csv'
        self.asin = 'B0CXL6B4QF'
        self.product_data = ""

    def operation_1(self):
        payload = { 'api_key': self.api_key, 'asin': self.asin, 'output_format': self.output_format }
        r = requests.get('https://api.scraperapi.com/structured/amazon/product', params=payload)
        self.product_data = r.text

    def operation_2(self):
        filename = "B0CXL6B4QF.csv"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.product_data)
        print(f"✅ CSV saved as {filename}")
    
    def run(self):
        self.operation_1()
        self.operation_2()

if __name__ == '__main__':
    AmazonScraper().run()