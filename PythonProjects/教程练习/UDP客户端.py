import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(('127.0.0.1',8888))
s.bind(('192.168.6.135',8888))

while True:
    data, addr = s.recvfrom(2048)
    mess=data.decode('utf-8')
    print(mess)
s.close

