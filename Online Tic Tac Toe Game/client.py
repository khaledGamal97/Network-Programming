#import libraries
from socket import *
from _thread import *
import threading
from tkinter import *
from tkinter import messagebox

S=socket(AF_INET,SOCK_STREAM)#create socket and this return file descriptor number
host='127.0.0.1' #server ip address
port=7000 #service port
S.connect((host,port)) #connect the server
#GUI window
wind=Tk()
wind.title("client") #gui title
wind.geometry("300x400") #gui dimensions

turn=1#client will start the game and can press the button if turn=1
#button_1 function
def clicked1():
    global turn  #this make changes to this variable affects the outer variable "turn"
    #if the first squre is empty"not clicked before" and it's the turn of client"turn=1"
    if btn1["text"]==" " and turn==1:
            btn1["text"]='X' #makes the empty squres value by "X"
            turn=2
            send('a',turn=2) #send the changed square number to the server
            check() #check if any player win or not
#button_2 function
def clicked2():
    global turn
    if btn2["text"]==" " and turn==1:
            btn2["text"]='X'
            turn=2
            send('b',turn=2)
            check()
#button_3 function
def clicked3():
    global turn
    if btn3["text"]==" " and turn==1:
            btn3["text"]='X'
            turn=2
            send('c',turn=2)
            check()
#button_4 function
def clicked4():
    global turn
    if btn4["text"]==" " and turn==1:
            btn4["text"]='X'
            turn=2
            send('d',turn=2)
            check()
#button_5 function
def clicked5():
    global turn
    if btn5["text"]==" " and turn==1:
            btn5["text"]='X'
            turn=2
            send('e',turn=2)
            check()
#button_6 function
def clicked6():
    global turn
    if btn6["text"]==" " and turn==1:
            btn6["text"]='X'
            turn=2
            send('f',turn=2)
            check()
 #button_7 function
def clicked7():
    global turn
    if btn7["text"]==" " and turn==1:
            btn7["text"]='X'
            turn=2
            send('g',turn=2)
            check()
#button_8 function
def clicked8():
    global turn
    if btn8["text"]==" " and turn==1:
            btn8["text"]='X'
            turn=2
            send('h',turn=2)
            check()
#button_9 function
def clicked9():
    global turn
    if btn9["text"]==" " and turn==1:
            btn9["text"]='X'
            turn=2
            send('i',turn=2)
            check()

count=1 #It holds the number of games played by the players
#this function checks that if any player of 2 players wins,or not, or the game is equal
def check():
    global count #this make changes to this variable affects the outer variable "count"
    count+=1 #increment the count by 1 at every time this function was called
    #i do the following to facilitates the code
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    #these cases determines if the game is ended or not!!!
    if(b1==b2 and b2==b3 and b1=='X'):#first case??
        win('X')
    if(b4==b5 and b5==b6 and b4=='X'):#second case??
        win('X')
    if(b7==b8 and b8==b9 and b7=='X'):#third case??
        win('X')
    if(b1==b4 and b4==b7 and b1=='X'):#fourth case??
        win('X')
    if(b2==b5 and b5==b8 and b2=='X'):#......
        win('X')
    if(b3==b6 and b6==b9 and b3=='X'):#......
        win('X')
    if(b1==b5 and b5==b9 and b1=='X'):#......
        win('X')
    if(b3==b5 and b5==b7 and b3=='X'):#......
        win('X')
    if count==10:#the last case if it happened,show the following message box!!
        send('q',turn=0) #send 'q' to the server to tell him that the Game is equal
        messagebox.showinfo("تعادل  ؟؟")
        wind.destroy()#close the GUI window

 #if any player wins,this function shows the following message box!!
def win(player):
    send(player,turn=0)
    messagebox.showinfo("congratulation --> player ",player)
    wind.destroy()

btn1=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked1)
btn1.grid(row=0,column=1)

btn2=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked2)
btn2.grid(row=0,column=2)

btn3=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked3)
btn3.grid(row=0,column=3)

btn4=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked4)
btn4.grid(row=1,column=1)

btn5=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked5)
btn5.grid(row=1,column=2)

btn6=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked6)
btn6.grid(row=1,column=3)

btn7=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked7)
btn7.grid(row=2,column=1)

btn8=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked8)
btn8.grid(row=2,column=2)

btn9=Button(wind,text=" ",bg='Yellow',fg='Black',width=5,
            height=5,font=["Helvetica",20],command=clicked9)
btn9.grid(row=2,column=3)


#function of the send button
#it sends the number of changed square plus the turn of the player will play
def send(x,turn):
    S.send((x+' '+str(turn)).encode('utf-8'))
#this function receive from server the number of changed Square and the turn
def receive_thread(S):
    global turn
    global count
    try:
        while True:
            received=(S.recv(2048)).decode('utf-8')#receive from the server
            X=received[0] #number of square that was changed
            turn=int(received[2])#player turn
            count+=1 #increment the count by 1 at every time i receive anything from the server
            #these change the square that was changed at the server
            if X=='a':  btn1["text"]='O'
            elif X=='b':   btn2["text"]='O'
            elif X=='c':   btn3["text"]='O'
            elif X=='d':   btn4["text"]='O'
            elif X=='e':   btn5["text"]='O'
            elif X=='f':   btn6["text"]='O'
            elif X=='g':   btn7["text"]='O'
            elif X=='h':   btn8["text"]='O'
            elif X=='i':   btn9["text"]='O'
            #if i receive 'o' then i know i lose the Game
            elif X=='O' and turn==0:
                messagebox.showinfo("YOU LOSE !!")
                wind.destroy()
            #IF I receive 'q' then the Game is "equal"
            elif X=='q' and turn==0:
               messagebox.showinfo("!!تعادل")
               wind.destroy()


    except:
        print("Game is terminated !! ")

#make a thread to receive from the server
receive=threading.Thread(target=receive_thread,args=(S,))
receive.start()#start the thread
wind.mainloop()#this function to show the GUI

S.close()#close the socket
