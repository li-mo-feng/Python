import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
if myclient:
    print("连接成功")
else:
    print("失败")
