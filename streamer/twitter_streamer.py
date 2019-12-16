#Listen to the tweets, based on keywords and hashtags
from tweepy.streaming import StreamListener
from tweepy import Stream

#For authentification
from tweepy import OAuthHandler

from credentails import twitter_credenatils as tc

#Class responsable for streaming the tweets
class TwitterStreamer:
    """
    Class used for streaming and processing tweets directly in real time from twitter
    """
    def stream_tweets(self, filename, hashtags):
        #Handling twitter auth and connect to the Streaming API
        listener = StdOutListener(filename)
        auth = OAuthHandler(tc.CONSUMER_API_KEY, tc.CONSUMER_API_SECRET_KEY)
        auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

        # Twitter stream
        strm = Stream(auth, listener)
        # listener is responsable for how to deal with data and errors

        # Filtring tweets and focus on hashtags and keywords
        strm.filter(track=hashtags)




class StdOutListener(StreamListener):
    """
    Basic listener class that just prints recived tweets to stdout (in console)
    """

    def __init__(self, filename):
        self.filename = filename

    def on_data(self, raw_data):
        # print the data "IN" from the listener
        try:
            print(raw_data)
            with open(self.filename, 'a') as f:
                f.write(raw_data)
        except BaseException as ex :
            print("Error on_data method: ", str(ex))

    def on_error(self, status_code):
        # When error happens
        print("ERROR: ", status_code)

if __name__ == "__main__":
    hashtags = ['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders']
    filename = 'tweets.json'

    tStreamer = TwitterStreamer()
    tStreamer.stream_tweets(filename, hashtags)

