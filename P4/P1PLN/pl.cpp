#include <iostream>
#include <map>    // diccionarios
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

#define CREATELEXIC 0
#define MAKETEST 0
#define CALCULATEDIFERENCE 1

int main(){
	map<string,map<string,int> > table; //map for word and submap for every gramatic class of each word
	string name, gramClas;
	ifstream training ("corpus.txt");

	long maxUse = -999999;
  	string mostUsed; //mostUsed gramatic Class
	if (training.is_open()){
		map<string,long> moreUsed;
		long uses;
	    while(training >> name >> gramClas && name != " "){
			table[name][gramClas]++; //count the times it's seen a specific word and specific grammar
			uses = ++moreUsed[gramClas]; //conting the gramclass 
			if(maxUse < uses){
				maxUse = uses;
				mostUsed = gramClas;
			}
		}
	    training.close();
  	}else{
  		cout << "Error opening corpus file" << endl;
  	}

#if	CREATELEXIC //defined at the beggining for creating the lexic.txt
  	ofstream lexic ("lexic.txt");
	for( map<string, map<string,int> >::iterator ii=table.begin(); ii!=table.end(); ++ii){ //iterate throw the maps
	   for (map<string,int>::iterator i = table[(*ii).first].begin() ; i != table[(*ii).first].end() ; ++i){
	   		lexic << (*ii).first << "\t" <<(*i).first << "\t" << (*i).second << endl; //storing in lexic.txt all information 
	   }
   	}
   	lexic.close();
#endif


#if MAKETEST //defined at the beggining for creating the test.txt
   	for(int i = 1 ; i <=2 ; ++i){
   		stringstream ss1,ss2;
   		string read,out;
   		ss1 << "test_" << i << ".txt";
   		ss2 << "our_test_" << i << ".txt";
	   	ifstream testinginp (ss1.str().c_str());
	   	ofstream testingout (ss2.str().c_str());
	   	while(testinginp >> name && name != " "){
	   		string bestpredict;
	   		int maxV = -99999;
	   		map<string,int>::iterator i;
	   		if(!table[name].size()){ //if it's empty we assign the most used gramClass
	   			bestpredict = mostUsed;
		   	}else{
		   		for (i= table[name].begin() ; i != table[name].end() ; ++i){ //if word have more than one get the most used
			   		if ((*i).second > maxV){
			   			maxV = (*i).second;
			   			bestpredict = (*i).first; //get the betpredit based in the number of times we had seen in the corpus
			   		}
			   	}
		   	}
		   	testingout << name << "\t" << bestpredict<<endl;
	   	}
	   	testinginp.close();
	   	testingout.close();
   	}
#endif

#if CALCULATEDIFERENCE //calculate the difference between out test and the real values of the word
   	for(int i = 1 ; i <= 2 ; ++i){
   		float cont = 0;
   		float total=0;
   		string name1,name2,gramClas1,gramClas2,read1,read2;
   		stringstream ss1,ss2;
		ss1 << "our_test_" << i << ".txt";
		ss2 << "gold_standard_" << i << ".txt";
		ifstream our(ss1.str().c_str());
		ifstream gold(ss2.str().c_str());
		while(gold >> name1 >> gramClas1 && name != " "){ //comparing the two files
			our >> name2 >> gramClas2;
			total++; //number of word of every file
			if(gramClas1 == gramClas2)cont++;//number of matches
		}
		cout << "Accuracy of test " << i << " it's : "<< ((float)cont/total)*100 << "% percentage " << endl; //calculate the accuracy
		our.close();
		gold.close();
   	}


#endif


}