import scrapy

from scrapy import Request

from magalu.items import MagaluItem

class SmartphonesSpider(scrapy.Spider):
    name = 'smartphones'
    allowed_domains = ['magazineluiza.com.br']

    url = 'https://www.magazineluiza.com.br/smartphone/celulares-e-smartphones/s/te/tcsp/?page={page}'

    def start_requests(self):
        yield Request(self.url.format(page=1), callback=self.parse)

    def parse(self, response):
        products = response.xpath("//ul[@role='main']/a")

        for product in products:
            item = MagaluItem()
            item["url"] = product.xpath("./@href").get()

            div = product.xpath("./div")[2]
            item["name"] = div.xpath("./h3/text()").get()

            price_selector = div.xpath("./div")[1].xpath("./div")[1]
            item["price"] = price_selector.xpath("./text()").get()

            if not item["price"]:
                item["price"] = price_selector.xpath("./span")[0].xpath("./text()").get()

            item["price"] = float(item["price"].split()[1].replace(",", ""))

            yield item