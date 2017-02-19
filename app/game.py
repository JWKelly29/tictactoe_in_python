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
        self.turn = True


    def takeTurn(self, mark, input_given):
        self.boardControl.setMarkBoard(mark, input_given)
        self.boardControl.printBoard()

    def is_game_won(self):
        win_conds = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        for win_cond in win_conds:
            if self.gameBoard[win_cond[0]] == self.gameBoard[win_cond[1]] and self.gameBoard[win_cond[1]] == self.gameBoard[win_cond[2]] and self.gameBoard[win_cond[0]]!= ' ':
                return True

    def main(self):
        self.gameActive = True
        self.startGame()
        self.game_active_loop()

    def check_input_between_1_and_9(self, input_given):
        try:
            if input_given > 9 or input_given < 1:
                raise Exception
        except:
            print('Pick a number between 1-9')
            return self.game_active_loop()

    def game_active_loop(self):
        while self.gameActive:
            if self.player1_turn == True:
                print("Choose a place to put your mark")
                position = int(input)
                self.check_input_between_1_and_9()
                self.takeTurn(self.player1.getMarker, position)
            else:
                print("Choose a place to put your mark")
                position = int(input)
                self.check_input_between_1_and_9()
                self.takeTurn(self.player2.getMarker, position)
