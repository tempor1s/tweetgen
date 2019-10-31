from flask import Flask, render_template, request
from lib.sample import get_sentence

app = Flask(__name__)

@app.route('/')
def index():
    num = int(request.args.get('num')) or 10
    sentence = get_sentence('lib/txt_files/sherlock.txt', num)
    return render_template('index.html', sentence=sentence, num=num)

if __name__ == "__main__":
    app.run(debug=True)