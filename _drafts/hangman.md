---
layout: post
title: Hangman
subtitle: A teaching opportunity
meta: The results of teaching my girlfriend Python.
---

<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

So now you've learned the syntax of Python, and are now ready for something else. Something harder. Something that will take the rest of your life to master. Now it's time for *actually doing something useful* with your code. This is the hardest part of programming. It's easy to learn the syntax of a language (unless you're learning [APL](https://en.wikipedia.org/wiki/APL_(programming_language))), but being able to translate problems into solutions is something that will take *significant* time and energy, regardless of whether you are using code, mathematics, or some other toolset.

The purpose of this post is to provide an outline for building a small Python project for the Python beginner. The game of Hangman is a fairly popular project for programming beginners for the following reasons:

* It's approachable -- the learner is likely already familiar with Hangman
* It's rewarding -- the learner gets to see the results

I will not be teaching any *syntax* -- the rules of the Python language -- in this tutorial. Instead, we're going to focus on the harder parts.

---

## Define:

Before we can write a program that does *anything*, we *must* first **define** what we want it to accomplish. Not doing so is an extremely common mistake we programmer folk make -- we often jump head first into a problem, trying to come up with a solution to a problem we don't even fully understand.

Therefore, here's the definition of our game.

* The game shall pick a random `target_word` from a predefined `word_bank`
* The game shall display an underscore for each letter in the `target_word`
* The game shall repeatedly prompt the user for letter guesses until they "hang" their man or correctly guess the `target_word`
    - On correct guesses:
        * The game shall indicate the guess was correct
        * The game shall display the `guess_word` -- which is the `target_word` filled out with correctly guessed letters, and underscores for unguessed letters
    - On incorrect guesses:
        * The game shall indicate the guess was incorrect
        * The game shall penalize the player by "hanging" an additional "body part"
    - On all guesses:
        * The game shall display the current state of the "hangman" and the `guess_word`
* Once play is finished:
    - If the user won:
        * The game shall congratulate the user
    - If the user lost:
        * The game shall display the `target_word` and the `guess_word`

---

## Design:

Another very common mistake among new programmers and old programmers alike is to immediately jump into their favorite code editor and start writing. This is where new programmers stall, and where old programmers make poor design decisions. The very first thing we need to do before writing any code is to **design** our product.

The word "design" means something very specific. The dictionary gives the following definition

> Design.
>
> 1. n. A plan or drawing produced to show the look and function or workings of (a building, garment, or other object) before it is built or made.
>
> 2. v. To decide upon the look and functioning of (a building, garment, or other object), typically by making a detailed drawing of it.

So let's go ahead and design our program.

### Flowcharts:

Not everyone likes using flowcharts, but that's what I'm going to use for this project because they tend to be more clear. Before we jump in though, I want to explain how to read and use a flowchart. The following is a simple flowchart that contains all of the symbols I will use.

<img class="centered" src="{{ "/assets/posts/hangman/flowchart1.svg" | prepend: site.baseurl }}" alt="An example flowchart">

The <img class="inline" src="{{ "/assets/posts/hangman/flowchart-start.svg" | prepend: site.baseurl }}" alt="Flowchart start symbol"> symbol represents the start of a program. The program will run until it reaches a <img class="inline" src="{{ "/assets/posts/hangman/flowchart-stop.svg" | prepend: site.baseurl }}" alt="Flowchart stop symbol"> symbol. This example program will ask for some form of input when it reaches an <img class="inline" src="{{ "/assets/posts/hangman/flowchart-input.svg" | prepend: site.baseurl }}" alt="Flowchart input symbol"> symbol. This input could be a commandline prompt, reading from a file, fetching a webpage, getting a button press, or any number of other forms of input. Similarly, the program will output some kind of information when it reaches an <img class="inline" src="{{ "/assets/posts/hangman/flowchart-output.svg" | prepend: site.baseurl }}" alt="Flowchart output symbol"> symbol. Again, this could be printing a message to the terminal, writing to a file, midifying a webpage, sending an email, lighting up an LED, or some other form of output. A <img class="inline" src="{{ "/assets/posts/hangman/flowchart-process.svg" | prepend: site.baseurl }}" alt="Flowchart process symbol"> symbol means the program does something at that point. It calls a function, performs some mathematical operation, generates a random number, or something else. Finally, we have the <img class="inline" style="height: 35pt !important" src="{{ "/assets/posts/hangman/flowchart-decision.svg" | prepend: site.baseurl }}" alt="Flowchart decision symbol"> symbols. These are where decisions are made. They don't have to be yes or no decisions, they could very well be something like the following

<img class="centered" src="{{ "/assets/posts/hangman/flowchart2.svg" | prepend: site.baseurl }}" alt="Another example flowchart">

### Hangman:

At its core, our program will have to start up, pick a random word, and start asking the user for input. We can start with a simple flowchart that shows this, and then add to it later.

<img class="centered" src="{{ "/assets/posts/hangman/hangman1.svg" | prepend: site.baseurl }}" alt="Another example flowchart">

Let's start at the top and work down.

1. The program begins
2. The program picks a `target_word`
3. The program asks the user for a guess
4. The program validates the user guess. A guess is invalid if:
    * It has already been guessed
    * It is not a single character
    * It is not in the alphabet

    These rules can be fairly flexible. For example, you could allow your `target_word` to include punctuation and numerals, you could penalize the user for guessing a number twice, or you could even guess multiple characters at a time. I would recommend sticking with these rules for now though, and extending them later.

    Another thing that this validation routine should do is convert the guess to uppercase or lowercase (your choice), so that guessing `A` is the same as guessing `a`.
5. If the guess is valid, the `guess_word` needs to be updated and displayed, and the hangman should be updated and displayed.
6. The program then determines if the game is won, lost, or still in progress. As long as the game is still in progress it loops back to the top and asks for a user guess again. Otherwise, the game is over.

---

## Implement:

Now that we have at least one design for our problem, it is now time to **implement** them. I'm going to give *my* implementation, but please realize -- there's more than one way to skin a cat -- you're welcome to try things your way.

* Overall structure:

    Let's build the program skeleton first. Everywhere the `pass` keyword is used is something you need to write yourself. If you're new to programming, I suggest you start with this skeleton, and try to fill it out yourself. However, if you'd like more of a challenge, try writing your own skeleton, and compare it when you're done.

    ```python
    #!/usr/bin/python3
    import os
    import random
    import sys


    def pick_random_word(filename):
        """Picks a random word from a given file"""
        pass


    def get_valid_input(guesses):
        """Prompts the user for valid input"""
        pass


    def is_guess_correct(guess, target_word):
        """Determines if the user guess is correct"""
        pass


    def determine_game_state(target_word, guesses):
        """Determines if the game has been won, lost, or if it is still in progress"""
        pass


    def display_guess_word(target_word, guesses):
        """Given the target word and the user guesses, displays the guess word"""
        pass


    def display_hangman(num_body_parts):
        """Given a number of body parts, displays the hangman"""
        pass


    def main(filename):
        """Runs the game"""
        target_word = pick_random_word(filename)
        guesses = set()
        game_state = None

        while game_state is None:
            try:
                # Game logic goes here
                pass
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
    ```

    Try to go no further unless you get stuck. There are many ways to write this, and your solution will most liekyl be different than mine, and that's okay.

* Picking a random `target_word` from a file:

    It's quite easy to pick a random item from a list, so we should focus on converting a file of words into a list of words.

    ```python
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
    ```

* Getting valid user input:

    ```python
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
    ```

* Determining if a valid guess is correct:

    ```python
    def is_guess_correct(guess, target_word):
        """Determines if the user guess is correct"""
        return guess in target_word
    ```

* Determining the game state:

    ```python
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
    ```

* Filling out the `guess_word` from the current guesses and the `target_word`:

    ```python
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
    ```

* Displaying the hangman. This was the hardest part for me.

    ```python
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
    ```

    If you're trying to write this yourself, a suitable alternative while you're trying to get your program working might be something like the following:

    ```python
    def display_hangman(num_body_parts):
        """Given a number of body parts, displays the hangman"""
        print('You have hung', num_body_parts, 'of your hangman!')
    ```

* Tying everything together in the `main` function:

    ```python
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
    ```

---

## Review:

Now we have a product. Yay. You worked for it, struggled, and eventually achieved your goal. But you're not done yet. Design is *never finished until you **review** your design*, and implement any bug fixes and feature improvements. See [Iterative Design](https://en.wikipedia.org/wiki/Iterative_and_incremental_development) for more information.

For example, when I reviewed my design, an improvement I wanted to make was the ability to use phrases in my target "word". See if you can improve your program somehow.
