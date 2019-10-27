def histogram(source_file):
    """
    Takes text file as a paramater and returns a histogram data structure that stores each unique word along with
    the number of times that the word appears in the source text.

    Params:
        source_file: .txt file that contains a corpus 

    Returns:
        Dict that contains unique words along with the number of times that word appears in text
    """
    # Dictonary Implementation - Fastest
    with open(source_file, 'r') as f:
        words = f.read().split()
        histo = {}
        for word in words:
            histo[word] = histo.get(word, 0) + 1
        return histo

def unique_words():
    pass


def frequency():
    pass


if __name__ == "__main__":
    histo = histogram('test.txt')
    print(histo)
    print(len(histo))