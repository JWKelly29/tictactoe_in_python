import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.set_name("John")
        self.player.set_marker("X")

    def test_get_name_returns_name(self):
        self.assertEqual(self.player.get_name(),"John")

    def test_get_marker_returns_marker(self):
        self.assertEqual(self.player.get_marker(), "X")

    def test_set_marker_may_not_be_set_to_anything_other_than_X_or_O(self):
        self.assertRaises(ValueError, self.player.set_marker,"Z")

if __name__ == '__main__':
    unittest.main()
