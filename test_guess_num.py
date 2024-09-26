import unittest
from unittest.mock import patch
import guess_num


class TestGuessNum(unittest.TestCase):
    @patch("builtins.input", side_effect=[50, 75, 62, 81, 99, 55])
    @patch("random.randint", return_value=55)
    def test_correct_guess(self, mock_randint, mock_input):
        result = guess_num.guessing_game()
        self.assertEqual(result, 6)
        print()

    @patch("builtins.input", side_effect=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    @patch("random.randint", return_value=55)
    def test_ten_tries(self, mock_randint, mock_input):
        result = guess_num.guessing_game()
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
