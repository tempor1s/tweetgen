from sys import argv
from random import choice, randint
from lib.utils import time_it


@time_it
def get_words_from_file(path):
    """
    Get words from a file

    Params:
        path: str - The path to the file that you want to read from. Can also be a file name

    Returns:
        list: A list of all the words in that file
    """
    with open(path, 'r') as f:
        return f.read().split('\n')


@time_it
def get_set_words_from_file(path):
    """
    Get all the words from a file as a set

    Params:
        path: str - The path to the file that you want to read from. Can also be the file name

    Returns:
        set: A set of all the words in that file
    """
    return set(line.strip() for line in open('/usr/share/dict/words'))


@time_it
def get_random_words(num, path):
    """
    Get x amount of random words from a file

    Params:
        num: int - The amount of words that you want to get
        path: str - The path to the file that you want to read from. Can also be the file name

    Returns: str - A string with the first letter capatalized and a period at the end. 'Sudo sentence'
    """
    words = get_words_from_file(path)

    random_words = []
    for i in range(int(num)):
        random_words.append(choice(words))
    return ' '.join(random_words).capitalize() + '.'


def get_random_word(path="/usr/share/dict/words"):
    """
    Get a single random word from a file

    Params:
        path: str - The path to the file you want to read from. Can also be a file name

    Returns:
        str: The random word
    """
    return choice(get_words_from_file(path))


if __name__ == '__main__':
    args = argv[1:3]
    path = '/usr/share/dict/words'
    words = get_random_words(args[0], path)
