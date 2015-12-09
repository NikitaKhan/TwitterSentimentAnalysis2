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

print test_tweets2

#The list of word features need to be extracted from the tweets. It is a list with every distinct words ordered by frequency of appearance. We use the following function to get the list plus the two helper functions.
word_features = get_word_features(get_words_in_tweets(tweets))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features