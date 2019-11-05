from operator import itemgetter
from random import choice
from utils import get_clean_words
import os


def histogram(source_file, vowels=False):
    """
    Takes text file as a paramater and returns a histogram data structure that stores each unique word along with
    the number of times that the word appears in the source text

    Params:
        source_file: .txt file that contains text you want to get a histrogram of
        vowels: bool - If we should do weighting based off of the amount of times a vowel appears

    Returns:
        words: dict - key of unique word and value of amount of times that word appears
    """
    # Dictonary Implementation - Essentially fastest implementation
    words = get_clean_words(source_file)
    histo = {}
    for word in words:
        histo[word] = histo.get(word, 0) + 1

    # Does weighting based off of how many vowels are in a word
    if vowels:
        for word in histo.keys():
            word_list = list(word)
            for c in word_list:
                if set('aeiou').intersection(c.lower()):
                    histo[word] = histo.get(word) + 1
            # if set('aeiou').intersection(word.lower()):
            #     histo[word] = histo.get(word) + 1
    return histo


def sort_histogram(histogram):
    """
    Sort a list or dictonary histogram with from greatest amount of appearances to least

    Params:
        histogram: dict, list - A list or dictonary histogram that you want to be sorted

    Returns:
        list: Sorted histogram as a list, or None if passed in value is not list or dictonary
    """
    if isinstance(histogram, dict):
        listed_histo = []
        for key in histogram.keys():
            listed_histo.append([key, histogram.get(key)])
        return sorted(listed_histo, key=itemgetter(1), reverse=True)
    elif isinstance(histogram, (list, tuple)):
        return sorted(histogram, key=itemgetter(1), reverse=True)
    else:
        return None


def log_histrogram(histogram, filename='log.txt'):
    """
    Log all entries in a histogram to a .txt file. Supports both dictonary and list histogram

    Params:
        histogram: dict, list - A list or dictionary histogram that you want to log to a file
        filename: str - name of file that you want to log to
            default: log.txt
    """
    # Try to remove the log file if there is a previous log file, otherwise just continue if the file doesn't exist
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

    with open(filename, 'a+') as f:
        if isinstance(histogram, dict):  # Check to see if the type is dictonary
            for key in histogram.keys():
                f.write(f'{key} {str(histogram.get(key))}\n')
        elif isinstance(histogram, list):  # For sorted lists :)
            for item in histogram:
                f.write(f'{item[0]} {item[1]}\n')


def get_histogram_from_log(filename):
    """
    Get entries from a histogram log file and put them into a dictonary

    Params:
        filename: file - name of file that you want to read from

    Returns:
        dict: New histogram as a dictonary
    """
    with open(filename, 'r') as f:
        # Remove any whitespace at beginning and end of file
        words = f.read().strip().split('\n')
        histo = {}
        for item in words:
            word, num = item.split()
            histo[word] = num
        return histo


def list_histogram(source_file):
    """
    Get a list version of a histogram from a text file

    Params:
        source_file: file - The file that you want to get a histogram of

    Returns:
        list: A list of lists that contain the amount of times that a word appears
    """
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


def tuple_histogram(source_file):
    """
    Get a tuple version of a histogram from a text file

    Params:
        source_file: file - The file you want to get a histogram of

    Returns:
        list: A list of tuples that contain the amount of a times the word appears
    """
    # TODO: Rewrite this to not use list_histogram
    words = get_clean_words(source_file)
    histo = []
    for word in words:
        count = 0
        for word2 in words:
            if word == word2:
                count += 1
        tup = (word, count)
        if tup not in histo:
            histo.append(tup)

    return histo


def count_histogram(source_file):
    """
    Get a list of lists that contain a count and the words that have that count

    Params:
        source_file: file - The file that you want to get a count histogram from

    Returns:
        list: A list of lists that contain the amount of times that a word appears
    """
    histo = histogram(source_file)
    max_len = max(histo.values())
    new_histo = []

    for i in range(1, max_len + 1):
        words = []
        for key in histo.keys():
            if histo.get(key) == i:
                words.append(key)
        if words:
            new_histo.append((i, words))

    return new_histo


def unique_words(histogram):
    """
    Return the amount of unique words in a histogram.  Works for dicts, lists and tuples
    Does not work for count histogram

    Params:
        histogram: dict, list, tuple - The histogram you want to get the unique amount of words from

    Returns:
        int: The amount of unique words in a histogram
    """
    # if isinstance(histogram, dict):
    #     count = 0
    #     for word in histogram.keys():
    #         if histogram.get(word) == 1:
    #             count += 1

    #     return count
    # elif isinstance(histogram, (list, tuple)):
    #     count = 0
    #     for word in histogram:
    #         if isinstance(word[1], int) and word[1] == 1:
    #             count += 1

    #     return count
    return len(histogram)


def frequency(word, histogram):
    """
    Returns the amount of times a specific word appears in a histogram

    Params:
        histogram: dict, list, tuple - The histogram you want to read from

    Returns:
        int: The amount of times that the word appears
    """
    word = word.lower()
    if isinstance(histogram, dict):
        return histogram.get(word, 0)
    elif isinstance(histogram, (list, tuple)):
        for entry in histogram:
            if entry[0] == word:
                return entry[1]
        return 0
