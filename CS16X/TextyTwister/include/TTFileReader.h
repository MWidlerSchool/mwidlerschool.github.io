#ifndef TTFILEREADER_H
#define TTFILEREADER_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "TTBSTree.h"

class TTFileReader
{
    public:
        TTFileReader();
        virtual ~TTFileReader();

        static bool fillTree(std::string fileName, TTBSTree& tree);

    protected:

    private:
};

#endif // TTFILEREADER_H
