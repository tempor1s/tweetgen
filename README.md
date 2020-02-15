# 🐦 TweetGen

TweetGen is a project that uses a markov language model to generate unique 'tweets' based off of a corpus.

## [Deployed Version](https://tweetgen.dev.benlafferty.me)

## 🚀 Getting Started

### Installation and Requirements

Requirements:

- [Python 3](https://www.python.org/)
- [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
- [MongoDB](https://www.mongodb.com/)

We are going to assume you have MongoDB installed and running. If not, please refer to the MongoDB [documentation.](https://www.mongodb.com/)

Installation:

```bash
# clone the respository
git clone https://github.com/tempor1s/tweetgen
# cd into the project
cd tweetgen
# create a virtual environment and install the required packages
pipenv shell
pipenv install
```

Congrats! You should now have a locally installed version of tweetgen!

### Running The Project Locally

If you have not yet followed the installation steps, go and do so before continuing.

Once you have everything installed, you need to rename `.env.example` to `.env` and populate the fields with real data.

```bash
# rename .env.example to .env
mv .env.example .env
# populate the .env file with correct data using your favorite text editor!
vim .env
```

Once you have renamed the `.env` file and populated it with the correct data, all you need to do is run the server!

```bash
# run the server (make sure you are in your virtual environment you created in an earlier step)
python3 app.py
# navigate to localhost to see your running application!
http://0.0.0.0:5000
```

Congrats! You now have a local version of Tweet Generator running!

## 🔨 Built With

- [Python](https://www.python.org/) - Programming Language
- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - Webserver
- [python-dotenv](https://pypi.org/project/python-dotenv/) - To keep secrets secret
- [pytest](https://docs.pytest.org/en/latest/) - For testing to make sure my code isn't broken
- [PyMongo](https://api.mongodb.com/python/current/) - For interfacing with MongoDB
- [python-twitter](https://github.com/bear/python-twitter) - For interfacing with Twitter
