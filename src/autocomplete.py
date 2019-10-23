from dictionary_words import get_words_from_file
from utils import time_it
from sys import argv
import random


@time_it
def autocomplete(s):
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
