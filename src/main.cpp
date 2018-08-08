/**
 * Open Source Software
 * see README.md for usage
 */
#include <iostream>
#include <fstream>
#include "MULRLexer.hpp"
#include "ListGen.hpp"
#include "ListGenJava.hpp"
#include <string>
using namespace std;


int main(int argc, const char * argv[]) {
    ifstream grammar;
    vector<string> statements;
	vector<string> preStmts;
	vector<string> enterStatements;
	vector<string> exitStatements;
    int cmdOption = 0;
	int fileLoc = 1;
    bool debug = false;
	bool java = false;
	bool staticClass = false;
	bool privateClass = false;
	bool preprocess = false;
	string interface;
	bool enterStmts = false;
	bool exitStmts = false;
	bool both = false;
	string outFile = "";
    if (argc < 2) {
        cerr<<"Error: Missing input file"<<endl;
        exit(1);
    } else if (argc > 3) {
		bool hasInputFile = false;
        for (int i = 0; i < argc; i++) {
        	if (argv[i][0] == '-') {
        		if (strcmp(argv[i], "-i") == 0) {
					hasInputFile = true;
					interface = argv[i+1];
					grammar.open(argv[++i]);
					fileLoc = i;
					if (!grammar) {
						cerr<<"Input file does not exist"<<endl;
						exit(1);
					}
				} else if (strcmp(argv[i], "--enter") == 0) {
					enterStmts = true;
				} else if (strcmp(argv[i], "--exit") == 0) {
					exitStmts = true;
				} else if (strcmp(argv[i], "--both") == 0) {
					enterStmts = false;
					exitStmts = false;
					both = true;
				} else if (strcmp(argv[i], "--debug") == 0) {
					debug = true;
				} else if (strcmp(argv[i], "--java") == 0) {
					java=true;
				} else if (strcmp(argv[i], "--static") == 0) {
					staticClass = true;
				} else if (strcmp(argv[i], "--preprocess") == 0) {
					preprocess = true;
				} else if (strcmp(argv[i], "-p") == 0) {
					preprocess = true;
				} else if (strcmp(argv[i], "--private") == 0) {
					privateClass = true;
				} else if (strcmp(argv[i], "--public") == 0) {
					privateClass = false;
				} else if (strcmp(argv[i], "-o") == 0) {
					outFile = argv[++i];
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
	if (preprocess) {
		cout<<"Enter Preprocessor Commands"<<endl;
		string stmt;
		while (getline(cin, stmt)) {
			if (stmt != ";") {
				preStmts.push_back(stmt);
			} else {
				break;
			}
		}
	}
	
	if (both) {
		cout<<"Enter Statements:"<<endl;
		string stmt;
		while (getline(cin, stmt)) {
			enterStatements.push_back(stmt);
			exitStatements.push_back(stmt);
		}
	}
	
	if (enterStmts) {
		cout<<"Enter Enter Function Statements"<<endl;
		string stmt;
		cout<<"->";
		while (getline(cin, stmt)) {
			cout<<"->";
			enterStatements.push_back(stmt);
		}
	}
	if (exitStmts) {
		cout<<"Enter Exit Function Statements"<<endl;
		string stmt;
		cout<<"->";
		while (getline(cin, stmt)) {
			cout<<"->";
			if (stmt != "") {
				preStmts.push_back(stmt);
			} else {
				break;
			}
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
	if (!java) {
    	ListGen * g = new ListGen(tokens);
    	g->createFile(ret, enterStatements, exitStatements, debug);
	} else {
		ListGenJava * java = new ListGenJava(tokens);
		java->createFile(outFile, enterStatements, exitStatements, debug, preStmts, privateClass, staticClass, interface);
	}
    //cout<<len<<endl;
	if (!java) {
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
	    system(cmd);
	    delete[] cmd;
	    delete[] ret;
	}
    while (!tokens.empty()) {
        delete tokens.back();
        tokens.pop_back();
    }
}
