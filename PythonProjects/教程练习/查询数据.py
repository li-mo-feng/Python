from pymongo import MongoClient

conn=MongoClient("127.0.0.1",27017)

db=conn.mydb
student=db.student
data=student.find({"name":"lisi"})
for i in data:
    print(i)
