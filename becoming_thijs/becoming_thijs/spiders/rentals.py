from scrapy import Spider

class RentalsSpider(Spider):
    name = "rentals"
    allowed_domains = ["funda.nl"]
    start_urls = ["https://www.funda.nl/zoeken/huur?selected_area=%5B%22haarlem%22%5D&price=%22-2000%22&floor_area=%2250-%22&type=%5B%22single%22,%22group%22%5D&object_type=%5B%22house%22,%22apartment%22%5D"]

    metadata = {
        "title": "Funda Apartment Grabber",
        "description": "Grabs apartments for rent from funda.nl",
        "template": True
    }

    def parse(self, response):
        item = {
            "html_response": response.text,
            "url": response.url
        }
        yield item
