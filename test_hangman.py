import Hangman
from Hangman import ask_user, guess, print_word, check_user_input

from unittest.mock import patch, MagicMock

from unittest import TestCase




def test_check_user_input_true():
    assert check_user_input("abcdeFGHIJKLÖÄPÜm") == "abcdeFGHIJKLÖÄPÜm".lower()


@patch("Hangman.ask_user", return_value="abc")
def test_check_user_input_false(ask_user):
    # check if it works for a word
    assert check_user_input(r"%abc") == "abc".lower()


    # check if it does throw error for numbers
    # assert check_user_input("hi1kasüäö") == False
    # # check if special signs throw and error
    # assert check_user_input("kl%") == False



