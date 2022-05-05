from Hangman import check_word, ask_user, guess, print_word


def test_check_word():
    # check if it works for a word
    assert check_word("Lausbua")
    # check if it does throw error for numbers
    assert check_word("hi1kasüäö") == False
    # check if special signs throw and error
    assert check_word("kl%") == False

