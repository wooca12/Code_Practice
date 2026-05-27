#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int idx = s.find('e');

    s = s.erase(idx, 1);

    cout << s << endl;

    return 0;
}