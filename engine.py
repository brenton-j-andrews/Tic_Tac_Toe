"""
This class stores all information concerning the current game state, including the board state and whose
turn it is. It will also check if winning conditions are present after each turn, check move legality, compute random
moves for an 'EASY' single player mode and run a MINIMAX algorithm for the 'HARD' single player mode.
"""

import random
import minimax


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
        self.test_mode = False

        # Below variables determine initial button status. Can be changed before each game.
        # self.difficult -> True means 'hard' mode, False means 'easy' mode.
        self.single_player = True
        self.is_x = True
        self.difficult = True

    # Method that checks the current game state for winning conditions.
    def check_win(self, symbol):
        # Check columns.
        col_count = 0
        for i in range(3):
            if self.board[i][col_count] == self.board[i][col_count + 1] == self.board[i][col_count + 2] == symbol:
                if not self.test_mode:
                    print(f"\n{symbol} Wins! Congratulations!")
                return True

        # Check rows.
        row_count = 0
        for j in range(3):
            if self.board[row_count][j] == self.board[row_count + 1][j] == self.board[row_count + 2][j] == symbol:
                if not self.test_mode:
                    print(f"\n{symbol} Wins! Congratulations!")
                return True

        # Check diagonal / anti-diagonal.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or self.board[2][0] == \
                self.board[1][1] == self.board[0][2] == symbol:
            if not self.test_mode:
                print(f"\n{symbol} Wins! Congratulations!")
            return True

        return False

    # Method that checks move legality.
    def legal(self, move):
        if self.board[move[0]][move[1]] != ' ':
            return False
        else:
            return True

    # Method that checks that moves remain.
    def moves_left(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return True
        if not self.test_mode:
            print("Its a draw!")
        return False

    # Method that generates random moves for 'easy ' mode and calls minimax function for 'hard' mode.
    def move_generator(self, difficulty, computer_symbol):
        if difficulty == 'E':
            legal_move = False
            while not legal_move:
                comp_move = [random.randint(0, 2), random.randint(0, 2)]
                if self.legal(comp_move):
                    return comp_move
        else:
            comp_move = minimax.find_best_move(self.board, computer_symbol)
            return comp_move
