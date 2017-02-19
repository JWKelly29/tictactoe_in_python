import unittest
from app.game import Game
from app.player import Player

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_initializes_with_correct_properties(self):
        self.assertIsInstance(self.game.player1, Player)
        self.assertIsInstance(self.game.player2, Player)
        self.assertEqual(self.game.gameBoard, {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '})
