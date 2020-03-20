#import libraries
from socket import *
from _thread import *
import threading
from tkinter import *
try:
    S=socket(AF_INET,SOCK_STREAM)
    host='127.0.0.1'
    port=7000
    #gui window
    wind=Tk()
    wind.title("client") #gui title
    wind.geometry("600x300") #gui dimensions
    lb1 = Label(wind,text= ' Enter a Message: ' ,font=( ' Verdana ' , 16))
    lb1.grid(row=0,column=0)
    send_entry = Entry(wind,font=( ' Verdana ' , 16), width=30) #textbox of the sent message
    send_entry.grid(row=1,column=1)
    #function of the send button 
    def button_fun():
        X=send_entry.get()
        S.send(X.encode('utf-8'))
        send_entry.delete(0,END)#Delete text from FIRST to LAST
    
    def receive_thread(S):
        while True:
            X=S.recv(2048)
            recv_lb["text"]=X.decode('utf-8')
    #send button
    send_btn = Button(wind,text= ' Send ' , font=( ' Verdana ' , 16), command=button_fun)
    send_btn.grid(row=2, column=1)
    lb2 = Label(wind,text= ' The received message : ' ,font=( ' Verdana ' , 16))
    lb2.grid(row=3,column=0)
    recv_lb = Label(wind,font=( ' Verdana ' , 16), width=30)#textbox of the recv message
    recv_lb.grid(row=4,column=1)
    #function to show the gui
    
    S.connect((host,port))
    
    receive=threading.Thread(target=receive_thread,args=(S,))
    receive.start()
    wind.mainloop()
    S.close()
except error as e:
    print(e)  
      
except KeyboardInterrupt:
    S.close()
    receive.join()
