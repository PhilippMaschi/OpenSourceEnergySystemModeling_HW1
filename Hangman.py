from typing import List


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
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    return user_input.lower()


def check_user_input(user_input: str) -> str:
    count = 0
    while True:
        count += 1
        # check if the word is actually a word:
        if not check_word(user_input):  # if its not a word, ask again
            print("That was not a word, try again")
            user_input = ask_user()
            # after 3 attempts end the game:
            if count == 3:
                print("you are incapable of typing a single word")
                quit()
        else:  # if it is a word, break the loop
            break
    return user_input.lower()


def guess(word: str, word_list: List[str], check_list: List[bool]) -> None:
    guess = input("Guess one letter: \n").lower()
    # check if guess was correct:
    if guess in word:
        print("That is correct, this letter is in the word")
        # update the check_list
        for index, letter in enumerate(word_list):
            if letter == guess:
                check_list[index] = True

    else:
        print("No, this letter is not in the word")


def print_word(word_list: List[str], check_list: List[bool]) -> None:
    # create string with only the letters that already have been guessed
    underscore_string = ""
    for index, letter in enumerate(word_list):
        if check_list[index]:  # if corresponding bool in check list is true, than print the letter
            underscore_string += letter
        else:
            underscore_string += "_"
    print(underscore_string)


def main():
    word = ask_user()
    # check if user input is correct
    word = check_user_input(word)
    # create a dictionary that withholds the status of the letters that have been guessed correctly:
    word_list = [letter for letter in word]
    check_list = [False for letter in word]
    # while loop to play the game:
    while True:
        guess(word=word,
              word_list=word_list,
              check_list=check_list)

        print_word(word_list=word_list,
                   check_list=check_list)

        # check if the game is over
        if all(value == True for value in check_list):
            print("well done!")
            break


if __name__ == "__main__":
    main()
