from scrapy.spider import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import BooksItem
import scrapy

class bookspider(CrawlSpider):
    name="books"
    start_urls=["http://books.toscrape.com/index.html"]

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths="//div/div/section/div[2]/ol/li/article/h3/a")
        links = le.extract_links(response)
        for link in links:
            bookurl=link.url
            yield scrapy.Request(bookurl,self.bookinfor)

        le2=LinkExtractor(restrict_css="ul.pager > li.next")
        # 这里获得当前页面的下一页的链接
        links=le2.extract_links(response)
        if len(links)==0:
            pass
        else:
            pageurl=links[0].url
            # 下一页的链接
            yield scrapy.Request(pageurl,self.parse)

    def bookinfor(self,response):
        print("=======================")
        selector=Selector(response)
        # 每一页的所有的图书链接
        bookname = selector.xpath("//*[@id='content_inner']/article/div[1]/div[2]/h1/text()").extract()[0]
        bookprice = selector.xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[1]/text()").extract()[0]
        booklevel = selector.xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[3]/@class").extract()[0]
        bookUPC = selector.css("#content_inner > article > table > tr:nth-of-type(1) > td::text").extract()[0]
        booknum = selector.xpath("//*[@id='content_inner']/article/table/tr[6]/td/text()").extract()[0]
        bookreviews = selector.xpath("//*[@id='content_inner']/article/table/tr[7]/td/text()").extract()[0]
        item=BooksItem(bookname=bookname,bookprice=bookprice,
                       booklevel=booklevel,bookUPC=bookUPC,
                       booknum=booknum,bookreviews=bookreviews)
        yield item
