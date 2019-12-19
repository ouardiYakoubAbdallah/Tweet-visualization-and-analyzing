#Listen to the tweets, based on keywords and hashtags
from tweepy.streaming import StreamListener
from tweepy import Stream,API,Cursor

#For authentification
from tweepy import OAuthHandler

from credentails import twitter_credenatils as tc



class Client:
    def __init__(self, tUser=None):
        #Do not specify the twitter user, it will go on your own timeline
        self.auth = TwitterAuthenticator().authenticate()
        self.tClient = API(self.auth)
        self.tUser = tUser

    def get_tweets(self, num):
        # Do not specify the twitter user (id = None), it will go on your own timeline
        tweets = []
        for tweet in Cursor(self.tClient.user_timeline, id=self.tUser).items(num):
            tweets.append(tweet)
        return tweets

    def get_freinds(self, num):
        #function that return a list with a number of friends
        friends = []
        for f in Cursor(self.tClient.friends, id=self.tUser).items(num):
            friends.append(f)
        return friends

    def get_home_timeline(self, num):
        #function that return a number of tweets that appear in home page
        tweets = []
        for tweet in Cursor(self.tClient.home_timeline, id=self.tUser).items(num):
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

    #me_client = Client()
    #print(client.get_tweets(5))

    client = Client('Raouf_db')
    print(client.get_tweets(1))
    tStreamer = TwitterStreamer()
    tStreamer.stream_tweets(filename, hashtags)

