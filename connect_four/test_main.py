import unittest
from main import *

class TestConnectFour(unittest.TestCase):

    def test_horizontal_win_one(self):
        newGame = ConnectFour()

        newGame.put(row=1,col=1, user=False)
        newGame.put(row=2,col=1, user=False)
        newGame.put(row=3,col=1, user=False)
        newGame.put(row=4,col=1, user=False)


        self.assertIsNotNone(newGame.hasWon())
        self.assertFalse(newGame.hasWon())

    def test_horizontal_win_two(self):
        newGame = ConnectFour()

        newGame.put(row=0,col=3, user=True)
        newGame.put(row=1,col=3, user=True)
        newGame.put(row=2,col=3, user=True)
        newGame.put(row=3,col=3, user=True)


        self.assertIsNotNone(newGame.hasWon())
        self.assertTrue(newGame.hasWon())


    def test_vertical_win(self):
        newGame = ConnectFour()

        newGame.put(row=2,col=2, user=True)
        newGame.put(row=2,col=3, user=True)
        newGame.put(row=2,col=4, user=True)
        newGame.put(row=2,col=5, user=True)


        self.assertIsNotNone(newGame.hasWon())
        self.assertTrue(newGame.hasWon())

    def test_diag_win(self):
        newGame = ConnectFour()

        newGame.put(row=0,col=0, user=True)
        newGame.put(row=1,col=1, user=True)
        newGame.put(row=2,col=2, user=True)
        newGame.put(row=3,col=3, user=True)

        self.assertIsNotNone(newGame.hasWon())
        self.assertTrue(newGame.hasWon())


if __name__ == '__main__':
    unittest.main()