# *-* coding:utf-8 *-*

from bs4 import BeautifulSoup
import scrapy
from scrapy.loader import ItemLoader
from meizitu.items import MeizituItem


class WxMeiZiTu(scrapy.Spider):
    name = 'wxmeizitu'
    start_urls = ['https://mp.weixin.qq.com/s/GEfQUt0ayIulxnovYIa7eA']
    allowed_domains = ['mp.weixin.qq.com']

    def start_requests(self):
        for u in self.start_urls:
            print(u)
            yield scrapy.Request(u, callback=self.parse, errback=self.errback, dont_filter=True)

    @staticmethod
    def parse_item(response):
        il = ItemLoader(item=MeizituItem(), response=response)
        il.add_css('image_urls', 'div[id="js_content"] img::attr(data-src)')
        return il.load_item()

    def parse(self, response):
        yield self.parse_item(response)  # ok

    def errback(self, failure):
        print(failure)
