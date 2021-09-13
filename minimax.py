# Minimax algorithm implementation.

# Returns a square value based on who is winning the game.
# Input board is from the game_state class.
def evaluate_board(game_board):

    # Check rows for winning conditions.
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    # Check columns for winning conditions.
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Check diagonal / anti diagonal for winning conditions.
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    if board[2][0] == board[1][1] == board[2][2]:
        if board[2][0] == 'X':
            return 10
        elif board[2][0] == 'O':
            return -10


# This function finds available moves and passes them to the minimax function for evaluation.
def find_best_move(game_board):
    highest_value = None
    best_move = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'

            # Pass move i, j into the minimax function for evaluation.
            move_value = minimax(board, 0, False)

            # Undo move [i][j].
            board[i][j] = ' '

            # Compare move_value and highest_value. If move_value is better update other values.
            if move_value > highest_value:
                highest_value = move_value
                best_move = [i, j]

    print(f"The best move right now is {best_move}.")
    return best_move


# Minimax function uses the evaluate_board function and recursion to see future game_states and make optimal moves.
def minimax(mm_board, depth, is_max):
    max_value = 10
    return max_value


# If no winning conditions are present, return value 0.
board = [['X', 'X', 'X'], [' ', 'O', ' '], ['O', ' ', 'O']]
print(find_best_move(board))
