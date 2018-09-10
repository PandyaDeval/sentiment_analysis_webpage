import nltk,pandas as pd, sys,pickle,random,os
from nltk.corpus import stopwords
#sys.path.insert(0,"C:/Users/Lenovo/Desktop/nlp/tweets")
from . import strip_puncts as sp,globals
print("Importing necessary libraries...")


#insert user created module path and import it
#sys.path.insert(0,"C:\\Users\\Lenovo\\Desktop\\nlp\\tweets")




#read training dataset
print("Reading Dataset...")
data = pd.read_csv(os.path.join(os.path.dirname(__file__),'trainingandtestdata/train_data.csv'),delimiter=",",header=0,encoding="latin1")

#tuples of tweets and their polarities
low=799498
high=800498
print("Forming samples...")
samples=list(((data['polarity'][n],data['text'][n]) for n in range(low,high)))
random.shuffle(samples)
globals.x=0
list1=[]
list1_p=[]


#filter all tweets
print("Filtering tweets and forming list1...")
list1=sp.filter_tweets(samples,(high-low))
for n in range(0,(high-low)):
	list1_p.append(list1[n][1])

print("Forming word_features...")
globals.word_features=sp.get_features(sp.get_words(list1))

#extract features from filtered wordlist of tweet taken as input
'''def extract_features(tweet):
	features={}
	for word in word_features:
		features['contains(%s)'%word]=(word in tweet)
	global x
	print("Trained:  %d"%x)
	x+=1
	return features'''

print("Creating training set...")
#Creating training set
training_set=nltk.classify.apply_features(sp.extract_features,list1,labeled=True)

print("Training Naive Bayes Classifier...")
#Training Naive Bayes Classifier
classifier=nltk.NaiveBayesClassifier.train(training_set)


print("Training Finished!")

'''print("Reading test dataset...")
test_data_positive = pd.read_csv(os.path.join(os.path.dirname(__file__),'trainingandtestdata/train_data_positive.csv'),delimiter=",",header=0,encoding="latin1")
test_data_negative = pd.read_csv(os.path.join(os.path.dirname(__file__),'trainingandtestdata/train_data_negative.csv'),delimiter=",",header=0,encoding="latin1")

low=0
high=20000
correct=0
incorrect=0
print("Forming samples...")
test_samples_positive=list(((test_data_positive['polarity'][n],test_data_positive['text'][n]) for n in range(70000,80000)))
test_samples_negative=list(((test_data_negative['polarity'][n],test_data_negative['text'][n]) for n in range(0,10000)))
test_samples=test_samples_positive+test_samples_negative
random.shuffle(test_samples)
globals.x=0
test_list1=[]
test_list1_p=[]


print("Filtering tweets and forming list1...")
test_list1=sp.filter_tweets(test_samples,(high-low))
for n in range(0,(high-low)):
	test_list1_p.append(test_list1[n][1])

print("Forming word_features...")
globals.test_word_features=sp.get_features(sp.get_words(test_list1))

print("Calculating accuracy...")
#accuracy=nltk.classify.accuracy(classifier,test_set)
for n in range(0,(high-low)):
	if(classifier.classify(sp.extract_features(sp.filter_words(test_samples[n][1])))==test_samples[n][0]):
		correct+=1
	else:
		incorrect+=1
	#print("%s:  real:  %d   predicted:  %d"%(test_samples[n][1], test_samples[n][0], (classifier.classify(sp.extract_features(sp.filter_words(test_samples[n][1]))))))
accuracy=correct/(correct+incorrect)
print("Correct: %d  Incorrect: %d  Accuracy: %f"%(correct,incorrect,accuracy))'''



def predict(tweet):
	if classifier.classify(sp.extract_features(sp.filter_words(tweet)))==4:
		return 'Positive'
	else:
		return 'Negative'