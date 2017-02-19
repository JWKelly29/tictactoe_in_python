from app.board import Board
from app.player import Player

class Game():
    def __init__(self):
        self.player1      = Player()
        self.player2      = Player()
        self.boardControl = Board()
        self.gameBoard    = self.boardControl.gameBoard()
