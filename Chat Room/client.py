from socket import *
from _thread import *
from tkinter import *


S = socket((AF_INET) , SOCK_STREAM)
host = "127.0.0.1"
port = 7000
S.connect((host , port))
#gui window
wind = Tk();
wind.title("Client") #gui title
wind.geometry("600x300")#gui dimensions
lb1 = Label(wind,text= ' Enter a Message: ' ,font=( ' Verdana ' , 16))
lb1.grid(row=0,column=0)
lb2 = Label(wind,text= ' The received message : ' ,font=( ' Verdana ' , 16))
lb2.grid(row=3,column=0)
recv_lb = Label(wind,font=( ' Verdana ' , 16), width=30)#label of the recv message
recv_lb.grid(row=4,column=1)

send_entry = Entry(wind,font=( ' Verdana ' , 16), width=30) #textbox of the sent message
send_entry.grid(row=1,column=1)

#function of the send button
def button_fun():
	message = send_entry.get()
	S.send(message.encode('utf-8'))
	send_entry.delete(0 , END)

send_btn = Button(wind,text= ' Send ' , font=( ' Verdana ' , 16), command=button_fun)
send_btn.grid(row=2, column=1)


def recvThread(S):
	while True:
		recv_lb["text"] = S.recv(2048).decode('utf-8')

start_new_thread(recvThread , (S,))

wind.mainloop();
