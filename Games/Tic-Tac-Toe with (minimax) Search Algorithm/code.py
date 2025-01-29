X = "X"
O = "O"
EMPTY = None

def initial_state():
    """Returns the initial state of the board."""
   
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

 
def player(board):
    # Returns the player whose turn it is
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    # Returns a set of all possible actions
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    # Returns a new board state after applying the action
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid move")
    
    player_turn = player(board)
    new_board = [row.copy() for row in board]
    new_board[i][j] = player_turn
    return new_board

def winner(board):
    # Returns the winner if there is one, otherwise None
    for player_turn in [X, O]:
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(cell == player_turn for cell in board[i]) or all(board[j][i] == player_turn for j in range(3)):
                return player_turn
        if all(board[i][i] == player_turn for i in range(3)) or all(board[i][2 - i] == player_turn for i in range(3)):
            return player_turn
    return None

def terminal(board):
    # Returns True if the game is over, False otherwise
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    # Returns the utility value of the board
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        # Maximize for X
        _, move = max_alpha_beta(board, float('-inf'), float('inf'))
    else:
        # Minimize for O
        _, move = min_alpha_beta(board, float('-inf'), float('inf'))

    return move

def max_alpha_beta(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_move = None
    for action in actions(board):
        value, _ = min_alpha_beta(result(board, action), alpha, beta)
        if value > v:
            v = value
            best_move = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break  # Beta cutoff
    return v, best_move

def min_alpha_beta(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_move = None
    for action in actions(board):
        value, _ = max_alpha_beta(result(board, action), alpha, beta)
        if value < v:
            v = value
            best_move = action
        beta = min(beta, v)
        if beta <= alpha:
            break  # Alpha cutoff
    return v, best_move
