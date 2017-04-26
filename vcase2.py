import tweepy
import json
import os
import time

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

os.environ["SPARK_HOME"] = "/usr/local/spark2"
#Variables that contains the user credentials to access Twitter API
from authentication import authentication

auth = authentication()
# Twitter API credentials
consumer_key = auth.getconsumer_key()
consumer_secret = auth.getconsumer_secret()
access_token = auth.getaccess_token()
access_token_secret = auth.getaccess_token_secret()

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    # Overload the on_status method
    def on_status(self, status):
        try:

            # Open a text file to save tweets to
            with open('python.json', 'a') as f:

                # Check if the tweet has coordinates, if so write it to text
                if (status.coordinates is not None):
                    f.write(status)
                return True

        # Error handling
        except BaseException as e:
            print("Error on_status: %s" % str(e))

        return True

    # Error handling
    def on_error(self, status):
        print(status)
        return True

    # Timeout handling
    def on_timeout(self):
        return True

if __name__ == '__main__':

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_stream = tweepy.Stream(auth, MyStreamListener())
    twitter_stream.userstream("with=following")