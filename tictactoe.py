"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    empty_squares = 0
    for l in board:
        empty_squares += l.count(EMPTY)

    return X if empty_squares % 2 != 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for r_idx, row in enumerate(board):
        for t_idx, tile in enumerate(row):
            if tile == EMPTY:
                actions_set.add((r_idx,t_idx))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_combinations = [[(0,0), (0,1), (0,2)],
                           [(1,0), (1,1), (1,2)],
                           [(2,0), (2,1), (2,2)],
                           [(0,0), (1,0), (2,0)],
                           [(0,1), (1,1), (2,1)],
                           [(0,2), (1,2), (2,2)],
                           [(0,0), (1,1), (2,2)],
                           [(0,2), (1,1), (2,0)]]

    for line in winner_combinations:
        x0, y0 = line[0]
        x1, y1 = line[1]
        x2, y2 = line[2]

        if board[x0][y0] == board[x1][y1] and board[x0][y0] == board[x2][y2]:
            return board[x0][y0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return not any(EMPTY in row for row in board) or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        util = 1
    elif winner_player == O:
        util = -1
    else:
        util = 0

    return util


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Retun value
    best_action = tuple()

    if player(board) == X:
        # if board is empty choose random to avoid unnecessary computing
        if is_empty_board(board):
            return (random.choice([0,1,2]),random.choice([0,1,2]))
        max_v = -2
        for action in actions(board):
            # calculate the result of the action
            next_board = result(board, action)
            # if the result of the action make you win return action
            if winner(next_board) == X:
                return action
            v = min_val(next_board, -math.inf, math.inf)
            if v > max_v:
                best_action = action
                max_v = v

    if player(board) == O:
        min_v = 2
        for action in actions(board):
            # calculate the result of the action
            next_board = result(board, action)
            # if the result of the action make you win return action
            if winner(next_board) == O:
                return action
            v = max_val(next_board, -math.inf, math.inf)
            if v < min_v:
                best_action = action
                min_v = v

    return best_action


def max_val(board, alpha, beta):
    """
    Returns the max value "v"
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_val(result(board, action), alpha, beta))
        # alpha-beta prunning
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v


def min_val(board, alpha, beta):
    """
    Returns the max value "v"
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action), alpha, beta))
        # alpha-beta prunning
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v


def gen_rand_board():
    """
    Generate a random board for testing
    """
    board = initial_state()
    for _idx in range(random.randrange(9)):
        player_turn = player(board)
        act = random.sample(actions(board), 1)[0]
        board[act[0]][act[1]] = player_turn
    return board


def ppb(board):
    """
    Print board for visualization
    """
    for row in board:
        row = [' ' if x == EMPTY else x for x in row]
        print(row[0], row[1], row[2])


def is_empty_board(board):
    """
    [board] -> bool
    Check if board is empty.
    """
    for row in board:
        if row.count(EMPTY) != 3:
            return False
    return True
