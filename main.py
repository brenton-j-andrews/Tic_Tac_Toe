"""
The main file will be our program driver.
It will handle user / computer input and update command line output / pygame graphics.
"""

import pygame as p
import engine
import time

# Initialize PyGame engine.
p.init()

# Board Dimension / Info Variables.
GAME_WIDTH = 800
GAME_HEIGHT = 600
DIMENSION = 3  # 3 x 3 squares in tic tac toe.
SQ_SIZE = GAME_HEIGHT / DIMENSION
# SQ_LOC has a color tuple and screen coordinates for each square printed to the pygame screen.
SQ_LOC = [((240, 240, 240), 0, 0), ((200, 200, 200), 200, 0), ((240, 240, 240), 400, 0), ((128, 128, 128), 600, 0),
          ((200, 200, 200), 0, 200), ((240, 240, 240), 200, 200), ((200, 200, 200), 400, 200),
          ((128, 128, 128), 600, 200), ((240, 240, 240), 0, 400), ((200, 200, 200), 200, 400),
          ((240, 240, 240), 400, 400), ((128, 128, 128), 600, 400)]

# Location tuples for 'X' and 'O' placement on the board.
PIECE_LOC = [
    [(100, 100), (300, 100), (500, 100)],
    [(100, 300), (300, 300), (500, 300)],
    [(100, 500), (300, 500), (500, 500)]]

# Button Constants. Will be updated when mode / difficulty / symbol and quit buttons are added to the interface.
light_color = (200, 200, 200)
dark_color = (100, 100, 100)
choose_symbol = p.font.SysFont('Arial', 60)
x_select = choose_symbol.render("X", False, (0, 0, 0))
o_select = choose_symbol.render('O', False, (0, 0, 0))
title_font = p.font.SysFont('cambria', 30)
button_font = p.font.SysFont('cambria', 20)
play_again_string = button_font.render("Play Again?", False, (0, 0, 0))


def main():
    screen = p.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    screen.fill(p.Color("white"))
    running = True
    game_complete = False  # game_won keeps track of current game status. running controls the entire script.

    game_state = engine.GameState()  # Initialize new game_state for next game.

    while running:

        # Menu buttons will be active until first time game board is clicked.
        game_state.game_start = False
        while not game_state.game_start:
            draw_game_state(screen, game_state)
            for e in p.event.get():
                mouse = p.mouse.get_pos()
                if e.type == p.MOUSEBUTTONDOWN:

                    # Single / two player buttons.
                    if 690 >= mouse[0] >= 625 and 155 >= mouse[1] >= 90:
                        game_state.single_player = True
                    if 775 >= mouse[0] >= 710 and 155 >= mouse[1] >= 90:
                        game_state.single_player = False

                    # Difficulty level buttons.
                    if 690 >= mouse[0] >= 625 and 245 >= mouse[1] >= 180:
                        game_state.difficulty = "H"
                        print(game_state.difficulty)
                    if 775 >= mouse[0] >= 710 and 245 >= mouse[1] >= 180:
                        game_state.difficulty = "E"

                    # 'X' or 'O' single player button.
                    if 695 >= mouse[0] >= 625 and 335 >= mouse[1] >= 270:
                        game_state.is_x = True
                    if 775 >= mouse[0] >= 710 and 335 >= mouse[1] >= 270:
                        game_state.is_x = False

                    # "Play again" button.
                    if game_state.game_complete:
                        if 775 >= mouse[0] >= 625 and 440 >= mouse[1] >= 375:
                            game_state.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                            game_state.game_complete = False

                    # Click board to start game.
                    if mouse[0] < 600:
                        game_state.game_start = True

            p.display.update()

        # Single player script.
        if game_state.single_player:

            # play_mode variable = 0: single player as X. val = 1: single player as O. val = 2: two player.
            if game_state.is_x:
                play_mode = 0
                computer_move = False
                computer_symbol = 'O'

            else:
                play_mode = 1
                computer_move = True
                computer_symbol = 'X'

            while not game_state.game_complete:
                draw_game_state(screen, game_state)
                mouse = p.mouse.get_pos()
                if not game_state.moves_left():
                    game_complete = True
                    break

                for e in p.event.get():
                    if e.type == p.QUIT:
                        running = False

                    # Computer move:
                    while computer_move:
                        time.sleep(.5)
                        comp_move = game_state.move_generator(computer_symbol=computer_symbol)
                        print(comp_move)
                        game_state.board[comp_move[0]][comp_move[1]] = computer_symbol
                        if game_state.check_win(computer_symbol):
                            draw_game_state(screen, game_state)
                            game_state.game_complete = True
                        computer_move = False

                    # Human move:
                    counter = 0
                    if e.type == p.MOUSEBUTTONDOWN:
                        # Ignore button presses in the menu area.
                        print(mouse)
                        if mouse[0] < 600 and counter == 0:
                            game_won, legal = game_state_mod(mouse, game_state, play_mode)
                            if not legal:
                                computer_move = False
                            else:
                                computer_move = True
                                if game_won:
                                    draw_game_state(screen, game_state)  # Update game_state before ending game loop.
                                    game_state.game_complete = True

                p.display.update()

        # Two player script.
        if not game_state.single_player:
            while not game_state.game_complete:
                draw_game_state(screen, game_state)
                mouse = p.mouse.get_pos()
                if not game_state.moves_left():
                    game_state.game_complete = True
                    break

                for e in p.event.get():
                    if e.type == p.QUIT:
                        running = False
                    if e.type == p.MOUSEBUTTONDOWN:
                        game_won = game_state_mod(mouse, game_state, play_mode=2)
                        if game_won:
                            draw_game_state(screen, game_state)  # Update game_state once more before ending game loop.
                            game_state.game_complete = True

                p.display.update()

        draw_game_state(screen, game_state)
        p.display.update()


# Function that draws current game state to pygame screen.
def draw_game_state(screen, game_state):
    for i in range(12):
        p.draw.rect(screen, SQ_LOC[i][0], [SQ_LOC[i][1], SQ_LOC[i][2], SQ_SIZE, SQ_SIZE])

    # Render menu text / buttons.
    title_text = title_font.render('Tic Tac Toe', False, (0, 0, 0))
    screen.blit(title_text, (625, 25))

    # Single / two player buttons. Single by default.
    if game_state.single_player:
        p.draw.rect(screen, (255, 255, 255), [625, 90, 65, 65])
        p.draw.rect(screen, (170, 170, 170), [710, 90, 65, 65])
    else:
        p.draw.rect(screen, (170, 170, 170), [625, 90, 65, 65])
        p.draw.rect(screen, (255, 255, 255), [710, 90, 65, 65])
    single_font = button_font.render('Single', False, (0, 0, 0))
    two_font = button_font.render('Two', False, (0, 0, 0))
    screen.blit(single_font, (630, 110))
    screen.blit(two_font, (720, 110))

    # Easy / Hard mode buttons. Easy by default.
    if game_state.difficulty == "H":
        p.draw.rect(screen, (255, 255, 255), [625, 180, 65, 65])
        p.draw.rect(screen, (170, 170, 170), [710, 180, 65, 65])
    else:
        p.draw.rect(screen, (170, 170, 170), [625, 180, 65, 65])
        p.draw.rect(screen, (255, 255, 255), [710, 180, 65, 65])
    hard_font = button_font.render('Hard', False, (0, 0, 0))
    easy_font = button_font.render('Easy', False, (0, 0, 0))
    screen.blit(hard_font, (635, 200))
    screen.blit(easy_font, (720, 200))

    # Choose X or O for single player buttons.
    if game_state.is_x:
        p.draw.rect(screen, (255, 255, 255), [625, 270, 65, 65])
        p.draw.rect(screen, (170, 170, 170), [710, 270, 65, 65])
    else:
        p.draw.rect(screen, (170, 170, 170), [625, 270, 65, 65])
        p.draw.rect(screen, (255, 255, 255), [710, 270, 65, 65])
    screen.blit(x_select, (642, 268))
    screen.blit(o_select, (725, 268))

    # Play again button.
    if game_state.game_complete:
        p.draw.rect(screen, (255, 255, 255), [625, 375, 150, 65])
    else:
        p.draw.rect(screen, (170, 170, 170), [625, 375, 150, 65])
    screen.blit(play_again_string, (650, 395))

    # Render x and o symbols from game state.
    for i in range(3):
        for j in range(3):
            if game_state.board[i][j] == 'X':
                screen.blit(x_select, PIECE_LOC[i][j])
            elif game_state.board[i][j] == 'O':
                screen.blit(o_select, PIECE_LOC[i][j])


# Function that takes user input, checks move legality, modifies the game_state and checks for winning conditions.
def game_state_mod(mouse, game_state, play_mode):
    # Check game_state object for player turn and skip second player turn using play_mode arg if in single player.
    if play_mode == 0:
        symbol = 'X'

    elif play_mode == 1:
        symbol = 'O'

    else:
        if game_state.x_to_play:
            symbol = 'X'
            game_state.x_to_play = False
        else:
            symbol = 'O'
            game_state.x_to_play = True

    # Find x_position.
    if mouse[1] < (GAME_WIDTH - 200) / 3:
        x_pos = 0
    elif mouse[1] < (GAME_WIDTH - 200) / 3 * 2:
        x_pos = 1
    elif mouse[1] < (GAME_WIDTH - 200):
        x_pos = 2
    else:
        x_pos = None

    # Find y_position.
    if mouse[0] < GAME_HEIGHT / 3:
        y_pos = 0
    elif mouse[0] < GAME_HEIGHT / 3 * 2:
        y_pos = 1
    elif mouse[0] < GAME_HEIGHT:
        y_pos = 2
    else:
        y_pos = None

    move = [x_pos, y_pos]
    if game_state.legal(move):
        print(game_state.legal(move))
        game_state.board[x_pos][y_pos] = symbol
        if game_state.check_win(symbol=symbol):
            return True

    else:
        if play_mode == 0 or play_mode == 1:
            return False, False
        game_state.x_to_play = not game_state.x_to_play

    if play_mode == 0 or play_mode == 1:
        return False, True
    else:
        return False


if __name__ == "__main__":
    main()
