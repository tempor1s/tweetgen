from flask import Flask, render_template, request, jsonify, redirect, url_for
from lib.dictogram import Dictogram
from lib.utils import get_clean_words
from pymongo import MongoClient
import os

# Set up flask app
app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetgen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites


@app.route('/', methods=['GET', 'POST'])
def index():
    path = 'lib/txt_files/test.txt'
    num = request.form.get('num', 10)
    #TODO: Implement vowel weighting check in ajax request and html
    vowel_weight = request.form.get('vowel', False)

    # Get all words from corpus to be passed into Dictogram
    words = get_clean_words(path)
    histo = Dictogram(words, vowel_weight)
    sentence = histo.get_sentence(int(num))

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
