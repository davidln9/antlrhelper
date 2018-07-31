//
//  ListGen.cpp
//  listP
//
//  Created by David Edwards on 7/27/18.
//  Copyright © 2018 David Edwards. All rights reserved.
//

#include "ListGen.hpp"
#include <iostream>
using namespace std;

ListGen::ListGen(vector<Token*> tokens) {
    this->tokens = tokens;
}

void ListGen::createFile() {
    size_t j = 0;
    string funcName;
    for (size_t i = 0; i < tokens.size(); i++) {
        if (tokens.at(i)->literal_text == "def") {
            //while (tokens.at(++j)->type != ID);			
			funcName = tokens.at(i+2)->literal_text;
            while (tokens.at(++i)->literal_text != "pass");
            tokens.at(i)->literal_text = "if self._eventTrace == 1:\n\t\t\tself._log.write(\"listener ... "+funcName+"\")\n\t\tpass";
        } else if (tokens.at(i)->literal_text == "class") {
			while (tokens.at(++i)->type != COLON);
			if (tokens.at(i+1)->type == ID) {
				tokens.at(i+1)->literal_text = "\n\t_eventTrace=0\n\tdef __init__(self, event:int):\n\t\tself._eventTrace=event\n\t"
					+tokens.at(i+1)->literal_text;
			} else if (tokens.at(i+1)->type == WS || tokens.at(i+1)->type == NEWLINE || tokens.at(i+1)->type == TAB) {
				tokens.at(i+1)->literal_text ="\n\t_eventTrace=0\n\tdef __init__(self, event:int, log):\n\t\tself._eventTrace=event\n\t\tself._log=log";
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
				cout<<"\t";
				i+=3;
			} else {
				cout<<" ";
			}
		} else if (tokens.at(i)->type == NEWLINE) {
			cout<<"\n";
		} else if (tokens.at(i)->type == TAB) {
			cout<<"\t";
		} else if (tokens.at(i)->type == SINGLE_QUOTE_STRING) {
			cout<<"\'"<<tokens.at(i)->literal_text<<"\'";
		} else if (tokens.at(i)->type == DOUBLE_QUOTE_STRING) {
			cout<<"\""<<tokens.at(i)->literal_text<<"\"";
		} else {
			cout<<tokens.at(i)->literal_text;
		}
    }
}

