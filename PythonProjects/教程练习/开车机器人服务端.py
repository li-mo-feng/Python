import socket
import threading


def run():
    print("接收消息ing")
    data, addr = s.accept()
    while True:
        mess = data.recv(4096)
        mess = mess.decode('utf-8')
        if not data:
            break
        print("老司机接收ing", mess)
        data.sendall(words.get(mess, '容老司机我想想哈').encode())
    data.close()
    s.close()
words={
    '你好':'上车吗?我是老司机',
    '你是谁':'我是老司机',
    '这是通往那里的车?':'肯定不是幼儿园的~',
    '我怎么才能上车？':'请输入我们的暗号？',
    '暗号是什么？':'请出门右转"www.baidu.com"',
    '我要上车！':'你要上那儿的车？',
    '我要上幼儿园的车':'www.1024xp.com你懂得',
    '我要上秋名山的车':'www.t66y.com收好不谢!请叫我雷锋'
}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(20)
thread1=mythread()

run()

'''
words={
    '你好':'上车吗?我是老司机',
    '你是谁':'我是老司机',
    '这是通往那里的车?':'肯定不是幼儿园的~',
    '我怎么才能上车？':'请输入我们的暗号？',
    '暗号是什么？':'请出门右转"www.baidu.com"',
    '我要上车！':'你要上那儿的车？',
    '我要上幼儿园的车':'www.1024xp.com你懂得',
    '我要上秋名山的车':'www.t66y.com收好不谢!请叫我雷锋'
}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(20)
print("接收消息ing")
data,addr=s.accept()
while True:
    mess=data.recv(4096)
    mess=mess.decode('utf-8')
    if not data:
        break
    print("老司机接收ing",mess)
    data.sendall(words.get(mess,'容老司机我想想哈').encode())
data.close()
s.close()
'''