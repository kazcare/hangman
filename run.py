import random

WORD_LIST = [
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


def welcome_user():
    """
    This function allows user to input their name.
    user cannot user numbers
    username must have characters only
    """

    print("\033[0;31m*****************************************************")
    print("\033[1;33m            | H | A | N | G | M | A | N |           ")
    print("\033[0;32m       Try to guess the word to win the game")
    print("\033[0;31m*****************************************************")
    username = None

    while True:
        username = input('\033[1;33m Enter your name: ')

        if not username.isalpha():
            print('Username must be alphabets only')
            continue
        else:
            print(f"\033[1;33m welcome {username}")
            break


def get_word():
    """
    Get a random word from the list of words
    """
    word = random.choice(WORD_LIST)
    return word.upper()


def display_hangman(tries):
    """
    Hangman images to show after every failed guess
    """
    STAGES = [
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
    return STAGES[tries]


def play_game(word):
    """
    Play function
    Loop to keep going until either the word is guessed
    or the attempts/ tries are expired
    """
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
    welcome_user()
    word = get_word()
    play_game(word)
    while input("\033[0;34mPlay Again? (Y/N): ").upper() == "Y":
        word = get_word()
        play_game(word)
    else:
        print('Thank you for taking time to play Hangman.')



if __name__ == "__main__":
    main()
