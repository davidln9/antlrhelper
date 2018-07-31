/**
 * Open Source Software
 * see README.md for usage
 */
#include <iostream>
#include <fstream>
#include "MULRLexer.hpp"
#include "ListGen.hpp"
#include <cstring>
using namespace std;


int main(int argc, const char * argv[]) {
    ifstream grammar;
    bool parse;
    if (argc < 2) {
        cerr<<"Error: Missing input file"<<endl;
        exit(1);
    } else if (argc == 2) {
//        cout<<argv[1];
        grammar.open(argv[1]);
        if (!grammar) {
            cerr<<"Input file does not exist"<<endl;
            exit(1);
        }
    }


    MULRLexer * lexer = new MULRLexer(grammar);
    vector<Token*> tokens = lexer->getTokens();
    grammar.close();
    size_t len = strlen(argv[1]);
    char * ret = new char[len+2];
    strcpy(ret, argv[1]);
    ret[len] = '1';
    ret[len+1] = '\0';
    ListGen * g = new ListGen(tokens);
    g->createFile(ret);
    //cout<<len<<endl;
    len*=2;
    len+=5;
    //cout<<len<<endl;
    //cout<<strlen(ret)<<endl;
    //cout<<strlen(argv[1])<<endl;
    char * cmd = new char[len+1];
    cmd[0] = 'm';
    cmd[1] = 'v';
    cmd[2] = ' ';

    for (size_t i = 0; i < strlen(ret); i++) {
        cmd[i+3] = ret[i];
    }
    cmd[3+strlen(ret)] = ' ';
    for (size_t i = 0; i < strlen(argv[1]); i++) {
        cmd[i+4+strlen(ret)] = argv[1][i];
    }
    cmd[4+strlen(ret)+strlen(argv[1])] = '\0';
    system(cmd);
    delete[] cmd;
    delete[] ret;
    while (!tokens.empty()) {
        delete tokens.back();
        tokens.pop_back();
    }
}