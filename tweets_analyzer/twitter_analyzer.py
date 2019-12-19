import pandas as pd
import numpy as np

from streamer.twitter_streamer import Client

class TweetAnalyzer:
    """
    A whole set of functionality to analyze and categorize content from previously retrieved tweets
    """
    def json_to_dataframe(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['length'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['device'] = np.array([tweet.source for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        return df

if __name__== '__main__':
    client = Client()
    analyzer = TweetAnalyzer()
    API =client.get_tClient()
    tweets = API.user_timeline(screen_name="tim_cook", count=10)
    df = analyzer.json_to_dataframe(tweets)
    print(df.head(10))