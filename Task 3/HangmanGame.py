import random
wordslist = [
        'quantum', 'cybersecurity', 'encryption', 'cloud', 'orange', 'universe', 'octopus', 'grape', 'awkward',
        'rhythm','artificial', 'butterfly','papaya', 'freedom', 'crocodile', 'parrot', 'flamingo', 'ostrich',
        'banana', 'database', 'galaxy', 'squirrel', 'giraffe','oxygen', 'mango', 'dolphin', 'kangaroo', 'robotics',
        'nanotechnology', 'mirror', 'justice', 'hippopotamus', 'bandwidth','algorithm', 'puzzle', 'alligator',
        'blockchain', 'zebra', 'gorilla', 'cherry', 'hedgehog', 'penguin', 'kiwi', 'apple','cheetah', 'peach',
        'automation', 'elephant', 'watermelon', 'tiger', 'lion', 'software', 'unique','firewall', 'processor'
]

# Hangman stages
HANGMAN_PICS = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
]


def get_random_word(word_list):
    # select a random word from the list
    return random.choice(word_list)


def display_game_state(hangman_pics, incorrect_guesses, correct_guesses, secret_word):
    print(hangman_pics[len(incorrect_guesses)])
    if incorrect_guesses:
        print("\nIncorrect guesses:", " ".join(incorrect_guesses))

    # Display guessed letters and underscores
    display_word = [letter if letter in correct_guesses else '_' for letter in secret_word]
    print("Word: ", " ".join(display_word))

def play_hangman():
    """Main function to play a round of Hangman."""
    secret_word = get_random_word(wordslist)
    incorrect_guesses = []
    correct_guesses = set()
    max_attempts = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")

    while True:
        display_game_state(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)

        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        elif guess in incorrect_guesses or guess in correct_guesses:
            print("You've already guessed that letter. Try another one.")
            continue

        # Check if the guessed letter is in the word
        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")

            # Check for win condition
            if all(letter in correct_guesses for letter in secret_word):
                display_game_state(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)
                print("\nCongratulations! You've guessed the word correctly!")
                break
        else:
            incorrect_guesses.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")

            # Check for loss condition
            if len(incorrect_guesses) == max_attempts:
                display_game_state(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)
                print("\nGame over! You've run out of guesses.")
                print(f"The word was: {secret_word}")
                break


def main():
    """Main game loop to play multiple rounds if desired."""
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman! Goodbye!")
            break


if __name__ == "__main__":
    main()
