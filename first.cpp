
#include <iostream>
#include <stdio.h>
#include <map>
#include <fstream>
#include <ostream>
#include <istream>
#include <string>
#include <sstream>
#include <stdlib.h>


void init (int argc, char** argv){
    std::ifstream infile;
    if(argc !=2){
        std::cerr << "wrong num of args: " << argc-1 << "please supply one infile name \n";
        exit(1);
    }

}


int main(int argc, char** argv){
  cout << "hello world \n ";
  /*init(argc,argv); 
  unsigned int committedInsts=0; 
  unsigned int fetchIndex=0;
  while(committedInsts<icount){
    committedInsts=commit(committedInsts);
    WB();
    Issue();
    Dispatch();
    Rename();
    Decode(); 
    fetchIndex=fetch(fetchIndex);
    cyclecount++; 
  }
  emitOutput(); 
  */
  return 0;
}