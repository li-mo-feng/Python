from scrapy.spider import CrawlSpider
from scrapy.linkextractors import LinkExtractor
import scrapy


class books(CrawlSpider):
    name = "books"
    start_urls = ["http://books.toscrape.com/index.html"]

    def parse(self, response):
        le = LinkExtractor(restrict_css=" ul.pager > li.next ")
        links = le.extract_links(response)
        # print(links)
        if len(links) == 0:
            pass
        else:
            url_next = links[0].url
            print("---------------------------------")
            print(url_next)
            print("---------------------------------")
            yield scrapy.Request(url_next, callback=self.parse)
