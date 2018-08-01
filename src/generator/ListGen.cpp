#include "ListGen.hpp"
#include <iostream>
#include <fstream>
using namespace std;

ListGen::ListGen(vector<Token*> tokens) {
    this->tokens = tokens;
}

void ListGen::createFile(string arg, string enterStatements, string exitStatements, bool debug) {
    ofstream fileOut;
    fileOut.open(arg);
    size_t j = 0;
    string funcName;
    for (size_t i = 0; i < tokens.size(); i++) {
        if (tokens.at(i)->literal_text == "def") {
            //while (tokens.at(++j)->type != ID);
            funcName = tokens.at(i+2)->literal_text;
			if (funcName[1] == 'n') {
	            while (tokens.at(++i)->literal_text != "pass");
				if (debug) {
	            	tokens.at(i)->literal_text = "if self._eventTraceEnabled is 1:\n\t\t\tself._log.write(\"listener ... "+funcName+"\\n\")\n\t\t";
				}
				if (enterStatements != "" && debug) {
	            	tokens.at(i)->literal_text += enterStatements;
				} else if (enterStatements != "") {
					tokens.at(i)->literal_text = enterStatements;
				}
			} else {
				while (tokens.at(++i)->literal_text != "pass");
				if (debug) {
					tokens.at(i)->literal_text = "if self._eventTraceEnabled is 1:\n\t\t\tself._log.write(\"listener ... "+funcName+"\\n\")\n\t\t";
				}
				if (exitStatements != "" && debug) {
					tokens.at(i)->literal_text += exitStatements;
				} else if (exitStatements != "") {
					tokens.at(i)->literal_text = exitStatements;
				}
			}
            
		} else if (tokens.at(i)->literal_text == "class") {
            while (tokens.at(++i)->type != COLON);
            if (tokens.at(i+1)->type == ID) {
                tokens.at(i+1)->literal_text = 
					"\n\t_eventTraceEnabled=0\n\t_log=None\n\tdef __init__(self, event:int, log):\n\t\tself._eventTraceEnabled=event\n\t\tself._log=log\n\n\t"
                    	+tokens.at(i+1)->literal_text;
            } else if (tokens.at(i+1)->type == WS || tokens.at(i+1)->type == NEWLINE || tokens.at(i+1)->type == TAB) {
                tokens.at(i+1)->literal_text =
					"\n\t_eventTraceEnabled=0\n\t_log=None\n\tdef __init__(self, event:int, log):\n\t\tself._eventTraceEnabled=event\n\t\tself._log=log\n\n\t";
                tokens.at(i+1)->type = ID;
            }
        }
    }
    bool replaceWS;
    for (size_t i = 0; i < tokens.size(); i++) {
        replaceWS = true;
        if (tokens.at(i)->type == WS) {
            for (int j = i; j < i+4; j++) {
                if (tokens.at(j)->type != WS) {
                    replaceWS = false;
                    break;
                }
            }
            if (replaceWS) {
                fileOut<<"\t";
                i+=3;
            } else {
                fileOut<<" ";
            }
        } else if (tokens.at(i)->type == NEWLINE) {
            fileOut<<"\n";
        } else if (tokens.at(i)->type == TAB) {
            fileOut<<"\t";
        } else if (tokens.at(i)->type == SINGLE_QUOTE_STRING) {
            fileOut<<"\'"<<tokens.at(i)->literal_text<<"\'";
        } else if (tokens.at(i)->type == DOUBLE_QUOTE_STRING) {
            fileOut<<"\""<<tokens.at(i)->literal_text<<"\"";
        } else {
            fileOut<<tokens.at(i)->literal_text;
        }
    }
    fileOut.close();
}
