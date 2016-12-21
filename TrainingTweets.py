import nltk
import random
import pickle
from nltk import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI    #Inherite the classifier type
from statistics import mode
import json


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for u in word_features:
        features[u] = (u in words)
    return features

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

if __name__ == '__main__':
    # allowed_word_types = ["J","N","V","!", ")", "("]
    allowed_word_types = ["J"]
    all_words = []
    documents = []
    short_pos = open("C:/Users/Pierre/AppData/Roaming/nltk_data\corpora/twitter_samples/positive_tweets.json",
                     "r")
    short_neg = open("C:/Users/Pierre/AppData/Roaming/nltk_data\corpora/twitter_samples/negative_tweets.json",
                     "r")
    # Create documents, only adjectives in it key words.

    for line in short_pos:
        toto = json.loads(line)
        documents.append((toto['text'], "pos"))
        words = word_tokenize(toto['text'])
        pos = nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())

    for line in short_neg:
        toto = json.loads(line)
        documents.append((toto['text'], "neg"))
        words = word_tokenize(toto['text'])
        pos = nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())

    pickle.dump(documents, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/documents.p", "wb"))

    # print(all_words)
    all_words = nltk.FreqDist(all_words)
    # print(all_words.most_common(100))
    # print(all_words["stupid"])
    # Trouve les mots les plus fréquent dans les reviews
    # word_features = list(all_words.keys())[:3000]
    word_features = list()
    for u in all_words.most_common(1000):
        word_features.append(u[0])
    print(word_features)
    pickle.dump(word_features, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/word_features.p", "wb"))

    # open('C:/Users/Pierre/AppData/Roaming/nltk_data/corpora/movie_reviews/neg/cv000_29416.txt','r').read()

    # On a pris un filtre de mots (random) ont regarde si ils sont dans le message, puis on donne le label
    # print(find_features((movie_reviews.words('neg/cv000_29416.txt'))))
    featuresets = [(find_features(rev), category) for (rev, category) in documents]

    random.shuffle(featuresets)

    training_set = featuresets[:9000]
    testing_set = featuresets[9000:]

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Original Naive Bayes Algo accuracy percent", (nltk.classify.accuracy(classifier, testing_set)) * 100)

    classifier.show_most_informative_features(15)

    # MultinomialNB Classifier
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)
    print("MNB_classifier accuracy percent", (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

    # GaussianNB Classifier
    # GaussianNB_classifier = SklearnClassifier(GaussianNB())
    # GaussianNB_classifier.train(trainin_set)
    # print("GaussianNB_classifier accuracy percent", (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)

    # BernoulliNB Classifier
    BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
    BernoulliNB_classifier.train(training_set)
    print("BernoulliNB_classifier accuracy percent",
          (nltk.classify.accuracy(BernoulliNB_classifier, testing_set)) * 100)

    # Linear model LogisticRegression, SGDClassifier
    LogisticRegression_Classifier = SklearnClassifier(LogisticRegression())
    LogisticRegression_Classifier.train(training_set)
    print("LogisticRegression_Classifier accuracy percent",
          (nltk.classify.accuracy(LogisticRegression_Classifier, testing_set)) * 100)

    SGDClassifier_Classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_Classifier.train(training_set)
    print("SGDClassifier_Classifier accuracy percent",
          (nltk.classify.accuracy(SGDClassifier_Classifier, testing_set)) * 100)

    # SVC model  import SVC, LinearSVC, NuSVC
    # SVC_Classifier = SklearnClassifier(SVC())
    # SVC_Classifier.train(training_set)
    # print("SVC_Classifier accuracy percent", (nltk.classify.accuracy(SVC_Classifier, testing_set))*100)

    LinearSVC_classifier = SklearnClassifier(LinearSVC())
    LinearSVC_classifier.train(training_set)
    print("LinearSVC_classifier accuracy percent", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

    NuSVC_classifier = SklearnClassifier(NuSVC())
    NuSVC_classifier.train(training_set)
    print("NuSVC_classifier accuracy percent", (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)

    voted_classifier = VoteClassifier(classifier, MNB_classifier, BernoulliNB_classifier, LogisticRegression_Classifier,
                                      SGDClassifier_Classifier, LinearSVC_classifier, NuSVC_classifier)

    print("voted_classifier accuracy percent", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

    # Pikles everything
    pickle.dump(classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/naivebayes.p", "wb"))

    pickle.dump(MNB_classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/MNB_classifier.p", "wb"))

    pickle.dump(BernoulliNB_classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/BernoulliNB_classifier.p", "wb"))

    pickle.dump(LogisticRegression_Classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/LogisticRegression_Classifier.p", "wb"))

    pickle.dump(SGDClassifier_Classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/SGDClassifier_Classifier.p", "wb"))

    pickle.dump(LinearSVC_classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/LinearSVC_classifier.p", "wb"))

    pickle.dump(NuSVC_classifier, open("C:/Users/Pierre/PycharmProjects/NLTK/Pickle/NuSVC_classifier.p", "wb"))
