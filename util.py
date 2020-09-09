"""All the stuff I use in the main file"""

import copy

X = "X"
O = "O"
EMPTY = " "

# Initialize board
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Prints out the board
def print_board(board):
    print("   |  0 |  1 |  2 ")
    print("__________________")
    for x in range(3):
        print(f" {x} | ", end =" ")
        for y in range(3):
            if y != 2:
                print(f"{board[x][y]} | ", end =" ")
            else:
                print(f"{board[x][y]}")
        if x != 2:
            print("__________________")

# Checks to see who's turn it is, returns none if game is over
def turn(board):
    # Check to see if it's the first move
    initial = initial_state()
    if board == initial:
        return X
    # Check to see if there was a winner
    elif terminal(board):
        return None

    # If not beginning or end...
    # check to see if there's more X's than O's...return char with less
    xcount = 0
    ocount = 0
    for row in board:
        xcount += row.count(X)
        ocount += row.count(O)

    if xcount > ocount:
        return O
    else:
        return X

# Makes sure that humans enters a valid input
def get_human_action(cord):
    while True:
        answer = input(f"{cord}: ")
        try:
            answer = int(answer)
            if answer < 3 and answer > 0:
                break
            else:
                print("Please type 0, 1, or 2.")
        except ValueError:
                print("Please type a whole number.")
    return answer


# Returns set of all possible actions (i, j) available on the board.
def actions(board):
    # Search through board and return indices of all the spaces that are EMPTY
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return(actions)


# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    # Check to make sure that cell is EMPTY ()
    if board[action[0]][action[1]] == EMPTY:
        # Check to see who's turn it is (which value to put in)
        current_player = turn(board)
        # Copy the board (necessary for the minimax function)
        copy_board = copy.deepcopy(board)
        # Update and return the copy
        copy_board[action[0]][action[1]] = current_player
        return(copy_board)
    else:
        print("That spot is taken already.")
        return None

# Returns True if game is over, False otherwise. Used in other functions.
def terminal(board):
    if winner(board) != None:
        return True

    for row in board:
        for item in row:
            if item == EMPTY:
                return False
    return True


# Returns winner of the game if there is one
def winner(board):
    # Check to see if either all X or O in any row (straight across)
    for row in board:
        if any(item != row[0] or item == EMPTY for item in row[1:]):
            pass
        else:
            return row[0]

    # Check to see if all X or O in any column
    unzipped = zip(*board)
    for row in unzipped:
        if any(item != row[0] or item == EMPTY for item in row[1:]):
            pass
        else:
            return row[0]

    # Check to see if all X or Y in either diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
# This is how the machine can understand the notion of winning/losing.
def utility(board):
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


# Figures out the best move for the ai to make
def minimax(board, machine):
    # Results list of x cord and y cord for the action
    if machine == X:
        # Figure out optimal move as X who wants to max score)
        (end_utility, action) = max(board, -2, 2)
        return action
    else:
        # Figure out optimal move as O who wants to min score
        (end_utility, action) = min(board, -2, 2)
        return action

def max(board, alpha, beta):
    # Check to see if there was a Winner after all these recursions
    if terminal(board):
        return (utility(board), None)

    # Get set of all the possible actions remaining on the board
    potential_actions = actions(board)

    # Set max = -2 as the worst possible scenario
    # Initialize empty value for best action
    max = -2
    final_action = None

    # Play through all of the actions
    for action in potential_actions:
        # Get new board for this action
        result_board = result(board, action)
        # See what min player would do (min function will determine if it is passed a terminal board)
        (min_result, min_action) = min(result_board, alpha, beta)
        # See if this action resulted a board score better than our current max
        if min_result > max:
            max = min_result
            final_action = action

        # Prune results so machine is faster by not looking at all possible options
        if max >= beta:
            return(max, final_action)

        if max > alpha:
            alpha = max
    return(max, final_action)


def min(board, alpha, beta):
    # Check to see if there was a Winner
    if terminal(board):
        return (utility(board), None)

    # Get set of all the possible actions remaining on the board
    potential_actions = actions(board)

    # Set min = 2 as worst case scenario
    # Initialize empty value for best action
    min = 2
    final_action = None

    # Play through all of the possible actions
    for action in potential_actions:
        # Get new board for this action
        result_board = result(board, action)
        # See what max player would do
        (max_result, max_action) = max(result_board, alpha, beta)
        # See if this action resulted in something better than current min
        if max_result < min:
            min = max_result
            final_action = action

        # Prune results so machine is faster by not looking at all possible options
        if min <= alpha:
            return(min, final_action)

        if min < beta:
            beta = min

    return(min, final_action)
