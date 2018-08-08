/**
 * Open Source Software
 */
#ifndef ListGenJava_hpp
#define ListGenJava_hpp

#include <stdio.h>
#include "TokenFeed.hpp"
#include <vector>
#include <fstream>

typedef struct functions {
	std::string name;
	std::string parser;
	std::string context;
	std::string param;
} functions;

class ListGenJava {
private:
    std::vector<Token*> tokens;
	std::string buildFile(std::ofstream &fileOut, std::vector<std::string> preStmts, bool privateClass, bool staticClass, 
		std::string interface, std::string arg);
public:
    ListGenJava(std::vector<Token*> tokens);
    void createFile(std::string arg, std::vector<std::string> enterStatements, std::vector<std::string> exitStatements, bool debug, 
		std::vector<std::string> preStmts, bool privateClass, bool staticClass, std::string interface);
};

#endif /* ListGenJava_hpp */
