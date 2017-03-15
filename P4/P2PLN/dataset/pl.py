import nltk , glob 
import sys

class SearchMostUsed:
    for filename in glob.glob('*_*'):
        fp = open(filename,"r")
        fdist = FreqDist(fp)
        print(fdist)
