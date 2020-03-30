#import libraries
from socket import *
from _thread import *
import threading
from tkinter import *
from tkinter import messagebox

try:
    S=socket(AF_INET,SOCK_STREAM)#create socket and this return file descriptor number
    S.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#if socket is used, make it available to reuse
    host='127.0.0.1' #server ip address
    port=7000 #service port
    S.bind((host,port)) #to bind socket with ip and port number
    S.listen(5)  #listen to comming clients,queue=5
    C,ad=S.accept() #this accept only one client to play with him
    #gui window
    wind=Tk()
    wind.title("server") #gui title
    wind.geometry("300x400") #gui dimensions
    turn=1#client will start the game and can press the button if turn=1
    #button_1 function
    def clicked1():
        global turn #this make changes to this variable affects the outer variable "turn"
        #if the first squre is empty"not clicked before" and it's the turn of server "turn=2"
        if btn1["text"]==" " and turn==2:
                btn1["text"]='O' #makes the empty squres value by "O"
                turn=1
                send('a',turn=1) #send the changed square number to the client
                check() #check if any player win or not
    #button_2 function
    def clicked2():
        global turn
        if btn2["text"]==" " and turn==2:
                btn2["text"]='O'
                turn=1
                send('b',turn=1)
                check()
    #button_3 function
    def clicked3():
        global turn
        if btn3["text"]==" " and turn==2:
                btn3["text"]='O'
                turn=1
                send('c',turn=1)
                check()
    #button_4 function
    def clicked4():
        global turn
        if btn4["text"]==" " and turn==2:
                btn4["text"]='O'
                turn=1
                send('d',turn=1)
                check()
    #button_5 function
    def clicked5():
        global turn
        if btn5["text"]==" " and turn==2:
                btn5["text"]='O'
                turn=1
                send('e',turn=1)
                check()
    #button_6 function
    def clicked6():
        global turn
        if btn6["text"]==" " and turn==2:
                btn6["text"]='O'
                turn=1
                send('f',turn=1)
                check()
     #button_7 function
    def clicked7():
        global turn
        if btn7["text"]==" " and turn==2:
                btn7["text"]='O'
                turn=1
                send('g',turn=1)
                check()
    #button_8 function
    def clicked8():
        global turn
        if btn8["text"]==" " and turn==2:
                btn8["text"]='O'
                turn=1
                send('h',turn=1)
                check()
    #button_9 function
    def clicked9():
        global turn
        if btn9["text"]==" " and turn==2:
                btn9["text"]='O'
                turn=1
                send('i',turn=1)
                check()

    count=1
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
        if(b1==b2 and b2==b3 and b1=='O'):#first case??
            win('O')
        if(b4==b5 and b5==b6 and b4=='O'):#second case??
            win('O')
        if(b7==b8 and b8==b9 and b7=='O'):#third case??
            win('O')
        if(b1==b4 and b4==b7 and b1=='O'):#fourth case??
            win('O')
        if(b2==b5 and b5==b8 and b2=='O'):#......
            win('O')
        if(b3==b6 and b6==b9 and b3=='O'):#......
            win('O')
        if(b1==b5 and b5==b9 and b1=='O'):#......
            win('O')
        if(b3==b5 and b5==b7 and b3=='O'):#......
            win('O')
        if count==10:#the last case if it happened,show the following message box!!
            send('q',turn=0) #send 'q' to the client to tell him that the Game is equal
            messagebox.showinfo("تعادل  ؟؟")
            wind.destroy()

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
        C.send((x+' '+str(turn)).encode('utf-8'))


    #creating a function to receive from client the number of changed Square and the turn
    def receive_thread(C):
        global count
        global turn
        try:
            while True:
                received=(C.recv(2048)).decode('utf-8') #receive from the client
                X=received[0] #number of square that was changed
                turn=int(received[2]) #player turn
                count+=1#increment the count by 1 at every time i receive anything from the client
                #these change the square that was changed at the client
                if X=='a':  btn1["text"]='X'
                elif X=='b':   btn2["text"]='X'
                elif X=='c':   btn3["text"]='X'
                elif X=='d':   btn4["text"]='X'
                elif X=='e':   btn5["text"]='X'
                elif X=='f':   btn6["text"]='X'
                elif X=='g':   btn7["text"]='X'
                elif X=='h':   btn8["text"]='X'
                elif X=='i':   btn9["text"]='X'
                #if i receive 'o' then i know i lose the Game
                elif X=='X' and turn==0:
                    messagebox.showinfo("YOU LOSE !!")
                    wind.destroy()
                #IF I receive 'q' then the Game is "equal"
                elif X=='q' and turn==0:
                   messagebox.showinfo("!!تعادل")
                   wind.destroy()

        except:
            print("Game is terminated !! ")
    #make a thread to receive from the client
    #to run the process(thread) of receiving
    start_new_thread(receive_thread,(C,))
    #function to show the GUI
    wind.mainloop()
    S.close()#close socket

#when any error has happened in socket, print it
except error as e:
    print(e)
#when i use any keyboard shortcuts
except KeyboardInterrupt:
    print("Game is terminated !! ")
