from flask import Flask, render_template
from lib.sample import get_sentence

app = Flask(__name__)

@app.route('/')
def index():
    sentence = get_sentence('lib/txt_files/sherlock.txt', amount=20)
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)