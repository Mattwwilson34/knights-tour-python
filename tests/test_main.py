import os
import sys
import unittest

sys.path.append(os.getcwd())
import knights_tour.main as main



class TestMain(unittest.TestCase):
    def test_is_valid_move(self):
        # move within bounds should return true
        self.assertTrue(main.is_valid_move(1, 1))
        self.assertTrue(main.is_valid_move(4, 4))

        # move out of bounds should return false
        self.assertFalse(main.is_valid_move(main.COLS, main.ROWS))


class TestGetValidMoves(unittest.TestCase):
    def test_get_valid_moves(self):
        # Test case 1: (0, 0)
        x, y = 0, 0
        expected_moves = [(2, 1), (1, 2)]
        actual_moves = main.get_valid_moves(x, y)
        self.assertCountEqual(actual_moves, expected_moves)

        # Test case 2: (3, 4)
        x, y = 3, 4
        expected_moves = [
            (1, 3),
            (2, 2),
            (4, 2),
        ]
        actual_moves = main.get_valid_moves(x, y)
        self.assertCountEqual(actual_moves, expected_moves)


if __name__ == "__main__":
    unittest.main()
