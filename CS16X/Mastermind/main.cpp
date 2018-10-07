#include "libtcod.hpp"
#include "Sequence.h"
#include "Game.h"
#include <string>
#include <Windows.h>

int moveCursorLeft(int curseLoc)
{
    if(curseLoc == 0)
    {
       return 3;
    }
    return curseLoc - 1;
}

int moveCursorRight(int curseLoc)
{
    if(curseLoc == 3)
    {
       return 0;
    }
    return curseLoc + 1;
}

void drawBoard()
{
    // draw guess slots
    for(int y = 0; y < 10; y += 1)
    for(int x = 0; x < 4; x += 1)
    {
       TCODConsole::root->setCharBackground(2 + (x * 2), (3 * y) + 2, Sequence::getColor(Sequence::DARK_GREY));
    }

    // draw player guess slots
    for(int x = 0; x < 4; x += 1)
    {
       TCODConsole::root->setCharBackground(2 + (x * 2), 34, Sequence::getColor(Sequence::DARK_GREY));
    }

    // draw reply slots
    for(int i = 0; i < 10; i += 1)
    for(int x = 11; x < 13; x += 1)
    {
       TCODConsole::root->setCharBackground(x, (i * 3) + 2, Sequence::getColor(Sequence::DARK_GREY));
       TCODConsole::root->setCharBackground(x, (i * 3) + 3, Sequence::getColor(Sequence::DARK_GREY));
    }

    std::string instructions{};
    instructions += "Mastermind \nimplementation\n2018, Michael Widler\n\n\n";
    instructions += "Use the arrow keys to set your input, and Enter or Space to submit your guess.\n\n\n";
    instructions += "Press Escape to quit.";
    TCODConsole::root->printRect(16, 1, 14, 30, instructions.data());

    std::string graphicsString{"Implements libtcod"};
    TCODConsole::root->printRect(12, 39, 30, 1, graphicsString.data());
}

void processTurn(Game& game)
{
    // draw guess in history
    for(int x = 0; x < 4; x += 1)
    {
       TCODConsole::root->setCharBackground(2 + (x * 2), (3 * game.guessesSoFar) + 2, Sequence::getColor(game.curSeq[x]));
    }

    // update game
    game.processTurn();

    // draw guess reply
    for(int x = 0; x < 2; x += 1)
    {
       TCODConsole::root->setCharBackground(11 + x, ((game.guessesSoFar - 1) * 3) + 2, Sequence::getColor(game.lastReply[x]));
       TCODConsole::root->setCharBackground(11 + x, ((game.guessesSoFar - 1) * 3) + 3, Sequence::getColor(game.lastReply[x + 2]));
    }
}

int main()
{
    //TCODConsole::setCustomFont("terminal_large.png",TCOD_FONT_LAYOUT_ASCII_INCOL);
    TCODConsole::initRoot(30, 40, "Mastermind", false);
    TCODConsole::root->setDefaultBackground(Sequence::getColor(Sequence::LIGHT_GREY));
    TCODConsole::root->setDefaultForeground(Sequence::getColor(Sequence::BLACK));

    TCODConsole::root->clear();
    drawBoard();
    TCODConsole::flush();

    int curseLoc{0};
    Game game{};

    // main loop
    bool breakF{false};
    while ( (!TCODConsole::isWindowClosed()) && (!breakF) )
    {
        // process key input
        TCOD_key_t key;
        TCODSystem::checkForEvent(TCOD_EVENT_KEY_PRESS,&key,NULL);

        if(game.getGameState() == Game::PLAYING)
        {
            switch(key.vk)
            {
                case TCODK_RIGHT    : curseLoc = moveCursorRight(curseLoc); break;
                case TCODK_LEFT     : curseLoc = moveCursorLeft(curseLoc); break;
                case TCODK_UP       : game.nextColor(curseLoc); break;
                case TCODK_DOWN     : game.prevColor(curseLoc); break;
                case TCODK_ESCAPE   : breakF = true; break;
                case TCODK_SPACE    :
                case TCODK_ENTER    : processTurn(game);
                                      curseLoc = 0;
                                      break;
                default             : ;
            }

            // place the arrow
            for(int x = 0; x < 4; x += 1)
            {
                if(x == curseLoc)
                {   // up arrow
                    if(game.getGameState() == Game::PLAYING)
                    {
                        TCODConsole::root->setChar(2 + (x * 2), 35, 24);
                    }
                    else
                    {
                        TCODConsole::root->setChar(2 + (x * 2), 35, ' ');
                    }
                }
                else
                {
                    TCODConsole::root->setChar(2 + (x * 2), 35, ' ');
                }
            }

            // draw player guess slots
            for(int x = 0; x < 4; x += 1)
            {
               TCODConsole::root->setCharBackground(2 + (x * 2), 34, Sequence::getColor(game.curSeq[x]));
            }
        }

        else // game is over
        {
            switch(key.vk)
            {
                case TCODK_ESCAPE   : breakF = true; break;
                case TCODK_SPACE    :
                case TCODK_ENTER    : game = Game{};
                                      curseLoc = 0;
                                      drawBoard();
                                      break;
                default             : ;
            }
        }
        // draw the state string
        TCODConsole::root->printRect(16, 20, 14, 30, game.getGameStateString().data());

        TCODConsole::flush();
    }

    return 0;
}
