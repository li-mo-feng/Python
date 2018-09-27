# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class YismeiPipeline(object):
    def process_item(self, item, spider):
        for each in item:
            if each is None:
                break
            else:
                return item

class MongoPipline(object):
    def __init__(self):
        self.connection=pymongo.MongoClient(settings['MON_HOST'],settings['MON_PORT'])
        db=self.connection[settings['MON_DB']]
        self.collection=db[settings['MON_COLL']]

    def process_item(self,item,spider):
        self.collection.insert(dict(item))
        return item