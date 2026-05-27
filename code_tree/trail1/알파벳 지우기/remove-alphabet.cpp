#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;

    string n1 = "", n2 = "";

    for (int i = 0; i < s1.length(); i++) {
        if (isdigit(s1[i]))
            n1 += s1[i];
    }
    for (int i = 0; i < s2.length(); i++) {
        if (isdigit(s2[i]))
            n2 += s2[i];
    }

    cout << stoi(n1) + stoi(n2) << endl;

    return 0;
}