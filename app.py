from flask import Flask, render_template, request, jsonify, redirect, url_for
from lib.dictogram import Dictogram
from lib.markov import Markov
from lib.utils import get_clean_words, get_all_user_tweets
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

twitter_api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

# Setup markov chain when the text is first created so it doesn't need to generated on every get request
path = 'lib/txt_files/donald.txt'
words = get_clean_words(path)
markov = Markov(words, 2)


@app.route('/', methods=['GET', 'POST'])
def index():
    num = request.form.get('num', 20)

    # Generate a new sentence that is num length long
    sentence = markov.generate_sentence()

    # for jquery
    if request.method == 'POST':
        return jsonify({'sentence': sentence})

    return render_template('index.html', sentence=sentence, num=num)


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
    tweets = get_all_user_tweets(twitter_api, username)
    tweets = ' '.join(tweets)

    words = tweets.split()
    
    markov = Markov(words, order=2)

    return render_template('user_tweets.html', sentence=markov.generate_sentence(), username=username)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
