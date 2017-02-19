from app.board import Board
from app.player import Player

class Game():
    def __init__(self):
        self.player1      = Player()
        self.player2      = Player()
        self.boardControl = Board()
        self.gameBoard    = self.boardControl.gameBoard()

    def startGame(self):
        print("Welcome to TicTacToe")
        print("What is Player1s Name?")
        player1_name = input(" : ")
        self.player1.setName(player1_name)
        print("What is Player2s Name?")
        player2_name = input(" : ")
        self.player2.setName(player2_name)
        print("Here is the board. Each cell of the grid is represented by the numbers 1 - 9 going from left to right, top to bottom.")
