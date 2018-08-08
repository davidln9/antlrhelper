#include "ListGenJava.hpp"
#include <iostream>
using namespace std;

ListGenJava::ListGenJava(vector<Token*> tokens) {
    this->tokens = tokens;
}

string ListGenJava::buildFile(ofstream &fileOut, vector<string> preprocess, bool privateClass, bool staticClass, string base, string listener) {
	
	while (!preprocess.empty()) {
		fileOut<<preprocess.back()<<endl;
		preprocess.pop_back();
	}
	
	fileOut<<endl<<endl<<endl;
	
	if (privateClass) {
		fileOut<<"private ";
		if (staticClass) {
			fileOut<<"static ";
		}
		fileOut<<"class ";
	} else {
		fileOut<<"public ";
		if (staticClass) {
			fileOut<<"static ";
		}
		fileOut<<"class ";
	}
	bool valid = false;

	if (base.at(base.size()-5) == '.') {
		if (base.at(base.size()-4) == 'j') {
			if (base.at(base.size()-3) == 'a') {
				if (base.at(base.size()-2) == 'v') {
					if (base.at(base.size()-1) == 'a') {
						valid = true;
					}
				}
			}
		}
	}
	
	if (!valid) {
		cerr<<"Base listener must be a .java file"<<endl;
		exit(1);
	}
	string realName = "";
	for (int i = 0; i < listener.size() - 5; i++) {
		realName += listener[i];
	}
	
	string baseName;
	for (int i = 0; i < base.size() - 5; i++) {
		baseName += base[i];
	}
	
	
	
	fileOut<<realName<<" "<<"extends"<<" "<<baseName<<" {"<<endl;
	return realName;
}

void ListGenJava::createFile(string arg, vector<string> enterStatements, vector<string> exitStatements, bool debug, vector<string> 
		preprocess, bool privateClass, bool staticClass, string base) {
    ofstream fileOut;
    fileOut.open(arg);
	string rName;
	rName = buildFile(fileOut, preprocess, privateClass, staticClass, base, arg);
	
	vector<functions*> names;
	
	string name;
	string parser;
	string context;
	bool isValid = false;
	string paramName;
	int i = 0;
	cout<<tokens.size()<<endl;
	cout<<(i<tokens.size())<<endl;
	while (i < tokens.size()) {
		if (tokens.at(i)->type == AMPERSAND) {
			i++;
			cout<<"@"<<endl;
			if (tokens.at(i)->literal_text == "Override") {
				i++;
				cout<<"Override"<<endl;
				while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
					i++;
				}
				if (tokens.at(i)->literal_text == "public") {
					i++;
					cout<<"public"<<endl;
					while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
						i++;
					}
					if (tokens.at(i)->literal_text == "void") {
						i++;
						cout<<"void"<<endl;
						while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
							i++;
						}
						name = tokens.at(i)->literal_text;
						cout<<name<<endl;
						i++;
						while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
							i++;
						}
						if (tokens.at(i)->type == LPAREN) {
							i++;
							cout<<"LPAREN"<<endl;
							while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
								i++;
							}
							if (tokens.at(i)->type == ID) {
								parser = tokens.at(i)->literal_text;
								i++;
								cout<<parser<<endl;
								while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
									i++;
								}
								if (tokens.at(i)->type == DOT) {
									i++;
									cout<<"DOT"<<endl;
									while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
										i++;
									}
									if (tokens.at(i)->type == ID) {
										context = tokens.at(i)->literal_text;
										cout<<context<<endl;
										i++;
										while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
											i++;
										}
										if (tokens.at(i)->type == ID) {
											paramName = tokens.at(i)->literal_text;
											i++;
											cout<<paramName<<endl;
											while (tokens.at(i)->type == WS || tokens.at(i)->type == TAB || tokens.at(i)->type == NEWLINE) {
												i++;
											}
											if (tokens.at(i)->type == RPAREN) {
												functions * f = new functions;
												f->name = name;
												f->parser = parser;
												f->context = context;
												f->param = paramName;
												names.push_back(f);
												cout<<"RPAREN"<<endl;
											}
										}
									}
								} 
							}						
						}
					}
				}
			}
		} else {
			i++;
		}
	}
	if (debug) {
		fileOut<<endl<<endl;
		fileOut<<"\tbool eventTraceEnabled = false;"<<endl;
		fileOut<<"\tpublic "<<rName<<"(int eventTrace) {"<<endl;
		fileOut<<"\t\tif (eventTrace != 0) {"<<endl;
		fileOut<<"\t\t\teventTraceEnabled = true;"<<endl;
		fileOut<<"\t\t}"<<endl<<endl;
		fileOut<<"\t}"<<endl;
	} else {
		fileOut<<endl<<endl;
		fileOut<<"\tpublic "<<rName<<"() {"<<endl<<"\t\t//empty constructor"<<endl;
		fileOut<<"\t}"<<endl;
	}
	while (!names.empty()) {
		fileOut<<endl;
		fileOut<<"\t@Override"<<endl;
		fileOut<<"\tpublic void "<<names.back()->name<<"("<<names.back()->parser<<"."
			<<names.back()->context<<" "<<names.back()->param<<") {"<<endl;
		if (debug) {
			fileOut<<"\t\tif (eventTraceEnabled) {"<<endl;
			fileOut<<"\t\t\tSystem.out.println(\"listener ... "<<names.back()->name<<"\");";
			fileOut<<"\n\t\t}"<<endl;
		}
		if (enterStatements.size() > 0 && rName[1] == 'n') {
			for (size_t i = 0; i < enterStatements.size(); i++) {
				fileOut<<"\t\t"<<enterStatements.at(i)<<endl;
			}
		}
		if (exitStatements.size() > 0 && rName[1] == 'x') {
			for (size_t i = 0; i < exitStatements.size(); i++) {
				fileOut<<"\t\t"<<exitStatements.at(i)<<endl;
			}
		}
		
		names.pop_back();
		
		fileOut<<"\n\t}"<<endl;
	}
	
	fileOut<<"}";
	
    fileOut.close();
}
