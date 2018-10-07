#include "TTLink.h"

TTLink::TTLink(TTPhrase phrase)
: phraseList{phrase}
{
    // ctor
}

TTLink::~TTLink()
{
    //dtor
}

// returns a copy of the phrase list
std::vector<TTPhrase> TTLink::getList() const
{
    return phraseList;
}

// get the left link
TTLink* TTLink::getLeft()
{
    return left;
}

// get the right link
TTLink* TTLink::getRight()
{
    return right;
}

// check if a left link exists
bool TTLink::hasLeft()
{
    return left == nullptr ? false : true;
}

// check if a right link exists
bool TTLink::hasRight()
{
    return right == nullptr ? false : true;
}

// roll down the left
TTLink* TTLink::setLeft(TTPhrase& newPhrase)
{
    TTLink* linkPtr = nullptr;
    // roll down if exists
    if(hasLeft())
    {
        linkPtr = left->add(newPhrase);
    }
    // else set as left
    else
    {
        linkPtr = new TTLink{newPhrase};
        left = linkPtr;
    }
    return linkPtr;
}

// roll down the right
TTLink* TTLink::setRight(TTPhrase& newPhrase)
{
    TTLink* linkPtr = nullptr;
    // roll down if already exists
    if(hasRight())
    {
        linkPtr = right->add(newPhrase);
    }
    // else set as right
    else
    {
        linkPtr = new TTLink{newPhrase};
        right = linkPtr;
    }
    return linkPtr;
}

// attempt to add a new node. Roll down if necessary
TTLink* TTLink::add(TTPhrase& newPhrase)
{
    int comparison = phraseList[0].compare(newPhrase);
    TTLink* linkPtr = nullptr;

    if(comparison == 0)
    {
        phraseList.push_back(newPhrase);
    }
    else if(comparison > 0)
    {
        linkPtr = setLeft(newPhrase);
    }
    else // comparison < 0
    {
        linkPtr = setRight(newPhrase);
    }
    return linkPtr;
}

// move down the tree to find a phrase who's first two strings match the last two of the passed phrase
std::array<std::string, 3>* TTLink::getRandomNext(std::array<std::string, 3>& curPhrase)
{
    int comparison = phraseList[0].compareForNext(curPhrase);
    std::array<std::string, 3>* linkPtr = nullptr;

    if(comparison == 0)
    {
        linkPtr = getRandomPhrase();
    }
    else if(comparison > 0)
    {
        if(left != nullptr)
        {
            linkPtr = left->getRandomNext(curPhrase);
        }
    }
    else // comparison < 0
    {
        if(right != nullptr)
        {
            linkPtr = right->getRandomNext(curPhrase);
        }
    }
    return linkPtr;
}

// return the entire tree, alphabetized. This may be friggin' huge.
void TTLink::traverse(std::vector<std::string>& bigList)
{
    if(this->hasLeft())
    {
        left->traverse(bigList);
    }
    for(TTPhrase curPhrase : phraseList)
    {
        bigList.push_back(curPhrase.toString());
    }
    if(this->hasRight())
    {
        right->traverse(bigList);
    }
}

// return a random phrase from this link
std::array<std::string, 3>* TTLink::getRandomPhrase()
{
    unsigned int index{std::rand() % phraseList.size()};
    return phraseList[index].getArray();
}
