from nltk import * 
from io import open
import glob 
import arff
import sys  

reload(sys)
sys.setdefaultencoding("utf-8")


N = 50


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
    fw.write("@RELATION  Words\n\n@ATTRIBUTE word     string\n@ATTRIBUTE file     string\n@ATTRIBUTE Freq.    NUMERIC\n")
    fw.write("\n@DATA\n")
    for filename in glob.glob('*_*'):
        fp = open(filename,"r",errors='ignore',encoding='utf-8')
        text = str(fp.read())
        words = tokenize.word_tokenize(text.decode('utf-8'))
        fd = FreqDist(words)
        for element in mostFreq:
            counter = fd.freq(element[0])
            listCounter[(element,filename)] = counter
            fw.write("\""+element[0]+"\""+","+filename+","+str(counter)+"\n")
    
    