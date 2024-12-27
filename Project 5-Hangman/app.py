import random
import string
from words import words

def get_valid_value(words):
    # Get a valid word (no spaces or hyphens) and convert to uppercase
    word = random.choice(words)
    while '-' in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    # Select a random valid word
    word = get_valid_value(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    used_letter = set()  # Letters guessed by the user

    # Assign lives based on word length
    if len(word) > 10:
        lives = 15
    elif len(word) >= 5:
        lives = 10
    else:
        lives = 5

    # Initialize guess counters
    correct_guesses = 0
    wrong_guesses = 0

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: {' '.join(used_letter)}")

        # Show the current state of the word
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Prompt the user to guess a letter
        user_letter = input("Guess the letter: ").upper()

        # Valid guess
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                correct_guesses += 1
            else:
                lives -= 1
                wrong_guesses += 1
                print("Letter is not in the word.")

        # Letter already guessed
        elif user_letter in used_letter:
            print(f"{user_letter} has already been guessed. Please try again.")

        # Invalid character
        else:
            print("Invalid character. Please try again.")

    # End of game
    if lives == 0:
        print(f"You died, sorry. The word was {word}.")
    else:
        print(f"You guessed the word {word}!")

    # Display guess statistics
    print(f"You made {correct_guesses} correct guesses and {wrong_guesses} wrong guesses.")

# Run the game
hangman()
