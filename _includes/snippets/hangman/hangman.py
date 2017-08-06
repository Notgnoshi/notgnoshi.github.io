#!/usr/bin/python3
import os
import random
import sys


def pick_random_word(filename):
    """Picks a random word from a given file"""
    # Create word bank.
    word_bank = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            # Strip line of surrounding whitespace and convert to lowercase.
            word = line.strip()
            word = word.lower()
            # Add word to word bank.
            word_bank.append(word)

    print('Loading', len(word_bank), 'words from', filename)

    # Pick random item from the word bank.
    return random.choice(word_bank)


def get_valid_input(guesses):
    """Prompts the user for valid input"""
    while True:
        # Get a user guess and convert it to lowercase.
        user_guess = input('Enter a guess: ')
        user_guess = user_guess.lower()
        # Valid user guesses are one character long and alphabetic.
        if len(user_guess) == 1 and user_guess.isalpha():
            # Check if the validated guess has already guessed.
            if user_guess in guesses:
                print('Already guessed:', user_guess)
            # If it hasn't already been guessed, return it.
            else:
                return user_guess
        # If the user gives invalid input, return to the top of the loop.
        else:
            print('Invalid input')


def is_guess_correct(guess, target_word):
    """Determines if the user guess is correct"""
    return guess in target_word


def determine_game_state(target_word, guesses):
    """Determines if the game has been won, lost, or if it is still in progress"""
    # Convert the target word into a set of target characters.
    target_set = set(target_word)
    # The elements of guesses that are not in target_set.
    incorrect_guesses = guesses.difference(target_set)

    # The user has incorrectly guessed too many times. The game has been lost.
    if len(incorrect_guesses) >= 6:
        return False
    # If every character in the target word is an element of guesses, the game has been won.
    if target_set.issubset(guesses):
        return True
    # Otherwise the game is still in progress
    else:
        return None


def display_guess_word(target_word, guesses):
    """Given the target word and the user guesses, displays the guess word"""
    guess_word = ""
    for character in target_word:
        # If the character has been guessed, add it to the guess word.
        if character in guesses:
            guess_word += character
        # Otherwise, fill in the character with an underscore.
        else:
            guess_word += '_'

    print(guess_word)


def display_hangman(num_body_parts):
    """Given a number of body parts, displays the hangman"""
    # An empty gallows.
    HANGMAN = "    ||============|      \n" \
              "    ||            |      \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "======================   \n"
    # A completely hung man.
    HUNGMAN = "    ||============|      \n" \
              "    ||            |      \n" \
              "    ||            O      \n" \
              "    ||           \\ /    \n" \
              "    ||            |      \n" \
              "    ||           / \\    \n" \
              "    ||                   \n" \
              "    ||                   \n" \
              "======================   \n"
    # The start and end indices of the bodyparts.
    HEAD_START = 26 * 2 + 18
    HEAD_END = HEAD_START + 1
    LEFT_ARM_START = 26 * 3 + 18
    LEFT_ARM_END = LEFT_ARM_START + 1
    RIGHT_ARM_START = LEFT_ARM_END + 1
    RIGHT_ARM_END = RIGHT_ARM_START + 1
    TORSO_START = 26 * 4 + 18
    TORSO_END = TORSO_START + 1
    LEFT_LEG_START = 26 * 5 + 17
    LEFT_LEG_END = LEFT_LEG_START + 1
    RIGHT_LEG_START = LEFT_LEG_END + 1
    RIGHT_LEG_END = RIGHT_LEG_START + 1

    # Feel free to add more body parts!
    if num_body_parts is 0:
        print(HANGMAN)
    elif num_body_parts is 1:
        print(HUNGMAN[:HEAD_END] + HANGMAN[HEAD_END:])
    elif num_body_parts is 2:
        print(HUNGMAN[:LEFT_ARM_START] + HANGMAN[LEFT_ARM_END:])
    elif num_body_parts is 3:
        print(HUNGMAN[:RIGHT_ARM_START] + HANGMAN[RIGHT_ARM_END:])
    elif num_body_parts is 4:
        print(HUNGMAN[:TORSO_START] + HANGMAN[TORSO_END:])
    elif num_body_parts is 5:
        print(HUNGMAN[:LEFT_LEG_START] + HANGMAN[LEFT_LEG_END:])
    elif num_body_parts is 6:
        print(HUNGMAN)
    else:
        print(HUNGMAN)


def main(filename):
    """Runs the game"""
    target_word = pick_random_word(filename)
    target_set = set(target_word)
    guesses = set()
    incorrect_guesses = set()
    game_state = None

    # Display an empty gallows.
    display_hangman(0)

    while game_state is None:
        try:
            # Get a valid user guess
            user_guess = get_valid_input(guesses)

            # Add the user guess to the set of guesses.
            guesses.add(user_guess)

            # Determine if the user guess is incorrect.
            if not is_guess_correct(user_guess, target_word):
                incorrect_guesses.add(user_guess)

            # Clear the screen before drawing the hangman.
            os.system('cls||clear')

            # Find the number of incorrect guesses and display that many body parts.
            display_hangman(len(incorrect_guesses))
            # Display the guess word.
            display_guess_word(target_word, guesses)
            # Determine the game state.
            game_state = determine_game_state(target_word, guesses)

        except KeyboardInterrupt:
            break

    # Game is over, give commentary to user.
    if game_state is True:
        print('You\'ve won! Thank you for playing!')
    elif game_state is False:
        print('I\'m sorry, it appears you have lost :(')
        print('The word you were looking for was', target_word)


if __name__ == '__main__':
    # If no commandline arguments are given, use a default file.
    if len(sys.argv) < 2:
        DEFAULT_WORD_LIST = 'hangman.txt'
        print('Running', sys.argv[0], 'on default word list found in', DEFAULT_WORD_LIST)
        main(DEFAULT_WORD_LIST)
    # Otherwise, use the user specified file.
    else:
        main(sys.argv[1])
