from flask import Flask, render_template, request, jsonify, redirect, url_for
from lib.dictogram import Dictogram
from lib.markov import MarkovChain
from lib.utils import get_clean_words
from pymongo import MongoClient
import os

# Set up flask app
app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetgen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

# Setup markov chain when the text is first created so it doesn't need to generated on every get request
path = 'lib/txt_files/sherlock.txt'
words = get_clean_words(path)
markov = MarkovChain(words)


@app.route('/', methods=['GET', 'POST'])
def index():
    num = request.form.get('num', 20)
    # TODO: Implement vowel weighting check in ajax request and html
    vowel_weight = request.form.get('vowel', False)

    # Generate a new sentence that is num length long
    sentence = markov.create_sentence(int(num))

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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
