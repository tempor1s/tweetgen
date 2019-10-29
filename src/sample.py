from histogram import histogram
from random import choice
from sys import argv

def sample(histogram):
    """
    Returns a random word from a histogram

    Params:
        histogram: dict, list, tuple - The histogram you want the random word from

    Returns:
        str: The random word
    """
    if isinstance(histogram, dict):
        return choice(list(histogram.keys()))
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        return choice(histogram)[0]


if __name__ == '__main__':
    args = argv[1:3]
    histo = histogram(args[0])
    print(sample(histo))