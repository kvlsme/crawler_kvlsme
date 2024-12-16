# crawler_kvlsme
Template for crawler based on scrapy-crawler

## Installation

1. Install Scrapy:
    ```bash
    pip3 install scrapy
    ```

2. Start a new Scrapy project:
    ```bash
    scrapy startproject name_of_your_project
    ```

3. Run the crawler:
    ```bash
    scrapy crawl template
    ```

## Usage

1. Modify the `start_urls` in `template.py` to include the URLs of the categories you want to scrape.
2. Adjust the XPath expressions in the `parse` and `parse_product` methods to match the structure of the target website.
3. Run the crawler using the command:
    ```bash
    scrapy crawl template
    ```

## Dependencies

- Python 3.x
- Scrapy

## Special Notes

- Ensure that the XPath expressions in the `template.py` file are updated to match the structure of the website you are scraping.
- The output is saved in a CSV file named `template.csv`. You can change this name in the `__init__` method of the `Template` class.

## Code Structure

- `template.py`: Contains the Scrapy spider code. It defines the crawler's name, start URLs, and parsing logic.
    - `start_urls`: List of URLs to start crawling from.
    - `parse`: Method to parse the category pages and extract product links.
    - `parse_product`: Method to parse individual product pages and extract required fields.
    - `get_next_page_url`: Method to generate the URL for the next page.

## Contributors

- Placeholder for contributors

## License

This project is licensed under the terms of the Mozilla Public License Version 2.0. See the [LICENSE](LICENSE) file for details.
