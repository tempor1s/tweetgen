#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super().__init__()  # Initialize this as a new list
        # Count words in given list, if any
        if word_list is not None:
            self.setup(word_list)
        # Add properties to track useful word counts for this histogram
        self.types = len(self)  # Count of distinct word types in this histogram
        self.tokens = sum([n[1] for n in self])  # Total count of all word tokens in this histogram

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        for item in self:
            if item[0] == word:
                item[1] += count
                self.tokens += count
                break
        else:
            # Append the new word with count if it does not exist, and update tokens and types
            self.append([word, count])
            self.tokens += count
            self.types = len(self)


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for item in self:
            if item[0] == word:
                return item[1]
        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for item in self:
            if word == item[0]:
                return True
        
        return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        for item in self:
            if item[0] == target:
                return self.index(item)

    def setup(self, word_list):
        for word in word_list:
            histo_entry = [word, 0]
            for word2 in word_list:
                if word == word2:
                    histo_entry[1] += 1
            # TODO: Remove this once I implement __contains__
            if histo_entry not in list(self):
                self.append(histo_entry)


if __name__ == "__main__":
    histo = Listogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])


# def print_histogram(word_list):
#     print('word list: {}'.format(word_list))
#     # Create a listogram and display its contents
#     histogram = Listogram(word_list)
#     print('listogram: {}'.format(histogram))
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
