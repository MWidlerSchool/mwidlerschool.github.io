#ifndef TTLINK_H
#define TTLINK_H

#include <vector>
#include <string>
#include <array>
#include "TTPhrase.h"

/*
    A class that holds nodes for a BSP tree.
*/

class TTLink
{
    public:
        TTLink(TTPhrase phrase);
        virtual ~TTLink();

        std::vector<TTPhrase> getList() const;
        TTLink* add(TTPhrase& phrase);
        TTLink* getLeft();
        TTLink* getRight();
        bool hasLeft();
        bool hasRight();
        void traverse(std::vector<std::string>& bigList);
        std::array<std::string, 3>* getRandomPhrase();
        std::array<std::string, 3>* getRandomNext(std::array<std::string, 3>& curPhrase);

    protected:

    private:
        std::vector<TTPhrase> phraseList;
        TTLink* left{nullptr};
        TTLink* right{nullptr};
        TTLink* setLeft(TTPhrase& link);
        TTLink* setRight(TTPhrase& link);
};

#endif // TTLINK_H
