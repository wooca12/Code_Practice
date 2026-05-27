#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    // if (s.find("ee") != string::npos)
    //     cout << "Yes ";
    // else
    //     cout << "No ";

    // if (s.find("ab") != string::npos)
    //     cout << "Yes";
    // else 
    //     cout << "No";

    bool exist1 = false, exist2 = false;
    for (int i = 0; i < s.length() - 1; i++) {
        if (s.substr(i, 2) == "ee")
            exist1 = "Yes";
        if (s.substr(i, 2) == "ab")
            exist2 = "Yes";
    }

    if (exist1) 
        cout << "Yes ";
    else
        cout << "No ";
    if (exist2)
        cout << "Yes";
    else
        cout << "No";
    return 0;
}