row5 = [' ',' ',' ',' ',' ',' ',' ']
row4 = [' ',' ',' ',' ',' ',' ',' ']
row3 = [' ',' ',' ',' ',' ',' ',' ']
row2 = [' ',' ',' ',' ',' ',' ',' ']
row1 = [' ',' ',' ',' ',' ',' ',' ']
row0 = [' ',' ',' ',' ',' ',' ',' ']
map = [row0,row1,row2,row3,row4,row5]

def display_board(map):
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
    for x in range(0,len(map)):
        print(f"{map[x]}\n")

def get_player1_chip():
    player1_chip = input("""Player 1, would you like to be "X" or "O"?: """)
    return player1_chip

def get_player2_chip(player1_chip):
    player2_chip = ""
    if player1_chip == "X":
        player2_chip = "O"
    else:
        player2_chip = "X"
    return player2_chip

def check_board_flat(map,player1_chip,player2_chip,game_over):
    for y in range(0,6):
        for x in range(0,4):
            if map[y][x] == "X":
                if map[y][x+1] == "X":
                    if map[y][x+2] == "X":
                        if map[y][x+3] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "X":
                                print("Player 2 wins!")       
                                game_over = True   
                                break                          
            elif map[y][x] == "O":
                if map[y][x+1] == "O":
                    if map[y][x+2] == "O":
                        if map[y][x+3] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over = True
                                break

def check_board_vert(map,player1_chip,player2_chip,game_over):
    for y in range(0,3):
        for x in range(0,7):
            if map[y][x] == "X":
                if map[y+1][x] == "X":
                    if map[y+2][x] == "X":
                        if map[y+3][x] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "X":
                                print("Player 2 wins!")
                                game_over = True   
                                break                                 
            elif map[y][x] == "O":
                if map[y+1][x] == "O":
                    if map[y+2][x] == "O":
                        if map[y+3][x] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over = True
                                break

def check_board_diag_positive(map,player1_chip,player2_chip,game_over):
    for y in range(0,3):
        for x in range(0,4):
                if map[y][x] == "X":
                    if map[y+1][x+1] == "X":
                        if map[y+2][x+2] == "X":
                            if map[y+3][x+3] == "X":
                                if player1_chip == "X":
                                    print("Player 1 wins!")
                                    game_over = True
                                    break
                                elif player2_chip == "X":
                                    print("Player 2 wins!")
                                    game_over = True
                                    break
                elif map[y][x] == "O":
                    if map[y+1][x+1] == "O":
                        if map[y+2][x+2] == "O":
                            if map[y+3][x+3] == "O":
                                if player1_chip == "O":
                                    print("Player 1 wins!")
                                    game_over = True
                                    break
                                elif player2_chip == "O":
                                    print("Player 2 wins!")
                                    game_over = True
                                    break

def check_board_diag_negative(map,player1_chip,player2_chip,game_over):
    for y in range(0,6):
        for x in range(0,4):
            if map[y][x] == "X":
                if map[y-1][x+1] == "X":
                    if map[y-2][x+2] == "X":
                        if map[y-3][x+3] == "X":
                            if player1_chip == "X":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "X":
                                print("Player 2 wins!")
                                game_over = True
                                break
            elif map[y][x] == "O":
                if map[y-1][x+1] == "O":
                    if map[y-2][x+2] == "O":
                        if map[y-3][x+3] == "O":
                            if player1_chip == "O":
                                print("Player 1 wins!")
                                game_over = True
                                break
                            elif player2_chip == "O":
                                print("Player 2 wins!")
                                game_over = True
                                break

def check_routine(map,player1_chip,player2_chip,game_over):
    check_board_flat(map,player1_chip,player2_chip,game_over)
    check_board_diag_positive(map,player1_chip,player2_chip,game_over)
    check_board_diag_negative(map,player1_chip,player2_chip,game_over)


def place_chip(map,player1_chip,player2_chip,player1s_go):
    if player1s_go == True:
        while player1s_go == True:
            temp0 = int(input("Player1, which row would you like to place a chip in?: "))
            if map[5][temp0] == 'X':
                print("This column is already full!")
            elif map[5][temp0] == 'O':
                print("This column is already full!")
            else:
                map[5][temp0] = player1_chip
                player1s_go = False

            for y in range(5,0):
                if map[y-1][temp0] == '':
                    map[y-1][temp0] = player1_chip
                else:
                    return player1s_go
                    break
    elif player1s_go == False:
        temp0 = 0
        while player1s_go == False:
            temp0 = int(input("Player2, which row would you like to place a chip in?: "))
            if map[5][temp0] == 'X':
                print("This column is already full!")
            elif map[5][temp0] == 'O':
                print("This column is already full!")
            else:
                map[5][temp0] = player2_chip
                player1s_go = True

        for y in range(5,0):
            if map[y-1][temp0] == '':
                map[y-1][temp0] = player2_chip
                map[y][temp0] = ''
            else:
                break

def main():
    player1s_go = True
    game_over = False

    player1_chip = get_player1_chip()
    player2_chip = get_player2_chip(player1_chip)

    while game_over == False:
        display_board(map)
        place_chip(map, player1_chip,player2_chip,player1s_go)
        check_routine(map,player1_chip,player2_chip,game_over)
    
if __name__ == "__main__":
    main()