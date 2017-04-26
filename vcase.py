import tweepy
import json
import os
import time


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

os.environ["SPARK_HOME"] = "/usr/local/spark2"

from authentication import authentication

auth = authentication()
# Twitter API credentials
consumer_key = auth.getconsumer_key()
consumer_secret = auth.getconsumer_secret()
access_token = auth.getaccess_token()
access_token_secret = auth.getaccess_token_secret()

api = tweepy.API(auth)

class StdOutListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):


        try:

            tweet = data.split(',"text":"')[1].split('","source')[0]
            tweets = tweet.encode("Windows-1250")
            screen_name = data.split(',"screen_name":"')[1].split('","location')[0]

            followers_count = data.split(',"followers_count":')[1].split(',"friends_count')[0]
            #created_at = data.split(',"created_at":')[1].split(',"id')[0]
            saveThis = time.time() + ' :: ' + tweets + ' :: ' + screen_name + ' :: ' + followers_count

            print saveThis

            saveFile = open('tweetsvcase.txt', 'a')

            saveFile.write(saveThis)

            saveFile.write('\n')

            saveFile.close()
            return True

        except BaseException, e:



            time.sleep(1)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':




    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())
    #stream.userstream("with=following")

    stream.userstream("with=following")

   # stream.filter(track=['doprava',  ], languages=['sk'])