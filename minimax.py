# Minimax algorithm implementation.

# Produces moves for the computer designed for an optimal game using recursion to see future game_states.  Will
# always win or draw the game.

"""
Current issue with minimax:
With computer as O, will often block x winning moves while an O winning move is present.
Computer playing as X doesn't seem to have this issue.
"""


def evaluate_board(game_board, max_player, min_player):
    # Check rows for winning conditions.
    for row in range(0, 3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2]:
            if game_board[row][0] == max_player:
                return 10
            elif game_board[row][0] == min_player:
                return -10

    # Check columns for winning conditions.
    for col in range(0, 3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col]:
            if game_board[0][col] == max_player:
                return 10
            elif game_board[0][col] == min_player:
                return -10

    # Check diagonal / anti diagonal for winning conditions.
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        if game_board[0][2] == max_player:
            return 10
        elif game_board[0][2] == min_player:
            return -10

    if game_board[2][0] == game_board[1][1] == game_board[2][2]:
        if game_board[2][0] == max_player:
            return 10
        elif game_board[2][0] == min_player:
            return -10

    else:
        return 0


# This function finds available moves and passes them to the minimax function for evaluation.
def find_best_move(game_board, computer_symbol):
    if computer_symbol == 'X':
        max_player = 'X'
        min_player = 'O'
    else:
        max_player = 'O'
        min_player = 'X'

    highest_value = -100
    best_move = [-1, -1]
    for i in range(3):
        for j in range(3):
            # This loop finds all possible moves to be evaluated.
            if game_board[i][j] == ' ':
                game_board[i][j] = max_player

                # Pass move i, j into the minimax function for evaluation.
                # 2nd arg: current depth, 3rd arg: max or min play.
                move_value = minimax(game_board, 0, False, max_player, min_player)
                print(move_value)
                # Undo move [i][j].
                game_board[i][j] = ' '

                # Compare move_value and highest_value. If move_value is better update other values.
                if move_value > highest_value:
                    highest_value = move_value
                    print(highest_value)
                    best_move = [i, j]

    print(f"The best move right now is {best_move}.")
    return best_move


# Function for determining if any moves remain.
def moves_left(game_board):
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                return True
    return False


# Minimax function uses the evaluate_board function and recursion to see future game_states and make optimal moves.
def minimax(game_board, depth, is_max, max_player, min_player):
    score = evaluate_board(game_board, max_player, min_player)
    print(depth)
    # If computer winning conditions met, return 10
    if score == 10:
        print('test')
        return score

    # If player winning conditions met:
    if score == -10:
        print('test 1')
        return score

    # Check for remaining moves.
    if not moves_left(game_board):
        print('test 2')
        return 0

    # If it is the maximizer turn:
    if is_max:
        best_move = -100

        # Traverse board and make move on empty cell.
        for i in range(3):
            for j in range(3):
                if game_board[i][j] == ' ':
                    game_board[i][j] = max_player

                    # Recursively call minimax function to play thru the game until winning conditions are met.
                    best_move = max(best_move, minimax(game_board, depth + 1, not is_max, max_player, min_player))

                    # Undo the move.
                    game_board[i][j] = ' '

        return best_move

    # If it is minimizes turn:
    else:
        best_move = 100

        # Traverse the board and make move on empty cell.
        for i in range(3):
            for j in range(3):
                if game_board[i][j] == ' ':
                    game_board[i][j] = min_player

                    # Call minimax function again!
                    best_move = min(best_move, minimax(game_board, depth + 1, not is_max, max_player, min_player))

                    game_board[i][j] = ' '

        return best_move


# Boards for test input:
board_1 = [[' ', ' ', 'O'], ['X', 'X', 'O'], [' ', ' ', 'X']]
board_2 = [[' ', ' ', 'O'], [' ', 'X', ' '], ['O', ' ', 'X']]

print(find_best_move(board_1, 'X'))
