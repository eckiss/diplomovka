import tweepy
import os
import json

from tweepy import Stream
from tweepy.streaming import StreamListener


os.environ["SPARK_HOME"] = "/usr/local/spark2"
from tweepy import OAuthHandler

consumer_key = 'tHW8rwAc7KSgDPpiQLFWzJ6mR'
consumer_secret = 'mzoPBQgol2iTStMG0DQKbKVmNWBkXz0rmZaORfr3THLBgvzZX8'
access_token = '725610589565947908-hpDvo0o4CFry5kq13TjgFERaFFn2eV3'
access_secret = 'hSSAec1LcgoIRlUT0XRRunlrbsUCGUxFw9jXN0ozVWzBD'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(40):
    # Process a single status
    print(status.text)



