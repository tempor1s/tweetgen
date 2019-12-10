import time
import re


def time_it(func):
    """
    A wrapper function that is used to get the time that a function takes
    Made with <3 by Ben Lafferty

    Use:
        @time_it
        def func():
            return 'hi'
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 1000) + ' ms')
        return result

    return wrapper


def get_clean_words(source_file):
    """
    Takes text file as a paramater and returns a list of all the words with all characters except for A-Z removed
    Keeps spaces and newline characters

    Params:
        source_file: file - A .txt file to read words from

    Returns:
        List of words from a text file

    Raises:
        File Not Found if source file does not exist
    """
    with open(source_file, 'r') as f:
        # words_file = f.read().lower()
        words_file = f.read()
        clean_words = re.sub(r'[^a-zA-Z\s]', '', words_file)
        return clean_words.split()