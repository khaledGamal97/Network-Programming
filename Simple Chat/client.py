from socket import *
S=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7000
S.connect((host,port))
while True:
    S.send(input("client: ").encode('utf-8'))
    Y=S.recv(2048)
    print("server: ",Y.decode('utf-8'))
S.close()