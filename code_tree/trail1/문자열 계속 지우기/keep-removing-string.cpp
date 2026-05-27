#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    while (a.find(b) != string::npos) {
        int idx = a.find(b);
        a = a.erase(idx, b.length());
    }
    cout << a << endl;
    return 0;
}