#ifndef TTBSTREE_H
#define TTBSTREE_H

#include "TTLink.h"
#include <string>
#include <vector>
#include <array>

class TTBSTree
{
    public:
        TTBSTree();
        virtual ~TTBSTree();

        void add(TTPhrase& newPhrase);
        void add(std::string str0, std::string str1, std::string str2);
        void clear();
        void deletePointers();
        std::array<std::string, 3> getRandomStart() const;
        std::array<std::string, 3> getRandomNext(std::array<std::string, 3>) const;
        int size() const;
        std::string sizeString() const;
        void getContents(std::vector<std::string>& strList) const; // the list is passed through by reference, as it will likely be quite large
    protected:

    private:
        TTLink* head{nullptr};
        std::vector<TTLink*> linkList{};
        std::vector<TTLink*> starterList{};
};

#endif // TTBSTREE_H
