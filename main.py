import random

# List of words that you can guess:
word_list = ["programming", "python", "guess", "hangman", "game", "keyboard", "computer", "developer", "algorithm"]

# random choice of word:
random_word = random.choice(word_list)

# Initializing the variables:
turns = 12
guessed_letters = []
correct_guesses = ['_'] * len(random_word)

# Players name:
player_name = input("Type your name: ")

# Welcome the player:
print("\nWelcome, {}:) You are now playing the Word Guessing Game.".format(player_name))

while turns > 0:
    # Displaying the current progress of the player:
    print("Word: " + " ".join(correct_guesses))

    # Ask the player to guess a random letter:
    guess = input("Take a guess at your random letter: ").lower()

    # Is the letter valid?
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. please only enter one alphabet at a time.")
        continue

    # Is the letter already guessed?
    if guess in guessed_letters:
        print("This letter is already guessed.")
        continue

    # Get the guessed letters in a list:
    guessed_letters.append(guess)

    # Check if the letter the player guessed is in the word:
    if guess in random_word:
        print("Correct, You are a genius!")
        # Update the correct_guesses, with the letters that are correctly guessed:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                correct_guesses[i] = guess
    else:
        print("Incorrect :(")
        turns -= 1

    # Check if the word is successfully guessed by the player:
    if '_' not in correct_guesses:
        print("\nCongrats, {}! You guessed the right word, the word was: '{}'".format(player_name, random_word))
        break

    print("Tries left: {}".format(turns))
    print("Letters that are already guessed: {}".format(", ".join(guessed_letters)))
    print("\n" + "-" * 30)

# If the player fails to guess the correct word, send a "Game Over" message:
if turns == 0:
    print("\nSorry, {}! You've run out of turns. The word was '{}'.".format(player_name, random_word))
