# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YismeiItem(scrapy.Item):
    date=scrapy.Field()
    title=scrapy.Field()
    summary=scrapy.Field()
    # main=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
