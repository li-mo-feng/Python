import pymysql
def sqlinfor():
    conn=pymysql.connect("localhost",'root','root','login',charset="utf8")
    if conn:
        print("连接成功")
        return conn
    else:
        print("连接失败")


    cur=conn.cursor()
    cur.execute()





