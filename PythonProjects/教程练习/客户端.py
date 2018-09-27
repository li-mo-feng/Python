import socket
s=socket.socket()
#s.connect(('127.0.0.1',8888))
s.connect(('127.0.0.1',8888))
while True:
    str=input()
    s.send(str.encode('UTF-8'))
    if str == "exit":
        break
s.close()



