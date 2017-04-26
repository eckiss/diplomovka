from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import tweepy

from authentication import authentication  # Consumer and access token/key


class TwitterStreamListener(tweepy.StreamListener):


    def on_status(self, status):
        self.get_tweet(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("chyba 403")
            return False

    @staticmethod
    def get_tweet(tweet):

        if tweet.coordinates is not None:
            x, y = map(tweet.coordinates['coordinates'][0], tweet.coordinates['coordinates'][1])
            map.plot(x, y, 'ro', markersize=2)
            plt.draw()


if __name__ == '__main__':

    # velkost mapy
    fig = plt.figure(figsize=(18, 4), dpi=250)

    # nazov mapy
    plt.title("Mapa")

    #
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    map.bluemarble(scale=0.3)


    plt.ion()

    # zobrazenie mapy
    plt.show()

    # prihlasenie
    auth = authentication()

    consumer_key = auth.getconsumer_key()
    consumer_secret = auth.getconsumer_secret()

    access_token = auth.getaccess_token()
    access_token_secret = auth.getaccess_token_secret()

    # overenie
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    myStream.filter(locations=[-180, -90, 180, 90], async=True)