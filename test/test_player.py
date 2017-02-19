import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.setName("John")

    def test_playerName_returns_name(self):
        self.assertEqual(self.player.getName(),"John")

if __name__ == '__main__':
    unittest.main()
