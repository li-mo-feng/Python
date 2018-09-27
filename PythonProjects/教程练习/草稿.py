from con_sql import sqlinfor
conn = sqlinfor()
cur = conn.cursor()
# num=input('qingshuru num')
# name=input('qingshuru name')
# password=input('qingshuru password')
# type=input('qingshuru type')
class Person():#定义一个类叫做人,里面有编号,姓名,密码,类型
    def __init__(self,num,name,password,type):
        self.num=num
        self.name=name
        self.paaword=password
        self.type=type

    def innum(self):
        innum=input("请输入您的编号")
        num=innum
        return num
    def inname(self):
        inname=input("请输入您的姓名")
        name=inname
        return name
    def inpassword(self):
        inpassword=input("请输入您的密码")
        password=inpassword
        return password

    def login(self,namein,passwordin):

        # while True:
        num=input("请选择您的身份1:教师 2:学生")
        if num==1:
            print(num)
            sql="select per_password from person_infor where per_name=%s and type=tea"
            conn.commit()
            cur.execute(sql,(namein))
            result=cur.fetchone()[0]#在这里需要注意,sql语句的结果是个元祖
            print(result)

            if len(result)==0:
                print("用户名错误,请重新输入")
            else:
                if passwordin==result:
                    print("登陆成功")
                    # break
                else:
                    print("账户名或者密码错误")

        elif num==2:
            sql="select per_password from person_infor where per_name=%s and type=tea"
            conn.commit()
            cur.execute(sql,(namein))
            result=cur.fetchone()[0]#在这里需要注意,sql语句的结果是个元祖
            print(result)

            if len(result)==0:
                print("用户名错误,请重新输入")
            else:
                if passwordin==result:
                    print("登陆成功")
                    # break
                else:
                    print("账户名或者密码错误")



c = Person(1, 'zhangsan', 'a123456', 'stu')
c.login(1,'zhangsan')