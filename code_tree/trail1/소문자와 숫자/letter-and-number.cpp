#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i]) != 0)
            cout << (char)tolower(s[i]);
        if (isdigit(s[i]) != 0) 
            cout << s[i];
    }
    
    return 0;
}