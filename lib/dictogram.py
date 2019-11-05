from operator import itemgetter
import os


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type"""

    def __init__(self, word_list=None):
        """
        Initialize this histogram as a new dict and count given words

        Params:
            word_list: list - A list of words you want to convert into a histogram
        """
        super().__init__()  # Initialize this as a new dict
        if word_list:
            for word in word_list:
                self[word] = self.get(word, 0) + 1
            # Create a histogram from the path
        # Add properties to track useful word counts for this histogram
        # Count of distinct word types in this histogram
        self.types = len(self)
        # Total count of all word tokens in this histogram
        self.tokens = sum(self.values())

    def add_count(self, word, count=1):
        """
        Increase frequency count of given word by given count amount

        Params:
            word: str - The word you want to increase the frequency of
            count: int - The amount you want to increase it by
        """
        self[word] = self.get(word, 0) + count
        # Increment the tokens amount so that we do not need to do any recalculations
        self.tokens += count
        self.types = len(self)  # TODO: Make this faster

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
        Get entries from a histogram log file and put them into a dictonary

        Params:
            filename: file - name of file that you want to read from

        Returns:
            dict: New histogram as a dictonary
        """
        with open(filename, 'r') as f:
            # Remove any whitespace at beginning and end of file
            words = f.read().strip().split('\n')
            for item in words:
                word, num = item.split()
                self[word] = int(num)
            return histo


if __name__ == "__main__":
    fish_text = 'one fish two fish red fish blue fish'
    histo = Dictogram(fish_text.split(' '))
    print(histo)
    histo.read_from_log()
    print(histo)

# def print_histogram(word_list):
#     print('word list: {}'.format(word_list))
#     # Create a dictogram and display its contents
#     histogram = Dictogram(word_list)
#     print('dictogram: {}'.format(histogram))
#     print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
#     for word in word_list[-2:]:
#         freq = histogram.frequency(word)
#         print('{!r} occurs {} times'.format(word, freq))
#     print()


# def main():
#     import sys
#     arguments = sys.argv[1:]  # Exclude script name in first argument
#     if len(arguments) >= 1:
#         # Test histogram on given arguments
#         print_histogram(arguments)
#     else:
#         # Test histogram on letters in a word
#         word = 'abracadabra'
#         print_histogram(list(word))
#         # Test histogram on words in a classic book title
#         fish_text = 'one fish two fish red fish blue fish'
#         print_histogram(fish_text.split())
#         # Test histogram on words in a long repetitive sentence
#         woodchuck_text = ('how much wood would a wood chuck chuck'
#                           ' if a wood chuck could chuck wood')
#         print_histogram(woodchuck_text.split())


# if __name__ == '__main__':
#     main()
