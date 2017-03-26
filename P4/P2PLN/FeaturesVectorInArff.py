import nltk
from FrequentWordsExtractor import FrequentWordsExtractor
from FrequencyVectorExtractor import FrequencyVectorExtractor
from BagOfWords import BagOfWords
import glob
import sys  

reload(sys)
sys.setdefaultencoding("utf-8")

class FeaturesVectorInArff:
    def __init__(self, tokens=50, files_path = 'dataset/*_*'):

        self.n_tokens = tokens
        self.files_path = files_path

        #Config nltk
        nltk.download('punkt')

    def generate(self, output_file='data.arff'):
        #Extract the n_tokens most used in full dataset
        words_extract = FrequentWordsExtractor(self.n_tokens)
        most_freq = words_extract.extract(self.files_path)

        #Frequency by text

        bag = BagOfWords()
        freq_vec_extractor = FrequencyVectorExtractor(most_freq)
        for file_name in glob.glob(self.files_path):
            bag.add(key = file_name , value = freq_vec_extractor.extract(file_name))

        #crear fitxer arff
        bag.writeInArff(most_freq, file_name=output_file)
