import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import PorterStemmer
exemple_text = "Hello Mr. Smith, how are you today? The weather is great and Python is awesome, I'am pythoned. The sky is blue"
print(sent_tokenize(exemple_text))
list_word = word_tokenize(exemple_text)
for w in word_tokenize(exemple_text):
    # print(PorterStemmer().stem(w)


    print(nltk.pos_tag(list_word))
    break



try:
    x = int(input('toto'))
except Exception as ValueError:
     print("les types ne mathent pas")




