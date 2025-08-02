<h1 align="center">Scraper_API_Demo</h1>

<p align="center">
  <img src="https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/Copy%20of%20favicon-512x512-1.png" width="200"/>
</p>

**Built with ScraperAPI**, this project showcases efficient and scalable web scraping strategies across multiple platforms, demonstrating the power of API access, proxy rotation, asynchronous processing, and structured data endpoints.

## API_ASYNC_PROXY

`API_ASYNC_PROXY` illustrates three distinct scraping strategies leveraging ScraperAPI’s core capabilities—API access, proxy rotation, and asynchronous processing:

* **API-based scraping** — Uses ScraperAPI’s direct endpoints to fetch and parse product listings with minimal setup, ideal for straightforward scraping needs.
* **Proxy-based scraping** — Routes requests through custom proxy configurations to bypass anti-bot measures on platforms like Amazon, enabling robust and uninterrupted data extraction.
* **Asynchronous batch scraping** — Employs ScraperAPI’s asynchronous batch jobs to collect large volumes of ASINs, followed by concurrent retrieval of detailed product data using multithreading, maximizing throughput and efficiency.

Across all approaches, the project extracts rich product information including titles, prices, ratings, images, and offer details from multiple pages. It supports flexible output formats such as JSON, CSV, and Excel to cater to varied downstream use cases.

## STRUCTURED_DATA_ENDPOINTS

`STRUCTURED_DATA_ENDPOINTS` illustrates advanced usage of ScraperAPI’s **Structured Data Endpoints** across multiple major platforms—Amazon, eBay, Google, Redfin, and Walmart—demonstrating scalable, multithreaded scraping workflows tailored for each domain:

* **Amazon** — Implements multi-page product searches with options to extract full product details or just ASINs. Detailed product and offer data are fetched concurrently for specified ASINs from static lists, user input, or search results. Supports JSON and CSV exports for bulk or single-product data.

* **eBay** — Conducts paginated search queries to collect product URLs, extracts numeric product IDs, and retrieves detailed product information with robust error handling. Multithreading accelerates data fetching, and all results are saved in JSON format for e-commerce analysis.

* **Google** — Executes paginated queries across multiple Google services including Search, Maps, Shopping, Jobs, and News. The workflow systematically expands pagination URLs and extracts structured data from each endpoint. Comprehensive error handling and data consolidation illustrate a scalable approach to gathering diverse search, local business, job, product, and news data.

* **Redfin** — Delivers thorough real estate data extraction by paginating through rental and for-sale listings, concurrently scraping detailed property information and agent profiles. Multithreading optimizes request concurrency, while error handling ensures robustness. Data is consolidated and saved as JSON for real estate insights.

* **Walmart** — Performs paginated search queries to collect product listings, extracts product IDs, and concurrently fetches detailed product data. Error handling and multithreading improve efficiency and resilience. All extracted product data is saved in JSON format for further analysis.

## From APIs to Visual Insights
This project provides a rich demonstration of ScraperAPI’s versatility—from simple API calls and proxy management to structured endpoint utilization and asynchronous, multithreaded data extraction—enabling scalable, efficient, and resilient scraping pipelines. Combined with insightful data visualizations, it showcases a complete journey from raw web data to structured analysis across varied domains.

The scraped datasets are further explored through a series of data visualizations, highlighting category distributions, pricing patterns, review sentiments, and more. Each visualization offers insights into domain-specific data collected from various platforms. Below are the visual analyses grouped by source.

## Amazon Data Visualization

**Sankey Diagram**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/AMAZON/Sankey_Diagram.png)
The Sankey Diagram, created using data from the `STRUCTURED_DATA_ENDPOINTS/AMAZON/lenovo_3.json` file, depicts the hierarchical flow of Lenovo products across three levels: **Category**, **Brand**, and **Series**. Each node represents a unique value from these levels, and the links between them illustrate how many products transition from one level to the next. The width of each link is proportional to the number of products, providing a clear visual representation of how products are distributed from broader categories to specific series.

**Word Cloud**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/AMAZON/Word_Cloud.png)
The Word Cloud, created using data from the `STRUCTURED_DATA_ENDPOINTS/AMAZON/lenovo_3.json` file, visually represents the most frequent terms found in the product **feature bullets** and **full descriptions** of Lenovo products. Words that appear more often are shown in larger font, offering a quick overview of key features and common terms associated with the products.

**Bar Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/AMAZON/Bar_Chart.png)
The Bar Chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/AMAZON/lenovo_3.json` file, visualizes the percentage distribution of customer star ratings (1 to 5 stars) for a Lenovo product. Each bar represents the proportion of reviews at a specific rating level, enabling a clear comparison of user satisfaction.

**Dual-Axis Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/AMAZON/Dual_Axis_Chart.png)
The Dual-Axis Chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/AMAZON/lenovo_3.json` file, displays both the estimated **number of reviews** and their corresponding **percentage** for each star rating. The left y-axis shows the review count as bars, while the right y-axis shows the percentage as a line plot, providing a detailed view of both the volume and proportion of customer feedback.

**Pie Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/AMAZON/Pie_Chart.png)
The Pie Chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/AMAZON/lenovo_3.json` file, shows the relative proportions of each star rating in a circular format. It highlights how customer reviews are distributed across the five rating levels, giving a quick snapshot of overall product sentiment.

## EBAY DATA VISUALIZATION

**Sunburst Chart**
![image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/EBAY/Sunburst_Chart.png)
The Sunburst chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/EBAY/ebay_products.json` file, visualizes the distribution of eBay products organized by **Brand** and **Condition**. The chart displays hierarchical segments where the inner rings represent brands and the outer rings represent product conditions within each brand. The size of each segment corresponds to the number of products, offering an intuitive view of how product availability varies across different brands and their conditions.

**Treemap**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/EBAY/Treemap.png)
The Treemap, created using data from the `STRUCTURED_DATA_ENDPOINTS/EBAY/ebay_products.json` file, visualizes the hierarchical distribution of eBay products by **Brand**, **Condition**, and **Color**. Each rectangle represents a category at one of these levels, with larger areas indicating a higher number of products. This layout provides a clear and compact view of how product characteristics are distributed and related across multiple dimensions.

**Sankey Diagram**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/EBAY/Sankey_Diagram.png)
The Sankey diagram, created using data from the `STRUCTURED_DATA_ENDPOINTS/EBAY/ebay_products.json` file, illustrates the flow of eBay products through three hierarchical levels: **Brand**, **Condition**, and **Location**. Each node represents a unique value from these categories, while the links between nodes show the quantity of products transitioning from one level to the next. The width of each link corresponds to the number of products, providing a clear visualization of how products are distributed across different brands, their conditions, and where they are located.

## GOOGLE DATA VISUALIZATION

**Pie Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/GOOGLE/Pie_Chart.png)
The pie chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/GOOGLE/google_maps_search_3.json` file, illustrates the proportional distribution of different **business types** identified in the dataset. Each slice of the chart represents a unique business category, and its size reflects the relative number of businesses falling under that type. This visualization provides a quick overview of the most common business categories based on Google Maps search results.

**Bar Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/GOOGLE/Bar_Chart.png)
The bar chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/GOOGLE/google_maps_search_3.json` file, displays the **number of businesses** grouped by their respective **types**. Each bar represents a specific business category, and its height corresponds to the total number of entries classified under that type. This visualization offers a clear comparison of how frequently different business types appear in the dataset based on Google Maps search results.

## REDFIN DATA VISUALIZATION

**Scatter Map**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/REDFIN/Scatter_Map.png)
The scatter map, created using data from the `STRUCTURED_DATA_ENDPOINTS/REDFIN/redfin_nyc_sale_data.json` file, visualizes the geographic distribution of **property listings across New York City**, with each point representing a property’s location. The color of each point reflects the **sale price**, while the size indicates the **square footage** of the property. This interactive map provides a spatial overview of pricing patterns and property sizes, helping to identify regional trends in the NYC real estate market.

**Treemap**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/REDFIN/Treemap.png)
The treemap, created using data from the `STRUCTURED_DATA_ENDPOINTS/REDFIN/redfin_nyc_sale_data.json` file, visualizes the distribution of **property prices** across different **property types** and **bedroom counts**. Each rectangle represents a unique combination of property type and number of beds, with the size indicating the total price and the color reflecting price intensity. This chart provides a clear hierarchical view of how property prices vary based on type and bedroom configuration in the NYC housing market.

**Scatter Plot**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/REDFIN/Scatter_Plot.png)
The scatter plot, created using data from the `STRUCTURED_DATA_ENDPOINTS/REDFIN/redfin_nyc_sale_data.json` file, illustrates the relationship between **square footage** and **sale price** of properties in New York City. Each point represents a property, with the **color** indicating its type and the **bubble size** reflecting its **price per square foot**. This visualization helps identify pricing patterns and property types across various size ranges, offering insights into market trends and value distribution.

**Box Plot**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/REDFIN/Box_Plot.png)
This box plot is generated using data from the `STRUCTURED_DATA_ENDPOINTS/REDFIN/redfin_nyc_sale_data.json` file and provides a statistical overview of **price per square foot** across different **property types** in New York City. Each box summarizes the distribution of prices within a category—showing the **median**, **interquartile range (IQR)**, and **potential outliers**. Individual property data points are also displayed to reveal the spread and variability within each group. This visualization enables a quick comparison of pricing trends among various property types.

**Sunburst Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/REDFIN/Sunburst_Chart.png)
The sunburst chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/REDFIN/redfin_nyc_sale_data.json` file, visualizes the hierarchical breakdown of **property prices** in New York City across three levels: **Property Type**, **Number of Bedrooms**, and **Number of Bathrooms**. The inner rings represent broader categories, while the outer rings show more specific details. The size of each segment corresponds to the total property price within that category, and the color intensity reflects price levels. This visualization provides an intuitive way to explore how property prices vary across different configurations.

## WALMART DATA VISUALIZATION

**Treemap**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/WALMART/Treemap.png)
The treemap, created using data from the `STRUCTURED_DATA_ENDPOINTS/WALMART/walmart_products.json` file, visualizes the hierarchical structure of Walmart products by category, brand, and variant name. The size of each rectangle represents the variant’s price, while the color indicates the discount percentage, providing an overview of pricing and discount patterns across different product groups.

**Sunburst Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/WALMART/Sunburst_Chart.png)
The sunburst chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/WALMART/walmart_products.json` file, illustrates the breakdown of Walmart products across category, brand, and variant name levels. Each segment’s size corresponds to the price, and the color shows the discount percentage, enabling an interactive exploration of product distribution and discounts in a layered, circular format.

**Bar Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/WALMART/Bar_Chart.png)
The grouped bar chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/WALMART/walmart_products.json` file, compares the current price against the old price for each product variant. Bars for each variant placed side-by-side illustrate how prices have changed, helping visualize discounts and price reductions across the product range.

**Bubble Chart**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/WALMART/Bubble_Chart.png)
The bubble chart, created using data from the `STRUCTURED_DATA_ENDPOINTS/WALMART/walmart_products.json` file, plots product variants based on their price and discount percentage. The size of each bubble represents the price, and the color corresponds to the brand, offering insights into how discounts vary by brand and product price.

**Word Cloud**
![Image](https://github.com/SHAIMOOM251283/SCRAPER_API_DEMO/blob/main/SCRAPER_API/IMAGES/WALMART/Word_Cloud.png)
The word cloud, created using data from the `STRUCTURED_DATA_ENDPOINTS/WALMART/walmart_products.json` file, displays the most frequent terms found in Walmart product short descriptions and customer reviews. Larger words indicate higher frequency, providing a quick visual insight into common themes and keywords associated with the products.