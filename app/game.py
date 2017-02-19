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


    def takeTurn(self, mark):
        print("Choose a place to put your mark")
        position = int(input)
        try:
            if position > 9 or position < 1:
                raise Exception
        except:
            print('Pick a number between 1-9')
            return self.takeTurn(mark)

        self.boardControl.setMarkBoard(mark, position)
        self.boardControl.printBoard()

    def is_game_won(self):
        win_conds = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        for win_cond in win_conds:
            if self.gameBoard[win_cond[0]] == self.gameBoard[win_cond[1]] and self.gameBoard[win_cond[1]] == self.gameBoard[win_cond[2]] and self.gameBoard[win_cond[0]]!= ' ':
                return True
