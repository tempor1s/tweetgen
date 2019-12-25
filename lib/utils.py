import time
import re
import twitter


def time_it(func):
    """
    A wrapper function that is used to get the time that a function takes
    Made with <3 by Ben Lafferty

    Use:
        @time_it
        def func():
            return 'hi'
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 1000) + ' ms')
        return result

    return wrapper


def get_clean_words(source_file):
    """
    Takes text file as a paramater and returns a list of all the words with all characters except for A-Z removed
    Keeps spaces and newline characters

    Params:
        source_file: file - A .txt file to read words from

    Returns:
        List of words from a text file

    Raises:
        File Not Found if source file does not exist
    """
    with open(source_file, 'r') as f:
        # words_file = f.read().lower()
        # words_file = f.read()
        # clean_words = re.sub(r'[^a-zA-Z\s]', '', words_file)
        clean_words = f.read()
        return clean_words.split()


def get_user_tweets_corpus(twitter_client, username, clean=False):
    """Get 3200 tweets from a user's timeline because that is the max possible, return them in a list."""
    # TODO: Improve
    tweets = []  # an empty list to store all the tweets
    max_id = None  # max_id will be the last tweet id so we can get 3200 tweets

    for _ in range(16):  # loop 16 times because 3200 / 200 per request is 16
        try:
            timeline = twitter_client.GetUserTimeline(
                screen_name=username, include_rts=False, count=200, max_id=max_id)  # get 200 tweets
        except twitter.TwitterError:
            return 'Sorry, hat user does not exist. Please try again.'
        for tweet in timeline:  # loop through each of the 200 tweets
            # check if we want to clean up the data that is being returned
            if clean:
                # get the text for the tweet
                tweet_text = tweet.text
                # do some basic checks to not add tweets if we are cleaning the text
                final = re.sub(r"http\S+", "", tweet_text)
                tweets.append(final)
            else:
                tweets.append(tweet.text)
        # get the last item in the timeline to be used as our next max_id for searching
        max_id = timeline[-1].id

    return ' '.join(tweets)