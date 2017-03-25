from io import open
from nltk import FreqDist, tokenize

#Given a file and a list of tokens to
class FrequencyVectorExtractor:

    def __init__(self,most_freq):
        self.most_freq = most_freq

    def extract(self, file_name):
        print("Extracting freqency vector of file... "+file_name)

        fp = open(file_name, "r", errors='ignore', encoding='utf-8')
        text = str(fp.read())
        words = tokenize.word_tokenize(text.decode('utf-8'))
        fd = FreqDist(words)
        freq_list = [fd.freq(element) for element in self.most_freq]

        return freq_list
