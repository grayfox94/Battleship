def battleship():
    import random
    c1 = [0,0]
    c2 = [0,0]
    board = [c1,c2]
    x = random.randrange(2)
    y = random.randrange(2)
    board[x][y] = 1
    #print(x,y)
    column = int(input("enter which column you think it resides. enter 0 or 1."))            
    hello = int(input("enter which row you think it resides. enter 0 or 1"))
    
    if board[column][hello] == 1 :
                 print("YOU WIN!")
                 
    elif board[column][hello] == 0:
                 print("You Lose.")
                 print("It was here.")
                 print(x,y)
                
