# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WatchbotItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class PoliticianItem(Item):
    name=Field()
    party = Field()
   # position = Field()
    biography = Field()
