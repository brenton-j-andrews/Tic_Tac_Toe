"""
The testing script will control games played by the computer against itself and incorporate some randomness to help find
engine errors. The script will often play perfect games that result in a draw, but every so often will play
suboptimal moves to start the game. The script will play a set number of games and direct
game outcome, first moves by X and O, if first moves were optimal (corner for X, center for O) and the end
game_state.board configuration into a Pandas Dataframe, which will then be sorted for easy analysis. It takes quite a
while to play the computer myself, and this script will hopefully be able to play millions of games relatively quickly
and return the important aggregate data.
"""

import pandas as pd
import engine
import random
import csv

# Optimal first moves for X, excluding [0, 0]. O will always play optimal first move [1, 1] if run by minimax function.
x_opt_moves = [[0, 2], [2, 0], [2, 2]]

n_games = int(input("Enter number of games to execute: "))
game_complete = False

# game_stats list stores information about all games played for transformation into a pandas DataFrame.
game_stats = []
game_counter = 0

# Repeat game loop until n_games executed.
for i in range(n_games):
    game_state = engine.GameState()  # Initialize new game_state.
    game_state.test_mode = True
    counter = 0
    test_mode = random.choice([0, 1, 2, 3, 4])  # Each int in test_mode corresponds with a style of play for X and O.
    x_move, o_move = [0, 0], [0, 0]
    result = ' '  # Will store end result of 1 simulation. Draw (d), X wins (X), O win (O).

    while not game_complete:
        # -------------------- X move generation. -------------------- #
        if test_mode == 0 or test_mode == 2 or test_mode == 3:  # Play mini-max.
            if test_mode == 3 and counter == 0:  # Test mode 3: x plays 1 rand opt move, then mini-max.
                x_move = random.choice(x_opt_moves)
            else:
                x_move = game_state.test_move_generator(difficulty='H', computer_symbol='X')

        elif test_mode == 1:  # X plays one rand move, then mini-max.
            if counter == 0:
                x_move = game_state.test_move_generator(difficulty='E', computer_symbol='X')
            else:
                x_move = game_state.test_move_generator(difficulty='H', computer_symbol='X')

        else:  # test_mode == 4 and X plays all random moves.
            x_move = game_state.test_move_generator(difficulty='E', computer_symbol='X')

        # X move placement and winning condition check.
        game_state.board[x_move[0]][x_move[1]] = 'X'
        if game_state.check_win(symbol='X'):
            result = 'X'
            game_complete = True

        # -------------------- O move generation. -------------------- #
        if test_mode == 0 or test_mode == 1 or test_mode == 4:  # Play mini-max.
            o_move = game_state.test_move_generator(difficulty='H', computer_symbol='O')

        elif test_mode == 2:  # O plays one rand move, then mini-max.
            if counter == 0:
                o_move = game_state.test_move_generator(difficulty='E', computer_symbol='O')
            else:
                o_move = game_state.test_move_generator(difficulty='H', computer_symbol='O')

        else:  # test_mode == 3 and O plays all random moves.
            o_move = game_state.test_move_generator(difficulty='E', computer_symbol='O')

        # O move placement and winning condition check.
        game_state.board[o_move[0]][o_move[1]] = 'O'
        if game_state.check_win(symbol='O'):
            result = 'O'
            game_complete = True

        # Check for draw conditions.
        if not game_state.moves_left():
            result = 'D'
            game_complete = True

        counter += 1

    game_stats.append([test_mode, result])
    print(f"Test mode: {test_mode}")
    print(f"Outcome: {result}")
    game_complete = False
    game_counter += 1


# # Convert game_stats list to csv for analysis in Jupyter.
# columns = ['Test Mode', 'Result']
#
with open('test_data.csv', 'a') as f:
    write = csv.writer(f)
    write.writerows(game_stats)
