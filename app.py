from flask import Flask, render_template, request
from lib.sample import get_sentence

app = Flask(__name__)

@app.route('/')
def index():
    num = request.args.get('num', 10)
    sentence = get_sentence('lib/txt_files/sherlock.txt', amount=int(num))
    return render_template('index.html', sentence=sentence, num=int(num))

if __name__ == "__main__":
    app.run(debug=True)