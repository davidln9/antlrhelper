//
//  ListGen.hpp
//  listP
//
//  Created by David Edwards on 7/27/18.
//  Copyright © 2018 David Edwards. All rights reserved.
//

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
    void createFile();
};

#endif /* ListGen_hpp */

