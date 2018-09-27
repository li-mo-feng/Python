# 教师端注册与登陆
# 先定义老师这个类的各种属性
# 然后定义登陆系统
# 首先连接数据库
# 之后对于输入值的判断,因为只要密码对应账号在库内找不到就可以直接返回"密码或者账号错误"
# 如果找得到那么提示登陆成功
import pymysql
from Teacher_infor import Teacher
from connsql import conn_infor

#TF是我将教师这个类独立成包
# class Teacher():#先定义一个类,叫做老师
#
#      def __init__(self,teacher_name,teacher_password):#然后初始化对象
#          self.name=teacher_name#这个对象有名字这个属性
#          self.password=teacher_password#这个名字有密码这个属性
#
#  #因为这三个值为用户输入,所以需要传递给对象,也就是teacher
#      def teacher_nameSet(self,teacher_name):
#          self.name=teacher_name
#      def teacher_nameGet(self):
#          return self.name
#      def teacher_passwordSet(self,teacher_password):
#          self.password=teacher_password
#      def teacher_passwordGet(self):
#          return self.password
def Login(Teacher):#在teacher类中定义一个方法login
    teacher_name=Teacher.teacher_nameGet()
    teacher_password=Teacher.teacher_passwordGet()
    conn = conn_infor
    # conn = pymysql.connect("localhost", 'root', 'root', 'teacher_infor', charset="utf8")
    # if conn:
    #     print("连接数据库体位OK")
    # else:
    #     print("连接的姿势不正确")
    sql1="select teacher_password as password1 from teacher_count  where teacher_name=%s"
    cur = conn.cursor()
    count = cur.execute(sql1, (teacher_name))
    # 统计同名下的密码的统计数

    if count==0:
        print( "您输入的用户名或者密码错误")
    else:
        password1 = cur.fetchone()[0]
        #使用cur类下面的获取值方法得到返回的结果赋值
    if teacher_password!=password1:
        print("您输入的账号或者密码错误")
        # 将获得的值与调用时传入的值进行判定
    else:                     #------------------------------------
        print( "恭喜登陆成功,请选择接下来的操作")
        while True:

            print(" 1:增加学生数据\n","2:修改学生数据\n","3:查找学生数据\n","4:删除学生数据\n","5:退出")

            fun1 = int(input("请输入您要进行的操作:"))
        #下面是增加学生信息的时候
            if fun1 == 1:
                def fun_insert():
                    stu_num = int(input("请输入新增学生的学号"))
                    stu_name = str(input("情输入新增学生的姓名"))
                    stu_password = str(input("请输入新增学生的密码"))
                    conn = Teacher.conn_infor()
                    cur = conn.cursor()
                    sql1 = "insert into student_infor values(%d,'%s','%s')"
                    cur.execute(sql1, (stu_num, stu_name, stu_password))
                    conn.commit()
                fun_insert()
                print("添加成功")


            elif fun1 == 2:


                def fun_update():
                    num = int(input("请输入需要修改的学生的学号:"))
                    print("1:修改姓名\n2:修改密码")
                    print("请选择你的操作")
                    n=int(input(""))
                    if n == 1:
                        #     选择修改学生的姓名
                        name = input("请输入新的姓名:")
                        cur = conn.cursor()
                        sql1 = "update student_infor set stu_name='%s' where stu_num=%d" % (name, num)
                        cur.execute(sql1)
                        conn.commit()
                        while Teacher:
                            print("修改成功,需要修改该同学的密码吗?\n","1:需要","2:不需要")
                            t=int(input())
                            if t==1 :
                                password = input("请输入新的密码")
                                cur = conn.cursor()
                                sql2 = "update student_infor set stu_password='%s' where stu_num=%d"%(password,num)
                                cur.execute(sql2)
                                pass

                        else:
                            password = input("请输入新的密码:")
                            cur = conn.cursor()
                            sql2 = "update student_infor set stu_password='%s' where stu_num=%d"%(password,num)
                            cur.execute(sql2)
                    fun_update()
                    #上面代码是赋予老师修改学生信息的操作的代码


            elif fun1 == 3:

                def fun_find():
                    num = int(input("请输入您要查找的学生信息的id:"))
                    cur = conn.cursor()
                    sql = "select * from student_infor where stu_num=%d" % (num)
                    cur.execute(sql)
                    conn.commit()
                    list=cur.fetchall()
                    print(list)
                fun_find()

            elif fun1 == 4:

                def fun_delete():
                    num = int(input("请输入您要删除的学生信息的id:"))
                    cur = conn.cursor()
                    sql = "delete from student_infor where stu_num= %d" % (num)
                    cur.execute(sql)
                    conn.commit()
                    print("删除成功")
                fun_delete()
            elif fun1 ==5:
                break


def Regiest(Teacher):#定义一个老师的注册方法
    teacher_name=Teacher.teacher_nameGet()
    teacher_password=Teacher.teacher_passwordGet()
    conn = pymysql.connect("localhost", 'root', 'root', 'teacher_infor', charset="utf8")
    cur = conn.cursor()
    if conn:
        print("连接数据库体位OK")
    else:
        print("连接的姿势不正确")
    print()
    sql1 = "select teacher_name from teacher_count where teacher_name=%s"
    a=cur.execute(sql1,(teacher_name))
    print(a)
    if teacher_name==a:
        print("这个昵称已经被别人霸占了,赶紧换一个吧")
    else:
        print("这个昵称居然还能用")
        if len(teacher_password)<=8:
            print("您输入的密码过短")
        else:
            if teacher_password.isnumeric():
                print("而且密码不能是纯数字")
            else:
                sql2="insert into teacher_count values(%s,%s)"
                cur.execute(sql2,(teacher_name,teacher_password))
                conn.commit()
                conn.close()
                return "注册成功"



a=Teacher('lisi','a12345679')
print(Login(a))


























