


class Board():

    def __init__(self):
        self.board = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}

    def gameBoard(self):
        return self.board

    def printBoard(self):
        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])

    def setMarkBoard(self,mark,position):
        self.gameBoard()[position] = mark
        return self.gameBoard()

    def isCellOccupied(self,position):
        return True if self.gameBoard()[position] != ' ' else False
