"""
This class stores all information concerning the current game state, such as the board layout and whose
turn it is. It will also check if winning conditions are present after each turn, check move legality and
provide a random move generator for single player testing / 'EASY' Mode.
"""


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
        self.is_won = False

    # Function that checks move legality.
    def legal(self, move):
        if self.board[move[0]][move[1]] != ' ':
            return False
        else:
            return True

    # Function checks the current game state for winning conditions.
    def check_win(self, symbol):
        # Check columns.
        col_count = 0
        for i in range(3):
            if self.board[i][col_count] == self.board[i][col_count + 1] == self.board[i][col_count + 2] == symbol:
                print(f"\n{symbol} Wins! Congratulations!")
                self.is_won = True

        # Check rows.
        row_count = 0
        for j in range(3):
            if self.board[row_count][j] == self.board[row_count + 1][j] == self.board[row_count + 2][j] == symbol:
                print(f"\n{symbol} Wins! Congratulations!")
                self.is_won = True

        # Check diagonal / anti-diagonal.
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or self.board[2][0] == \
                self.board[1][1] == self.board[0][2] == symbol:
            print(f"\n{symbol} Wins! Congratulations!")
            self.is_won = True

        return False

