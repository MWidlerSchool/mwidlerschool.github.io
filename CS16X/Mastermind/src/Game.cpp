#include "Game.h"
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

Game::Game()
{
    srand(time(NULL));
    newGame();
}

Game::~Game()
{
    //dtor
}

void Game::newGame()
{
    for(Sequence& seq : previous)
    {
        seq = Sequence{};
    }

    curSeq[0] = Sequence::RED;
    curSeq[1] = Sequence::RED;
    curSeq[2] = Sequence::RED;
    curSeq[3] = Sequence::RED;

    answer = Sequence{};
    randomize(answer);
    guessesSoFar = 0;
}

void Game::nextColor(int index)
{
    curSeq[index] = Sequence::getNextColor(curSeq[index]);
}

void Game::prevColor(int index)
{
    curSeq[index] = Sequence::getPrevColor(curSeq[index]);
}

// randomizes the passed sequence
void Game::randomize(Sequence& seq)
{
    for(int i = 0; i < 4; i++)
    {
        int newVal{std::rand() % 6};
        Sequence::Color c{seq.getColorByInt(newVal)};
        seq.setColor(c, i);
    }
}

void Game::checkGuess()
{
    previous[guessesSoFar].assignByArray(curSeq);
}

int Game::getBlackResponses()
{
    return answer.getTotalBlack(previous[guessesSoFar]);
}

int Game::getWhiteResponses()
{
    return answer.getTotalWhite(previous[guessesSoFar]);
}

void Game::processTurn()
{
    previous[guessesSoFar].assignByArray(curSeq);
    int black = getBlackResponses();
    int white = getWhiteResponses();

    for(int i = 0; i < 4; i++)
    {
        if(black > i)
        {
            lastReply[i] = Sequence::BLACK;
        }
        else if(black + white > i)
        {
            lastReply[i] = Sequence::WHITE;
        }
        else
        {
            lastReply[i] = Sequence::DARK_GREY;
        }
    }

    guessesSoFar += 1;

    // check for end of game
    if(black == 4)
    {
        curGameState = WON;
    }
    else if(guessesSoFar == 10)
    {
        curGameState = LOST;
    }
}

Game::GameState Game::getGameState()
{
    return curGameState;
}

std::string Game::getGameStateString()
{
    std::string val{""};
    switch(getGameState())
    {
        case PLAYING : val = "Game State:\nPLAYING\n                                    "; break;
        case WON     : val = "Game State:\nWON    \nPress ENTER or SPACE to play again."; break;
        case LOST    : val = "Game State:\nLOST   \nPress ENTER or SPACE to play again."; break;
        default      : val = "Game State:\nERROR  "; break;
    }
    return val;
}
