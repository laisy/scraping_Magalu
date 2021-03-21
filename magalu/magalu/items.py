# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class MagaluItem(Item):
    url = Field()
    name = Field()
    price = Field()
    freight = Field()

class FreightItem(Item):
    url = Field()
    deadline = Field()
    description = Field()
    price = Field()
