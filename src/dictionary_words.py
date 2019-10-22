from sys import argv
from random import choice


def get_dict_words(num):
    path = "/usr/share/dict/words"
    with open(path, "r") as f:
        all_words = f.read().split('\n')
        random_words = []
        for i in range(int(num)):
            random_words.append(choice(all_words))
        return ' '.join(random_words) + '.'


if __name__ == '__main__':
    # Only get 1 arg and then convert it to int to get that amount of words
    args = argv[1:3]
    words = get_dict_words(args[0])
    print(words)