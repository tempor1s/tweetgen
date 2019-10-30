from histogram import histogram, sort_histogram
from random import choice, choices
from sys import argv

def sample(histogram, amount=1):
    """
    Returns a random word from a histogram

    Params:
        histogram: dict, list, tuple - The histogram you want k random words from

    Returns:
        list: list of k random words
    """
    if isinstance(histogram, dict):
        return choice(list(histogram.keys()))
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        return choice(histogram)[0]
    
def ez_sample(histogram, amount=1):
    """
    The ez way to return a random word from a histogram that is weighted

    Params:
        histogram: dict, list, tuple - The histogram you want k random words from

    Returns:
        list: list of k random words
    """
    if isinstance(histogram, dict):
        # return choice(list(histogram.keys()))
        return choices(list(histogram.keys()), list(histogram.values()), k=amount)
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        return choices([val[0] for val in histogram], [val[1] for val in histogram], k=amount)


if __name__ == '__main__':
    args = argv[1:4]
    histo = histogram(args[0])
    new_sample = ez_sample(histo, int(args[1]))

    new_histo = {}
    for samp in new_sample:
        new_histo[samp] = new_histo.get(samp, 0) + 1

    print(sort_histogram(new_histo))