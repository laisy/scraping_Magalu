# import do scrapy para usar as classes que o pacote fornece.
import scrapy

from scrapy import Request

from magalu.items import MagaluItem

# a partir a classe Spider, crio uma subclasse SmartphonesSpider
# possui métodos e comportamentos que definem como seguir URLs e extrair dados das páginas que encontrar para saber onde procurar e quais dados procurar. 
class SmartphonesSpider(scrapy.Spider):
    name = 'smartphones'
    allowed_domains = ['magazineluiza.com.br']
    base_url = 'https://www.magazineluiza.com.br'
    url = 'https://www.magazineluiza.com.br/smartphone/celulares-e-smartphones/s/te/tcsp?page={page}'

    def start_requests(self):
        yield Request(self.url.format(page=1), callback=self.parse)

    def parse(self, response):
        products = response.xpath("//ul[@role='main']/a")

        for product in products:
            item = MagaluItem()
            item["url"] = product.xpath("./@href").get()

            div = product.xpath("./div")[2]
            item["name"] = div.xpath("./h3/text()").get()

            try:
                price_selector = div.xpath("./div")[1].xpath("./div")[1]
                item["price"] = price_selector.xpath("./text()").get()
            
            except IndexError:
                price_selector = div.xpath("./div").xpath("./div")[1]
                item["price"] = price_selector.xpath("./span").xpath("./text()").get()

            if not item["price"]:
                item["price"] = price_selector.xpath("./span").xpath("./text()").get()

            if item["price"] != None:
                item["price"] = float(item["price"].split()[1].replace(",", ""))

            yield item

            next_page = response.xpath("//link[@rel='next']/@href").get()
            if next_page:
                yield Request(self.base_url + next_page, callback=self.parse)