


class Board():

    EMPTY = ' '

    def __init__(self):
        self.board = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}

    def game_board(self):
        return self.board

    def print_board(self):
        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])

    def set_mark_board(self,mark,position):
        self.game_board()[position] = mark
        return self.game_board()

    def is_cell_occupied(self,position):
        return True if self.game_board()[position] != self.EMPTY else False

    def is_board_full(self):
        for index in range(1, 10):
            if self.game_board()[index] == self.EMPTY:
                return False
        return True

    def reset_game_board(self):
        self.gameboard = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}
