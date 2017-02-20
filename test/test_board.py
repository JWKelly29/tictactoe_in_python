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

    def test_board_isBoardFull_method_returns_false_if_board_not_full(self):
        self.board.setMarkBoard("X",1)
        self.assertEqual(self.board.isBoardFull(), False)
        
    def test_board_isBoardFull_method_returns_true_if_board_full(self):
        self.board.setMarkBoard("X",1)
        self.board.setMarkBoard("X",2)
        self.board.setMarkBoard("X",3)
        self.board.setMarkBoard("X",4)
        self.board.setMarkBoard("X",5)
        self.board.setMarkBoard("X",6)
        self.board.setMarkBoard("X",7)
        self.board.setMarkBoard("X",8)
        self.board.setMarkBoard("X",9)
        self.assertEqual(self.board.isBoardFull(), True)



if __name__ == '__main__':
    unittest.main()
