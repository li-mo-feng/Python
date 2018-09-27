import pymysql

# sql="select * from character_人物"
# cur.execute(sql)
# for i in cur:
#     print(i)
#------------
# sql1="select * from character_人物 where 人物id=1001"
# cur.execute(sql1)
# for j in cur:
#     print(j)
#sql修改语句
sql3="update student_详情 set 学号=10086 where 姓名='小孙'"
# 执行语句
cur.execute(sql3)
# 查询语句
sql4="select * from student_详情"
# 执行语句
cur.execute(sql4)
# 提交数据库
conn.commit()

for j in cur:
    print('------------')
    print(j)
conn.close()
# 删除
sql5="delete from student_详情 where 姓名='小孙'"
cur.execute(sql5)
sql6="select * from student_详情"
cur.execute(sql6)
conn.commit()
for j in cur:
    print('------------')
    print(j)
conn.close()
# 增加
cur=conn.cursor()
sql7="insert into student_详情(姓名,性别,年龄,出生日期,个人简介,学号)" \
     "values('大黄','男',15,19941215,'我是个帅哥',10087)"
cur.execute(sql7)
conn.commit()
for k in cur:
    print(k)
conn.close()
#
import pymysql
s=pymysql.connect(user="root",password="root",host="localhost",db="student",charset="utf8")
if s:
    print("数据库连接成功")
else:
    print("数据库连接失败")


# ##########创建数据库
# s.cursor()#查询数据----conn是自定义名称...用cursor()获取操作游标
# s.ex
# sql1="create table 玩家装备"
# cur.execute(sql1)
# sql2="select * from 玩家装备"
# cur.execute(sql2)
# s.commit()
# for a in cur:
#     print(a)
# s.close()
