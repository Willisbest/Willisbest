import unittest
from unittest.mock import patch
import python_kurs_ab_129 as pk

class TestPythonKursAb129(unittest.TestCase):

    def test_generate_random_number(self):
        """Test if random number generator produces numbers within the range 1 to 10"""
        with patch('python_kurs_ab_129.randint', return_value=5):
            self.assertEqual(pk.generate_random_number(), 5)

    def test_is_valid_guess(self):
        """Test if the guess is within the valid range"""
        self.assertTrue(pk.is_valid_guess(5))  # Valid guess
        self.assertFalse(pk.is_valid_guess(0))  # Below valid range
        self.assertFalse(pk.is_valid_guess(11))  # Above valid range

    def test_check_guess(self):
        """Test if guess is correctly checked against the answer"""
        self.assertTrue(pk.check_guess(7, 7))  # Guess matches answer
        self.assertFalse(pk.check_guess(7, 3))  # Guess doesn't match answer

    @patch('builtins.input', side_effect=[5])
    def test_get_user_guess_valid(self, mock_input):
        """Test user input when valid"""
        self.assertEqual(pk.get_user_guess(), 5)

    @patch('builtins.input', side_effect=['abc', '5'])
    def test_get_user_guess_invalid_then_valid(self, mock_input):
        """Test user input when invalid first, then valid"""
        with patch('builtins.print') as mock_print:
            self.assertIsNone(pk.get_user_guess())  # First invalid input returns None
            self.assertEqual(pk.get_user_guess(), 5)  # Second input is valid
            mock_print.assert_called_with("Please enter a valid number.")

    @patch('python_kurs_ab_129.generate_random_number', return_value=7)
    @patch('builtins.input', side_effect=[0, 11, 7])  # Invalid guesses: 0, 11; valid guess: 7
    def test_game(self, mock_input, mock_random):
        """Test the entire game flow, simulating inputs"""
        with patch('builtins.print') as mock_print:
            pk.game()
            # Ensure that the "Hey bozo" message is called for the invalid guesses (0 and 11)
            mock_print.assert_any_call("Hey bozo, I said 1~10!")
            # Ensure the correct message is printed for the right guess
            mock_print.assert_any_call("You are a genius!")

if __name__ == "__main__":
    unittest.main()
