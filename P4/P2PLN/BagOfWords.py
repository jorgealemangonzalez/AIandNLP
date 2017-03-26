
from io import open

class BagOfWords(dict):

    def add(self, key, value):
        self[key] = value

    def writeInArff(self, most_freq, file_name='data.arff'):
        print("Writing data on "+file_name)
        arff_file = open(file_name, "wb");
        arff_file.write("@RELATION  Words\n\n")
        for attribut in most_freq:
            arff_file.write("@attribute \"" + attribut + "\" REAL" + "\n")
        arff_file.write("@attribute 'genero' {female,male}\n")
        arff_file.write("@data\n")

        for filename, freq in self.iteritems():
            gender = filename.split("_")[1]
            f_list = str(freq).replace("]","").replace("[","")
            arff_file.write(f_list + ", " + gender + "\n")

