import re
from textblob import TextBlob


class SentimentAnalysis:

    def __init__(self, tweet):
        self.tweet = tweet

    # only for english language
    def execute(self):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.tweet)

        # set sentiment
        if analysis.sentiment.polarity > 0:
            data = {'text': self.tweet, 'sentiment': 'positive'}
        elif analysis.sentiment.polarity == 0:
            data = {'text': self.tweet, 'sentiment': 'neutral'}
        else:
            data = {'text': self.tweet, 'sentiment': 'negative'}

        return data

if __name__ == "__main__":
	# calling main function
    SentimentAnalysis('hard to learn NLTK').execute()