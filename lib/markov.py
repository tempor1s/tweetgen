from dictogram import Dictogram
from utils import get_clean_words


class MarkovChain(dict):
    def __init__(self, word_list):
        super().__init__() # Initialize this as a new dict

        # if word_list:
        #     for i, word in enumerate():
        #         word = self.get(word, None)
        #         if word:
        #             word.add_word(word, 1)
        #         else:
        #             self[word] = Dictogram(list(word_list[i + 1]), False)
                    

    def add_histo(self, word):
        "Add a word / histo combo. Should work for if word already exists or of it does not."
        pass

    def sample(self, word):
        """
        Gets a random word from the histogram with the word as key

        Params:
            word: str - The word you want to sample from
        """
        pass


if __name__ == "__main__":
    words = get_clean_words('txt_files/example.txt')
    chain = MarkovChain(words)
    print(chain)