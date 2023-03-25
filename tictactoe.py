"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return None
    actions = set()
    for rowIndex, row in enumerate(board):
        for cellIndex, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((rowIndex, cellIndex))
    return actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print(action)
    # print(actions(board))

    if action not in actions(board):
        raise Exception("Invalid action")
    
    
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True
    



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def max_value(board):
    if terminal(board):
        return utility(board), None
    currMax = -1
    optimal_action = None
    for action in actions(board):
        maxX, move = min_value(result(board, action))
        if maxX > currMax:
            currMax = maxX
            move = optimal_action
            if currMax == 1:
                return currMax, move
    return currMax, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    currMin = 1
    optimal_action = None
    for action in actions(board):
        minO, move = max_value(result(board, action))
        if minO < currMin:
            currMin = minO
            move = optimal_action
            if currMin == -1:
                return currMin, move
    return currMin, move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    if player(board) == X:
        for action in actions(board):
            maxX, best_action = max_value(result(board, action))
            return best_action
    
    if player(board) == O:
        v = 1
        for action in actions(board):
            maxO, best_action = min_value(result(board, action))
            return best_action

