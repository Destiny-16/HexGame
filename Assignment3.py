from tkinter import *

root = Tk()
root.title("Hex Game")
root.geometry("500x500")

frame =Frame(root,width=500,height=500)
frame.place(x=0,y=0)
draw=Canvas(frame,width=500,height=500)
draw.place(x=0,y=0)

player = ''
computer = ''

#draw.create_line(150,90,80,180,width=3) #1 to 6
#draw.create_line(150,90,80,180,width=3, dash=(3,5))#1 to 6
#draw.create_line(150,90,240,80,width=3) #1 to 2
#draw.create_line(150,90,240,80,width=3, dash=(3,5))#1 to 2
#draw.create_line(250,90,300,170,width=3) #2 to 3
#draw.create_line(250,90,300,170,width=3, dash=(3,5))#2 to 3



def drawBoard():
    draw.create_oval(150, 90, 140, 80, fill='black') #1
    draw.create_oval(250, 90, 240, 80, fill='black') #2
    draw.create_oval(310, 180, 300, 170, fill='black') #3
    draw.create_oval(250, 280, 240, 270, fill='black') #4
    draw.create_oval(150, 280, 140, 270, fill='black') #5
    draw.create_oval(80, 180, 70, 170, fill='black') #6

def setPlayers():
    player = input("Whice Player? 1(solid) or 2(dashed)?: ")

    if(player == '1'):
        print("your are solid lines")
        computer = "p2"
    elif(player == '2'):
        print("your are dashed lines")
        computer = "p1"
    else:
        print("invalid input")
        exit();

    





setPlayers()
drawBoard()






