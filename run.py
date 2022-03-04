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
    'behaviour'
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





def main():
    """
    Main function to call main functions
    """
    word = get_word()
    