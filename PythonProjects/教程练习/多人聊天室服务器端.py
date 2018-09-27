import socket#-----导入包
import threading#---导入包
def reic(name,s):#----定义函数,形参name和s
    while True:#-------循环运行
        d = s.recv(1024)
        print(name+":"+d.decode('utf-8'))
    s.close()


serv=socket.socket()
serv.bind(('192.168.6.144',9999))
serv.listen(5)
while True:
    s,a=serv.accept()
    name=s.recv(1024).decode('utf-8')
    threading.Thread(target=reic,args=(name,s,)).start()
serv.close()