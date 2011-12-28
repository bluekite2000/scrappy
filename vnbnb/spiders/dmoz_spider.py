from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.item import Item, Field

class HotelItem(Item):
    name = Field()
    address = Field()
    desc = Field()
    image_urls = Field()
    images = Field()

class MininovaSpider(CrawlSpider):

    name = 'dmoz'
    allowed_domains = ['www.agoda.com']
    start_urls = ['http://www.agoda.com/asia/vietnam/ho_chi_minh_city.html']
    rules = [Rule(SgmlLinkExtractor(allow=['http://www.agoda.com/asia/vietnam/ho_chi_minh_city/\w+\.html']), 'parse_hotel')]

    def parse_hotel(self, response):
        x = HtmlXPathSelector(response)

        hotel = HotelItem()
        hotel['name'] = x.select("//span[@id='ctl00_ctl00_MainContent_ContentMain_hotelheader1_lblHotelName']/text()").extract()
        hotel['address'] = x.select("//p[@class='fontsmalli sblueboldunder']/text()").extract()
        hotel['desc'] = x.select("//div[@id='ctl00_ctl00_MainContent_ContentMain_HotelInformation1_pnlDescription']/div[1]/text()").extract()
        hotel['image_urls'] = x.select("//table[@id='ctl00_ctl00_MainContent_ContentMain_HotelPhotos1_dtlPhoto']//tr//td/img/@src").extract()

        return hotel