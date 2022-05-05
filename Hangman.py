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
    return user_input.lower()


word = ask_user()
while True:
    # check if the word is actually a word:
    if not check_word(word):  # if its not a word, ask again
        print("That was not a word, try again")
        word = ask_user()
    else:  # if it is a word, break the loop
        break

# create a dictionary that withholds the status of the letters that have been guessed correctly:
word_dict = {letter: False for letter in word}


def guess() -> None:
    guess = input("Guess one letter: \n").lower()
    # check if guess was correct:
    if guess in word:
        # update the word_dict
        word_dict[guess] = True
        print("That is correct, this letter is in the word")
    else:
        print("No, this letter is not in the word")


def print_word() -> None:
    # create string with only the letters that already have been guessed
    underscore_string = ""
    for letter, status in word_dict.items():
        if status:
            underscore_string += letter
        else:
            underscore_string += "_"
    print(underscore_string)


# while loop to play the game:
while True:
    guess()
    print_word()

    # check if the game is over
    if all(value == True for value in word_dict.values()):
        print("well done!")
        break
