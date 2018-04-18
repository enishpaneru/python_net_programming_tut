from socket import *
from time import sleep

s=socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",9000))
s.listen(5)

while True:
    c,a=s.accept()
    print("Request received from"+str(a))
    print(c.recv(10000))
    c.send(b'hello boy')
    c.close()
