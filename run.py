import random

word_list = [
    'alarming',
    'engineer',
    'collect',
    'confirmation',
    'greeting',
    'mechanic',
    'jubilee',
    'success',
    'current',
    'behaviour',
    'elephant',
    'technology',
    'energy',
    'archeology',
    'aeroplane',
    'toucan',
    'chemistry',
    'biology',
    'scorpion',
    'physics'
]


def get_word():
    """
    Get a random word from the list of words
    """
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    """
    Hangman images to show after every failed guess
    """
    stages = [
        """\033[0;31m
             ________
            |       |
            |       O
            |      /|\\
            |      / \\
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |       O
            |      /|\\
            |      /
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |       O
            |      /|\\
            |
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |       O
            |      /|
            |
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |       O
            |       |
            |
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |       O
            |
            |
            |____________
            """,
        """\033[0;31m
             ________
            |       |
            |
            |
            |
            |____________
            """
    ]
    return stages[tries]


def play(word):
    """
    Play function
    Loop to keep going until either the word is guessed
    or the attempts/ tries are expired
    """
    print("\033[0;31m*****************************************************")
    print("\033[1;33m            | H | A | N | G | M | A | N |           ")
    print("\033[0;32m       Try to guess the word to win the game")
    print("\033[0;31m*****************************************************")

    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("\033[0;36mLet's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("\033[0;34mPlease guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"\033[0;33mYou already guessed the letter, {guess}")
            elif guess not in word:
                print(f"\033[0;31mSorry! {guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"\033[0;32mGood job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print(f"\033[0;33mSORRY! {guess} is not a valid character")
        print(display_hangman(tries))
        print(f"\033[0;31m{tries} attempts are remaining.")
        print("\n")
        print(word_completion)
        print("\n")
    if guessed:
        print("\033[0;32m\n|W|E| |H|A|V|E| |A| |W|I|N|N|E|R|")
        print(f"Congratulations! You have guessed the word: {word}.\n")
    else:
        print("\033[0;31m\n | S | O | R | R | Y |")
        print(f"The word was {word}. You didn't win it this time.")
        print("\033[0;31mTry Again!\n")


def main():
    """
    Main function to call main functions
    """
    word = get_word()
    play(word)
    while input("\033[0;34mPlay Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
