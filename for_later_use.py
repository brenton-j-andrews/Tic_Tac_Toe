"""
File for storing old functions / code that will be implemented later.
"""


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


play_mode = 't'
game_on = True
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


"""
Pygame Stuff!
"""

# Function that renders menu text and buttons.
def render_buttons(screen, mouse):
    # Single Player Button
    if 610 <= mouse[0] <= 690 and 10 <= mouse[1] <= 90:
        p.draw.rect(screen, dark_color, [610, 10, 80, 80])
    else:
        p.draw.rect(screen, light_color, [610, 10, 80, 80])
    screen.blit(one_player, (615, 45))

    # Two Player Button
    if 710 <= mouse[0] <= 790 and 10 <= mouse[1] <= 90:
        p.draw.rect(screen, dark_color, [710, 10, 80, 80])
    else:
        p.draw.rect(screen, light_color, [710, 10, 80, 80])
    screen.blit(two_players, (715, 45))

    # Menu Text.
    screen.blit(single_text, (630, 110))

    # Single Player X Button
    if 610 <= mouse[0] <= 690 and 150 <= mouse[1] <= 240:
        p.draw.rect(screen, light_color, [610, 150, 80, 80])
    else:
        p.draw.rect(screen, (255, 255, 255), [610, 150, 80, 80])
    screen.blit(x_select, (628, 145))

    # Single Player O Button
    if 710 <= mouse[0] <= 790 and 150 <= mouse[1] <= 240:
        p.draw.rect(screen, light_color, [710, 150, 80, 80])
    else:
        p.draw.rect(screen, (255, 255, 255), [710, 150, 80, 80])
    screen.blit(o_select, (728, 145))

    # Quit Button
    if 610 <= mouse[0] <= 790 and 505 <= mouse[1] <= 585:
        p.draw.rect(screen, dark_color, [610, 505, 180, 80])
    else:
        p.draw.rect(screen, light_color, [610, 505, 180, 80])
    screen.blit(quit_button, (675, 530))


# Function that converts mouse value to action.
def mouse_down(mouse, screen, game_state):

    # Quit Button action.
    if 610 <= mouse[0] <= 790 and 505 <= mouse[1] <= 585:
        exit()


# Pygame button stuff...
small_button_font = p.font.SysFont('Corbel', 15)
large_button_font = p.font.SysFont('Corbel', 40)
choose_symbol = p.font.SysFont('Arial', 80)
one_player = small_button_font.render('One Player', False, (255, 255, 255))
two_players = small_button_font.render('Two Players', False, (255, 255, 255))
quit_button = large_button_font.render("Quit", False, (255, 255, 255))
single_text = small_button_font.render("Single Player Options:", False, (0, 0, 0))