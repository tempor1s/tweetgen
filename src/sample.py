from histogram import histogram
from random import choice

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
    histo = histogram('test.txt')
    print(sample(histo))