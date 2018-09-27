# -*- coding: utf-8 -*-


# 在网站爬取小说一定要注意章节顺序，否则顺序颠倒
# 只能用单线程
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor



class XiugaiSpider(CrawlSpider):

    name = 'xiugai'
    start_urls = ['http://www.tetexs.com/html/48849/']

    def parse(self, response):
        path = 'E:/爬虫成果/都市小说/'
        le=LinkExtractor(restrict_xpaths='//*[@id="list"]/dl/dd/a')
        pages=le.extract_links(response)
        count=0
        for page in pages:
            yield scrapy.Request(page.url,self.neirong)

    def neirong(self,response):
        path = 'E:/爬虫成果/都市小说/'
        url=Selector(response)
        zhengwens=url.css('#content > p').extract()
        titles=url.css('#bgdiv > div.border_b > div:nth-child(1) > h2 > font').extract()
        for p in zhengwens:
            for title in titles:
                ss=p.replace('\r\n\r\n\xa0\xa0\xa0\xa0','').replace('<br>','').replace('tsflessvedsgregsteredversoofdeompler.doloddeomplert','')
                print(ss)
                file=open(path+'都市沉浮录'+'.txt','a+',encoding='utf-8')
                file.write(title)
                file.write('\n')
                file.write(ss)
                file.close()

