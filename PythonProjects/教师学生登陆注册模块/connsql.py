def conn_infor():
    import pymysql
    conn = pymysql.connect("localhost", 'root', 'root', 'teacher_infor', charset="utf8")
    if conn:
        print("连接数据库体位OK")
        # return conn
    else:
        print("连接的姿势不正确")