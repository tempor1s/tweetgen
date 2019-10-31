from flask import Flask
from lib.sample import get_sentence

app = Flask(__name__)

@app.route('/')
def index():
    return get_sentence('lib/txt_files/test.txt')

if __name__ == "__main__":
    app.run(debug=True)