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


@patch("Hangman.input", return_value="h")
def test_guess_true(self):
    word_list = [letter for letter in "haalloo"]
    check_list = [False, False, False, True, True, False, False]
    assert guess(word_list, check_list) == "That is correct, this letter is in the word"


@patch("Hangman.input", return_value="x")
def test_guess_false(self):
    word_list = [letter for letter in "haalloo"]
    check_list = [True, False, False, True, True, False, False]
    assert guess(word_list, check_list) == "No, this letter is not in the word"


def test_print_word():
    word_list = [letter for letter in "haalloo"]
    check_list = [True, False, False, True, True, False, False]
    assert print_word(word_list, check_list) == "h__ll__"


