row5 = [' ',' ',' ',' ',' ',' ',' ']
row4 = [' ',' ',' ',' ',' ',' ',' ']
row3 = [' ',' ',' ',' ',' ',' ',' ']
row2 = [' ',' ',' ',' ',' ',' ',' ']
row1 = [' ',' ',' ',' ',' ',' ',' ']
row0 = [' ',' ',' ',' ',' ',' ',' ']
map = [row0,row1,row2,row3,row4,row5]
done = False
game_over = False
player1_go = True
player1_chip = ""
player2_chip = ""
column_choice = 0
player1_chip = input("""Player 1, would you like to be "X" or "O"?: """)
if player1_chip == "X":
    player2_chip = "O"
else:
    player2_chip = "X"
while game_over != True:
    for x in range(0,7):
        if x == 6:
            print(f"  {x}\n")
        else:
            print(f"  {x}",end="  ")
    for x in range(0,7):
        if x == 6:
            print(f"  |\n")
        else:
            print(f"  |",end="  ")
    for x in range(0,7):
        if x == 6:
            print(f"  \/\n")
        else:
            print(f"  \/",end=" ")
    for x in range(len(map),0,-1):
        print(f"{map[x-1]}\n")
    if player1_go == True:
        while done != True:
            column_choice = int(input("Player 1, which row do you choose?: "))
            if map[5][column_choice] != ' ':
                print("This stack is full!")
            else:
                done = True
        done = False
        map[5][column_choice] = player1_chip
        if map[4][column_choice] == ' ':
            map[4][column_choice] = player1_chip
            map[5][column_choice] = ' '
            if map[3][column_choice] == ' ':
                map[3][column_choice] = player1_chip
                map[4][column_choice] = ' '
                if map[2][column_choice] == ' ':
                    map[2][column_choice] = player1_chip
                    map[3][column_choice] = ' '
                    if map[1][column_choice] == ' ':
                        map[1][column_choice] = player1_chip
                        map[2][column_choice] = ' '
                        if map[0][column_choice] == ' ':
                            map[0][column_choice] = player1_chip
                            map[1][column_choice] = ' '
        player1_go = False
    else:
        while done != True:
            column_choice = int(input("Player 2, which row do you choose?: "))
            if map[5][column_choice] != ' ':
                print("This stack is full!")
            else:
                done = True
        done = False
        map[5][column_choice] = player2_chip
        if map[4][column_choice] == ' ':
            map[4][column_choice] = player2_chip
            map[5][column_choice] = ' '
            if map[3][column_choice] == ' ':
                map[3][column_choice] = player2_chip
                map[4][column_choice] = ' '
                if map[2][column_choice] == ' ':
                    map[2][column_choice] = player2_chip
                    map[3][column_choice] = ' '
                    if map[1][column_choice] == ' ':
                        map[1][column_choice] = player2_chip
                        map[2][column_choice] = ' '
                        if map[0][column_choice] == ' ':
                            map[0][column_choice] = player2_chip
                            map[1][column_choice] = ' '
        player1_go = True
    for y in range(0,6):
        for x in range(0,4):
            if map[y][x] == "X":
                if map[y][x+1] == "X":
                    if map[y][x+2] == "X":
                        if map[y][x+3] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "X":
                                print("Player 2 wins!")   
                                game_over= True                           
            elif map[y][x] == "O":
                if map[y][x+1] == "O":
                    if map[y][x+2] == "O":
                        if map[y][x+3] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over= True
    for y in range(0,3):
        for x in range(0,7):
            if map[y][x] == "X":
                if map[y+1][x] == "X":
                    if map[y+2][x] == "X":
                        if map[y+3][x] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "X":
                                print("Player 2 wins!") 
                                game_over= True                               
            elif map[y][x] == "O":
                if map[y+1][x] == "O":
                    if map[y+2][x] == "O":
                        if map[y+3][x] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over= True
    for y in range(0,3):
        for x in range(0,4):
                if map[y][x] == "X":
                    if map[y+1][x+1] == "X":
                        if map[y+2][x+2] == "X":
                            if map[y+3][x+3] == "X":
                                if player1_chip == "X":
                                    print("Player 1 wins!")
                                    game_over= True
                                elif player2_chip == "X":
                                    print("Player 2 wins!")
                                    game_over= True
                elif map[y][x] == "O":
                    if map[y+1][x+1] == "O":
                        if map[y+2][x+2] == "O":
                            if map[y+3][x+3] == "O":
                                if player1_chip == "O":
                                    print("Player 1 wins!")
                                    game_over= True
                                elif player2_chip == "O":
                                    print("Player 2 wins!")
                                    game_over= True
    for y in range(0,6):
        for x in range(0,4):
            if map[y][x] == "X":
                if map[y-1][x+1] == "X":
                    if map[y-2][x+2] == "X":
                        if map[y-3][x+3] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "X":
                                print("Player 2 wins!")
                                game_over= True
            elif map[y][x] == "O":
                if map[y-1][x+1] == "O":
                    if map[y-2][x+2] == "O":
                        if map[y-3][x+3] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over= True
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over= True
for x in range(0,7):
    if x == 6:
        print(f"  {x}\n")
    else:
        print(f"  {x}",end="  ")
for x in range(0,7):
    if x == 6:
        print(f"  |\n")
    else:
        print(f"  |",end="  ")
for x in range(0,7):
    if x == 6:
        print(f"  \/\n")
    else:
        print(f"  \/",end=" ")
for x in range(len(map),0,-1):
    print(f"{map[x-1]}\n")