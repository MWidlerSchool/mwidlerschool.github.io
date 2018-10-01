#include <iostream>
//#include <string>

using namespace std;

int main()
{
    //string name{""};
    char name[30];
    cout << "Please enter your name:\n";
    //cin >> name;
    cin.getline(name, 30);
    cout << "Hello, " << name << "! Also, world." << endl;
    return 0;
}
