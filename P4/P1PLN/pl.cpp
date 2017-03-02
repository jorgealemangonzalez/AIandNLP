#include <iostream>
#include <vector> // vectores
#include <list>   // listas
#include <map>    // diccionarios
#include <algorithm>
#include <utility> //make_pair
#include <cmath>
#include <set>
#include <sstream>
#include <string>
#include <fstream>


#define X first
#define Y second
#define LI long long
#define MP make_pair
#define PB push_back
#define SZ size()
#define SQ(a) ((a)*(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;

#define CREATELEXIC 0
#define MAKETEST 0
#define CALCULATEDIFERENCE 1

int main(){
	map<string,map<string,int> > table;
	string name, gramClas;
	map<string,long> moreUsed;
	ifstream training ("corpus.txt");
	if (training.is_open()){
	    while(training >> name >> gramClas && name != " "){
			table[name][gramClas]++; //conting the times
			moreUsed[gramClas]++; //conting the gramclass 
		}
	    training.close();
  	}else{
  		cout << "Error opening corpus file" << endl;
  	}

  	long max = -999999;
  	string mostUsed;
  	for(map<string,long>::iterator it = moreUsed.begin() ; it != moreUsed.end() ; ++it){
  		if((*it).second > max){
  			mostUsed = (*it).first; //the most used gramClass
  			max=(*it).second;
  		}
  	}
#if	CREATELEXIC
  	ofstream lexic ("lexic.txt");
	for( map<string, map<string,int> >::iterator ii=table.begin(); ii!=table.end(); ++ii){
	   for (map<string,int>::iterator i = table[(*ii).first].begin() ; i != table[(*ii).first].end() ; ++i){
	   		lexic << (*ii).first << "\t" <<(*i).first << "\t" << (*i).second << endl; //storing in lexic.txt all information 
	   }
   	}
   	lexic.close();
#endif


#if MAKETEST
   	for(int i = 1 ; i <=2 ; ++i){
   		stringstream ss1,ss2;
   		string read,out;
   		ss1 << "test_" << i << ".txt";
   		ss2 << "our_test_" << i << ".txt";
	   	ifstream testing (ss1.str().c_str());
	   	ofstream testguini (ss2.str().c_str());
	   	while(testing >> name && name != " "){
	   		string bestpredict;
	   		int max = -99999;
	   		map<string,int>::iterator i;
	   		if(!table[name].size()){ //if it's empty the most used TODO Improve thiss
	   			bestpredict = mostUsed;
		   	}else{
		   		for (i= table[name].begin() ; i != table[name].end() ; ++i){ //if word have more than one get the most used
			   		if ((*i).second > max){
			   			max = (*i).second;
			   			bestpredict = (*i).first;
			   		}
			   	}
		   	}
		   	testguini << name << "\t" << bestpredict<<endl;
	   	}
	   	testing.close();
	   	testguini.close();
   	}
#endif

#if CALCULATEDIFERENCE
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
			total++;
			if(gramClas1 == gramClas2)cont++;
		}
		cout << "Accuracy of test " << i << " it's : "<< ((float)cont/total)*100 << "% percentage " << endl;
		our.close();
		gold.close();
   	}


#endif


}