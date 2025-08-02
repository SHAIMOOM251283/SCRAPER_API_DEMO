<h1 align="center">Scraper_API_Demo</h1>

<p align="center">
  <img src="https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/Copy%20of%20favicon-512x512-1.png" width="200"/>
</p>

**Built with ScraperAPI**, this project showcases efficient and scalable web scraping strategies across multiple platforms, demonstrating the power of API access, proxy rotation, asynchronous processing, and structured data endpoints.

## API\_ASYNC\_PROXY

`API_ASYNC_PROXY` illustrates three distinct scraping strategies leveraging ScraperAPI’s core capabilities—API access, proxy rotation, and asynchronous processing:

* **API-based scraping** — Uses ScraperAPI’s direct endpoints to fetch and parse product listings with minimal setup, ideal for straightforward scraping needs.
* **Proxy-based scraping** — Routes requests through custom proxy configurations to bypass anti-bot measures on platforms like Amazon, enabling robust and uninterrupted data extraction.
* **Asynchronous batch scraping** — Employs ScraperAPI’s asynchronous batch jobs to collect large volumes of ASINs, followed by concurrent retrieval of detailed product data using multithreading, maximizing throughput and efficiency.

Across all approaches, the project extracts rich product information including titles, prices, ratings, images, and offer details from multiple pages. It supports flexible output formats such as JSON, CSV, and Excel to cater to varied downstream use cases.

## STRUCTURED\_DATA\_ENDPOINTS

`STRUCTURED_DATA_ENDPOINTS` illustrates advanced usage of ScraperAPI’s **Structured Data Endpoints** across multiple major platforms—Amazon, eBay, Google, Redfin, and Walmart—demonstrating scalable, multithreaded scraping workflows tailored for each domain:

* **Amazon** — Implements multi-page product searches with options to extract full product details or just ASINs. Detailed product and offer data are fetched concurrently for specified ASINs from static lists, user input, or search results. Supports JSON and CSV exports for bulk or single-product data.

* **eBay** — Conducts paginated search queries to collect product URLs, extracts numeric product IDs, and retrieves detailed product information with robust error handling. Multithreading accelerates data fetching, and all results are saved in JSON format for e-commerce analysis.

* **Google** — Executes paginated queries across multiple Google services including Search, Maps, Shopping, Jobs, and News. The workflow systematically expands pagination URLs and extracts structured data from each endpoint. Comprehensive error handling and data consolidation illustrate a scalable approach to gathering diverse search, local business, job, product, and news data.

* **Redfin** — Delivers thorough real estate data extraction by paginating through rental and for-sale listings, concurrently scraping detailed property information and agent profiles. Multithreading optimizes request concurrency, while error handling ensures robustness. Data is consolidated and saved as JSON for real estate insights.

* **Walmart** — Performs paginated search queries to collect product listings, extracts product IDs, and concurrently fetches detailed product data. Error handling and multithreading improve efficiency and resilience. All extracted product data is saved in JSON format for further analysis.

This projects provide a rich demonstration of ScraperAPI’s versatility—from simple API calls and proxy management to structured endpoint utilization and asynchronous, multithreaded data extraction—enabling **scalable, efficient, and resilient scraping pipelines** across varied domains and data formats.

## Data Visualization

**Amazon Product Data Sankey Diagram**
![Image]()
The Sankey Diagram, created using data from the `AMAZON/lenovo_3.json` file, depicts the hierarchical flow of Lenovo products across three levels: **Category**, **Brand**, and **Series**. Each node represents a unique value from these levels, and the links between them illustrate how many products transition from one level to the next. The width of each link is proportional to the number of products, providing a clear visual representation of how products are distributed from broader categories to specific series.

**Amazon Products Feature & Description Word Cloud**
![Image]()
The Word Cloud, created using data from the `AMAZON/lenovo_3.json` file, visually represents the most frequent terms found in the product **feature bullets** and **full descriptions** of Lenovo products. Words that appear more often are shown in larger font, offering a quick overview of key features and common terms associated with the products.