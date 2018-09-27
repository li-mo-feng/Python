from Person import *
from con_sql import *

class teacher(Person):#型一个一个老师这个类,继承自人
    def __init__(self, num, name, password,type='tea'):
        Person.__init__(self, num, name, password,type)
    def num(self):
        innum=input("请输入您的编号")
        num=innum
        return num
    def name(self):
        inname=input("请输入您的姓名")
        name=inname
        return name
    def password(self):
        inpassword=input("请输入您的密码")
        password=inpassword
        return password


num=input("请输入您的操作 1:登陆 2:注册 3:退出")

while num==1:
    Person.login()






# teacher=Person()
# teacher.num()
#     while True:
#          print("1:查询学生信息\n","2:修改自己的姓名","3:修改学生的姓名","4:修改学生的密码","5:删除学生账户","6:增加学生账户")
#          num=input("请选择操作")
#          if num==1:
#              pass
