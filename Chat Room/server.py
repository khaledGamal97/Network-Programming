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
clients=[] #list of connected clients
#this function recieves messages from clients and then forward them to the others.
def ConnectNewUser(c,ad):
    while True:
        m=c.recv(2048)
        msg=ad[0]+':'+m.decode('utf-8') #concatenate message with the address of the sender
        SendToAll(msg,c)
#this function forward the recieved message to other clients.       
def SendToAll(msg,con):
    for client in clients:
        if client != con:
            client.send(msg.encode('utf-8'))
            
while True:
    C,ad=S.accept()
    clients.append(C)#add the new client to the list of connected clients
    #start a thread to send and recieve to\from clients
    start_new_thread(ConnectNewUser,(C,ad))
    
S.close()