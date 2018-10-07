#include "TTPhrase.h"

TTPhrase::TTPhrase(std::string str0, std::string str1, std::string str2)
: words{str0, str1, str2}
{
    // ctor
}

TTPhrase::~TTPhrase()
{
    //dtor
}

// returns a copy of the words
std::array<std::string, 3>* TTPhrase::getArray()
{
    return &words;
}

// output phrase as a space-seperated string
std::string TTPhrase::toString() const
{
    std::string returnVal{words[0] + " " + words[1] + " " + words[2]};
    return returnVal;
}

/*
compares alphabetically to another TTPhrase.
<0 = this phrase comes before
0  = this phrase is alphabetically equivalent
>0 = this phrase comes after
*/
int TTPhrase::compare(const TTPhrase& that) const
{
    int returnVal = this->words[0].compare(that.words[0]);

    // look at second word if first are same
    if(returnVal == 0)
    {
        returnVal = this->words[1].compare(that.words[1]);
    }
    return returnVal;
}

// compares the last two strings of the passed phrase to the first two of this
int TTPhrase::compareForNext(const std::array<std::string, 3>& curPhrase) const
{
    int returnVal = this->words[0].compare(curPhrase[1]);

    // look at second word if first are same
    if(returnVal == 0)
    {
        returnVal = this->words[1].compare(curPhrase[2]);
    }
    return returnVal;
}

// check if this is a valid sentence start
bool TTPhrase::isStarter() const
{
    return (words[0][0] >= 'A' && words[0][0] <= 'Z') ? true : false;
}


