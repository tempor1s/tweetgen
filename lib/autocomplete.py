from dictionary_words import get_words_from_file
from sys import argv
import random


def autocomplete(s):
    """
    Get all words that start with a certain string. Basic autocomplete

    Params:
        s: str - The string that you want to 'autocomplete'

    Returns:
        list: List of all the words that start with the given string
    """
    words = get_words_from_file('/usr/share/dict/words')
    return [w for w in words if w.startswith(s)]

    # ret = []
    # for word in words:
    #     sub_str = word[:len(s)]
    #     if s == sub_str:
    #         ret.append(word)

    # return ret


if __name__ == '__main__':
    args = argv[1:3]
    print(autocomplete(args[0]))
