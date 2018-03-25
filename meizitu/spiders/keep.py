# *-* coding:utf-8 *-*

import scrapy
from scrapy.loader import ItemLoader
from meizitu.items import MeizituItem
import json


class Keep(scrapy.Spider):
    count = 1
    name = 'keep'
    start_urls = ['https://api.gotokeep.com/social/v3/timeline/hot']

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse, errback=self.errback, dont_filter=True)

    @staticmethod
    def parse_item(response):
        il = ItemLoader(item=MeizituItem(), response=response)
        entries = filter(lambda x: x['author']['gender'] is not 'M', json.loads(response.body)['data']['entries'])
        images = []
        for entry in entries:
            try:
                images += entry["images"]
                images.append(entry['photo'])
            except KeyError as e:
                print(json.dumps(entry, indent=2))
        else:
            print(json.loads(response.body)['now'], len(images))
        il.add_value('image_urls', images)
        return il.load_item()

    def parse(self, response):
        yield self.parse_item(response)  # ok
        last_id = json.loads(response.body)['data']['lastId']
        next_page = 'https://api.gotokeep.com/social/v3/timeline/hot?lastId=' + last_id
        print(self.count, next_page)
        self.count += 1
        yield scrapy.Request(next_page, callback=self.parse)

    def errback(self, failure):
        print(failure)
