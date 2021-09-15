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
import minimax
import random


# Optimal first moves for X. O will always play optimal first move [1, 1] if run by minimax function.
x_opt_moves = [[0, 0], [0, 2], [2, 0], [2, 2]]

n_games = int(input("Enter number of games to execute: "))
game_complete = False

# game_stats list stores information about all games played for transformation into a pandas DataFrame.
game_stats = []

# Repeat game loop until n_games executed.
for i in range(n_games):
    game_state = engine.GameState()  # Initialize new game_state.
    result = ' '

    while not game_complete:
        # X to play...
        x_move = game_state.move_generator(difficulty='H', computer_symbol='X')
        game_state.board[x_move[0]][x_move[1]] = 'X'
        if game_state.check_win(symbol='X'):
            result = 'X'
            print("X wins!")
            game_complete = True

        # O to play...
        o_move = game_state.move_generator(difficulty='H', computer_symbol='O')
        game_state.board[o_move[0]][o_move[1]] = 'O'
        if game_state.check_win(symbol='O'):
            result = 'O'
            print("O wins!")
            game_complete = True

        if not game_state.moves_left():
            result = 'D'
            game_complete = True

    game_stats.append([result, game_state.board])
    game_complete = False


# Aggregate data from game_stats using pandas.
game_df = pd.DataFrame(game_stats, columns=['game_result', 'end board'])
print(f"Draws with minimax function played by 'X' and 'O': {game_df.game_result.value_counts().item()}")


















