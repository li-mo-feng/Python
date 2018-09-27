import pymongo
myconn=pymongo.MongoClient("localhost",27017)
if myconn:
    print("success")
else:
    print("failed")

db = myconn["student"]
# 数据库名称
mycol=db["infor"]
#
mydict={"name":"张三","sex":"男","age":"24"}
x=mycol.insert_one(mydict)
m
c=mycol.find()
for item in c:
    print(item)