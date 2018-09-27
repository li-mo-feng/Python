from pymongo import MongoClient

conn=MongoClient("127.0.0.1,27017")
if conn:
    print("数据库连接成功")
else:
    print("连接失败")

db=conn.mydb
student=db.student
student.insert({"name":"小刚","age":19})
for i in student.find():
    print(i)
conn.close()