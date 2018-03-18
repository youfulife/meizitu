# *-* coding:utf-8 *-*

from bs4 import BeautifulSoup
import scrapy
from scrapy.loader import ItemLoader
from meizitu.items import MeizituItem


class MeiZiTu(scrapy.Spider):
    name = 'meizitu'
    start_urls = ['http://www.meizitu.com/a/5582.html']
    allowed_domains = ['meizitu.com']

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.errback, dont_filter=True)

    @staticmethod
    def parse_item(response):
        il = ItemLoader(item=MeizituItem(), response=response)
        il.add_css('image_urls', 'div[id="picture"] img::attr(src)')
        return il.load_item()

    def parse(self, response):
        yield self.parse_item(response)  # ok
        for a in response.css('a::attr(href)').extract():
            if not a:
                continue
            next_page = response.urljoin(a)
            for domain in self.allowed_domains:
                if domain in next_page:
                    break
            else:
                continue
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def errback(self, failure):
        pass
