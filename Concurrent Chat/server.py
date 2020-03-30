#import libraries
from socket import *
from _thread import * #multi threading package
import threading
S=socket(AF_INET,SOCK_STREAM) #create socket and this return file descriptor number
S.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#if socket is used, make it available to reuse
host='127.0.0.1' #server ip
port=7000        #service port
S.bind((host,port)) #to bind socket with ip and port number
S.listen(5) #listen to comming clients
#creating a function to receive from client
def receive_thread(C):
    while True:
        X=C.recv(2048)
        print(X.decode('utf-8'))
#
def client_thread(C):
    receive=threading.Thread(target=receive_thread,args=(C,))
    receive.start()
    while True:
        C.send(input("server: ").encode('utf-8'))
while True:
    C,ad=S.accept()
    print("connection from: ",ad[0])
    X=C.recv(2048)
    start_new_thread(client_thread,(C,))
    
S.close()
