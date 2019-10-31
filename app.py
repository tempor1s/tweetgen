from flask import Flask, render_template, request, jsonify, redirect, url_for
from lib.sample import get_sentence
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
    if request.method == 'POST':
        num = request.form.get('num')
        sentence = get_sentence('lib/txt_files/sherlock.txt', int(num))

        return jsonify({'sentence': sentence})

    sentence = get_sentence('lib/txt_files/sherlock.txt', 10)
    return render_template('index.html', sentence=sentence, num=10)


@app.route('/favorites', methods=['GET', 'POST'])
def favorites_viewe():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        favorites.insert_one({'sentence': sentence})

        return jsonify({'sentence': sentence})

    return render_template('favorites.html', sentences=favorites.find({}))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('POST', 5000))
