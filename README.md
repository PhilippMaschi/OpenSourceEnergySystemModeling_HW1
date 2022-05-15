# OpenSourceEnergySystemModeling_HW1
first homework for the course Open Source Energy System Modeling 2022

A very simple hangman game. Start the program, type in a word and then guess single letters. The 
program terminates when all letters are guessed correctly.

Functions:

ask_user: asks the user for an input and returns the input as lower case. This will be the 
    Hangman-word which has to be guessed.

check_user_input: checks if the user input returned by the ask_user function only 
    contains letters. If not, the ask_user function is called again. After 3 failed attempts the
    of typing a word without numbers or special characters, the program quits.

guess: asks the user for a letter as input and checks if this letter is in the Hangman-word. 
    Returns a feedback to the user (string).

print_word: after each guess the letters of the Hangman-word are printed as underscores. Letters
    that have been guessed correctly already are displayed.




