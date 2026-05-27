#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, q;
    cin >> a >> q;

    int len = a.length();

    for (int i = 0; i < q.length(); i++) {
        if (q[i] == 'L') {
            a = a.substr(1, len - 1) + a.substr(0, 1);
        }
        else {
            a = a.substr(len - 1, 1) + a.substr(0, len - 1);
        }
    }
    cout << a << endl;

    return 0;
}