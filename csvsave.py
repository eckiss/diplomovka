

import tweepy
import csv
import datetime

from operator import add

from authentication import authentication

auth = authentication()
# Twitter API credentials
consumer_key = auth.getconsumer_key()
consumer_secret = auth.getconsumer_secret()
access_key = auth.getaccess_token()
access_secret = auth.getaccess_token_secret()


def get_all_tweets():


    # overenie
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # pole tweetov
    alltweets = []

    # pocet tweetov na ziskanie
    new_tweets = api.home_timeline(count=200)

    # ulozene
    alltweets.extend(new_tweets)

    # id koniec
    oldest = alltweets[-1].id - 1

    #
    while len(new_tweets) > 0:
        print "od %s" % (oldest)


        new_tweets = api.home_timeline(count=200, max_id=oldest)

        #ulozenie dalsich tweetov
        alltweets.extend(new_tweets)


        oldest = alltweets[-1].id - 1

        print "...%s po" % (len(alltweets))



    # ulozenie tweetov do pola
    outtweets = [
        [
            tweet.created_at,
            tweet.text.encode("utf-8"),


        ]
        for tweet in alltweets
        ]

    # for i in range(outtweets):
    #     for j in range(outtweets):
    #         print '{:2}'.format(outtweets[i][j]),
    #     print

    # ulozenie
    with open('doprava_tweets.csv' , 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["Datum", "text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':

    get_all_tweets()