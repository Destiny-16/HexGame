from tkinter import *

root = Tk()
root.title("Hex Game")
root.geometry("500x500")

frame =Frame(root,width=500,height=500)
frame.place(x=0,y=0)
draw=Canvas(frame,width=500,height=500)
draw.place(x=0,y=0)

player = ""
computer = ""
start = ""
end = ""
turn = ""
p = ['0']*100
c = ['0']*100
i = 0
j = 0

class Node:
    x1 = 0 
    y1 = 0
    x2 = 0
    y2 = 0
    node = ''

n1 = Node()
n1.node = '1'
n1.x1 = 150
n1.y1 = 90
n1.x2 = 140
n1.y2 = 80

n2 = Node()
n2.node = '2'
n2.x1 = 250
n2.y1 = 90
n2.x2 = 240
n2.y2 = 80

n3 = Node()
n3.node = '3'
n3.x1 = 310
n3.y1 = 180
n3.x2 = 300
n3.y2 = 170

n4 = Node()
n4.node = '4'
n4.x1 = 250
n4.y1 = 280
n4.x2 = 240
n4.y2 = 270

n5 = Node()
n5.node = '5'
n5.x1 = 150
n5.y1 = 280
n5.x2 = 140
n5.y2 = 270

n6 = Node()
n6.node = '6'
n6.x1 = 80
n6.y1 = 180
n6.x2 = 70
n6.y2 = 170




def drawBoard():
    draw.create_oval(n1.x1, n1.y1, n1.x2, n1.y2, fill='black') #1
    draw.create_oval(n2.x1, n2.y1, n2.x2, n2.y2, fill='black') #2
    draw.create_oval(n3.x1, n3.y1, n3.x2, n3.y2, fill='black') #3
    draw.create_oval(n4.x1, n4.y1, n4.x2, n4.y2, fill='black') #4
    draw.create_oval(n5.x1, n5.y1, n5.x2, n5.y2, fill='black') #5
    draw.create_oval(n6.x1, n6.y1, n6.x2, n6.y2, fill='black') #6


def setPlayers():
   choice = input("Whice Player? 1(solid) or 2(dashed)?: ")

   if(choice == '1'):
        print("you are solid lines")
        computer = "p2"
        player = "p1"
        turn = player
        
   elif(choice == '2'):
        print("you are dashed lines")
        computer = "p1"
        player = "p2"
        turn = computer
        
   else:
        print("invalid input")
        exit();

   n = [turn, player, computer]
   return n
        

    
def drawLine(turn, player, computer, i, j):
    start = input("Starting node: ")
    end = input("Ending node: ")
    
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0
    node1 = ''
    node2 = ''

    
    if(start == n1.node):
        x3 = n1.x1
        y3 = n1.y1
        node1 = n1.node
    elif(start == n2.node):
        x3 = n2.x1
        y3 = n2.y1
        node1 = n2.node
    elif(start == n3.node):
        x3 = n3.x1
        y3 = n3.y1
        node1 = n3.node
    elif(start == n4.node):
        x3 = n4.x1
        y3 = n4.y1
        node1 = n4.node
    elif(start == n5.node):
        x3 = n5.x1
        y3 = n5.y1
        node1 = n5.node
    elif(start == n6.node):
        x3 = n6.x1
        y3 = n6.y1
        node1 = n6.node
    else:
        print("invalid entry")
        exit()

    if(end == n1.node):
        x4 = n1.x2
        y4 = n1.y2
        node2 = n1.node
    elif(end == n2.node):
        x4 = n2.x2
        y4 = n2.y2
        node2 = n2.node
    elif(end == n3.node):
        x4 = n3.x2
        y4 = n3.y2
        node2 = n3.node
    elif(end == n4.node):
        x4 = n4.x2
        y4 = n4.y2
        node2 = n4.node
    elif(end == n5.node):
        x4 = n5.x2
        y4 = n5.y2
        node2 = n5.node
    elif(end == n6.node):
        x4 = n6.x2
        y4 = n6.y2
        node2 = n6.node
    else:
        print("invalid entry")
        exit()

    if(turn == "p1"):
        draw.create_line(x3,y3,x4,y4,width=3)
    else:
        draw.create_line(x3,y3,x4,y4,width=3, dash=(3,5))

    if(turn == player):
        p[i] = [node1, node2]
        i = i + 1
    elif( turn == computer):
        c[j] = [node1, node2]
        j = j + 1


    return [i,j]

        


def getPlayer(turn, player, computer):

 
    if (turn != player):
        turn = player
       
    else:
        turn = computer

    return turn

        

    
def checkWinner():
    return False;

#def ComputerChoice():
    
    
    


n = [0]*3
increment = [0]*2
winner = False
n = setPlayers()

turn = n[0]
player = n[1]
computer = n[2]


while(winner == False):
    print(turn, "'s", " turn")
    drawBoard()
    increment = drawLine(turn, player, computer, i, j)
    i = increment[0]
    j = increment[1]
    frame.update()
    turn = getPlayer(turn, player, computer)
    winner = checkWinner()

    print('p', p)
    print('c', c)

    






