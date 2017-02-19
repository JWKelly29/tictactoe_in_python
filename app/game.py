from app.board import Board

class Game():
    def __init__(self):
        self.player1      = 'O'
        self.player2      = 'X'
        self.boardControl = Board()
        self.gameBoard    = self.boardControl.gameBoard()

    
