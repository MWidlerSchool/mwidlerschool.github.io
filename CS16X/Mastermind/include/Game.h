#ifndef GAME_H
#define GAME_H

#include "Sequence.h"
#include <random>

class Game
{
    public:
        enum GameState{PLAYING, WON, LOST};
        std::array<Sequence::Color, 4> curSeq{};
        std::array<Sequence::Color, 4> lastReply{};
        Sequence answer{};
        std::array<Sequence, 10> previous{};
        int guessesSoFar{0};

        Game();
        virtual ~Game();

        void nextColor(int index);
        void prevColor(int index);
        void newGame();
        int random();
        void randomize(Sequence& seq);
        void checkGuess();
        void processTurn();
        int getBlackResponses();
        int getWhiteResponses();
        GameState getGameState();
        std::string getGameStateString();


    protected:

    private:
        GameState curGameState{PLAYING};
};

#endif // GAME_H
