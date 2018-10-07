#include "TTFileReader.h"

TTFileReader::TTFileReader()
{
    //ctor
}

TTFileReader::~TTFileReader()
{
    //dtor
}

// fills a passed tree with a text file
bool TTFileReader::fillTree(std::string fileName, TTBSTree& tree)
{
    fileName.append(".txt");
    std::ifstream inFile(fileName, std::ios::in);

    // early exit in case of problem
    if(!inFile)
    {
        return false;
    }

    std::string val0{};
    std::string val1{};
    std::string val2{};

    inFile >> val0;
    inFile >> val1;
    inFile >> val2;
    tree.add(val0, val1, val2);

    // iterate through the file, adding to tree
    while(inFile)
    {
        val0 = val1;
        val1 = val2;
        inFile >> val2;
        tree.add(val0, val1, val2);
    }

    inFile.close();
    return true;
}
