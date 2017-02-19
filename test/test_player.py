import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.setName("John")
        self.player.setMarker("X")

    def test_getName_returns_name(self):
        self.assertEqual(self.player.getName(),"John")

    def test_getMarker_returns_marker(self):
        self.assertEqual(self.player.getMarker(), "X")

    def test_setMarker_may_not_be_set_to_anything_other_than_X_or_O(self):
        self.assertRaises(ValueError, self.player.setMarker,"Z")

if __name__ == '__main__':
    unittest.main()
