import Sentiment_mod
import nltk
from nltk import word_tokenize
print(Sentiment_mod.sentiment("This movie was awesome! The acting was great, plot was wonderfull, and here were python and really exiting"))
print(Sentiment_mod.sentiment("I mean how coult it be worse?"))

print(nltk.pos_tag(word_tokenize("I'm loved, she I'm dead!")))