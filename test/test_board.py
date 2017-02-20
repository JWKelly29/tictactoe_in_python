import unittest
from app.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_initailizes_with_empty_board(self):
        empty_board = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}
        self.assertEqual(self.board.game_board(), empty_board)

    def test_set_arkBoard_puts_X_on_board(self):
        self.board.set_mark_board("X",3)
        self.assertEqual(self.board.game_board()[3], "X")

    def test_board_isCellOccupied_method_returns_true_if_cell_occupied(self):
        self.board.set_mark_board("X",3)
        self.assertEqual(self.board.is_cell_occupied(3), True)

    def test_board_isCellOccupied_method_returns_false_if_cell_not_occupied(self):
        self.assertEqual(self.board.is_cell_occupied(3), False)

    def test_board_isBoardFull_method_returns_false_if_board_not_full(self):
        self.board.set_mark_board("X",1)
        self.assertEqual(self.board.is_board_full(), False)

    def test_board_isBoardFull_method_returns_true_if_board_full(self):
        self.board.set_mark_board("X",1)
        self.board.set_mark_board("X",2)
        self.board.set_mark_board("X",3)
        self.board.set_mark_board("X",4)
        self.board.set_mark_board("X",5)
        self.board.set_mark_board("X",6)
        self.board.set_mark_board("X",7)
        self.board.set_mark_board("X",8)
        self.board.set_mark_board("X",9)
        self.assertEqual(self.board.is_board_full(), True)



if __name__ == '__main__':
    unittest.main()
