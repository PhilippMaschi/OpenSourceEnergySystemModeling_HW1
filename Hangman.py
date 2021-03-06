from typing import List


# user input one word
def ask_user() -> str:
    """
    Returns the user input as a string in lowercase
    :rtype: str
    """
    user_input = input("Type a word that needs to be guessed \n"
                       "don't use space, numbers or special characters: \n")
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    return user_input.lower()


def check_user_input(user_input: str) -> str:
    """
    checks if the user input is of a word and does not contain special characters, blanks or numbers.
    If so the user is asked again to give an input. After 3 failed attempts to provide a word, the program stops.
    :param user_input: str
    :return: str
    """
    count = 0
    while True:
        # check if the word is actually a word:
        if not user_input.isalpha():  # if its not a word, ask again
            print("That was not a word, try again")
            user_input = ask_user()
            # after 3 attempts end the game:
            if count == 3:
                print("you are incapable of typing a single word")
                quit()
            count += 1
        else:  # if it is a word, break the loop
            break
    return user_input.lower()


def guess(word_list: List[str], check_list: List[bool]) -> str:
    """
    The user us asked to type in one letter as a guess. It is being checked if the letter is contained in the word.
    :rtype: str
    """
    guess = input("Guess one letter: \n").lower()
    # check if guess was correct:
    if guess in word_list:
        # update the check_list
        for index, letter in enumerate(word_list):
            if letter == guess:
                check_list[index] = True
        return "That is correct, this letter is in the word"

    else:
        return "No, this letter is not in the word"


def print_word(word_list: List[str], check_list: List[bool]) -> str:
    """
    prints the letters that have not been guessed as underscores and the letters that have already been guessed
    :param word_list: list of single letters
    :param check_list: list of bools describing if the letters already have been guessed
    :return: str
    """
    # create string with only the letters that already have been guessed
    underscore_string = ""
    for index, letter in enumerate(word_list):
        if check_list[index]:  # if corresponding bool in check list is true, than print the letter
            underscore_string += letter
        else:
            underscore_string += "_"
    return underscore_string


def main():
    word = ask_user()
    # check if user input is correct
    word = check_user_input(word)
    # create a dictionary that withholds the status of the letters that have been guessed correctly:
    word_list = [letter for letter in word]
    check_list = [False for letter in word]
    # while loop to play the game:
    while True:
        print(
            guess(word_list=word_list,
                       check_list=check_list)
        )
        print(
            print_word(word_list=word_list,
                       check_list=check_list)
        )

        # check if the game is over
        if all(value == True for value in check_list):
            print("well done!")
            break


if __name__ == "__main__":
    main()
