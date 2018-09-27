from con_sql import sqlinfor
conn = sqlinfor()
cur = conn.cursor()

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
        if Person.innum(self)==1:
            sql="select per_password from person_infor where per_name=%s"
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
        elif Person.innum(self)==2:
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




    # 因为输入的信息不是活动值,所以错误后必须
    def find(self):#查询学生的信息
        numin=int(input("请输入要查询的学生的编号"))
        sql="select * from person_infor where per_num=%s"
        cur.execute(sql, numin)
        result = cur.fetchall()
        conn.commit()
        print(result)


    def update_name(self):#修改自己或者学生的名字
        numin =input("请输入要修改的学生的编号")
        namein=input("请输入需要修改的学生的姓名")
        sql="update person_infor set per_name=%s where per_num=%s"
        cur.execute(sql,(namein,numin))
        conn.commit()
        sql1="select * from person_infor where per_num=%s"#查询修改后的结果
        cur.execute(sql1,(numin))
        result=cur.fetchone()
        print(result)

    def regiest(self):#注册模块
        while True:
            print("欢迎注册，请选择注册身份或者操作 1；教师 2:学生 3:退出")
            num=input("请选择您的身份")
            if num==1:
                inname=input("请输入您的名字")
                inpassword=input("请输入您的密码")
                sql1="select per_name from person_infor where per_name= %s"
                cur.execute(sql1,(inname))
                result=cur.fetchall()[1]

                for i in result:
                    if inname==i:
                        print("昵称已经被占用,请重新输入")
                    else:
                        print("此昵称可用")
                        if len(inpassword)<=8:
                            print("密码太短了")
                        elif inpassword.isalnum():
                            print("密码不能是纯数字")
                        else:
                            sql="insert into person_infor values(1,'%s','%s','teacher')"
                            cur.execute(sql,(inname,inpassword))
                            print("注册成功")
            #          学生注册模块
            elif num==2:
                inname = input("请输入您的名字")
                inpassword = input("请输入您的密码")
                sql1 = "select per_name from person_infor where per_name= %s"
                cur.execute(sql1, (inname))
                result = cur.fetchall()[1]

                for i in result:
                    if inname == i:
                        print("昵称已经被占用,请重新输入")
                    else:
                        print("此昵称可用")
                        if len(inpassword) <= 8:
                            print("密码太短了")
                        elif inpassword.isalnum():
                            print("密码不能是纯数字")
                        else:
                            sql = "insert into person_infor values(1,'%s','%s','student')"
                            cur.execute(sql, (inname, inpassword))
                            return "注册成功"

            elif num==3:
                # 不想注册了想退出
                break

c = Person(1, 'zhangsan', 'a123456', 'stu')
c.login(1,'zhangsan')
#
# Person.fin
# # c.login('zhangsan','a123456')
# # c.update_name()





