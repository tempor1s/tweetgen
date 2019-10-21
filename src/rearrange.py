from sys import argv
from random import shuffle


def rearrange(arr):
    shuffle(arr)
    return ' '.join(arr)


if __name__ == '__main__':
    val = rearrange(argv[1:])
    print(val)