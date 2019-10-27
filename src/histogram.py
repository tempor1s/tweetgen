from utils import time_it
from operator import itemgetter
import os
import re


def get_clean_words(source_file):
    with open(source_file, 'r') as f:
        words_file = f.read()
        clean_words = re.sub(r'[^a-zA-Z\s]', '', words_file)
        return clean_words.split()


@time_it
def histogram(source_file):
    """
    Takes text file as a paramater and returns a histogram data structure that stores each unique word along with
    the number of times that the word appears in the source text.  Only accepts clean data

    Params:
        source_file: .txt file that contains a corpus 

    Returns:
        Dict that contains unique words along with the number of times that word appears in text
    """
    # Dictonary Implementation - Nothing can beat the performance of this.
    # Also, this will not clean words - so please pass it a corpus that isn't messed up :)
    words = get_clean_words(source_file)
    histo = {}
    for word in words:
        if word:
            histo[word] = histo.get(word, 0) + 1
    return histo


@time_it
def sort_histogram(dict_histogram):
    """
    Takes a dictonary histogram and returns into a sorted list based off of amount of times a word appears
    """
    listed_histo = []
    for key in dict_histogram.keys():
        listed_histo.append([key, dict_histogram.get(key)])
    return sorted(listed_histo, key=itemgetter(1), reverse=True)


@time_it
def log_histrogram(histogram, filename='log.txt'):
    """
    Log all entries in a histogram to a text file.
    """
    # Try to remove the log file if there is a previous log file, otherwise just continue if the file doesn't exist
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

    with open(filename, 'a+') as f:
        if type(histogram) == type({}):  # Check to see if the type is dictonary
            for key in histogram.keys():
                f.write(f'{key} {str(histogram.get(key))}\n')
        elif type(histogram) == type([]):  # For sorted lists :)
            for item in histogram:
                f.write(f'{item[0]} {item[1]}\n')


@time_it
def get_histogram_from_log(filename):
    with open(filename, 'r') as f:
        # Remove any whitespace at beginning and end of file
        words = f.read().strip().split('\n')
        histo = {}
        for item in words:
            word, num = item.split()
            histo[word] = num
        return histo


# This is a disgusting approach lmaoooo. Only about 950ms slower than my dictonary version :)
@time_it
def list_histogram(source_file):
    words = get_clean_words(source_file)
    histo = []
    for word in words:
        histo_entry = [word, 0]
        for word2 in words:
            if word == word2:
                histo_entry[1] += 1
        if histo_entry not in histo:
            histo.append(histo_entry)

    return histo


# LMAOOOOOOOOOOOOOOOOOOOOOOOOOO
@time_it
def tuple_histogram(source_file):
    words = get_clean_words(source_file)
    histo = []
    for word in words:
        histo_entry = [word, 0]
        for word2 in words:
            if word in word2:
                histo_entry[1] += 1
        if histo_entry not in histo:
            histo.append(histo_entry)

    tup = []
    for item in histo:
        tup.append(tuple(item))

    return tup

# I am going to optimize these I swear
@time_it
def count_histogram(source_file):
    words = get_clean_words(source_file)
    max_len = len(max(words, key=len))
    histo = []
    for i in range(1, max_len - 1):
        histo_entry = [i, []]
        for word in words:
            if i == len(word):
                if word.lower() not in histo_entry[1]:
                    histo_entry[1].append(word.lower())
        histo.append(histo_entry)

    return histo


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word, 0)


if __name__ == "__main__":
    print(get_histogram_from_log('log.txt'))
