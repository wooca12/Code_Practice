#include <iostream>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;

    if (s1.length() > s2.length())
        cout << s1 << " " << s1.length() << endl;
    else if (s1.length() < s2.length())
        cout << s2 << " " << s2.length() << endl;
    else
        cout << "same" << endl;

    return 0;
}