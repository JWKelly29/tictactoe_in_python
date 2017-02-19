import unittest
from app.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_initailizes_with_empty_board(self):
        empty_board = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}
        self.assertEqual(self.board.gameBoard(), empty_board)



if __name__ == '__main__':
    unittest.main()
