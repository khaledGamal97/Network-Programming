#import libraries
from socket import *
from _thread import * #multi threading package
import threading
from tkinter import *
try:
    S=socket(AF_INET,SOCK_STREAM) #create socket and this return file descriptor number
    S.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#if socket is used, make it available to reuse
    host='127.0.0.1' #server ip
    port=7000       #service port
    S.bind((host,port)) #to bind socket with ip and port number
    S.listen(5) #listen to comming clients,queue=5
    #gui window
    wind=Tk()
    wind.title("server") #gui title
    wind.geometry("600x300") #gui dimensions
    lb1 = Label(wind,text= ' Enter a Message: ' ,font=( ' Verdana ' , 16))
    lb1.grid(row=0,column=0)
    send_entry = Entry(wind,font=( ' Verdana ' , 16), width=30) #textbox of the sent message
    send_entry.grid(row=1,column=1)
    #function of the send button 
    def button_fun():
        X=send_entry.get()
        C.send(X.encode('utf-8'))
        send_entry.delete(0,END)#Delete text from FIRST to LAST

    #creating a function to receive from client
    def receive_thread(C):
        while True:
            Y=C.recv(2048)
            recv_lb["text"]=Y.decode('utf-8')
  
        
        
        
    #send button
    send_btn = Button(wind,text= ' Send ' , font=( ' Verdana ' , 16), command=button_fun)
    send_btn.grid(row=2, column=1)
    lb2 = Label(wind,text= ' The received message : ' ,font=( ' Verdana ' , 16))
    lb2.grid(row=3,column=0)
    recv_lb = Label(wind,font=( ' Verdana ' , 16), width=30)#label of the recv message
    recv_lb.grid(row=4,column=1)
    #this accept only one client to take with him and share information
    C,ad=S.accept()
    #to run the process(thread) of receiving
    start_new_thread(receive_thread,(C,))
    
    
    #function to show the gui
    wind.mainloop()
    S.close()#close socket
except error as e:#if there is any an error
    print(e)
except KeyboardInterrupt:#if you used any shortcuts on keyboard to terminate the chat!!
    print("chat is terminated !! ")
    S.close()
    
    
        
    
        
