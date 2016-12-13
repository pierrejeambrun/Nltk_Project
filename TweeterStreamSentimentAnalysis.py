import Sentiment_mod
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import nltk
from nltk import word_tokenize
import elasticsearch
import time
import tweepy


# consumer key, consumer secret, access token, access secret.
ckey = '43JtDMW8WBHYfZ8U1T6VgkiiC'
csecret = 'e1O9thgnZuzEFADU7ZbHFAgCPnsoIscMiz6sqsWvHG3mJN01jT'
atoken = '807792617891176453-WtmpWxzSIIJOkd9mqyWQyj8ATmISpmV'
asecret = 'L0sHegncguAMuNXD6ejcS42Sf7ahA2zpbLHs8ipjL3D4U'
es = elasticsearch.Elasticsearch()
# Put a sentiment on each tweet, but we take only tweet with at least 2 adjectives.
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        n = 0
        for i in nltk.pos_tag(word_tokenize(tweet)):
            if i[1][0] == "J" :
                n += 1
        if n >=2 :
            print(tweet, Sentiment_mod.sentiment(tweet))
            time.sleep(0.2)
            print('\n')
            es.index(index="tweeter",
                     doc_type="streamsentiment",
                     body={
                           "text": all_data["text"],
                           "sentiment": Sentiment_mod.sentiment(tweet)[0],
                           "confidence": Sentiment_mod.sentiment(tweet)[1],
                            "fielddata": True
                           })
        return True


    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# api= tweepy.API(auth)
# api.update_status("Trying out my new app, Stream sentiment analysis ! #Tweepy #OAuth #ElasticSearch #NLTK")


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"], languages=["en"])

