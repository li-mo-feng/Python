# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class MyImagePipline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url=request.url
        file_name=url.split('/')[-1]
        #文件名
        return file_name

class Pic360Pipeline(object):
    def process_item(self, item, spider):
        return item
