/**
 * Open Source Software
 */
#ifndef ListGen_hpp
#define ListGen_hpp

#include <stdio.h>
#include "TokenFeed.hpp"
#include <vector>

class ListGen {
private:
    std::vector<Token*> tokens;
public:
    ListGen(std::vector<Token*> tokens);
    void createFile(std::string arg, std::string enterStatements, std::string exitStatements, bool debug);
};

#endif /* ListGen_hpp */
