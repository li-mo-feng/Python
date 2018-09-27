from class_student import student
from connsql import conn_infor
#登陆模块
def login(student):
    name=student.stu_nameGet()
    num=student.stu_numGet()
    password=student.stu_passwordGet()

    conn=conn_infor()
    cur=conn.cursor
    sql1="select stu_name,stu_num from student_infor where stu_name=%s and stupassword=%s"
    na=cur.excute(sql1,(name,password))
    if name==na:
        print("登陆成功")
