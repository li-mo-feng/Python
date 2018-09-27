from pymongo import MongoClient

conn=MongoClient("127.0.0.1,27017")
if conn:
    print("数据库连接成功")
else:
    print("连接失败")

