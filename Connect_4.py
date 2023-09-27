row5 = [' ',' ',' ',' ',' ',' ',' ']
row4 = [' ',' ',' ',' ',' ',' ',' ']
row3 = [' ',' ',' ',' ',' ',' ',' ']
row2 = [' ',' ',' ',' ',' ',' ',' ']
row1 = [' ',' ',' ',' ',' ',' ',' ']
row0 = [' ',' ',' ',' ',' ',' ',' ']
map = [row0,row1,row2,row3,row4,row5] #This map represents the how the game would look in real life
done = False 
game_over = False #When this is true the game ends
player1_go = True #This boolean is used to switch between player 1s go and player 2s go
player1_chip = ""
player2_chip = "" #sets the variable type for these variables so there isnt a confusion with data types
column_choice = 0 #same as before with setting variable types
player1_chip = input("""Player 1, would you like to be "X" or "O"?: """) #sets the players 'chips'
if player1_chip == "X":
    player2_chip = "O"
else:
    player2_chip = "X"
while game_over != True: #Main game loop
    for x in range(0,7): #prints the 'game board' so to speak
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
    if player1_go == True: #if player 1s go is true he or she can place there chip in a column of their choice
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
                    map[2][column_choice] = player1_chip #this algorythm mimics how the chip would fall in real life, it checks for each level if the ->
                    map[3][column_choice] = ' '          #-> space below is free, if it is the chip is placed and the one above chances to empty ->
                    if map[1][column_choice] == ' ':     #-> (mimics motion of a falling chip)
                        map[1][column_choice] = player1_chip
                        map[2][column_choice] = ' '
                        if map[0][column_choice] == ' ':
                            map[0][column_choice] = player1_chip
                            map[1][column_choice] = ' '
        player1_go = False
    else:
        while done != True:
            column_choice = int(input("Player 2, which row do you choose?: "))
            if map[5][column_choice] != ' ': # checks if the top of the board is full (cant put any more in)
                print("This stack is full!")
            else:
                done = True
        done = False
        map[5][column_choice] = player2_chip #same thing happens if its player 2s go
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
    for y in range(0,6): #BIG checking algorythm
        for x in range(0,4):#This one checks horizontaly
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
    for y in range(0,3): # checks vertically
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
    for y in range(0,3): #checks diagonally with a positive gradient
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
    for y in range(0,6): # checks diagonally with a negative gradient
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
for x in range(0,7): #Displays the end result once a game over is detected
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
