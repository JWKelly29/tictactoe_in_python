import unittest
from app.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_initailizes_with_empty_board(self):
        empty_board = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}
        self.assertEqual(self.board.gameBoard(), empty_board)

    def test_setMarkBoard_puts_X_on_board(self):
        self.board.setMarkBoard("X",3)
        self.assertEqual(self.board.gameBoard()[3], "X")

    def test_board_isCellOccupied_method_returns_true_if_cell_occupied(self):
        self.board.setMarkBoard("X",3)
        self.assertEqual(self.board.isCellOccupied(3), True)

    def test_board_isCellOccupied_method_returns_false_if_cell_not_occupied(self):
        self.assertEqual(self.board.isCellOccupied(3), False)



if __name__ == '__main__':
    unittest.main()
