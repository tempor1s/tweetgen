from utils import time_it

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
    # Dictonary Implementation - Fastest
    # Also, this will not clean words - so please pass it a corpus that isn't messed up :)
    with open(source_file, 'r') as f:
        words = f.read().split()
        histo = {}
        for word in words:
            histo[word] = histo.get(word, 0) + 1
        return histo

# This is a disgusting approach lmaoooo. Only about 950ms slower than my dictonary version :)
@time_it
def list_histogram(source_file):
    with open(source_file, 'r') as f:
        words = f.read().split()
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
    with open(source_file, 'r') as f:
        words = f.read().split()
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
    with open(source_file, 'r') as f:
        words = f.read().split()
        histo = []
        passed_words = []
        for word in words:
            count = 0
            for word2 in words:
                if word == word2:
                    count += 1
            if word not in passed_words:
                passed_words.append(word)
                histo.append(count)
        return histo


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word, 0)


if __name__ == "__main__":
    histo = histogram('test.txt')
    # histo = tuple_histogram('test.txt')
    # histo = count_histogram('test.txt')
    print(histo)
    print(unique_words(histo))
    print(frequency('and', histo))
