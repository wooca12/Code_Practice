#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    if (s.find("ee") != string::npos)
        cout << "Yes ";
    else
        cout << "No ";

    if (s.find("ab") != string::npos)
        cout << "Yes";
    else 
        cout << "No";
    return 0;
}