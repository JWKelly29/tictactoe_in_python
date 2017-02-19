import unittest
from app.game import Game
from app.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_initializes_with_correct_properties(self):
        self.assertIsInstance(self.game.player1, Player)
        self.assertIsInstance(self.game.player2, Player)
        self.assertEqual(self.game.gameBoard, {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '})

    def test_game_can_find_winner(self):
        self.game.boardControl.setMarkBoard("X",1)
        self.game.boardControl.setMarkBoard("X",2)
        self.game.boardControl.setMarkBoard("X",3)
        self.assertEqual(self.game.is_game_won(), True)

    def test_game_can_take_turn(self):
        self.game.takeTurn("X",2)
        self.assertEqual(self.game.gameBoard, {1:' ' , 2: "X", 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '})

    
