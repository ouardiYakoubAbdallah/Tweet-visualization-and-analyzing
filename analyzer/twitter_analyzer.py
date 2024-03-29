import pandas as pd
import numpy as np

from streamer.twitter_streamer import Client

class TweetAnalyzer:
    """
    A whole set of functionality to analyze and categorize content and results from previously retrieved tweets
    """

    def json_to_dataframe(self, tweets):
        df = pd.DataFrame()
        df['tweets'] = np.array([tweet.text for tweet in tweets])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['length'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['device'] = np.array([tweet.source for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        return df

    def average_len(self, dataframe):
        #function that return the average length
        return np.mean(dataframe['length'])

    def most_likes(self, dataframe):
        #function that return the like's number for the most liked tweet
        return np.max(dataframe['likes'])

    def most_rt(self, dataframe):
        #function that return the RT's number for the most retweeted tweet
        return np.max(dataframe['retweets'])

