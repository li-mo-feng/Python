import pymysql
db=pymysql.Connect("localhost","root","root","test")
# 默认顺序：IP，用户名，密码，数据库名称
cursor=db.cursor()
if cursor:
    print("连接成功")
else:
    print("连接失败")
