class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list):
        """Initialize this histogram as a new dict and count given words."""
        super().__init__()  # Initialize this as a new dict
        if word_list:
            for word in word_list:
                self[word] = self.get(word, 0) + 1
            # Create a histogram from the path
        # Add properties to track useful word counts for this histogram
        self.types = len(self)  # Count of distinct word types in this histogram
        self.tokens = sum(self.values())  # Total count of all word tokens in this histogram

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self[word] = self.get(word, 0) + count
        self.tokens += count # Increment the tokens amount so that we do not need to do any recalculations
        self.types = len(self) # TODO: Make this faster

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        return self.get(word, 0)


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
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
