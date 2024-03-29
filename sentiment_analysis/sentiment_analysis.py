from textblob import TextBlob
import re

class TweetCleanner:

    def clean(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


class SentimentAnalyzer:

    def analyze_sentiment(self, tweet_cleaned):
        analysis = TextBlob(tweet_cleaned)

        if analysis.sentiment.polarity > 0 :
            return 'Positive'
        elif analysis.sentiment.polarity == 0 :
            return 'Neutral'
        else:
            return 'Negative'