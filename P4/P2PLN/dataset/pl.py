from nltk import * 
from io import open
import glob 
import arff
import sys  

reload(sys)
sys.setdefaultencoding("utf-8")


N = 50

if __name__=="main":
    mostFreqWord()

class SearchMostUsed:

    fdist = "".encode('utf-8')
    for filename in glob.glob('*_*'):
        fp = open(filename,"r",errors='ignore',encoding='utf-8')
        text = str(fp.read())
        fdist += text
        fp.close()
    words = tokenize.word_tokenize(fdist.decode('utf-8'))
    mostFreq = FreqDist(words).most_common(N)

    #contar cuantas vegades surt cada paraula per text
    listCounter = {}
    fw = open("data.arff","wb");
    fw.write("@RELATION  Words\n\n")
    for attribut in mostFreq:
        fw.write("@attribute \""+attribut[0]+"\" REAL" + "\n")
    fw.write("@attribute 'genero' {female,male}\n")
    fw.write("@data\n")
    for filename in glob.glob('*_*'):
        fp = open(filename,"r",errors='ignore',encoding='utf-8')
        text = str(fp.read())
        words = tokenize.word_tokenize(text.decode('utf-8'))
        fd = FreqDist(words)
        listCounter[(filename)] = []
        for element in mostFreq:
            listCounter[(filename)].append(fd.freq(element[0]))


    #crear fitxer arff

    for filename in listCounter:
        a = filename
        a = a.split("_")[1]
        p = str(listCounter[(filename)])
        p = p.split("[")[1]
        p = p.split("]")[0]
        fw.write( p +"," +a + "\n")