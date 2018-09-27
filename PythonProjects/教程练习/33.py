import socket
import threading
def run(s):
    while True:
        str == "exit"

    s.send("hhhh".encode('UTF-8'))
    s.close()


s = socket.socket()
# s.connect(('127.0.0.1',8888))
s.connect(('192.168.6.135', 8888))
while True:
    str == "exit"

s.send("hhhh".encode('UTF-8'))
s.close()



