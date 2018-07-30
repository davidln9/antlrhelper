//
//  main.cpp
//  MULR
//
//  Created by David Edwards on 7/13/18.
//  Copyright © 2018 David Edwards. All rights reserved.
//

#include <iostream>
#include <fstream>
#include "MULRLexer.hpp"
#include "ListGen.hpp"
using namespace std;


int main(int argc, const char * argv[]) {
    // insert code here...
    //cout << "Hello, World!\n";
    ifstream grammar;
    bool parse;
    if (argc < 2) {
        cerr<<"Error: Missing input file"<<endl;
        exit(1);
    } else if (argc == 2) {
        cout<<argv[1];
        grammar.open(argv[1]);
        parse = false;
    }
    
    
    MULRLexer * lexer = new MULRLexer(grammar);
    vector<Token*> tokens = lexer->getTokens();
    grammar.close();
    
    ListGen * g = new ListGen(tokens);
    g->createFile();
    
    while (!tokens.empty()) {
        delete tokens.back();
        tokens.pop_back();
    }
    
    
    
    //    writer->~TokenWriter();
    
    return 0;
}


