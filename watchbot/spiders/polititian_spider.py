from scrapy.spider import BaseSpider
from watchbot.items import PoliticianItem
from scrapy.selector import HtmlXPathSelector

BTN = 17
#Aktueller Bundestag ist der BTN-te Bundestag
BASEURL = "http://www.bundestag.de/bundestag/abgeordnete%d/alphabet/index.html" % BTN
 

class PoliticianSpider(BaseSpider):
    name = "Poli"
    allowed_domains = ["bundestag.de"]
    start_urls = [ BASEURL ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//div[@class="linkIntern"]')
        items = []
        for link in links:
            name = link.select('a/text()').extract()
            url = link.select('a/@href').extract()
            name = name.pop().encode('UTF-8',errors='strict')
            url = url.pop().encode('UTF-8',errors='strict')
            item = PoliticianItem()
            item['name']= name.partition(',')[0]+name.partition(',')[2].partition(',')[0]
            item['party'] = name.partition(',')[2].partition(',')[2].strip("\r\n")
            item['biography'] = url
            items.append(item)
            print name
        return items

