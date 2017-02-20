import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.set_name("John")
        self.player.set_marker("X")

    def test_get_name_returns_name(self):
        self.assertEqual(self.player.get_name(),"John")

    

if __name__ == '__main__':
    unittest.main()
