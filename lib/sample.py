from lib.histogram import histogram, sort_histogram
from lib.utils import time_it
from random import random, choice, choices, uniform
from sys import argv
from bisect import bisect


def sample(histogram, amount=1):
    """
    Returns a random word from a histogram

    Params:
        histogram: dict, list, tuple - The histogram you want k random words from

    Returns:
        list: list of k random words
    """
    if isinstance(histogram, dict):
        total = sum(list(histogram.values()))
        print(total)

        return choice(list(histogram.keys()))
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        return choice(histogram)[0]


@time_it
def weighted_sample(histogram, amount=1):
    """
    Return a random word from a histogram that is weighted

    Params:
        histogram: dict, list, tuple - The histogram you want k random words from

    Returns:
        list: list of k random words
    """
    # Check if the histogram is a dict
    if isinstance(histogram, dict):
        return choose(population=list(histogram.keys()), weights=list(histogram.values()), k=amount)

    # Check if it is tuple or list
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        population = [val[0] for val in histogram]
        weights = [val[1] for val in histogram]
        
        return choose(population=population, weights=weights, k=amount)
        # return choose(population=[val[0] for val in histogram], weights=[val[1] for val in histogram], k=amount)


def choose(population, weights, k=1):
    cum_weights = list(get_weighted(weights))
    total = cum_weights[-1]

    return [population[bisect(cum_weights, random() * total)] for i in range(k)]


def get_weighted(iterable):
    """
    Similar to python intertool but stripped down to be specific for use in getting weights

    Arguments:
        iterable: list, tuple - What you want to get the weighted values from

    Yields:
        New combined total for each item in interable
    """
    it = iter(iterable)
    total = None

    try:
        total = next(it)
    except StopIteration:
        return
    yield total

    for el in it:
        total = total + el
        yield total


def get_sentence(source_file, amount=10):
    histo = histogram(source_file)
    weighted_words = weighted_sample(histo, amount)

    return ' '.join(weighted_words).capitalize() + '.'


if __name__ == '__main__':
    args = argv[1:4]
    histo = histogram(args[0])
    total = int(args[1])
    new_sample = weighted_sample(histo, total)

    new_histo = {}
    for samp in new_sample:
        new_histo[samp] = new_histo.get(samp, 0) + 1

    for key in new_histo:
        new_histo[key] = new_histo.get(key) / total

    for key in new_histo:
        print(f'{key} => {new_histo.get(key)} => {new_histo.get(key) * total}')