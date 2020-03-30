from socket import *
from _thread import *
import threading
S=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7000
def receive_thread(s):
    while True:
        X=S.recv(2048)
        print(X.decode('utf-8'))

S.connect((host,port))
receive=threading.Thread(target=receive_thread,args=(S,))
receive.start()
while True:
    S.send(input("client: ").encode('utf-8'))
    
S.close()
    