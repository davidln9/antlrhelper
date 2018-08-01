/**
 * Open Source Software
 * see README.md for usage
 */
#include <iostream>
#include <fstream>
#include "MULRLexer.hpp"
#include "ListGen.hpp"
#include <string>
using namespace std;


int main(int argc, const char * argv[]) {
    ifstream grammar;
    vector<string> statements;
	string enterStatements="";
	string exitStatements="";
    int cmdOption = 0;
	int fileLoc = 1;
    bool debug = false;
    if (argc < 2) {
        cerr<<"Error: Missing input file"<<endl;
        exit(1);
    } else if (argc > 3) {
		bool hasInputFile = false;
        for (int i = 0; i < argc; i++) {
        	if (argv[i][0] == '-') {
        		if (strcmp(argv[i], "-i") == 0) {
					hasInputFile = true;
					grammar.open(argv[++i]);
					fileLoc = i;
					if (!grammar) {
						cerr<<"Input file does not exist"<<endl;
						exit(1);
					}
				} else if (strcmp(argv[i], "--enter") == 0) {
					enterStatements = argv[++i];
				} else if (strcmp(argv[i], "--exit") == 0) {
					exitStatements = argv[++i];
				} else if (strcmp(argv[i], "--both") == 0) {
					enterStatements = argv[++i];
					exitStatements = enterStatements;
				} else if (strcmp(argv[i], "--debug") == 0) {
					debug = true;
				} else {
					cerr<<"Unknown option "<<argv[i]<<endl;
					exit(1);
				}
        	}
        }
		if (!hasInputFile) {
			cerr<<"Missing Input File"<<endl;
			exit(1);
		}
    } else {
    	grammar.open(argv[1]);
		if (!grammar) {
			cerr<<"Input file does not exist"<<endl;
			exit(1);
		}
    }


    MULRLexer * lexer = new MULRLexer(grammar);
    vector<Token*> tokens = lexer->getTokens();
    grammar.close();
    size_t len = strlen(argv[fileLoc]);
    char * ret = new char[len+2];
    strcpy(ret, argv[fileLoc]);
    ret[len] = '1';
    ret[len+1] = '\0';
    ListGen * g = new ListGen(tokens);
    g->createFile(ret, enterStatements, exitStatements, debug);
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
    for (size_t i = 0; i < strlen(argv[fileLoc]); i++) {
        cmd[i+4+strlen(ret)] = argv[fileLoc][i];
    }
    cmd[4+strlen(ret)+strlen(argv[fileLoc])] = '\0';
	cout<<cmd<<endl;
    system(cmd);
    delete[] cmd;
    delete[] ret;
    while (!tokens.empty()) {
        delete tokens.back();
        tokens.pop_back();
    }
}
