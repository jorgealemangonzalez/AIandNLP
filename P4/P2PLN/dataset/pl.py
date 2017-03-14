import nltk , glob 
import sys


class SearchMostUsed: 
	WordsCount = {}
	for filename in glob.glob('*_*'):
		fp = open(filename,"r")
		for word in fp.read().split():
   			WordsCount[(word)] = 1
   		#for i in range(len(WordsCount)):
   		#	print(WordsCount[i])
   		#close(fp)
   		for i in range(len(WordsCount)) :
   			print(WordsCount[i])
   		#close(fp)