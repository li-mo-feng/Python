import socket
import time
sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mess="www.1024xp.com"
i=0
while True:
    i += 1
    data=(mess+str(i)).encode('utf-8')
    sever.sendto(data,('127.0.0.1',8888))
    time.sleep(1)

sever.close()