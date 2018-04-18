from socket import *

newsocket=socket(AF_INET,SOCK_DGRAM)
newsocket.sendto(b'go back',('127.0.0.1',9000))
data,addr=newsocket.recvfrom(10000)
print(data,addr)
