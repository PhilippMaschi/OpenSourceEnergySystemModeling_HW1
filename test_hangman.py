import Hangman
from Hangman import ask_user, guess, print_word, check_user_input
from unittest.mock import patch, MagicMock


def test_check_user_input_true():
    assert check_user_input("abcdeFGHIJKLÖÄPÜm") == "abcdeFGHIJKLÖÄPÜm".lower()


@patch("Hangman.ask_user")
def test_check_user_input_false(mock_ask_user):
    # try if space throws an error and the number as well as a special character:
    mock_ask_user.side_effect = ["a bc", "a3c", "abc"]  # in the end "abc" is provided so the code wont quit
    # check if it works for a word
    assert check_user_input(r"%abc") == "abc".lower()


    # check if it does throw error for numbers
    # assert check_user_input("hi1kasüäö") == False
    # # check if special signs throw and error
    # assert check_user_input("kl%") == False



