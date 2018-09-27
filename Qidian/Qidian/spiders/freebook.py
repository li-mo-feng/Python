# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import requests

class FreebookSpider(scrapy.Spider):
    name = 'freebook'
    # allowed_domains = ['www.qidian.com/free']
    # start_urls = ['http://www.qidian.com/free/']/



    def start_requests(self):
        base_url = 'http://www.qidian.com/free/'
        res=requests.get(base_url)
        selector=Selector(res)
        items=selector.css('#limit-list > div > ul > li')
        try:
            for item in items:
                get_url=item.css('.book-mid-info h4 a::attr(href)').extract()
                print('--------------')
                print(get_url)
                print('--------------')
        except:
            pass


