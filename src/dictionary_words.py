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
        all_words = f.read().split('\n')  # .readlines()  or .readline() in a for loop
        random_words = []
        for i in range(int(num)):
            random_words.append(choice(all_words))
        return ' '.join(random_words).capitalize() + '.'

        # Work on this a bit more and try different variations
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


def get_words_from_file(path):
    # Fastest version of reading from file
    with open(path, 'r') as f:
        return f.read().split('\n')
    # This version is about 60ms slower every time - better space complexity i assume because doesnt have to store as string then convert to arr
    # with open(path, 'r') as f:
    #     return f.readlines()


@time_it
def get_set_words_from_file(path):
    # Use a generator to put all lines into a set and return
    return set(line.strip() for line in open('/usr/share/dict/words'))


@time_it
def get_random_words(num):
    path = "/usr/share/dict/words"
    words = get_words_from_file(path)

    random_words = []
    for i in range(int(num)):
        random_words.append(choice(words))
    return ' '.join(random_words).capitalize() + '.'



def get_random_word():
    path = "/usr/share/dict/words"
    words = get_words_from_file(path)

    return choice(words)


if __name__ == '__main__':
    # Only get 1 arg and then convert it to int to get that amount of words
    args = argv[1:3]
    words = get_random_words(args[0])
    print(words)