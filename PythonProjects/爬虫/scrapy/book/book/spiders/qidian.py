# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['book.qidian.com/info/1010191960#Catalog']
    start_urls = ['http://book.qidian.com/info/1010191960#Catalog/']

    def list(self, response):
        le=LinkExtractor(restrict_xpaths='//*[@id="j-catalogWrap"]/div/div/ul/li/a')
        links=le.extract_links(response)
        for link in links:
            url=link.url
            print("---------------")
            print(url)
            print("---------------")
            yield scrapy.Request(url,self.parse)

            # // *[ @ id = "chapter-382639401"] / div / div[2] / p[27]

    def parse(self, response):
        selector=Selector(response).xpath('//*[@id="chapter-382639401"]/div/div/p').extract()
        print("=============")
        print(type(selector))
        print(selector)
        print("=============")


