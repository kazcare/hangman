import random
from word import WORD_LIST

AQUA_COLOR = '\033[96m'
RED_COLOR = '\033[0;31m'
YELLOW_COLOR = '\033[1;33m'
GREEN_COLOR = '\033[0;32m'
BLUE_COLOR = '\033[0;34m'


def welcome_user():
    """
    This function allows user to input their name.
    user cannot user numbers
    username must have characters only
    """

    print(AQUA_COLOR + '****************************************************')
    print(YELLOW_COLOR + '           | H | A | N | G | M | A | N |          ')
    print(GREEN_COLOR + '       Try to guess the word to win the game')
    print(AQUA_COLOR + '****************************************************')
    username = None

    while True:
        username = input(f'{YELLOW_COLOR}Enter your name: ')

        if not username.isalpha():
            print(f'{YELLOW_COLOR}Username must be alphabets only')
            continue
        else:
            print(f'{YELLOW_COLOR}welcome {username}')
            break
    print(
        '\n'
        f'{GREEN_COLOR}How to Play: \n\n'
        f'The aim is to make the correct word by guessing '
        'the letters one at a time. \n\n'
        f'1. To guess, type a letter of your choice and hit enter.\n'
        f'2. If you are right the letter will appear on screen.\n'
        f'3. If you are wrong the hangman will start to appear.\n'
        f'4. You have 6 attempts to guess correctly or Game Over!!\n'
        f'5. If you have any issues please hit the Run Program Button!!\n'
    )


def get_word():
    """
    Get a random word from the list of words
    """
    word = random.choice(WORD_LIST)
    return word.upper()


def display_hangman(attempts):
    """
    Hangman images to show after every failed guess
    """
    STAGES = [
        RED_COLOR + """
             ________
            |       |
            |       O
            |      /|\\
            |      / \\
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |       O
            |      /|\\
            |      /
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |       O
            |      /|\\
            |
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |       O
            |      /|
            |
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |       O
            |       |
            |
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |       O
            |
            |
            |____________
            """,
        RED_COLOR + """
             ________
            |       |
            |
            |
            |
            |____________
            """
    ]
    return STAGES[attempts]


def play_game(word):
    """
    Play function
    Loop to keep going until either the word is guessed
    or the attempts/ tries are expired
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries_remaining = 6

    print(f"{YELLOW_COLOR}Let's play Hangman!")
    print(display_hangman(tries_remaining))
    print(word_completion)
    print('\n')
    while not guessed and tries_remaining > 0:
        guess = input(f'{BLUE_COLOR} Please guess a letter: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'{YELLOW_COLOR}You already guessed the letter {guess}')
            elif guess not in word:
                print(f'{RED_COLOR}Sorry! {guess} is not in the word.')
                tries_remaining -= 1
                guessed_letters.append(guess)
            else:
                print(f'{GREEN_COLOR}Good job, {guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print(f'{YELLOW_COLOR}SORRY! {guess} is not a valid character')
        print(display_hangman(tries_remaining))
        print(f'{RED_COLOR}{tries_remaining} attempts are remaining.')
        print('\n')
        print(word_completion)
        print('\n')
    if guessed:
        print(f'{GREEN_COLOR}\n|W|E| |H|A|V|E| |A| |W|I|N|N|E|R|')
        print(f'{GREEN_COLOR}You have guessed the word: {word}.\n')
    else:
        print(f'{RED_COLOR}\n | S | O | R | R | Y |')
        print(f'{RED_COLOR}The word was {word}. You didn"t win it this time.')
        print(f'{RED_COLOR}Try Again!\n')


def main():
    """
    Main function to call main functions
    """
    welcome_user()
    word = get_word()
    play_game(word)
    while input(f'{BLUE_COLOR}Play Again? (Y/N): ').upper() == "Y":
        word = get_word()
        play_game(word)
    else:
        print('Thank you for taking time to play Hangman.')


if __name__ == "__main__":
    main()
