import Sentiment_mod
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy


# consumer key, consumer secret, access token, access secret.
ckey = '43JtDMW8WBHYfZ8U1T6VgkiiC'
csecret = 'e1O9thgnZuzEFADU7ZbHFAgCPnsoIscMiz6sqsWvHG3mJN01jT'
atoken = '807792617891176453-WtmpWxzSIIJOkd9mqyWQyj8ATmISpmV'
asecret = 'L0sHegncguAMuNXD6ejcS42Sf7ahA2zpbLHs8ipjL3D4U'


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        print(tweet, Sentiment_mod.sentiment(tweet))
        print('\n')
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# api= tweepy.API(auth)
# api.update_status("Trying out my new app, Stream sentiment analysis ! #Tweepy #OAuth #ElasticSearch #NLTK")


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Ed "], languages=["en"])

