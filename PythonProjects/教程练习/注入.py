import pymysql
conn=pymysql.connect(user="root",password="root",host="localhost",db="TEST",charset="utf8")
cur=conn.cursor()
username="zhangsan"
passwrod="123456"
sql="select * from stu_infor where usaername=%s and pass =%d"%(username,'passwrod')
# sql="select * from stu_infor where username=%s and password=%d"
cur.execute(sql)
print(cur.fetchall())