import unittest
from app.game import Game

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_initializes_with_correct_properties(self):
        self.assertEqual(self.game.player1, 'O')
        self.assertEqual(self.game.player2, 'X')
        self.assertEqual(self.game.gameBoard, {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '})
