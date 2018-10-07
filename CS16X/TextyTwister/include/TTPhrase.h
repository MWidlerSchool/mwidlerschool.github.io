#ifndef TTPHRASE_H
#define TTPHRASE_H

#include <string>
#include <array>

class TTPhrase
{
    public:
        TTPhrase(std::string str0, std::string str1, std::string str2);
        virtual ~TTPhrase();

        std::array<std::string, 3>* getArray();
        int compare(const TTPhrase& that) const;
        int compareForNext(const std::array<std::string, 3>& curPhrase) const;
        std::string toString() const;
        bool isStarter() const;


    protected:

    private:
        std::array<std::string, 3> words;

};

#endif // TTPHRASE_H
