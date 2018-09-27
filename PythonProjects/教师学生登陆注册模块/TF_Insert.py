def fun_insert():
    num = int(input("请输入新增学生的学号"))
    name = str(input("情输入新增学生的姓名"))
    password = str(input("请输入新增学生的密码"))
    cur = conn.cursor()
    sql1="insert into student_infor values(%d,'%s','%s')"%(num,name,password)
    cur.execute(sql1)
    conn.commit()
    return cur.execute(sql1)




# 当选择修改的内容的时候,输入学生的学号,然后选择修改名字,性别,密码

def fun_update():
    num = int(input("请输入需要修改的学生的学号:"))
    print("1:修改姓名\n2:修改密码")
    print("请选择你的操作")
    n = int(input(""))
    if n == 1:
        #     选择修改学生的姓名
        name = input("请输入新的姓名:")
        cur = conn.cursor()
        sql1 = "update student_infor set stu_name='%s' where stu_num=%d" % (name, num)
        cur.execute(sql1)
        conn.commit()
        print("修改成功,需要修改该同学的密码吗?\n", "1:需要", "2:不需要")
        t = int(input())

        if t == 1:
            password = input("请输入新的密码")
            cur = conn.cursor()
            sql1 = "update student_infor set stu_password='%s' where stu_num=%d" % (password, num)
            cur.execute(sql1)
            pass

    else:
        password = input("请输入新的密码:")
        cur = conn.cursor()
        sql2 = "update student_infor set stu_password='%s' where stu_num=%d" % (password, num)
        cur.execute(sql2)


fun_update()
# 上面代码是赋




def fun_delect():
    num=input("请输入您要删除的学生信息的id:")
    cur =conn.cursor()
    sql="delect from stu_infor where stu_num=%d"%(num)
    cur.execute(sql)
    conn.commit()
    conn.close()































































