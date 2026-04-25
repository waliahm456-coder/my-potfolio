import time as tm

grid = [["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],]

def a():
    if current_player == "Player 1":
        grid[aplace][0] = symbol1
    else:
        grid[aplace][0] = symbol2

def s():
    if current_player == "Player 1":
        grid[splace][1] = symbol1
    else:
        grid[splace][1] = symbol2

def d():
    if current_player == "Player 1":
        grid[dplace][2] = symbol1
    else:
        grid[dplace][2] = symbol2

def f():
    if current_player == "Player 1":
        grid[fplace][3] = symbol1
    else:
        grid[fplace][3] = symbol2

def g():
    if current_player == "Player 1":
        grid[gplace][4] = symbol1
    else:
        grid[gplace][4] = symbol2

def h():
    if current_player == "Player 1":
        grid[hplace][5] = symbol1
    else:
        grid[hplace][5] = symbol2

def jm():
    if current_player == "Player 1":
        grid[jplace][6] = symbol1
    else:
        grid[jplace][6] = symbol2


def display():
    # Determine the maximum width needed for each cell content.
    # Here all items are single-digit integers, so a width of 1 is sufficient.
    cell_width = 1 
    num_cols = len(grid[0])
    
    # Create the horizontal border line, e.g., "+---+---+---+"
    border_line = "+" + "+".join(["-" * (cell_width + 2)] * num_cols) + "+"

    print(border_line)
    for row in grid:
        # Format each cell with padding and vertical separators
        row_str = "| " + " | ".join(str(x).center(cell_width) for x in row) + " |"
        print(row_str)
        print(border_line)

def wins():
    display()
    print("--------------")
    print(current_player,"won!")
    print("--------------")

def outside():
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    print("Move outside the Board")
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    tm.sleep(1)

#Initialisation
aplace = 5
splace = 5
dplace = 5
fplace = 5
gplace = 5
hplace = 5
jplace = 5
win = False
turns = 1
symbolized = False

    
while not win:
    turned = True
    #Checking player turn
    if turns%2 == 1:
        current_player = "Player 1"
    else:
        current_player = "Player 2"
    
    #Game Prompt
    print("+---+---+---+---+---+---+---+")
    print("| A | S | D | F | G | H | J |")
    print("+---+---+---+---+---+---+---+")
    print()
    display()
    print("----------------------------------------")
    print("Your move will follow rules of GRAVITY!!")
    print("----------------------------------------")

    #Input validation
    while not symbolized:
        symbol1 = input("Player 1: Enter your symbol: ")
        symbol2 = input("Player 2: Enter your symbol: ")
        while symbol1 == symbol2:
            print("Same Symbol selected by both players!")
            symbol1 = input("Player 1: Enter your symbol: ")
            symbol2 = input("Player 2: Enter your symbol: ")
        symbolized = True
    print("    ----    ")
    print(current_player, "Turn")
    print("    ----    ")
    move = input("Enter move ( a, s, d, f, g, h, j): ").lower()
    while move != "a" and move != "s" and move != "d" and move != "f" and move != "g" and move != "h" and move != "j":
        print("!!!!!!!!!!!!!!!!")
        print(" Invalid Move")
        print("!!!!!!!!!!!!!!!!")
        move = input("Enter move ( a, s, f, g, h, j): ").lower()

   

    print()
    print("---------------------")
    print()

    #Moves action
    if move.lower() == "a":
        if aplace > -1:
            a()
            aplace = aplace - 1
        else:
            outside()
            turned = False

    if move.lower() == "s":
        if splace > -1:
            s()
            splace = splace - 1
        else:
            outside()
            turned = False

    if move.lower() == "d":
        if dplace > -1:
            d()
            dplace = dplace - 1
        else:
            outside()
            turned = False

    if move.lower() == "f":
        if fplace > -1:
            f()
            fplace = fplace - 1
        else:
            outside()
            turned = False

    if move.lower() == "g":
        if gplace > -1:
            g()
            gplace = gplace - 1
        else:
            outside()
            turned = False

    if move.lower() == "h":
        if hplace > -1:
            h()
            hplace = hplace - 1
        else:
            outside()
            turned = False

    if move.lower() == "j":
        if jplace > -1:
            jm()
            jplace = jplace - 1
        else:
            outside()
            turned = False

    #Check winning
    #lines
    players = [symbol1, symbol2]
    loops = [3, 2, 1, 0]
    for n in players:
        #horizontals
        for j in range(5, -1, -1):
            for i in range(4):
                    if grid[j][i] == n and grid[j][i+1] == n and grid[j][i+2] == n and grid[j][i+3] == n:
                        wins()
                        win = True 

        #verticles
        for j in range(6, -1, -1):
            for i in range(3):
                if grid[i][j] == n and grid[i+1][j] == n and grid[i+2][j] == n and grid[i+3][j] == n:  
                        wins()
                        win = True 
        # #daigonals
        # #ones
        # #up
        # #positives
        # if grid[3][0] == n and grid[2][1] == n and grid[1][2] == n and grid[0][3] == n:
        #     wins()
        #     win = True

        # #negatives
        # if grid[0][3] == n and grid[1][4] == n and grid[2][5] == n and grid[3][6] == n:
        #     wins()
        #     win = True

        # #down
        # #positives
        # if grid[5][3] == n and grid[4][4] == n and grid[3][5] == n and grid[2][6] == n:
        #     wins()
        #     win = True

        # #negatives
        # if grid[5][3] == n and grid[4][2] == n and grid[3][1] == n and grid[2][0] == n:
        #     wins()
        #     win = True

        # #twos
        # #up
        # for j in range(4, 2, -1):
        #     for i in range(2):
        #         if grid[j][i] == n and grid[j-1][i+1] == n and grid[j-2][i+2] == n and grid[j-3][i+3] == n:
        #             wins()
        #             win = True 
                
        # #down
        # for j in range(5, 3, -1):
        #     for i in range(2, 4):
        #         if grid[j][i] == n and grid[j-1][i+1] == n and grid[j-2][i+2] == n and grid[j-3][i+3] == n:
        #             wins()
        #             win = True
            
        # #threes
        # for x in range(2):
        #     for i in range(3):
        #         if grid[5][i+x] == n and grid[4][i+1+x] == n and grid[3][i+2+x] == n and grid[2][i+3+x] == n:
        #             wins()
        #             win = True

        # diagonals (complete, same style as yours)

        # up-right (start rows 5,4,3 ; cols 0..3)
        for r in range(5, 2, -1):        # r = 5,4,3
            for c in range(0, 4):       # c = 0,1,2,3
                if grid[r][c] == n and grid[r-1][c+1] == n and grid[r-2][c+2] == n and grid[r-3][c+3] == n:
                    wins()
                    win = True

        # down-right (start rows 0,1,2 ; cols 0..3)
        for r in range(0, 3):            # r = 0,1,2
            for c in range(0, 4):       # c = 0,1,2,3
                if grid[r][c] == n and grid[r+1][c+1] == n and grid[r+2][c+2] == n and grid[r+3][c+3] == n:
                    wins()
                    win = True

        # up-left (start rows 5,4,3 ; cols 3..6)
        for r in range(5, 2, -1):        # r = 5,4,3
            for c in range(3, 7):       # c = 3,4,5,6
                if grid[r][c] == n and grid[r-1][c-1] == n and grid[r-2][c-2] == n and grid[r-3][c-3] == n:
                    wins()
                    win = True

        # down-left (start rows 0,1,2 ; cols 3..6)
        for r in range(0, 3):            # r = 0,1,2
            for c in range(3, 7):       # c = 3,4,5,6
                if grid[r][c] == n and grid[r+1][c-1] == n and grid[r+2][c-2] == n and grid[r+3][c-3] == n:
                    wins()
                    win = True



    if turned:
        turns +=1    