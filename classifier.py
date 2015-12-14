import nltk
from nltk.probability import ELEProbDist, FreqDist, DictionaryProbDist
import csv


from nltk.probability import ELEProbDist, FreqDist

from nltk import NaiveBayesClassifier
from collections import defaultdict

syria = ['One of the most heartbreaking scenes is seeing a father feel helpless for his children. :( #SyrianRefugees #Syria',
         'Lets not admit anyone new from the Middle East until we vet those already here - @RandPaul to @trish_regan #SyrianRefugees #ISIS',
         'Obama wants to make it harder for law abiding citizen to own a gun while making it easier for #SyrianRefugees to come to U.S. #SanBernadino',
         'Farooks terrorist killer wife was one of those Muslim moms from the Middle East who Obama mocked us for scrutinizing. #SyrianRefugees',
         'Barack Insane Obama is wanting States to give the #SyrianRefugees "Free  Food Stamps"? #WTF! That stupis #FotherMucker! #ImpeachHisAss',
         'Obama to Turkey: control your borders. Turkey to Obama: you first. #SyrianRefugees',
         'Arent their other Muslim countries willing to take the #SyrianRefugees ?? Why not?',
         '#Jordan King Abdullah says military, diplomatic & human #development responses needed 2 #Syria crisis.',
         '#Syria. I am going to bed in New York City with you like an ache in my chest, like tears in my eyes, and like a lump in my throat.',
         'Well done Canade #HumanityFirst #refugees #Syria Good luck friends helping this effort @ZEEMANA and others ',
         'Over 40 terrorist rebel shells & rockets have fallen on west Aleppo now. Lots of casualties, going 2b another massacre like yesterday #Syria',
         'The Saudis hold a conference of #Syria rebel groups in Riyadh today incl Jihadists Ahrar al-Sham and Jaysh al-Islam',
         'No further debate on #syria needed as already been debated in the Commons this month say MPs',
         'Opening of the largest private library in West #Aleppo - With education we will defeat the forces of evil. #Syria ',
         '#ISIS claim they repelled an opposition offensive on Kafrah in northern Aleppo south of the Turkish border #Syria',
         'The village, south of the Turkish border, was taken during the night by opposition forces and retaken by ISIS this morning #Syria',
         'Boris Johnson: We must do a deal with the devil in #Syria Like this isnt STANDARD UK policy everywhere, all the time #realpolitiks',
         '15 air strikes on Akrad and Turkman mountains this morning. #Latakia #Syria',
         'Around 700 Tunisian women have traveled to #Syria to join extremist groups, according to #Tunisias Minister for Women Samira Merai.',
         'Its very confusing and hard to know this Airstrike for which Country with all this Warplanes and Airstrikes above our heads #Raqqa #Syria']


saudiArabia = ['#Hajj stampede in #SaudiArabia killed at least 2,411 pilgrims, a new AP count shows, 3 times more than what the Saudis acknowledged.',
               'A new @AP count shows that at least 2,411 pilgrims died in the crush and stampede that struck #hajj this year in #SaudiArabia.',
               'Who needs #Daesh when youve got #SaudiArabia a turnkey terrorist state ',
               'Peace-activists from #Yemen started a blog showing all Saudi warcrimes in Yemen. Expose #SaudiArabia',
               '#Houthis and Pro Saleh fighters clash with #Saudi forces in #Asir, #Najran & #Jizan regions in #SaudiArabia ',
               '#SaudiArabia Education Ministry remove 80 books incl. those by Qatab, Al-Banna & Qardawi from schools',
               '#SueMeSaudi you death worshipping misogynistic homophobic racist reptiles fuk you #SaudiArabia #ISIS #Daeshbags ',
               '#SaudiArabia invites 65 Syrian opposition figures to Riyadh ahead of peace talks',
               '52 mercenary in Riyadh are given 72 hours to leave #SaudiArabia Best kind of news!',
               '#SaudiArabia plans to stone a woman for adultery (but not the man). How #Isis of you #SueMeSaudi #saudiarabiaisisis ',
               'Well depends on what is meant by "deal", not formal like #SaudiArabia, but #ISIS is #Obama #USA trained,armed,funded ',
               'They might not be Daesh if they are simply talking to you...#SaudiArabia',
               'Change is happening in #SaudiArabia w/ 900 #Saudi women campaigning in Dec12 #municipal #elections -1st opportunity for #women to #vote',
               '#Kenya envoy to #SaudiArabia admitted to hospital after being hit by speeding car in Riyadh.  ',
               '#SaudiArabia #Art Scene Is Horrified by the Death Sentence Given to #Poet #AshrafFayadh',
               'One would dearly wish that #SaudiArabia would strike #Yemen also with a CHARM offensive...  ',
               'The hypocrisy of #UK govmnt is staggering. #Lies to serve their rich partners. Munitions Sales to #SaudiArabia.',
               'Saudi Arabia Complains About Hostility Towards Refugees, While Taking in Zero Refugees #SaudiArabia',
               'More than 900 women are running for office in #Saudi Arabia',
               'Learn about the #tribal #society in #SaudiArabia from my latest #blog post']

pakistan = ['Why Modi sweated over getting India-Pakistan ties on track',
            '#IStandWithAhmadis I believe that freedom of speech and freedom of religion go hand-in-hand in #Pakistan',
            '#IStandWithAhmadis The Ahmadi community is persecuted throughout #Pakistan by few portions of society .',
            '#BigThreeSlappedNajamSethi These are bluddy anti pak agents. Who degrade #Pakistan in every field & every forum ',
            'Thanks for all your prayers, love and support. Im humbled to be the 1st #UNwomen ambassador in #PAKISTAN',
            'Thousands abducted by #Pakistan army in 15 years. Puppet govt; accepted 8500+ only this year, but they are still missing. #HumanRightsDay',
            'Its good to know that #India and #Pakistan have announced intent to resume composite dialogue. Hope this window is not wasted. #HeartOfAsia',
            '- Pakistani cricket fans right now being like... #Cricket #India #Pakistan ',
            'Has Sushma Swaraj come to Pakistan with a plan for peace? Ask the two NSAs who met suddenly and secretly in Bangkok #Pakistan #india',
            '#Pakistan not ready for nuclear restraints as stated by FO. Civil nuclear deal at this stage only about parity with India 2/5',
            'Main points of my @HouseForeign subcommittee testimony today: Important to bring #Pakistan & all countries with nukes in nuclear regime 1/5',
            'Deadlock in #Pakistan-India relations have eased to some extent: Advisor on Foreign Affairs',
            'Islamic State is having a hard time taking root in #Pakistan',
            'Great day that needs to be celebrated. Local government system (despite many flaws&limitations) revived in #Pakistan after 8 years.',
            'Birds migrating from #Siberia to #Pakistan at advent of winter start arriving in various parts of Sindh and Punjab.',
            '#Pakistan needs #RuleOfLaw. No exceptionalism. Punish criminal acts  whether committed in name of religion, honour or patriotism.',
            'Enough lip service against terrorism. Stop enabling, encouraging, supporting Taliban Inc. Theyre #FasadisNotJihadis #Pakistan',
            'Renewed focus on #Pakistan and militancy in international media while press here remains consumed with domestic local government elections']

china = ['#China govt cyber chief justifies pervasive Internet #censorship http://bit.ly/1U8ihpu  "Freedom is our goal" LOL ',
         '#Chinas onshore yuan continues to weaken. This is going to have global consequences if it continues. ',
         'What a way for #China to mark #HumanRightsDay: another phase of sham trial of lawyer Pu Zhiqiang',
         '#China cuts yuans reference rate to weakest since 2011',
         'The amazing ways #WeChat is used in #China',
         'Basic commuter gear in #China',
         '#China trade numbers remained sluggish in November; imports and exports contracting ',
         '#Chinas #Yuan Set for Weakest Close Since 2011 as Exports, Reserves Drop http://bloom.bg/1HRFjzz  via @business ',
         '#China air pollution could prematurely kill more than 250,000 people currently living in countrys major cities http://on.wsj.com/1NdvtEY ',
         '#China issues 1st "red alert" for smog',
         'Just returned from an incredible trip to #China. Posting delayed as all western social media channels are blocked. ',
         'Whoops! Xi Jinping resigns, according to typo in #China state media report http://gu.com/p/4ep4t/stw ',
         'Chinese company Wanda Sports is aiming to become the worlds first sports firm with an income of $10 billion #china #sport',
         'German industrial production rebounded in Oct but stayed below expectations as #China weighs http://bloom.bg/1m6iuhG  ',
         '#China bars Canadas Miss World contender, a human rights activist, from contest. BOYCOTT! ',
         'More #China brokers disappear: Citic Securities says unable to contact two senior executives http://reut.rs/1INj48Q ',
         'In Nigeria, #China Investment Comes With a Downside http://nyti.ms/1SFfrHI ',
         'Going home by Jonathan Chua #China ']

chinaNews = ['Dance-related products a hit with those aged above 50',
             'Beijing lifts red alert but smog will be back in two days',
             'Shanghai to build its most romantic graffitti wall',
             'Miss World contestants visit welfare center in Hainan',
             'National parks for pandas planned in China ',
             'Govt funds help 410 mln Chinese students in five years',
             'Chinas draft law allows public libraries to be named after donators',
             '5 missing after S China fishing boat collision ',
             'Polish man who stole Chinese actress safe arrested in Copenhagen',
             'China to register unregistered citizens',
             'Terror rumormonger detained in Central China',
             'Chinas beauty by rail',
             'Think all Chinese dama do is dance, buy gold? Think again',
             'China urges faster, cheaper Internet by year end',
             'China urges stronger global anti-terrorism cooperation',
             'Yangtze River gets cleaner',
             'Chinese tourists in Australia outspend Brits, Americans and Canadians combined',
             'China forex reserves plunge to lowest level since Feb 2013 ',
             'Life in smoggy Beijing amid red alert',
             'Christmas lights across the worlds shopping districts']

pknews = ['Arrived in #Pakistan to attend the 5th Ministerial Conference on Heart of Asia Istanbul Process on Afghanistan. ',
          'When the mirror lies writes @SumairaJajja  http://www.dawn.com/news/1073952  on physical, sexual harassment faced by female journalists in #Pakistan',
          'Pakistan is a place where Mullah target innocent Ahmadis by spreading hate against them.',
          'Aqeela Asifi fought for #girlseducation in #Pakistan. And won.LEGEND. ',
          'Last year @USAIDPakistan provided training & eqpmt to 431 care providers in #Pakistan for Helping Babies Breathe. #MomAndBaby',
          'EAM @SushmaSwaraj meets #Pakistan PM Nawaz Sharif in #Islamabad ',
          'PM @narendramodi will visit #Pakistan next year, says @SushmaSwaraj in #Islamabad',
          'Debate: Should India be hopeful that this time #Pakistan will not backstab?',
          'California shooter Tashfeen Malik attended classes at Al-Huda in #Pakistan, says teacher',
          '7.2 magnitude #earthquake jolts northern #Pakistan',
          'A night, a lifetime at the Urs in Bhit Shah http://dawn.com/news/1224552/  #Pakistan',
          'These sites are of national and cultural importance, and will attract tourists http://www.dawn.com/news/1224500/  #Pakistan ',
          'Spies leaked secret information to #Pakistan about laser fence on Indian border',
          '#Malala you are one hell of a girl! @MalalaFund #pakistan ',
          '#Pakistans vulnerability 2 natural hazards #ClimateChange has potential 2 delay development ',
          'Molotov explosive kills 12 people at Cairo restaurant: One of the officials said the attack',
          'I can see #Pakistan rise once more',
          'A fly-on-the-wall look at #Pakistans disappointing start at #COP21',
          '#Pakistan hangs four militants linked to last years Taliban attack on Army Public School in']

sanews = ['Jobless rate in #SaudiArabia could exceed 20 percent by 2030, consulting firm predicts',
          '#SaudiArabia agrees to retry Sri Lankan maid sentenced to death by stoning ',
          'President #Barzani of #Kurdistan met with King #Salman of #SaudiArabia ',
          '#Saudi prince sues city of LA over mansion spat',
          '#Saudi King "very worried" about #Lebanon unrest ',
          '#Saudi Arabia pledges $3.5bn in aid to #Yemen ',
          '#Saudi Arabia signs deal with #UK to buy air force training jets in $3 billion deal -',
          '#Bahrain protests: #Shias rally against closer ties with #Saudi Arabia -',
          'The Battle Raging Within #Saudi Arabia Over Womens Rights ',
          '#NYT: Saudi Arabia = #Daesh/#ISIS #SaudiArabia, an ISIS That Has Made It #SaudiArabiaisISIS',
          '#SAUDI Saudi FM says Syrias #Assad must leave or be forced out.',
          '#Saudi #Women Face Off Against Men for First Time in #Elections ',
          'a decade ago, King Abdullah said hed pay the cost for any #Saudi who wanted to #study abroad',
          'The mention of #saudi stoning people remains incorrect',
          '@nytimes is saying what #Iran is shouting for several years: #Saudi Arabia, an #ISIS That Has Made It http://nyti.ms/1jb0qkq ',
          'NY Times: #Saudi King reassured by #Obama over #Iran. http://dlvr.it/C44gJf   #IranTalks #IranDeal #News #USA #UK',
          '@nytimes #US #Saudi Meddling cost #Syrian lose their Homes n run flee for life <>When will #US #saudi say #refugeeswelcome',
          'Report: #Saudi-led forces using US-made cluster bombs in #Yemen: http://nyti.ms/1LZVATT  via @nytimes']

def readCSV():
    file = open('full_training_dataset.csv')
    reader = csv.reader(file)
    finalList = []
    tup = ()
    list1 = []
    pos_tweets = []
    neg_tweets = []
 # simply iterate through it
    for line in reader:
      list1 = line[1]
      tup = (list1, line[0])
      if (line[0] == 'positive'):
        pos_tweets.append(tup)
      elif (line[0] == 'negative'):
        neg_tweets.append(tup)     
    return pos_tweets, neg_tweets

pos_tweets, neg_tweets = readCSV()

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


#print test_tweets2

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
    #print features
    return features

#features
extract_features(['love', 'this', 'car'])

#The variable  training_setcontains the labeled feature sets. It is a list of tuples which each tuple containing the feature dictionary and the sentiment string for each tweet. The sentiment string is also called label
training_set = nltk.classify.apply_features(extract_features, tweets)


#Lets take a look inside the classifier train method in the source code of the NLTK library. label_probdist is the prior probability of each label and feature_probdist is the feature/value probability dictionary. Those two probability objects are used to create the classifier.
def train(labeled_featuresets, estimator=ELEProbDist):
    # Create the P(label) distribution
    print "hello"
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    print label_probdist.prob('positive')
    print label_probdist.prob('negative')
    print feature_probdist[('negative', 'contains(best)')].prob(True)
    return NaiveBayesClassifier(label_probdist, feature_probdist)

#train the classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)


#test
for tweet in sanews:
    #print classifier.show_most_informative_features(32)
    print classifier.classify(extract_features(tweet.split()))
tweet = 'Nikita has been defeated'
print classifier.classify(extract_features(tweet.split()))


#print label_probdist.prob('positive')
#print label_probdist.prob('negative')
#print feature_probdist[('negative', 'contains(best)')].prob(True)
#print classifier.show_most_informative_features(32)


#test
#tweet = 'Larry is my friend'
#print classifier.classify(extract_features(tweet.split()))
















