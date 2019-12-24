from flask import Flask, render_template, request, jsonify, redirect, url_for
from lib.dictogram import Dictogram
from lib.markov import Markov
from lib.utils import get_clean_words, get_user_tweets_corpus
from pymongo import MongoClient
import os
import twitter  # for tweeting

from dotenv import load_dotenv  # for secrets
load_dotenv()

# Set up flask app
app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetgen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

# Setup twitter API
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.getenv('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)

# Setup markov chain when the text is first created so it doesn't need to generated on every get request
path = 'lib/txt_files/donald.txt'
words = get_clean_words(path)
markov = Markov(words, 2)


@app.route('/', methods=['GET', 'POST'])
def index():
    markov_order = 2
    sentences_per_tweet = 1
    number_of_tweets = 1
    username = ''

    if request.method == 'POST':
        username = request.form.get('username')
        markov_order = request.form.get('markov_order', 2)
        sentences_per_tweet = request.form.get('sentences_per_tweet', 1)
        number_of_tweets = request.form.get('number_of_tweets', 1)

        return redirect(url_for('user', username=username, markov_order=2,
                                sentences_per_tweet=sentences_per_tweet,
                                number_of_tweets=number_of_tweets))

    return render_template('index.html', markov_order=markov_order,
                           sentences_per_tweet=sentences_per_tweet,
                           number_of_tweets=number_of_tweets)


@app.route('/donald-tweetgen', methods=['GET', 'POST'])
def donald_tweetgen():
    num = request.form.get('num', 20)

    # Generate a new sentence that is num length long
    sentence = markov.generate_sentence()

    # for jquery
    if request.method == 'POST':
        return jsonify({'sentence': sentence})

    return render_template('donald_tweetgen.html', sentence=sentence, num=num)


@app.route('/favorites', methods=['GET', 'POST'])
def favorites_view():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        db.favorites.insert_one({'sentence': sentence})

        return jsonify({'sentence': sentence})

    return render_template('favorites.html', sentences=favorites.find({}))


@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    if request.method == 'POST':

        sentence = request.form.get('sentence')
        if len(sentence) > 280:
            return 'Length of sentence is longer than allowed tweet limit.'

        print(twitter_api.VerifyCredentials())
        twitter_api.PostUpdate(sentence)
        # TODO: Redirect back to home page?
        return 'Tweet was successful!'


@app.route('/user/<username>', methods=['POST', 'GET'])
def user(username):
    # get user tweets corpus
    tweets = get_user_tweets_corpus(twitter_api, username)
    # get order of markov chain
    order = int(request.args.get('markov_order', 2))
    # get the amount of sentences to be generated for each tweet
    sentences_per_tweet = int(request.args.get('sentences_per_tweet', 1))
    # get the number of tweets to be generated
    number_of_tweets = int(request.args.get('number_of_tweets', 1))

    # split corpus into indiviual words
    # TODO: Clean up the corpus
    words = tweets.split()
    # Generate a markov chain with all the words in the corpus with a specific order
    markov = Markov(words, order=order, sentences=sentences_per_tweet)

    return render_template('user_tweets.html', sentence=markov.generate_sentence(), username=username)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
