import glob
from io import open
from nltk import tokenize, FreqDist

class FrequentWordsExtractor:

    def __init__(self,number_words):
        self.number_words = number_words

    def extract(self,files_path):
        print("Extracting the {} most common words...".format(self.number_words))

        fdist = "".encode('utf-8')
        for filename in glob.glob(files_path):
            fp = open(filename,"r",errors='ignore',encoding='utf-8')
            text = str(fp.read())
            fdist += text
            fp.close()
        words = tokenize.word_tokenize(fdist.decode('utf-8'))
        most_freq = FreqDist(words).most_common(self.number_words)
        result = [token for token,_ in most_freq]
        print("Extracted successfully")

        return result
