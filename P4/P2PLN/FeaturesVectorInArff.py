import nltk
from io import open
from FrequentWordsExtractor import FrequentWordsExtractor
from FrequencyVectorExtractor import FrequencyVectorExtractor
import glob
import sys  

reload(sys)
sys.setdefaultencoding("utf-8")

class FeaturesVectorInArff:
    def __init__(self, tokens=50, files_path = 'dataset/*_*'):
        
        self.n_tokens = 50
        self.files_path = files_path

        #Config nltk
        nltk.download('punkt')

    def generate(self):
        #Extract the n_tokens most used in full dataset
        words_extract = FrequentWordsExtractor(self.n_tokens)
        most_freq = words_extract.extract(self.files_path)

        #contar cuantas vegades surt cada paraula per text

        list_counter = {}
        freq_vec_extractor = FrequencyVectorExtractor(most_freq)
        for file_name in glob.glob(self.files_path):
            list_counter[file_name] = freq_vec_extractor.extract(file_name)


        #crear fitxer arff
        arff_file = open("data.arff", "wb");
        arff_file.write("@RELATION  Words\n\n")
        for attribut in most_freq:
            arff_file.write("@attribute \"" + attribut + "\" REAL" + "\n")
        arff_file.write("@attribute 'genero' {female,male}\n")
        arff_file.write("@data\n")

        for filename, freq in list_counter.iteritems():
            gender = filename.split("_")[1]
            f_list = str(freq).replace("]","").replace("[","")
            arff_file.write(f_list + ", " + gender + "\n")
