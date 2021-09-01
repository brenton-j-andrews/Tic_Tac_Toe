import random

# Board representation strings:
hor_sep = '-----------'
x_char = 'X'
o_char = 'O'


# Function that prints board representation in terminal.
def board_rep(board):
    print('    1   2   3')
    for i in range(3):
        j = 0
        print(f'{i + 1}   {board[i][j]} | {board[i][j + 1]} | {board[i][j + 2]} ', end=' ')
        if i != 2:
            print(f'\n   {hor_sep}')
    print("\n")

    return


# Checks if winning conditions are met.
def check_win(board, player):
    # Check columns.
    col_count = 0
    for i in range(3):
        if board[i][col_count] == board[i][col_count + 1] == board[i][col_count + 2] == player:
            print(f"\n{player} Wins! Congratulations!")
            return True

    # Check rows.
    row_count = 0
    for j in range(3):
        if board[row_count][j] == board[row_count + 1][j] == board[row_count + 2][j] == player:
            print(f"\n{player} Wins! Congratulations!")
            return True

    # Check diagonal / anti-diagonal.
    if board[0][0] == board[1][1] == board[2][2] == player or board[2][0] == board[1][1] == board[0][2] == player:
        print(f"\n{player} Wins! Congratulations!")
        return True

    return False


# Checks that square isn't already occupied.
def legal(board, func_move):
    # Check that func_move is valid.
    if func_move[0] > 3 or func_move[1] > 3:
        return False
    if board[func_move[1] - 1][func_move[0] - 1] != ' ':  # Check that grid space is empty.
        return False
    else:
        return True


# Player move input.
def make_move(board, func_count):
    if func_count % 2 == 0:
        symbol = x_char
    else:
        symbol = o_char
    legal_move = False
    while not legal_move:
        func_move = list(map(int, input(f"{symbol}, Enter your move as 'x y': ").split()))
        print('\n')
        if legal(board, func_move):
            func_count += 1
            return func_move, func_count
        else:
            print("Illegal move, try again.")

    return


# Easy mode computer 'engine' -> Generates random moves.
def rand_move(board):
    legal_move = False
    while not legal_move:
        comp_move = [random.randint(1, 3), random.randint(1, 3)]
        if legal(board, comp_move):
            return comp_move


# Game initialization:
play_mode = input("Type 's' for single player or 't' for two player: ")
game_on = True
single_player = False

# Two player script:
if play_mode == 't':
    while game_on:
        print('\n')
        board_arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        game_won = False
        move_count = 0
        moves = 1

        # Game script.
        while not game_won:
            board_rep(board_arr)
            print('\n')

            # X input.
            move, move_count = make_move(board_arr, func_count=move_count)
            board_arr[move[1] - 1][move[0] - 1] = 'X'
            board_rep(board_arr)
            if check_win(board_arr, 'X'):
                game_won = True
                break

            # O input.
            move, move_count = make_move(board_arr, func_count=move_count)
            board_arr[move[1] - 1][move[0] - 1] = 'O'
            board_rep(board_arr)
            if check_win(board_arr, 'O'):
                game_won = True
                break

            # Check for a draw.
            if moves >= 4:
                print("Its a draw!")
                game_won = True

        new_game = input("Play again? (y / n): ")
        if new_game == 'n':
            game_on = False

# Single player script:
if play_mode == 's':
    diff = input("Choose difficulty ('e', 'h'): ")
    player_symbol = input("Choose 'X' or 'O': ")
    if player_symbol == 'X':
        comp_symbol = 'O'
    else:
        comp_symbol = 'X'

    while game_on:
        print('\n')
        board_arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        game_won = False
        moves = 1

        while not game_won:
            print('\n')
            board_rep(board_arr)  # board_rep prints current GameState.
            game_won = False
            moves = 1

            # X move input.
            if player_symbol == 'X':
                move_count = 0
                move, move_count = make_move(board_arr, func_count=move_count)
            else:
                print("X makes a move:\n")
                move = rand_move(board_arr)

            board_arr[move[1] - 1][move[0] - 1] = 'X'
            board_rep(board_arr)
            if check_win(board_arr, 'X'):
                game_won = True
                break

            # O move input.
            if player_symbol == 'O':
                move_count = 1
                move, move_count = make_move(board_arr, func_count=move_count)
            else:
                print("O makes a move:\n")
                move = rand_move(board_arr)

            board_arr[move[1] - 1][move[0] - 1] = 'O'
            if check_win(board_arr, 'O'):
                game_won = True
                break

            # Check for a draw.
            if moves >= 4:
                print("Its a draw!")
                game_won = True

        new_game = input("Play again? (y / n): ")
        if new_game == 'n':
            game_on = False
