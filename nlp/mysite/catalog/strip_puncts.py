'''
data = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\trainingandtestdata\\train_data.csv",delimiter=",",header=0,encoding="latin1")
import sys
sys.path.insert(0,"C:\\Users\\Lenovo\\Desktop\\nlp")
'''
import string,nltk,sys,re
#sys.path.insert(0,"C:\\Users\\Lenovo\\Desktop\\nlp\\tweets")
from . import globals
from nltk.corpus import stopwords
def xyz(s):
	puncts=string.punctuation
	puncts=puncts.replace("'","")
	puncts=puncts.replace("%","")
	s=" ".join(filter(lambda x:x[0]!='@',s.split()))
	for c in puncts:
		 s=s.replace(c,"")
	s=" ".join(w.lower() for w in s.split())
	s=" ".join(re.sub(r"http.*","",w) for w in s.split())
	return s
	
def extract_features(tweet):
	features={}
	for word in globals.word_features:
		features['contains(%s)'%word]=(word in tweet)
	print("Trained:  %d"%globals.x)
	globals.x+=1
	return features
	
def get_features(wordlist):
	wordlist=nltk.FreqDist(wordlist)
	features=wordlist.keys()
	return features
	
def get_words(tweets):
	all=[]
	for (words,polarity) in tweets:
		all.extend(words)
	return all
	
def filter_tweets(samples,n):
	list1=[]
	for n in range(0,n):
		filtered=[]
		for word in xyz(samples[n][1]).split():
			if word not in stopwords.words('english'):
				filtered.append(word)
		list1.append((filtered,samples[n][0]))
		print("Filtered:  %d"%n)
	return list1
	
def filter_words(s):
	filtered=[]
	for word in xyz(s).split():
		if word not in stopwords.words('english'):
			filtered.append(word)
	return filtered