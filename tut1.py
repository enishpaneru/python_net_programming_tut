from socket import *

newsocket=socket(AF_INET,SOCK_STREAM)
newsocket.settimeout(4)
newsocket.connect(("127.0.0.1",9000))
newsocket.send(b'go back')
try:
    data=newsocket.recv(10000)
except timeout:
    data=[]
print(data)
newsocket.close()