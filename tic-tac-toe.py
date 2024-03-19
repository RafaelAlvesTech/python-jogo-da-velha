
player1 = "X"
player2 = "O"

board = [["__", "|__", "|__"],
         ["__", "|__", "|__"],
         ["  ", "|  ", "|  "]]  # Fixed empty spaces in the board representation

def board_view():
    for row in board:  # Simplified loop for board printing
        print("".join(row))

def position_occupied(position):  # Renamed function to follow PEP8 naming conventions
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    row, col = positions[position]
    return board[row][col] != "__" and board[row][col] != "  "  # Adjusted condition

def make_move(player):
    while True:  # Keep asking for input until a valid move is made
        try:
            position = int(input(f"Player {player}, enter your position (1-9): "))
            if 1 <= position <= 9:
                if not position_occupied(position):
                    positions = {
                        1: (0, 0), 2: (0, 1), 3: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2),
                        7: (2, 0), 8: (2, 1), 9: (2, 2)
                    }
                    row, col = positions[position]
                    board[row][col] = player
                    break  # Exit the loop if the move is valid
                else:
                    print("Position already occupied!")
            else:
                print("Invalid position! Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def check_winner():
    for i in range(3):  # Check rows and columns for a win
        if board[i][0] == board[i][1] == board[i][2] != "__":
            return board[i][0]  # Return the winning player
        if board[0][i] == board[1][i] == board[2][i] != "__":
            return board[0][i]  # Return the winning player

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != "__":
        return board[0][0]  # Return the winning player
    if board[0][2] == board[1][1] == board[2][0] != "__":
        return board[0][2]  # Return the winning player

    return None  # Return None if no winner


def check_draw():
    for row in board:
        for cell in row:
            if cell == "__" or cell == "  ":
                return False  # Game is not a draw if there are empty cells
    return True  # Otherwise, it's a draw


def tic_tac_toe():
    player = player1  # Start with player 1
    while True:
        board_view()
        make_move(player)
        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break
        player = player2 if player == player1 else player1  # Switch players


if __name__ == "__main__":
    tic_tac_toe()