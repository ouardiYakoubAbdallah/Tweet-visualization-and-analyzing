from analyzer.twitter_analyzer import TweetAnalyzer
from streamer.twitter_streamer import Client, TwitterStreamer
from visualizer.tweet_visualizer import TweetVisualizer
from sentiment_analysis.sentiment_analysis import TweetCleanner,SentimentAnalyzer

import numpy as np

if __name__== '__main__':
    hashtags = ['donald trump', 'hillary clinton', 'barack obama']
    filename = 'tweets.json'
    username = 'tim_cook'

    #----------- STREAM TWEETS -----------
    tStreamer = TwitterStreamer()
    tStreamer.stream_tweets(filename, hashtags)

    # ----------- ANALYZE TWEETS -----------
    client = Client()
    analyzer = TweetAnalyzer()
    API = client.get_tClient()
    tweets = API.user_timeline(screen_name=username, count=25)
    df = analyzer.json_to_dataframe(tweets)
    print(df.head(10))

    # ----------- VISUALIZE DATA -----------

    visualizer = TweetVisualizer(df,'date',legend=True)
    visualizer.draw_single('likes',color='b')
    visualizer.show()

    # ----------- SENTIMENT ANALYSIS -----------

    cleaner = TweetCleanner()
    sentiment = SentimentAnalyzer()
    df['sentiment'] = np.array(tuple(sentiment.analyze_sentiment(cleaner.clean(tweet)) for tweet in df['tweets']))
    print(df.head(10))