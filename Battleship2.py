import random
import tkinter
#from buttongrid import *

Chits = 0
Bhits = 0
Shits = 0
Dhits = 0
Ghits = 0
turns = 0
board = []
def Gridmaker():
    A = [0,0,0,0,0,0,0,0,0,0]
    B = [0,0,0,0,0,0,0,0,0,0]
    C = [0,0,0,0,0,0,0,0,0,0]
    D = [0,0,0,0,0,0,0,0,0,0]
    E = [0,0,0,0,0,0,0,0,0,0]
    F = [0,0,0,0,0,0,0,0,0,0]
    G = [0,0,0,0,0,0,0,0,0,0]
    H = [0,0,0,0,0,0,0,0,0,0]
    I = [0,0,0,0,0,0,0,0,0,0]
    J = [0,0,0,0,0,0,0,0,0,0]

    boats = ['B','S','D','G','C']
    global board
    board = [A,B,C,D,E,F,G,H,I,J]
    
    
    for i in range(5):
        collision = True
        direction = random.randrange(4)
        if boats[i] == 'B':
            if direction == 0: 
                #battleship points up
                x = random.randrange(10)
                y = random.randrange(3,10)
                board[x][y] = 'B'
                board[x][(y-1)] = 'B'
                board[x][(y-2)] = 'B'
                board[x][(y-3)] = 'B'
            elif direction == 1:
                #battleship points south
                x = random.randrange(10)
                y = random.randrange(0,7)
                board[x][y] = 'B'
                board[x][(y+1)] = 'B'
                board[x][(y+2)] = 'B'
                board[x][(y+3)] = 'B'
            elif direction == 2:
                #battleship points west
                x = random.randrange(3,10)
                y = random.randrange(10)
                board[x][y] = 'B'
                board[x-1][y] = 'B'
                board[x-2][y] = 'B'
                board[x-3][y] = 'B'
            elif direction == 3:
                #battleship points east
                x = random.randrange(0,7)
                y = random.randrange(10)
                board[x][y] = 'B'
                board[(x+1)][y] = 'B'
                board[(x+2)][y] = 'B'
                board[(x+3)][y] = 'B'
        elif boats[i] == 'S':
            if direction == 0:
                #Submarine points north
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(2,10)
                    if board[x][y] == 0 and board[x][(y-1)] == 0 and board[x][(y-2)] == 0 :
                        collision = False
                        board[x][y] = 'S'
                        board[x][(y-1)] = 'S'
                        board[x][(y-2)] = 'S'
            if direction == 1:
                #Submarine poitns south
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(0,8)
                    if board[x][y] == 0 and board[x][(y+1)] == 0 and board[x][(y+2)] == 0 :
                        collision = False
                        board[x][y] = 'S'
                        board[x][(y+1)] = 'S'
                        board[x][(y+2)] = 'S'
            if direction == 2:
                #Submarine points west
                while collision == True:
                    x = random.randrange(2,10)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x-1][y] == 0 and board[x-2][y] == 0 :
                        collision = False
                        board[x][y] = 'S'
                        board[x-1][y] = 'S'
                        board[x-2][y] = 'S'
            if direction == 3:
                #Submarine points east
                while collision == True:
                    x = random.randrange(0,8)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x+1][y] == 0 and board[x+2][y] == 0 :
                        collision = False
                        board[x][y] = 'S'
                        board[x+1][y] = 'S'
                        board[x+2][y] = 'S'

        elif boats[i] == 'D':
            if direction == 0:
                #Destroyer points north
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(2,10)
                    if board[x][y] == 0 and board[x][(y-1)] == 0 and board[x][(y-2)] == 0 :
                        collision = False
                        board[x][y] = 'D'
                        board[x][(y-1)] = 'D'
                        board[x][(y-2)] = 'D'
            if direction == 1:
                #Destroyer points South
                    while collision == True:
                        x = random.randrange(10)
                        y = random.randrange(0,8)
                        if board[x][y] == 0 and board[x][(y+1)] == 0 and board[x][(y+2)] == 0 :
                            collision = False
                            board[x][y] = 'D'
                            board[x][(y+1)] = 'D'
                            board[x][(y+2)] = 'D'
            if direction == 2:
                #Destroyer points West
                  while collision == True:
                    x = random.randrange(2,10)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x-1][y] == 0 and board[x-2][y] == 0 :
                        collision = False
                        board[x][y] = 'D'
                        board[x-1][y] = 'D'
                        board[x-2][y] = 'D'
            if direction == 3:
                #Destroyer points East
                while collision == True:
                    x = random.randrange(0,8)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x+1][y] == 0 and board[x+2][y] == 0 :
                        collision = False
                        board[x][y] = 'D'
                        board[x+1][y] = 'D'
                        board[x+2][y] = 'D'

        elif boats[i] == 'G':
            if direction == 0:
                #Gunboat points North
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(1,10)
                    if board[x][y] == 0 and board[x][(y-1)] == 0 :
                        collision = False
                        board[x][y] = 'G'
                        board[x][(y-1)] = 'G'
            if direction == 1:
                #Gunboat points South
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(0,9)
                    if board[x][y] == 0 and board[x][(y+1)] == 0 :
                        collision = False
                        board[x][y] = 'G'
                        board[x][(y+1)] = 'G'
            if direction == 2:
                #Gunboat points West
                while collision == True:
                    x = random.randrange(1,10)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x-1][y] == 0 :
                        collision = False
                        board[x][y] = 'G'
                        board[x-1][y] = 'G'
            if direction == 3:
                #Gunboat points East
                while collision == True:
                    x = random.randrange(0,9)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x+1][y] == 0 :
                        collision = False
                        board[x][y] = 'G'
                        board[x+1][y] = 'G'

        elif boats[i] == 'C':
            if direction == 0:
                #Carrier points North
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(4,10)
                    if board[x][y] == 0 and board[x][(y-1)] == 0 and board[x][(y-2)] == 0 and board[x][y-3] == 0 and board[x][y-4] == 0 :
                        collision = False
                        board[x][y] = 'C'
                        board[x][(y-1)] = 'C'
                        board[x][y-2] = 'C'
                        board[x][y-3] = 'C'
                        board[x][y-4] = 'C'
            if direction == 1:
                #Carrier points South
                while collision == True:
                    x = random.randrange(10)
                    y = random.randrange(0,6)
                    if board[x][y] == 0 and board[x][(y+1)] == 0 and board[x][(y+2)] == 0 and board[x][y+3] == 0 and board[x][y+4] == 0 :
                        collision = False
                        board[x][y] = 'C'
                        board[x][(y+1)] = 'C'
                        board[x][y+2] = 'C'
                        board[x][y+3] = 'C'
                        board[x][y+4] = 'C'
            if direction == 2:
                #Carrier points West
                while collision == True:
                    x = random.randrange(4,10)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x-1][y] == 0 and board[x-2][y] == 0 and board[x-3][y] == 0 and board[x-4][y] == 0 :
                        collision = False
                        board[x][y] = 'C'
                        board[x-1][y] = 'C'
                        board[x-2][y] = 'C'
                        board[x-3][y] = 'C'
                        board[x-4][y] = 'C'
            if direction == 3:
                #Carrier points East
                while collision == True:
                    x = random.randrange(0,6)
                    y = random.randrange(10)
                    if board[x][y] == 0 and board[x+1][y] == 0 and board[x+2][y] == 0 and board[x+3][y] == 0 and board[x+4][y] == 0 :
                        collision = False
                        board[x][y] = 'C'
                        board[x+1][y] = 'C'
                        board[x+2][y] = 'C'
                        board[x+3][y] = 'C'
                        board[x+4][y] = 'C'
    for i in range(10):
        print(board[i])
   
    A1 = [0,0,0,0,0,0,0,0,0,0]
    B1 = [0,0,0,0,0,0,0,0,0,0]
    C1 = [0,0,0,0,0,0,0,0,0,0]
    D1 = [0,0,0,0,0,0,0,0,0,0]
    E1 = [0,0,0,0,0,0,0,0,0,0]
    F1 = [0,0,0,0,0,0,0,0,0,0]
    G1 = [0,0,0,0,0,0,0,0,0,0]
    H1 = [0,0,0,0,0,0,0,0,0,0]
    I1 = [0,0,0,0,0,0,0,0,0,0]
    J1 = [0,0,0,0,0,0,0,0,0,0]

    playersheet = [A1,B1,C1,D1,E1,F1,G1,H1,I1,J1]
    
def battleship(x,y,var):
    column = x
    row = y
    check = var
    global Bhits
    global Shits
    global Dhits
    global Ghits
    global Chits
    global turns
    if check['background'] != 'blue':
        print('You have already chosen that spot. Choose Again!')
    else:
        if board[column][row] == 0:
            check['background'] = 'white'
            turns = turns + 1
        elif board[column][row] == 'B':
            Bhits = Bhits + 1
            check['background'] = 'red'
            turns = turns + 1
            if Bhits == 4:
                print('You sunk my Battleship')
        elif board[column][row] == 'S':
            Shits = Shits + 1
            check['background'] = 'red'
            turns = turns + 1
            if Shits == 3:
                print('You sunk my Submarine')
        elif board[column][row] == 'D':
            Dhits = Dhits + 1
            check['background'] = 'red'
            turns = turns + 1
            if Dhits == 3:
                print('You sunk my Destroyer')
        elif board[column][row] == 'G':
            Ghits = Ghits + 1
            check['background'] = 'red'
            turns = turns + 1
            if Ghits == 2:
                print('You sunk my Gunboat')
        elif board[column][row] == 'C':
            Chits = Chits + 1
            check['background'] = 'red'
            turns = turns + 1
            if Chits == 5:
                print('You sunk my Carrier')
    if turns > 50:
        Losescreen = tkinter.Tk()
        YOULOSE = tkinter.Button(Losescreen, text = 'You Lose!', command = Losescreen.destroy)
        YOULOSE.pack()
        Losescreen.mainloop()
    elif (Chits + Bhits + Shits + Dhits + Ghits) == 17:
        winscreen = tkinter.Tk()
        YOUWIN = tkinter.Button(winscreen, text = 'YOU WIN!', command = winscreen.destroy)
        YOUWIN.pack()
        winscreen.mainloop()
        print('YOU WIN!')
Gridmaker()
root = tkinter.Tk()
button00 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,0,button00))
button01 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,1,button01))
button02 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,2,button02))
button03 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,3,button03))
button04 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,4,button04))
button05 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,5,button05))
button06 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,6,button06))
button07 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,7,button07))
button08 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,8,button08))
button09 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(0,9,button09))
button10 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,0,button10))
button11 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,1,button11))
button12 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,2,button12))
button13 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,3,button13))
button14 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,4,button14))
button15 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,5,button15))
button16 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,6,button16))
button17 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,7,button17))
button18 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,8,button18))
button19 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(1,9,button19))
button20 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,0,button20))
button21 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,1,button21))
button22 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,2,button22))
button23 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,3,button23))
button24 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,4,button24))
button25 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,5,button25))
button26 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,6,button26))
button27 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,7,button27))
button28 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,8,button28))
button29 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(2,9,button29))
button30 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,0,button30))
button31 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,1,button31))
button32 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,2,button32))
button33 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,3,button33))
button34 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,4,button34))
button35 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,5,button35))
button36 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,6,button36))
button37 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,7,button37))
button38 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,8,button38))
button39 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(3,9,button39))
button40 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,0,button40))
button41 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,1,button41))
button42 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,2,button42))
button43 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,3,button43))
button44 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,4,button44))
button45 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,5,button45))
button46 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,6,button46))
button47 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,7,button47))
button48 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,8,button48))
button49 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(4,9,button49))
button50 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,0,button50))
button51 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,1,button51))
button52 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,2,button52))
button53 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,3,button53))
button54 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,4,button54))
button55 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,5,button55))
button56 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,6,button56))
button57 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,7,button57))
button58 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,8,button58))
button59 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(5,9,button59))
button60 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,0,button60))
button61 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,1,button61))
button62 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,2,button62))
button63 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,3,button63))
button64 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,4,button64))
button65 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,5,button65))
button66 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,6,button66))
button67 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,7,button67))
button68 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,8,button68))
button69 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(6,9,button69))
button70 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,0,button70))
button71 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,1,button71))
button72 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,2,button72))
button73 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,3,button73))
button74 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,4,button74))
button75 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,5,button75))
button76 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,6,button76))
button77 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,7,button77))
button78 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,8,button78))
button79 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(7,9,button79))
button80 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,0,button80))
button81 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,1,button81))
button82 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,2,button82))
button83 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,3,button83))
button84 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,4,button84))
button85 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,5,button85))
button86 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,6,button86))
button87 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,7,button87))
button88 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,8,button88))
button89 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(8,9,button89))
button90 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,0,button90))
button91 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,1,button91))
button92 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,2,button92))
button93 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,3,button93))
button94 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,4,button94))
button95 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,5,button95))
button96 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,6,button96))
button97 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,7,button97))
button98 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,8,button98))
button99 = tkinter.Button(root,background = 'blue', height = 1, width = 2, command = lambda : battleship(9,9,button99))
button00.grid(row=0, column =0)
button01.grid(row=0, column =1)
button02.grid(row=0, column =2)
button03.grid(row=0, column =3)
button04.grid(row=0, column =4)
button05.grid(row=0, column =5)
button06.grid(row=0, column =6)
button07.grid(row=0, column =7)
button08.grid(row=0, column =8)
button09.grid(row=0, column =9)
button10.grid(row=1, column =0)
button11.grid(row=1, column =1)
button12.grid(row=1, column =2)
button13.grid(row=1, column =3)
button14.grid(row=1, column =4)
button15.grid(row=1, column =5)
button16.grid(row=1, column =6)
button17.grid(row=1, column =7)
button18.grid(row=1, column =8)
button19.grid(row=1, column =9)
button20.grid(row=2, column =0)
button21.grid(row=2, column =1)
button22.grid(row=2, column =2)
button23.grid(row=2, column =3)
button24.grid(row=2, column =4)
button25.grid(row=2, column =5)
button26.grid(row=2, column =6)
button27.grid(row=2, column =7)
button28.grid(row=2, column =8)
button29.grid(row=2, column =9)
button30.grid(row=3, column =0)
button31.grid(row=3, column =1)
button32.grid(row=3, column =2)
button33.grid(row=3, column =3)
button34.grid(row=3, column =4)
button35.grid(row=3, column =5)
button36.grid(row=3, column =6)
button37.grid(row=3, column =7)
button38.grid(row=3, column =8)
button39.grid(row=3, column =9)
button40.grid(row=4, column =0)
button41.grid(row=4, column =1)
button42.grid(row=4, column =2)
button43.grid(row=4, column =3)
button44.grid(row=4, column =4)
button45.grid(row=4, column =5)
button46.grid(row=4, column =6)
button47.grid(row=4, column =7)
button48.grid(row=4, column =8)
button49.grid(row=4, column =9)
button50.grid(row=5, column =0)
button51.grid(row=5, column =1)
button52.grid(row=5, column =2)
button53.grid(row=5, column =3)
button54.grid(row=5, column =4)
button55.grid(row=5, column =5)
button56.grid(row=5, column =6)
button57.grid(row=5, column =7)
button58.grid(row=5, column =8)
button59.grid(row=5, column =9)
button60.grid(row=6, column =0)
button61.grid(row=6, column =1)
button62.grid(row=6, column =2)
button63.grid(row=6, column =3)
button64.grid(row=6, column =4)
button65.grid(row=6, column =5)
button66.grid(row=6, column =6)
button67.grid(row=6, column =7)
button68.grid(row=6, column =8)
button69.grid(row=6, column =9)
button70.grid(row=7, column =0)
button71.grid(row=7, column =1)
button72.grid(row=7, column =2)
button73.grid(row=7, column =3)
button74.grid(row=7, column =4)
button75.grid(row=7, column =5)
button76.grid(row=7, column =6)
button77.grid(row=7, column =7)
button78.grid(row=7, column =8)
button79.grid(row=7, column =9)
button80.grid(row=8, column =0)
button81.grid(row=8, column =1)
button82.grid(row=8, column =2)
button83.grid(row=8, column =3)
button84.grid(row=8, column =4)
button85.grid(row=8, column =5)
button86.grid(row=8, column =6)
button87.grid(row=8, column =7)
button88.grid(row=8, column =8)
button89.grid(row=8, column =9)
button90.grid(row=9, column =0)
button91.grid(row=9, column =1)
button92.grid(row=9, column =2)
button93.grid(row=9, column =3)
button94.grid(row=9, column =4)
button95.grid(row=9, column =5)
button96.grid(row=9, column =6)
button97.grid(row=9, column =7)
button98.grid(row=9, column =8)
button99.grid(row=9, column =9)
root.mainloop()
if turns > 30:
    print("YOU LOSE!")
