#include "Sequence.h"

Sequence::Sequence()
{
    for(TCODColor& c : seq)
    {
        c = Sequence::getColor(DARK_GREY);
    }
}

Sequence::~Sequence()
{
    //dtor
}

Sequence::Sequence(Color c0, Color c1, Color c2, Color c3)
{
   seq[0] = Sequence::getColor(c0);
   seq[1] = Sequence::getColor(c1);
   seq[2] = Sequence::getColor(c2);
   seq[3] = Sequence::getColor(c3);
}

void Sequence::setColor(const Color& c, int index)
{
    seq[index] = getColor(c);
}

TCODColor const Sequence::getColor(const Sequence::Color& c)
{
    TCODColor val{};
    switch(c)
    {
        case BLACK      : val = TCODColor::black; break;
        case WHITE      : val = TCODColor::white; break;
        case LIGHT_GREY : val = TCODColor::lighterGrey; break;
        case DARK_GREY  : val = TCODColor::grey; break;
        case RED        : val = TCODColor::red; break;
        case YELLOW     : val = TCODColor::yellow; break;
        case GREEN      : val = TCODColor::green; break;
        case CYAN       : val = TCODColor::cyan; break;
        case BLUE       : val = TCODColor::blue; break;
        case PINK       : val = TCODColor::fuchsia; break;

        default         : val = TCODColor::black;
    }

    return val;
}


Sequence::Color const Sequence::getNextColor(const Sequence::Color& c)
{
    Color val{};
    switch(c)
    {
        case RED        : val = YELLOW; break;
        case YELLOW     : val = GREEN; break;
        case GREEN      : val = CYAN; break;
        case CYAN       : val = BLUE; break;
        case BLUE       : val = PINK; break;
        case PINK       : val = RED; break;

        default         : val = BLACK;
    }

    return val;
}


Sequence::Color const Sequence::getPrevColor(const Sequence::Color& c)
{
    Sequence::Color val{};
    switch(c)
    {
        case RED        : val = PINK; break;
        case YELLOW     : val = RED; break;
        case GREEN      : val = YELLOW; break;
        case CYAN       : val = GREEN; break;
        case BLUE       : val = CYAN; break;
        case PINK       : val = BLUE; break;

        default         : val = BLACK;
    }

    return val;
}

// returns true if the color is at the passed location (0-3)
bool Sequence::checkColorAt(const Sequence& that, int index)
{
    if(seq[index] == that.seq[index])
    {
        return true;
    }
    return false;
}

// returns true if the color is present in the array, excepting the index (0-3)
bool Sequence::checkColorNotAt(const Sequence& that, int index)
{
    for(int i = 0; i < 4; i += 1)
    {
        if(i == index)
        {
            continue;
        }
        if(seq[i] == that.seq[index])
        {
            return true;
        }
    }
    return false;
}

// counts the number of black pegs to respond
int Sequence::getTotalBlack(const Sequence& guess)
{
    int val = 0;
    for(int i = 0; i < 4; i += 1)
    {
        if(checkColorAt(guess, i))
        {
            val++;
        }
    }
    return val;
}

// counts the number of white pegs to respond
int Sequence::getTotalWhite(const Sequence& guess)
{
    int val = 0;
    for(int i = 0; i < 4; i += 1)
    {
        if(checkColorAt(guess, i) == false)
        if(checkColorNotAt(guess, i))
        {
            val++;
        }
    }
    return val;
}


Sequence::Color Sequence::getColorByInt(int i)
{
    Color c = BLACK;
    switch(i)
    {
        case 0        : c = RED; break;
        case 1        : c = YELLOW; break;
        case 2        : c = GREEN; break;
        case 3        : c = CYAN; break;
        case 4        : c = BLUE; break;
        case 5        : c = PINK; break;

        default       : c = BLACK;
    }
    return c;
}

void Sequence::assignByArray(std::array<Sequence::Color, 4> val)
{
    for(int i = 0; i < 4; i += 1)
    {
        seq[i] = getColor(val[i]);
    }
}
