#Listen to the tweets, based on keywords and hashtags
from tweepy.streaming import StreamListener
from tweepy import Stream

#For authentification
from tweepy import OAuthHandler

from credentails import twitter_credenatils as tc

#Class which allow us to print the tweets
class StdOutListener(StreamListener):
    #override

    #print the data "IN" from the listener
    def on_data(self, raw_data):
        print(raw_data)
        return 1

    #When error happens
    def on_error(self, status_code):
        print("ERROR: ", status_code)
        return 0

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(tc.CONSUMER_API_KEY, tc.CONSUMER_API_SECRET_KEY)
    auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

    #Twitter stream
    strm = Stream(auth, listener)
    #listener is responsable for how to deal with data and errors

    #Filtring tweets and focus on hashtags and keywords
    strm.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])

