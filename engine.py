"""
This class stores all information concerning the current game state, such as the board layout and whose
turn it is. It will also check if winning conditions are present after each turn, check move legality and
provide a random move generator for single player testing / 'EASY' Mode.
"""

import random


class GameState:
    def __init__(self):
        # The game board is represented by a 2d list. The empty strings inside will store X's and O's as players
        # make moves.
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.x_to_play = True

    # Function checks the current game state for winning conditions.
    def check_win(self, symbol):
        # Check columns.
        col_count = 0
        for i in range(3):
            if self.board[i][col_count] == self.board[i][col_count + 1] == self.board[i][col_count + 2] == symbol:
                print(f"\n{symbol} Wins! Congratulations!")
                return True

        # Check rows.
        row_count = 0
        for j in range(3):
            if self.board[row_count][j] == self.board[row_count + 1][j] == self.board[row_count + 2][j] == symbol:
                print(f"\n{symbol} Wins! Congratulations!")
                return True

        # Check diagonal / anti-diagonal.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or self.board[2][0] == \
                self.board[1][1] == self.board[0][2] == symbol:
            print(f"\n{symbol} Wins! Congratulations!")
            return True

        return False

    # Function that checks move legality.
    def legal(self, move):
        if self.board[move[0]][move[1]] != ' ':
            return False
        else:
            return True

    # Function that generates random legal move and updates the game state for 'easy' mode.
    def rand_move(self, comp_symbol):
        legal_move = False
        while not legal_move:
            comp_move = [random.randint(0, 2), random.randint(0, 2)]
            if self.legal(comp_move):
                return comp_move

