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