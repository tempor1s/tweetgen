import random
import re

try:
    from lib.dictogram import Dictogram
    from lib.utils import get_clean_words
    from lib.queue import Queue
except ModuleNotFoundError:
    from queue import Queue
    from dictogram import Dictogram
    from utils import get_clean_words


class Narkov(dict):
    def __init__(self, word_list, order=2):
        super().__init__()
        self.order = order  # order of the markov chain
        self.memory = Queue(order)  # for sampling from markov model

        if word_list is not None:
            self['START'] = Dictogram()
            self._create_chain(word_list)

    def _create_chain(self, word_list):
        for i, message in enumerate(word_list + word_list[:self.order]):
            if i < self.order:  # to fill the queue initally so that we do not add states that are smaller than order
                self.memory.enqueue(message)  # enqueue each new item
            else:
                current_state = self.memory.serialize()  # the current state
                self.memory.enqueue(message)  # create the new state
                new_state = self.memory.serialize()  # the next state

                # TODO: improve how I want to sample start tokens
                if re.match('[A-Z]', current_state[0]) is not None:
                    # TODO: Don't add start tokens
                    self['START'].add_count(current_state)

                if current_state in self:  # check to see if the state already exists
                    # if it does just add the next state to it
                    self[current_state].add_count(message)
                else:
                    # otherwise create a new dictogram with the new state
                    self[current_state] = Dictogram([message])
        
        self.memory.clear()

    def generate_sentence(self):
        """Generate a sentence from the internal markov chain."""
        # starting_state = random.choice(list(self.keys()))

        # enque the items into the current memory
        # for item in starting_state:
        #     self.memory.enqueue(item)

        # for _ in range(length):
        #     next_state = self[starting_state].sample()[0]
        #     self.memory.enqueue(next_state)
        #     yield next_state
        #     starting_state = self.memory.serialize()

        
        starting_state = self['START'].sample()[0] # word from starting state
        sentence_list = list()
        sentence_list.extend(starting_state) # the start of the sentence :)
        
        failsafe = 0 # Count to keep as a failsafe if there is no punctuation.
        
        for item in starting_state: # loop through starting state and add those items to the queue
            self.memory.enqueue(item)

        while True:
            # increase failsafe
            failsafe += 1
            # get the next state by samplying the current state
            next_state = self[starting_state].sample()[0] # a word
            # enque the word into 'memory'
            self.memory.enqueue(next_state)
            # add the item to the list
            sentence_list.append(next_state)

            # check if the word is an end token
            if re.search('[\.\?\!]', next_state) is not None:
                self.memory.clear()
                return ' '.join(sentence_list)
            # set the new 'starting' state to the the tuple that is currently in 'memory'
            starting_state = self.memory.serialize()

            if failsafe > 30: # if ran 30 times exit
                break # break out of infinite loop

        self.memory.clear() # clear memory for next generation
        return ' '.join(sentence_list) + '.'


if __name__ == "__main__":
    words = get_clean_words('txt_files/donald.txt')

    m = Narkov(words, 2)
    print(m)

    print(m.generate_sentence())
