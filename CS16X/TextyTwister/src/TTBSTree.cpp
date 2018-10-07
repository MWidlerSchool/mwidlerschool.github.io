#include "TTBSTree.h"

TTBSTree::TTBSTree()
{
    //ctor
}

TTBSTree::~TTBSTree()
{
    deletePointers();
}

// cleans up heap-allocated data. Called by clear() and destructor
void TTBSTree::deletePointers()
{
    for(auto linkPtr : linkList)
    {
        delete linkPtr;
        linkPtr = nullptr;
    }
}

// wipes the tree clean as a whistle
void TTBSTree::clear()
{
    deletePointers();
    head = nullptr;
    linkList.clear();
    starterList.clear();
}

// adds a new node to the tree. Usually called by overloaded function
void TTBSTree::add(TTPhrase& newPhrase)
{
    // set newPhrase as head if no head present
    if(head == nullptr)
    {
        head = new TTLink{newPhrase};
        linkList.push_back(head);

        if(newPhrase.isStarter())
        {
            starterList.push_back(head);
        }
    }

    // else roll down the tree
    else
    {
        TTLink* linkPtr = head->add(newPhrase);
        if(linkPtr != nullptr)
        {
            linkList.push_back(linkPtr);
            if(newPhrase.isStarter())
            {
                starterList.push_back(linkPtr);
            }
        }
    }
}

// main addition function
void TTBSTree::add(std::string str0, std::string str1, std::string str2)
{
    TTPhrase phrase{str0, str1, str2};
    this->add(phrase);
}

// returns the total size of the tree
int TTBSTree::size() const
{
    return linkList.size();
}

// returns the size of the tree, as well as how many starter and ending links exist
std::string TTBSTree::sizeString() const
{
    std::string str{"Links: " + std::to_string(linkList.size()) + ", Starter Links: " + std::to_string(starterList.size())};
    return str;
}

// traverses the tree and fills an alphebetized list of contents. This . . . an be quite large
void TTBSTree::getContents(std::vector<std::string>& strList) const
{
    if(head != nullptr)
    {
        head->traverse(strList);
    }
}

// returns a random starting array
std::array<std::string, 3> TTBSTree::getRandomStart() const
{
    int index{std::rand() % (int)starterList.size()};
    return *starterList[index]->getRandomPhrase();
}

// returns a random array, who's first two strings match the last two passed.
std::array<std::string, 3> TTBSTree::getRandomNext(std::array<std::string, 3> oldPhrase) const
{
    return *(head->getRandomNext(oldPhrase));
}
