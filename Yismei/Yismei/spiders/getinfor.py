# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from ..items import YismeiItem

class GetinforSpider(scrapy.Spider):
    name = 'getinfor'
    # allowed_domains = ['www.yishimei123.com/']
    # start_urls = ['http://www.yishimei123.com//']
    def start_requests(self):
        base_url='http://www.yishimei123.com/catalog.asp'
        for i in range(1,3):
            page='?page=%s'%(i)
            url=base_url+page
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        selector=Selector(response)
        items=selector.xpath('//*[@id="divMain"]/div')
        item=YismeiItem()
        for infor in items:
            item['date']=infor.css('.post-date::text').extract()
            item['title']=infor.css('.post-title a::text').extract()
            item['summary']=infor.css('.post-body p::text').extract()
            yield item