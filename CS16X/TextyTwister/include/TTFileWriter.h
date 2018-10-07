#ifndef TTFILEWRITER_H
#define TTFILEWRITER_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "TTBSTree.h"

class TTFileWriter
{
    public:
        TTFileWriter();
        virtual ~TTFileWriter();

        static bool writeOutput(std::string fileName, TTBSTree& tree);
        static bool isEnder(std::string str);

    protected:

    private:
};

#endif // TTFILEWRITER_H
