import numpy as np
import random
from time import sleep

# Constants for players
PLAYER_X = 1
PLAYER_O = 2
EMPTY = 0


# Creates an empty board
def create_board():
    return np.array([[EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY]])


# Check for empty places on board
def possibilities(board):
    return [(i, j) for i in range(len(board)) 
            for j in range(len(board)) if board[i][j] == EMPTY]


# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    if selection:  # Check if there are any possible moves
        current_loc = random.choice(selection)
        board[current_loc] = player
    return board


# Checks whether the player has three of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        if all(board[x, y] == player for y in range(len(board))):
            return True
    return False


# Checks whether the player has three of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        if all(board[y][x] == player for y in range(len(board))):
            return True
    return False


# Checks whether the player has three of their marks in a diagonal row
def diag_win(board, player):
    if all(board[i, i] == player for i in range(len(board))) or \
       all(board[i, len(board) - 1 - i] == player for i in range(len(board))):
        return True
    return False


# Evaluates whether there is a winner or a tie
def evaluate(board):
    for player in [PLAYER_X, PLAYER_O]:
        if row_win(board, player) or col_win(board, player)or diag_win(board, player):
            return player
    if np.all(board != EMPTY):
        return -1  # Tie
    return 0  # No winner yet


# Main function to start the game
def play_game():
    board = create_board()
    winner = 0
    counter = 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [PLAYER_X, PLAYER_O]:
            board = random_place(board, player)
            print(f"Board after {counter} move:")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


# Driver Code
winner = play_game()
if winner == -1:
    print("The game is a tie!")
else:
    print(f"The winner is: Player {winner}")


