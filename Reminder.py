


# How to save something with pickle and reopen it
# classifier_f = open("naivebayes.pickle", "rb");    to get our initialized instance of the naive classifier.
# classifier = pickle.load(classifier_f)
# classifier_f.close()

# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump(classifier,save_classifier)
# save_classifier.close()

# Les Exception:
#
# try:
#     x = int(input('toto'))
# except Exception as ValueError:
#      print("les types ne mathent pas")


# Les boucles:
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

# Definir une classe:
# class Complexe:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart