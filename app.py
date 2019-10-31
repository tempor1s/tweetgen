from flask import Flask, render_template, request, jsonify
from lib.sample import get_sentence

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get('num')
        sentence = get_sentence('lib/txt_files/sherlock.txt', int(num))

        return jsonify({'sentence': sentence})

    sentence = get_sentence('lib/txt_files/sherlock.txt', 10)
    return render_template('index.html', sentence=sentence, num=10)


@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    if request.method == 'POST':
        pass

    return render_template('favorites.html')


if __name__ == "__main__":
    app.run(debug=True)
