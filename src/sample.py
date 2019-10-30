from histogram import histogram, sort_histogram
from random import random, choice, choices, uniform
from sys import argv
from bisect import bisect
from itertools import accumulate
from utils import time_it


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


def accum(iterable):
    it = iter(iterable)
    total = None
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for el in it:
        total = total += el


@time_it
def ez_sample(histogram, amount=1):
    """
    The ez way to return a random word from a histogram that is weighted

    Params:
        histogram: dict, list, tuple - The histogram you want k random words from

    Returns:
        list: list of k random words
    """
    if isinstance(histogram, dict):
        return choices_implementation(population=list(histogram.keys()), weights=list(histogram.values()), k=amount)
    elif isinstance(histogram, list) or isinstance(histogram, tuple):
        return choices_implementation(population=[val[0] for val in histogram], weights=[val[1] for val in histogram], k=amount)


def choices_implementation(population, weights=None, cum_weights=None, k=1):
    if cum_weights is None:
        if weights is None:
            total = len(population)
            return [population[int(random * total)] for i in range(k)]
        cum_weights = list(accumulate(weights))
        print(cum_weights)
    elif weights is not None:
        raise TypeError('Cannot specify both weights and cumulative weights')
    if len(cum_weights) != len(population):
        raise ValueError('The number of weights does not match the population')
    total = cum_weights[-1]
    hi = len(cum_weights) - 1
    print(random() * total)
    print(population[bisect(cum_weights, random() * total, 0, hi)])
    return [population[bisect(cum_weights, random() * total, 0, hi)] for i in range(k)]


if __name__ == '__main__':
    args = argv[1:4]
    histo = histogram(args[0])
    total = int(args[1])
    new_sample = ez_sample(histo, total)

    new_histo = {}
    for samp in new_sample:
        new_histo[samp] = new_histo.get(samp, 0) + 1

    for key in new_histo:
        new_histo[key] = new_histo.get(key) / total

    for key in new_histo:
        print(f'{key} => {new_histo.get(key)} => {new_histo.get(key) * total}')
    # tot_percent = 0
    # for key in new_histo:
    #     tot_percent += new_histo.get(key)
    
    # print(tot_percent)