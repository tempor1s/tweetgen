from sys import argv
from random import choice, randint
from utils import time_it
from linecache import getline


@time_it
def get_dict_words(num):
    """Get x amount of random words from the file"""
    # Commented out are other implementations to try to be faster using caching an
    path = "/usr/share/dict/words"
    with open(path, "r") as f:
        all_words = f.read().split('\n')
        random_words = []
        for i in range(int(num)):
            random_words.append(choice(all_words))
        return ' '.join(random_words) + '.'

        # all_words = dict((x, x) for x in f.read().split('\n'))
        # random_words = []
        # for i in range(int(num)):
        #     random_words.append(choice(list(all_words.keys())))
        # return ' '.join(random_words) + '.'
    

    # This in theory is the fastest because of caching, but would have to get length of file or hardcode it
    # rand_words = []
    # for i in range(int(num)):
    #     word = getline(path, randint(0, 200000))[:-1]
    #     rand_words.append(word)
    # return ' '.join(rand_words) + '.'



if __name__ == '__main__':
    # Only get 1 arg and then convert it to int to get that amount of words
    args = argv[1:3]
    words = get_dict_words(args[0])
    print(words)