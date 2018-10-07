#ifndef SEQUENCE_H
#define SEQUENCE_H

#include "libtcod.hpp"
#include <array>
#include <random>


class Sequence
{
    public:
        enum Color{WHITE, BLACK, DARK_GREY, LIGHT_GREY,
                   RED, YELLOW, GREEN, CYAN, BLUE, PINK};

        Sequence();
        Sequence(Color c0, Color c1, Color c2, Color c3);
        virtual ~Sequence();

        static const TCODColor getColor(const Color& c);
        static const Color getNextColor(const Color& c);
        static const Color getPrevColor(const Color& c);
        void setColor(const Color& c, int index);
        bool checkColorAt(const Sequence& that, int index);
        bool checkColorNotAt(const Sequence& that, int index);
        int getTotalBlack(const Sequence& guess);
        int getTotalWhite(const Sequence& guess);
        Color getColorByInt(int i);
        void assignByArray(std::array<Sequence::Color, 4> val);


    protected:

    private:
        std::array<TCODColor, 4> seq;
};

#endif // SEQUENCE_H
