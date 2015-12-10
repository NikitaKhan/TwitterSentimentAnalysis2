import nltk
from nltk.probability import ELEProbDist, FreqDist, DictionaryProbDist
from nltk import NaiveBayesClassifier
from collections import defaultdict

#hardcoded tweets to start off with
pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

test_tweets = [('I feel happy this morning', 'positive'),
               ('Larry is my friend', 'positive'),
               ('I do not like that man', 'negative'),
               ('My house is not great', 'negative'),
               ('Your song is annoying', 'negative')]

#create a list of tuples - each containing 2 elements - 1. list containing the words and 2. type of sentiment
#get rid of words less than 2 characters
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))

test_tweets2 = []
for (words, sentiment) in test_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    test_tweets2.append((words_filtered, sentiment))



#The list of word features need to be extracted from the tweets. It is a list with every distinct words ordered by frequency of appearance. We use the following function to get the list plus the two helper functions.

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

#To do that, we first need a feature extractor. The one we are going to use returns a dictionary indicating what words are contained in the input passed. Here, the input is the tweet. We use the word features list defined above along with the input to create the dictionary.
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    print features
    return features

#features
extract_features(['love', 'this', 'car'])

#The variable  training_setcontains the labeled feature sets. It is a list of tuples which each tuple containing the feature dictionary and the sentiment string for each tweet. The sentiment string is also called label
training_set = nltk.classify.apply_features(extract_features, tweets)

#train the classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

#Lets take a look inside the classifier train method in the source code of the NLTK library. label_probdist is the prior probability of each label and feature_probdist is the feature/value probability dictionary. Those two probability objects are used to create the classifier.
def train(labeled_featuresets, estimator=ELEProbDist):
    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    print label_probdist.prob('positive')
    print label_probdist.prob('negative')
    print feature_probdist[('negative', 'contains(best)')].prob(True)
    return NaiveBayesClassifier(label_probdist, feature_probdist)

print "hello"
print classifier.show_most_informative_features(32)
print "hello"

#test
tweet = 'Nikita has been defeated'
print classifier.classify(extract_features(tweet.split()))



















