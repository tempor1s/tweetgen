from dotenv import load_dotenv
from dictionary_words import get_random_word
import requests
import os
load_dotenv()

DICTONARY_API_KEY = os.getenv('DICTONARY_API_KEY')


def get_random_word_and_def():
    """
    Get a random word and definition

    Returns:
        word: str - The word that the defintion is for
        definition: str - The defintion of the word

        Format:
            word, str
    """
    while True:
        word = get_random_word()
        url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={DICTONARY_API_KEY}'
        r = requests.get(url)
        try:
            definition = r.json()[0]['shortdef']
            return word, definition
        except TypeError:
            pass


def main():
    """
    Just a function that contains the logic to play the vocab game
    """
    print('Welcome to my guessing game! Give me a second to fetch a defintion for you!')
    word, definition = get_random_word_and_def()

    print('Thanks for waiting! Here is the definition for the word, can you guess it?  \n')
    print(definition)
    print('\n')

    guess = input('Guess:  ')

    if guess == word:
        print('Congrats! You won!')
    else:
        print(f'You lost... the word was {word}')


if __name__ == '__main__':
    main()
