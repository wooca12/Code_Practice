#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    // s = s.substr(0, 1) + s.substr(2);
    // s = s.substr(0, s.length() - 2) + s.substr(s.length() - 1);

    s = s.erase(1, 1);
    s = s.erase(s.length() - 2, 1);
    
    cout << s << endl;


    return 0;
}