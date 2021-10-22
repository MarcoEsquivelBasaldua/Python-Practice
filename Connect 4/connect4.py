"""
Python is easy

Author: Marco Antonio Esquivel Basaldua
Project: 1
Date: 3/2/2021

Code Description:
    This code executes CONNECT 4 game
    Player 1 is represented as X
    Player 2 is represented as O
    Each player's turn is anounced on terminal
    Columns are enumerated from 0 to 6 from left to right

    Code crashes if the entered number is otside [0,6]
    code does not considers the cases where a player attempts to make a move on an already full column
"""
board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def draw_board():
    for i_ in range(12):
        if i_%2 == 0:
            i = i_//2
            for j in range(7):
                if board[i][j] == 0 and j<6:
                    print(' ', end='|')
                elif board[i][j] == 0 and j==6:
                    print(' ')
                elif board[i][j] == 1 and j<6:
                    print('X', end='|')
                elif board[i][j] == 1 and j==6:
                    print('X')
                elif board[i][j] == 2 and j<6:
                    print('O', end='|')
                elif board[i][j] == 2 and j==6:
                    print('O')
            
        else:
            print('-'*13)



def check_winner():
    #check by rows
    for i in range(6):
        player1 = 0
        player2 = 0
        for j in range(7):
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2

    #check by cols
    for j in range(7):
        player1 = 0
        player2 = 0
        for i in range(6):
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2

    #check by \ diagonals
    for i in range(3):
        j = 0

        player1 = 0
        player2 = 0
        while i < 6 and j < 7:
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2
            
            i += 1
            j += 1

    for j in range(4):
        i = 0

        player1 = 0
        player2 = 0
        while i < 6 and j < 7:
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2
            
            i += 1
            j += 1

    #check by / diagonals
    for i in range(3):
        j = 6

        player1 = 0
        player2 = 0
        while i < 6 and j > 0:
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2
            
            i += 1
            j -= 1

    for j in range(6,-1,2):
        i = 0

        player1 = 0
        player2 = 0
        while i < 6 and j > 0:
            if board[i][j] == 1:
                player1 +=1
                player2 = 0
            elif board[i][j] == 2:
                player1 = 0
                player2 +=1
            else:
                player1 = 0
                player2 = 0
            
            if player1 == 4:
                return True, 1
            elif player2 == 4:
                return True, 2
            
            i += 1
            j -= 1
    
    return False, 0

winner = 0
win = False
while True:
    print('Player 1 moves')
    col = int(input('Enter chosen column '))
    
    i = 0
    for j in range(6):
        i = j
        if board[j][col] != 0:
            break
        if j == 5:
            i = 6

    i -=1
    board[i][col] = 1
    draw_board()

    win, winner = check_winner()
    if win:
        break

    print('Player 2 moves')
    col = int(input('Enter chosen column '))
    
    i = 0
    for j in range(6):
        i = j
        if board[j][col] != 0:
            break
        if j == 5:
            i = 6

    i -=1
    board[i][col] = 2
    draw_board()

    win, winner = check_winner()
    if win:
        break

print('Winner is player',winner)