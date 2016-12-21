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
ckey =
csecret =
atoken =
asecret =
es = elasticsearch.Elasticsearch()
# Put a sentiment on each tweet, but we take only tweet with at least 2 adjectives.
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = all_data['text']
            n = 0
            for i in nltk.pos_tag(word_tokenize(tweet)):
                if i[1][0] == "J":
                    n += 1
            if n >= 2:
                print(tweet, Sentiment_mod.sentiment(tweet))
                print('\n')
                es.index(index="tweeter",
                         doc_type="streamsentiment",
                         body={
                             "fielddata" : {"text_keyword": all_data["text"],
                                "sentiment_keyword": Sentiment_mod.sentiment(tweet)[0],
                                "confidence": Sentiment_mod.sentiment(tweet)[1],
                                         }
                         })
        except KeyError:

            return True


    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# api= tweepy.API(auth)
# api.update_status("Trying out my new app, Stream sentiment analysis ! #Tweepy #OAuth #ElasticSearch #NLTK")


twitterStream = Stream(auth, listener())
twitterStream.filter(twitterStream.filter(track=[""], languages=["en"]))

