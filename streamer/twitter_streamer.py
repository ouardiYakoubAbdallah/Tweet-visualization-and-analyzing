#Listen to the tweets, based on keywords and hashtags
from tweepy.streaming import StreamListener
from tweepy import Stream,API,Cursor

#For authentification
from tweepy import OAuthHandler

from credentails import twitter_credenatils as tc



class Client:
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate()
        self.tClient = API(self.auth)

    def get_user_tweets(self, num):
        tweets = []
        for tweet in Cursor(self.tClient.user_timeline).items(num):
            tweets.append(tweet)
        return tweets
class TwitterAuthenticator:

    def authenticate(self):
        auth = OAuthHandler(tc.CONSUMER_API_KEY, tc.CONSUMER_API_SECRET_KEY)
        auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer:
    """
    Class used for streaming and processing tweets directly in real time from twitter
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, filename, hashtags):
        #Handling twitter auth and connect to the Streaming API
        listener = TwitterListener(filename)
        auth = self.twitter_authenticator.authenticate()

        # Twitter stream
        strm = Stream(auth, listener)
        # listener is responsable for how to deal with data and errors

        # Filtring tweets and focus on hashtags and keywords
        strm.filter(track=hashtags)




class TwitterListener(StreamListener):
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
        # triggered when error happens while streaming tweets

        if status_code == 420 :
            return False
        print("ERROR: ", status_code)

if __name__ == "__main__":
    hashtags = ['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders']
    filename = 'tweets.json'

    #client = Client()
    #print(client.get_tweets(5))

    tStreamer = TwitterStreamer()
    tStreamer.stream_tweets(filename, hashtags)

