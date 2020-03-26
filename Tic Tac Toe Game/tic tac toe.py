#import libraries
from tkinter import *
from tkinter import messagebox,Button,Label
#GUI window
wind=Tk()
wind.title("Tic Tac Toe")#GUI window title
wind.geometry("400x300")#window dimensions
lb1=Label(wind,text="player1:X",font=["Helvetica",15])
lb1.grid(row=0,column=0)
lb1=Label(wind,text="player2:O",font=["Helvetica",15])
lb1.grid(row=1,column=0)

turn=1 #variable holds the value which determines the turn of the player who its turn
#making 9 functions to the 9 buttons of the 9 squres
def clicked1():#button_1 function
    global turn #this make changes to this variable affects the outer variable "turn"
    if btn1["text"]==" ":#if the first squre is empty"not clicked before"
        if turn==1:#If it is the turn of the player"X" to play 
            turn=2 
            btn1["text"]='X' #makes the empty squres value by "X"
        else: #If it is the turn of the player"O" to play
            turn=1
            btn1["text"]='O' #makes the empty squres value by "O"
        check() #check if any player win or not
        
def clicked2(): #.....
    global turn
    if btn2["text"]==" ":#.....
        if turn==1:#.....
            turn=2
            btn2["text"]='X'#.....
        else:#.....
            turn=1
            btn2["text"]='O'#.....
        check() #......
        
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn=2
            btn3["text"]='X'
        else:
            turn=1
            btn3["text"]='O'
        check()
        
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn=2
            btn4["text"]='X'
        else:
            turn=1
            btn4["text"]='O'
        check()
        
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn=2
            btn5["text"]='X'
        else:
            turn=1
            btn5["text"]='O'
        check()
        
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn=2
            btn6["text"]='X'
        else:
            turn=1
            btn6["text"]='O'
        check()
        
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn=2
            btn7["text"]='X'
        else:
            turn=1
            btn7["text"]='O'
        check()

def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn=2
            btn8["text"]='X'
        else:
            turn=1
            btn8["text"]='O'
        check()

def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn=2
            btn9["text"]='X'
        else:
            turn=1
            btn9["text"]='O'
        check()

count=1 #It holds the number of games played by the players
#this function checks that if any player of 2 players wins,or not, or the game is equal
def check():
    global count  #this make changes to this variable affects the outer variable "count"
    count+=1 #increment the count by 1 at every time this function was called
    #To simplify and shorten the code
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    #the following cases determines if the game is ended or not!!!
    if(b1==b2 and b2==b3 and b1=='X')or(b1==b2 and b2==b3 and b1=='O'):#first case
        win(b1)
    if(b4==b5 and b5==b6 and b4=='X')or(b4==b5 and b5==b6 and b4=='O'):#second case
        win(b4)
    if(b7==b8 and b8==b9 and b7=='X')or(b7==b8 and b8==b9 and b7=='O'):#third case
        win(b7)
    if(b1==b4 and b4==b7 and b1=='X')or(b1==b4 and b4==b7 and b1=='O'):#.......
        win(b1)
    if(b2==b5 and b5==b8 and b2=='X')or(b2==b5 and b5==b8 and b2=='O'):#.......
        win(b2)
    if(b3==b6 and b6==b9 and b3=='X')or(b3==b6 and b6==b9 and b3=='O'):#.......
        win(b3)
    if(b1==b5 and b5==b9 and b1=='X')or(b1==b5 and b5==b9 and b1=='O'):#.......
        win(b1)
    if(b3==b5 and b5==b7 and b3=='X')or(b3==b5 and b5==b7 and b3=='O'):#.......
        win(b3)
    if count==10:
        #if count=10 --> show the following message
        messagebox.showinfo("اللعبة اتقفلت يا ريس  ؟؟")
        wind.destroy()
    
def win(player): #if any player wins,this function shows the following message box to the winner!!
    messagebox.showinfo("congratulation --> player ",player) 
    wind.destroy()
        
btn1=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked1)
btn1.grid(row=0,column=1)

btn2=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked2)
btn2.grid(row=0,column=2)

btn3=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked3)
btn3.grid(row=0,column=3)

btn4=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked4)
btn4.grid(row=1,column=1)

btn5=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked5)
btn5.grid(row=1,column=2)

btn6=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked6)
btn6.grid(row=1,column=3)

btn7=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked7)
btn7.grid(row=2,column=1)

btn8=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked8)
btn8.grid(row=2,column=2)

btn9=Button(wind,text=" ",bg='Yellow',fg='Black',width=3,
            height=1,font=["Helvetica",15],command=clicked9)
btn9.grid(row=2,column=3)

wind.mainloop() #this function to show the GUI
