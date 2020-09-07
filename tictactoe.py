""" Quick game I designed to allow you to play tic tac toe against your computer. The project goal was to use a minimax function and alpha-beta pruning to teach the computer how to play both optimally and quickly."""

import util as util
import time

X = "X"
O = "O"
EMPTY = " "

# Welcome human
print("Welcome to Tic Tac Toe: Human Vs Computer.")
print("Let's see if you can beat the machine.")
time.sleep(1)
# Initialize board and give directions
board = util.initial_state()
util.print_board(board)
print("Directions:")
print("Use the grid to give the X (on top) and Y (on side) coordinate of the position you would like to play in.")
print("For example the space in the upper left-hand corner would be X: 0, Y: 0")
time.sleep(3)
# Make sure human puts in a valid choice
while True:
    human = input("Will you be player X or O?: ").upper()
    if human == "X" or human == "O":
        break
    print("Please type X or O.")


# Asign which player is who based off above
if human == X:
    machine = O
else:
    machine = X

# intialize board
board = util.initial_state()

# run the game until there's a winner or tie
while True:
    # figure out who's turn it is
    player = util.turn(board)

    if player == human:
        print()
        print("Your turn...give the coordinates of the space you'd like to play in. X is shown on top and Y is shown on the side.")
        while True:
            # Make sure human cooperates
            x_cord = util.get_human_action("X")
            y_cord = util.get_human_action("Y")
            # Making sure that result function doesn't return None because the spot is filled
            potential_board = util.result(board, (y_cord, x_cord))
            if potential_board != None:
                board = potential_board
                break
        util.print_board(board)
    elif player == machine:
        print()
        print("The computer is thinking.")
        time.sleep(3)
        # Computer figures out move
        action = util.minimax(board, machine)
        # you don't have to check to make sure the board is using an empty space here because the actions() takes care of that
        board[action[0]][action[1]] = machine
        util.print_board(board)
    else:
        # game over
        winner = util.winner(board)
        if winner == None:
            print("It's a tie.")
        elif winner == machine:
            print("You lost. Better luck next time...")
        elif winner == None:
            print("You've done the impossible! You won!")
        quit()
