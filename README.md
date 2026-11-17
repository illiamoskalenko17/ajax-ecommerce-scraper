# AJAX E-Commerce Web Scraper

A robust, production-ready Python web scraper designed to extract real-time product catalogs (names, prices, and direct URLs) from dynamic e-commerce platforms. 

## Key Features
- **AJAX & POST Request Handling**: Bypasses static limitations by emulating server-side asynchronous data fetching (`action=load_products`).
- **Automated Pagination**: Iterates dynamically through category pages using a robust loop until all available records are retrieved.
- **Data Filtering**: Intentionally filters out unavailable/out-of-stock items (based on CSS pseudo-classes and `.darkened` state flags).
- **Structured Export**: Seamlessly aggregates parsed data into a clean, structured CSV format using `pandas` with full UTF-8 support.

## Tech Stack
- **Python 3.x**
- **Requests** (HTTP session emulation & POST handling)
- **BeautifulSoup4** (`lxml` parser for efficient HTML traversal)
- **Pandas** (Tabular data manipulation and CSV export)

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/ajax-ecommerce-scraper.git](https://github.com/your-username/ajax-ecommerce-scraper.git)
   cd ajax-ecommerce-scraper