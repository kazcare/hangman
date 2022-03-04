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







def main():
    """
    Main function to call main functions
    """
    word = get_word()
    