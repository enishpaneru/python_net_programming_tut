from socket import *
from time import sleep

s=socket(AF_INET,SOCK_DGRAM)
s.bind(("127.0.0.1",9000))

while True:
    c,a=s.recvfrom(10000)
    print("Request received from"+str(a))
    print(c)
    sleep(5)
    s.sendto(b'hello',a)
