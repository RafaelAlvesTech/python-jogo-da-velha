"""
Traditional Tic-Tac-Toe in Python

The Exercise for Educational Purposes

Knowledge that can be applied: Algorithms,
input, data processing and output, use of variables,
use of conditional structures if else, repetition structures and functions.
Possible Results:

1. Winner
2. Draw

Steps:
1. Start new game
2. Show the board and instructions. X or o save option to player 1 and player 2. 
3 . Board 3x3 vertical array A, B, C and horizontal 1, 2, 3.
while !winner or !draw:
4. Get player 2 input id vertical and horizontal. Check valide ocuppied position and valide input.
5. Get player 2 input id vertical and horizontal. Check valide ocuppied position and valide input.

6. Check if there is a winner or draw.

7. Funciton for board print


------------------------------------------------

8*. Adiconal features: Game mode, player vs player, player vs computer, computer vs computer.
9*. Adiconal features: Score board, player 1 vs player 2.
10*. Adiconal features: Make logical with object oriented programming.
11.* Make Minimum Big  O notation for the algorithm.
.
"""


from numpy import void


player1 = "X"
player2 = "O"

board = [["__", "|__", "|__"],
             ["__", "|__", "|__"],
             [" ", "|  ", "|  "]]

def board_view() -> bool:
    contador = 0
    for i in range(len(board)):
        for j in range(len(board)):
            contador += 1
            print(board[i][j], end="")
            if contador >= 3:
                print(" \n ")
                contador = 0
                return True
            else:
                print(" | ", end="")
    return False

def postion_ocupped(position1: int) -> bool:
    if position1 == 1:
        if board[0][0] != "__":
            return True
    elif position1 == 2:
        if board[0][1] != "__":
            return True
    elif position1 == 3:
        if board[0][2] != "__":
            return True
    elif position1 == 4:
        if board[1][0] != "__":
            return True
    elif position1 == 5:
        if board[1][1] != "__":
            return True
    elif position1 == 6:
        if board[1][2] != "__":
            return True
    elif position1 == 7:
        if board[2][0] != " ":
            return True
    elif position1 == 8:
        if board[2][1] != " ":
            return True
    elif position1 == 9:
        if board[2][2] != " ":
            return True

    else:
        return False

def make_move(player: str, position: int )-> bool:
    player = input("Input ""X"" or ""O"" :")
    if player == "X":
        player = player1
    elif player == "O":
        player = player2
    else:
        print("Invalid input")
        return False
    print(board_view())
    position = input(int("Enter the player1 postion docuped : "))
    if position == 1 and not postion_ocupped(position):
        board[0][0] += player
    elif position == 2 and not postion_ocupped(position):
        board[0][1] += player
    elif position == 3  and not postion_ocupped(position):
        board[0][2] += player
    elif position == 4 and not postion_ocupped(position):
        board[1][0] += player
    elif position == 5  and not postion_ocupped(position):
        board[1][1] += player
    elif position == 6  and not postion_ocupped(position):
        board[1][2] += player
    elif position == 7 and not postion_ocupped(position):
        board[2][0] += player
    elif position == 8 and not postion_ocupped(position):
        board[2][1] += player
    elif position == 9  and not postion_ocupped(position):
        board[2][2] += player
    else:
        print("Invalid position")
        return False
    print(board_view())
    return True

def winner_or_draw():
 if "x" in board[0][0] and board[0][1] and board[0][2]:
         print("The player1 is winner")
 elif "x" in board[0][0] and board[0][1] and board[0][2]:
         print("The player1 is winner")
 elif "x" in board[1][0] and board[1][1] and board[1][2]:
            print("The player1 is winner")
 elif "x" in board[2][0] and board[2][1] and board[2][2]:
        print("The player1 is winner")
 elif "x" in board[0][0] and board[1][0] and board[2][0]:
            print("The player1 is winner")
 elif "x" in board[0][1] and board[1][1] and board[2][1]:
            print("The player1 is winner")
 elif "x" in board[0][2] and board[1][2] and board[2][2]:
            print("The player1 is winner")
 elif "x" in board[0][0] and board[1][1] and board[2][2]:
            print("The player1 is winner")
 elif "x" in board[0][2] and board[1][1] and board[2][0]:
            print("The player1 is winner")
 elif "o" in board[0][0] and board[0][1] and board[0][2]:
            print("The player2 is winner")
 elif "o" in board[0][0] and board[0][1] and board[0][2]:
            print("The player2 is winner")
 elif "o" in board[1][0] and board[1][1] and board[1][2]:
            print("The player2 is winner")
 elif "o" in board[2][0] and board[2][1] and board[2][2]:
            print("The player2 is winner")
 elif "o" in board[0][0] and board[1][0] and board[2][0]:
            print("The player2 is winner")
 elif "o" in board[0][1] and board[1][1] and board[2][1]:
            print("The player2 is winner")
 elif "o" in board[0][2] and board[1][2] and board[2][2]:
            print("The player2 is winner")
 elif "o" in board[0][0] and board[1][1] and board[2][2]:
            print("The player2 is winner")
 elif "o" in board[0][2] and board[1][1] and board[2][0]:
            print("The player2 is winner")







"""
 Table winner
player1 = board[0][0] and board[0][1] and board[0][2] 
player2 = board[0][0] and board[0][1] and board[0][2]
player1 = board[1][0] and board[1][1] and board[1][2] 
player2 = board[1][0] and board[1][1] and board[1][2]
player1 = board[2][0] and board[2][1] and board[2][2] 
player2 = board[2][0] and board[2][1] and board[2][2]
player1 = board[0][0] and board[1][0] and board[2][0]
player2 = board[0][0] and board[1][0] and board[2][0]
player1 = board[0][1] and board[1][1] and board[2][1]
player2 = board[0][1] and board[1][1] and board[2][1]
player1 = board[0][2] and board[1][2] and board[2][2]
player2 = board[0][2] and board[1][2] and board[2][2]
player1 = board[0][0] and board[1][1] and board[2][2]
player2 = board[0][0] and board[1][1] and board[2][2]
player1 = board[0][2] and board[1][1] and board[2][0]
player2 = board[0][2] and board[1][1] and board[2][0]
 """