#include "TTFileWriter.h"

#include <iostream>

TTFileWriter::TTFileWriter()
{
    //ctor
}

TTFileWriter::~TTFileWriter()
{
    //dtor
}


bool TTFileWriter::writeOutput(std::string fileName, TTBSTree& tree)
{
    fileName.append(".txt");
    std::ofstream outFile{fileName, std::ios::out};

    // early exit in case of problem
    if(!outFile)
    {
        return false;
    }

    // random valid start
    int sentences{0};
    std::array<std::string, 3> curLink{tree.getRandomStart()};
    outFile << "   " << curLink[0] << " " << curLink[1] << " " << curLink[2] << " ";

    // add another 500 words past the first three
    for(int i = 0; i < 500; i++)
    {
        curLink = tree.getRandomNext(curLink);
        outFile << curLink[2] << " ";

        // newline and indent every once in a while, for readability
        if(isEnder(curLink[2]))
        {
            sentences += 1;
            if(sentences >= 4)
            {
                outFile << "\n   ";
                sentences = 0;
            }
        }
    }

    outFile.close();
    return true;
}

// check if this is a valid sentence start
bool TTFileWriter::isEnder(std::string str)
{
    bool isEnd{false};
    if(str.back() == '.' || str.back() == '?' || str.back() == '!')
    {
        isEnd = true;
    }
    return isEnd;
}
