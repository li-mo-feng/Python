import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))
while True:
    c=input("老司机等你来聊天：")
    s.sendall((c.encode('utf-8')))
    data=s.recv(4096)
    data=data.decode('utf-8')
    print("老司机发话了:",data)
    if c.lower()=="肾不够用了":
        break
s.close()




