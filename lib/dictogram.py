from operator import itemgetter
from bisect import bisect
import os
from random import random, choice, choices, uniform, randint
from itertools import accumulate


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type"""
    def __init__(self, word_list=None, vowels=False):
        """
        Initialize this histogram as a new dict and count given words

        Params:
            word_list: list - A list of words you want to convert into a histogram
        """
        super().__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        # Count of distinct word types in this histogram
        self.types = 0
        # Total count of all word tokens in this histogram
        self.tokens = 0 
        # Count words in a given list, if any
        if word_list:
            for word in word_list:
                self.add_count(word, 1)
        # Weighting based off of values
        if word_list and vowels:
            for word in self.keys():
                word_list = list(word)
                for c in word_list:
                    if set('aeiou').intersection(c.lower()):
                        self.add_count(word, 1)


    def add_count(self, word, count=1):
        """
        Increase frequency count of given word by given count amount

        Params:
            word: str - The word you want to increase the frequency of
            count: int - The amount you want to increase it by
        """
        # IF the word is going to be a new word then increase types by 1
        # TODO: Combine this new with new word so that you do not have to access array twice
        if self.get(word, 0) == 0:
            self.types += 1

        # If word does not exist create it with a value of count, otherwise add count to the already exiting value
        self[word] = self.get(word, 0) + count

        # Increment the tokens amount so that we do not need to do any recalculations
        self.tokens += count

    def frequency(self, word):
        """
        Return frequency count of given word, or 0 if word is not found.

        Params:
            word: str - The word you want to get the frequency of

        Returns:
            int - Frequency of word, 0 if not found
        """
        return self.get(word, 0)

    def get_sorted(self):
        """
        Sort a list or dictonary histogram with from greatest amount of appearances to least

        Params:
            histogram: dict, list - A list or dictonary histogram that you want to be sorted

        Returns:
            list: Sorted histogram as a list, or None if passed in value is not list or dictonary
        """
        # Create a new list for the sorted items to be appended to
        listed_histo = []
        # For every key in self (Dictogram), append a new [word, count] pair to the list
        for key in self.keys():
            listed_histo.append([key, self.get(key)])
        # Return a sorted list that is sorted based off of the count in each pair.
        return sorted(listed_histo, key=itemgetter(1), reverse=True)

    def log(self, filename='log.txt'):
        """
        Log all entries in a histogram to a .txt file. Supports both dictonary and list histogram

        Params:
            histogram: dict, list - A list or dictionary histogram that you want to log to a file
            filename: str - name of file that you want to log to
                default: log.txt
        """
        # Try to remove an old log file if it already exists, otherwise just continue and create new one.
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

        # Open the file in append+ mode, which will create a file if it does not exist
        with open(filename, 'a+') as f:
            # Loop through every key in self (Dictogram)
            for key in self.keys():
                # Write each line to file with word and ammount of times it appears with a newline after it
                f.write(f'{key} {str(self.get(key))}\n')

    def read_from_log(self, filename='log.txt'):
        """
        Get entries from a histogram log file and put them into self (dictogram)

        Params:
            filename: file - name of file that you want to read from
        """
        with open(filename, 'r') as f:
            # Remove any whitespace at beginning and end of file and split words into list
            words = f.read().strip().split('\n')
            # Loop through every item that was read from the file
            for item in words:
                # Split it into word, number pair and set it to an item in self
                word, num = item.split()
                self.add_count(word, int(num))

    def sample(self, amount=1):
        """
        Return a random word from self (Dictogram) that is weighted

        Params:
            amount: int - The amount of weighted random words that you want

        Returns:
            list: list of k random words
        """
        # Pass dictogram keys, values, and amount into choose function to k large list of weighted samples
        return self._choose(population=list(self.keys()), weights=list(self.values()), k=amount)

    def _choose(self, population, weights, k):
        """
        Return k amount of weighted random values.

        Params:
            population: list, tuple - A list of values you want to get the weighted sample from
            weights: list (ints) - A list of all the values that you want to use as weights
            k: int - The amount random weighted words you you want to be returned

        Returns:
            list: A List of k random weighted words 
        """
        # Get all the weights
        cum_weights = list(accumulate(weights))
        # Get the total, which will be the last item in weights
        total = cum_weights[-1]

        # Return k amount of weighted items
        return [population[bisect(cum_weights, random() * total)] for i in range(k)]

    def get_sentence(self, amount=10):
        """
        Get a 'sentence' which is basically a list of random words with the first letter capitalized and a period added onto the end

        Params:
            histo: The histogram you want to get your sentence from
            amount: int - The length you want your 'sentence' to be

        Returns:
            sentence: str - The sentence as a string
        """
        # Get x amount of weighted words from dictogram and then return them in 'sentence' structure
        weighted_words = self.sample(amount)
        return ' '.join(weighted_words).capitalize() + '.'


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = histogram.sample(10000)
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()