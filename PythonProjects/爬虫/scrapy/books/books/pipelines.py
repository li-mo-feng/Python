# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
# import redis
class BooksPipeline(object):
#     def open_spider(self,spider):
#         self.item_index=0
#         self.conn=redis.StrictRedis()
#
#     def close_spider(self,spider):
#         self.conn.connection_pool.disconnect()
#
    def process_item(self, item, spider):
#         item=dict(item)
#         self.item_index+=1
#         self.conn.hmset("book:%s" % self.item_index,item)
#         return item


        self.dbpool=adbapi.ConnectionPool('MySQLdb',host='localhost',db='test5',
                                          user='root',password='root',charset='utf8')
        self.dbpool.runInteraction(self.insert_db,item)
        return item

    def insert_db(self,tx,item):
        sql = "insert into books values (%s,%s,%s,%s,%s,%s)"
        values = (item['bookname'],
                  item['bookprice'],
                  item['booklevel'],
                  item['bookUPC'],
                  item['booknum'],
                  item['bookreviews'])
        tx.execute(sql, values)


    # Mongodb的语法

    # import pymysql
    # from pymongo import MongoClient
    # class Books6MangodbPipeline(object):
    #     def process_item(self, item, spider):
    #         conn = MongoClient("localhost", 27017)
    #         con = conn.books.books_info
    #         con.insert(dict(item))
    #         conn.close()
    #         return item
