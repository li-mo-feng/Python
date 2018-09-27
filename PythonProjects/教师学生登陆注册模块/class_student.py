from connsql import conn_infor

class student():#定义类class
    def __init__(self,stu_num,stu_name,stu_password):#类的初始化
        self.num=stu_num
        self.name=stu_name
        self.password=stu_password

    def stu_numGet(self,stu_num):
        self.num=stu_num
    def stu_nameGet(self,stu_name):
        self.name=stu_name
    def stu_passwordGet(self,stu_password):
        self.password=stu_password




























    # 修改姓名或者密码的模块
    def update(self,stu_num,stu_name,stu_password):
        print('"需要修改什么内容:"\n,"1:姓名"\n,"2:密码"')
        n=input("")
        conn = conn_infor
        cur = conn.cursor()
        if n==1:
            print("请依次输入修改后的名字,你的编号,和你的密码")
            sql1=("update student_infor set stu_name=%s where stu_num=%d and sut_password=%s")
            cur.excute(sql1,(stu_name,stu_num,stu_password))
            cur.commite()
            print("修改成功")
        elif n==2:
            print("请依次输入修改后的密码,你的编号和,你的姓名")
            sql2=("update student_infor set stu_password=%s where stu_num=%d and stu_name=%s")
            cur.excute(sql2,(stu_password,stu_num,stu_name))


    update()










