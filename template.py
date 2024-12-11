# pip3 install scrapy;
# scrapy startproject name_of_your_project;
# scrapy crawl template;


import scrapy
import csv

class Template(scrapy.Spider):
    name = "template"   # You can change your crawler's name
    start_urls = [
        "#",   # Link to the first category page, for example: "https://example.com/your/category/" or "https://example.com/your/category/page=1"
        "#"    # Link to the next page if the first one doesn't have a page index, for example: "https://example.com/your/category/page=2"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = open("template.csv", "w", newline="", encoding="utf-8")   # here you can change the name of csv-file
        self.writer = csv.writer(self.file)
        self.writer.writerow(["Field1", "Field2", "Field3"])   # quantity and name of columns in csv-file.

    def closed(self, reason):
        if self.file:
            self.file.close()

    def parse(self, response):
        product_links = response.xpath(
            "#"   # relative path to product page, for example: "//a[@class='productLink_KM4PI']/@href"
        ).getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)

        next_page_url = self.get_next_page_url(response.url)
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_product(self, response):
        try:
            field1 = response.xpath(
                "#"   #relative path to field1, for example: "//h1[@class='jcdpl']/text()"
            ).get(default="-").strip()

            field2 = response.xpath(
                "#"   #relative path to field2, for example: "//span[@class='ky6t2']/text()"
            ).get(default="-").strip()

            field3 = response.xpath(
                "#"   #relative path to field3, for example: "//div[@class='I21qs']/text()"
            ).get(default="-").strip()

            # you can also add more

            self.writer.writerow([field1, field2, field3])
        except Exception as e:
            self.logger.error(f"Error parsing product: {e}")

    def get_next_page_url(self, current_url):
        # https://example.com/your/category/page=1
        # for example: "page="
        parts = current_url.split("page=")   # write what´s in front of page index
        if len(parts) == 2:
            page_number = int(parts[1])
            next_page_number = page_number + 1   # write down how much the index should increase
            next_page_url = f"{parts[0]}page={next_page_number}"   # write what´s in front of page index
            return next_page_url
        else:
            return None