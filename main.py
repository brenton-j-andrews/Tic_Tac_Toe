"""
The main file will be our program driver.
It will handle user / computer input and update command line output / pygame graphics.
"""

# This comment is another test for figuring out branching, hello test_1 branch..

import pygame as p
import engine

# Initialize PyGame engine.
p.init()

# Board Dimension / Info Variables.
GAME_WIDTH = GAME_HEIGHT = 600
DIMENSION = 3  # 3 x 3 squares in tic tac toe.
SQ_SIZE = GAME_HEIGHT / DIMENSION
# SQ_LOC has a color tuple and screen coordinates for each square printed to the pygame screen.
SQ_LOC = [((240, 240, 240), 0, 0), ((200, 200, 200), 200, 0), ((240, 240, 240), 400, 0),
          ((200, 200, 200), 0, 200), ((240, 240, 240), 200, 200), ((200, 200, 200), 400, 200),
          ((240, 240, 240), 0, 400), ((200, 200, 200), 200, 400), ((240, 240, 240), 400, 400)]

# Location tuples for 'X' and 'O' placement on the board.
PIECE_LOC = [
    [(100, 100), (300, 100), (500, 100)],
    [(100, 300), (300, 300), (500, 300)],
    [(100, 500), (300, 500), (500, 500)]]


# Button Constants.
light_color = (200, 200, 200)
dark_color = (100, 100, 100)
choose_symbol = p.font.SysFont('Arial', 80)
x_select = choose_symbol.render("X", False, (0, 0, 0))
o_select = choose_symbol.render('O', False, (0, 0, 0))


def main():
    screen = p.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    game_state = engine.GameState()
    screen.fill(p.Color("white"))
    running = True
    while running:
        draw_game_state(screen, game_state)
        mouse = p.mouse.get_pos()
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.MOUSEBUTTONDOWN:
                game_won = game_state_mod(mouse, game_state)
                if game_won:
                    running = False
                    break

        p.display.update()
        if game_state.is_won:
            running = False


# Function that draws current game state to pygame screen.
def draw_game_state(screen, game_state):
    for i in range(9):
        p.draw.rect(screen, SQ_LOC[i][0], [SQ_LOC[i][1], SQ_LOC[i][2], SQ_SIZE, SQ_SIZE])

    # Render x and o symbols from game state.
    for i in range(3):
        for j in range(3):
            if game_state.board[i][j] == 'X':
                screen.blit(x_select, PIECE_LOC[i][j])
            elif game_state.board[i][j] == 'O':
                screen.blit(o_select, PIECE_LOC[i][j])


# Function that takes user input, checks move legality, modifies the game_state and checks for winning conditions.
def game_state_mod(mouse, game_state):

    # Check game_state object for player turn.
    if game_state.x_to_play:
        symbol = 'X'
        game_state.x_to_play = False
    else:
        symbol = 'O'
        game_state.x_to_play = True
    move = []

    # Find x_position.
    if mouse[0] < GAME_WIDTH / 3:
        x_pos = 0
    elif mouse[0] < GAME_WIDTH / 3 * 2:
        x_pos = 1
    elif mouse[0] < GAME_WIDTH:
        x_pos = 2
    else:
        x_pos = None

    # Find y_position.
    if mouse[1] < GAME_HEIGHT / 3:
        y_pos = 0
    elif mouse[1] < GAME_HEIGHT / 3 * 2:
        y_pos = 1
    elif mouse[1] < GAME_HEIGHT:
        y_pos = 2
    else:
        y_pos = None

    move = [y_pos, x_pos]
    print(move)
    if game_state.legal(move):
        game_state.board[y_pos][x_pos] = symbol
        if game_state.check_win(symbol=symbol):
            print(game_state.board)

    else:
        game_state.x_to_play = not game_state.x_to_play
        print(game_state.x_to_play)

    return False


if __name__ == "__main__":
    main()
