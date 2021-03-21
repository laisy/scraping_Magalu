
import pandas as pd

from scrapy import Spider, Request

from magalu.items import FreightItem


class FreightSmartphonesSpider(Spider):
    name = 'freight_smartphones'

    freight_url = 'https://www.magazineluiza.com.br/produto/calculo-frete/55360000/155590400/magazineluiza.json'

    def start_requests(self):
        #df = pd.read_csv('result.csv')
        url_product = 'https://www.magazineluiza.com.br/smartphone-motorola-moto-g9-play-64gb-verde-turquesa-4gb-ram-65-cam-tripla-selfie-8mp/p/155590400/te/g9py/'
        id_product = url_product.split('/')[5]
        zip_code = '55360000'

        headers = {
            "referer": url_product
        }

        yield Request(self.freight_url.format(zip_code=zip_code, id_product=id_product), headers=headers, callback=self.parse)  

    def parse(self, response):
        print(response.text)