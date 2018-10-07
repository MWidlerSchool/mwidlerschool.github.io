#include <iostream>

#include "TTBSTree.h"
#include "TTFileReader.h"
#include "TTFileWriter.h"
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// read in the file name. Reads the entire line, then removes the newline character at the end
string getFileName()
{
    cin.ignore();           // get any newlines out of the buffer
    string fileName{};
    getline(cin, fileName);  // get entire line
    return fileName;
}

// writes output to a .txt file
void writeOut(TTBSTree& tree)
{
    cout << "Please enter the filename to save this output under (this will overwrite any existing file with this name):\n";
    string fileName{getFileName()};
    if(TTFileWriter::writeOutput(fileName, tree))
    {
        cout << "Successfully wrote output to file '" << fileName << ".txt'." << endl;
    }
    else
    {
        cout << "Failed to write output to file '" << fileName << ".txt'." << endl;
    }
}

// reads in a .txt file, and adds it to the tree
void readIn(TTBSTree& tree)
{
    cout << "Please enter the name of the file to add (omit the '.txt'):\n";
    string fileName{getFileName()};

    if(TTFileReader::fillTree(fileName, tree))
    {
        cout << "Successfully read in '" << fileName << ".txt'.\n";
    }
    else
    {
        cout << "Unsuccessful at reading in '" << fileName << ".txt'.\n";
    }
}

int main()
{
    srand(static_cast<unsigned int>(time(0)));
    TTBSTree tree{};
    char selection{'?'};
    cout << "Welcome to Texty Twister. Read in one or more .txt files to see Markovian output.\n";

    // main loop
    while(true)
    {
        cout << "Please make your selection: (R)ead in, (W)rite out, (C)lear, or E(x)it\n";
        cin >> selection;

        switch(selection)
        {
            case 'r' :
            case 'R' :  readIn(tree);
                        break;
            case 'w' :
            case 'W' :  writeOut(tree);
                        break;
            case 'c' :
            case 'C' :  tree.clear();
                        break;
            case 'x' :
            case 'X' :  exit(0);
                        break;
            default  :  cout << "Command not understood.\n";
        }
        cout << "Current size: " << tree.sizeString() << "\n\n\n";
    }  // end main while loop
    return 0;
}
