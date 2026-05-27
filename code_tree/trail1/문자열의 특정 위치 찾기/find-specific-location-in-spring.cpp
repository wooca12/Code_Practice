#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    char c;
    cin >> s >> c;

    int idx = s.find(c);
    
    if (idx != string::npos)
        cout << idx << endl;
    else
        cout << "No" << endl;
    return 0;
}