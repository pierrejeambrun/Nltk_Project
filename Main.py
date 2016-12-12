import Sentiment_mod
import nltk
print(Sentiment_mod.sentiment("This movie was awesome! The acting was great, plot was wonderfull, and here were python and really exiting"))
print(Sentiment_mod.sentiment("That was odd and inappropriate "))

print(nltk.pos_tag("I'm not don't feel today"))