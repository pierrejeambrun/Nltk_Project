
import pickle
from nltk.classify import ClassifierI
from statistics import mode, _counts
from TrainingMovieReviews import find_features
from nltk.tokenize import word_tokenize


# Create documents, only adjectives in it key words.

save_classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/documents.p", "rb"))

word_features = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/word_features.p", "rb"))


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        table = _counts(votes)

        return table[0][0]

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(_counts(votes)[0][0])
        conf = choice_votes / len(votes)
        return conf


# Pikles everything
classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/naivebayes.p", "rb"))

MNB_classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/MNB_classifier.p", "rb"))

BernoulliNB_classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/BernoulliNB_classifier.p", "rb"))

LogisticRegression_Classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/LogisticRegression_Classifier.p", "rb"))

SGDClassifier_Classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/SGDClassifier_Classifier.p", "rb"))

LinearSVC_classifier = pickle.load(open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/LinearSVC_classifier.p", "rb"))

voted_classifier = VoteClassifier(classifier, MNB_classifier, BernoulliNB_classifier, LogisticRegression_Classifier,
                                  SGDClassifier_Classifier, LinearSVC_classifier)




def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for u in word_features:
        features[u] = (u in words)
    return features