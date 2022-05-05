def check_word(string: str) -> bool:
    # check if numbers, special chars or spaces are in the string
    if string.isalpha():
        return True
    else:
        return False


# user input one word
def ask_user() -> str:
    user_input = input("Type a word that needs to be guessed \n"
                       "don't use space, numbers or special characters: \n")
    while True:
        # check if the word is actually a word:
        if not check_word(user_input):  # if its not a word, ask again
            print("That was not a word, try again")
            user_input = ask_user()
        else:  # if it is a word, break the loop
            break
    return user_input.lower()


def guess(word: str, word_dict: dict) -> None:
    guess = input("Guess one letter: \n").lower()
    # check if guess was correct:
    if guess in word:
        # update the word_dict
        word_dict[guess] = True
        print("That is correct, this letter is in the word")
    else:
        print("No, this letter is not in the word")


def print_word(word_dict: dict) -> None:
    # create string with only the letters that already have been guessed
    underscore_string = ""
    for letter, status in word_dict.items():
        if status:
            underscore_string += letter
        else:
            underscore_string += "_"
    print(underscore_string)


def main():
    word = ask_user()
    # create a dictionary that withholds the status of the letters that have been guessed correctly:
    word_dict = {letter: False for letter in word}
    # while loop to play the game:
    while True:
        guess(word=word,
              word_dict=word_dict)
        print_word(word_dict=word_dict)

        # check if the game is over
        if all(value == True for value in word_dict.values()):
            print("well done!")
            break


if __name__ == "__main__":
    main()
