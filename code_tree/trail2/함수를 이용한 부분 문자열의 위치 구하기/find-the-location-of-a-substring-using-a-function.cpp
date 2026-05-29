#include <iostream>
#include <string>
using namespace std;

int SubSequence(string a, string b) {
    int idx = -1;

    int n1 = a.length();
    int n2 = b.length();

    for (int i = 0; i < n1; i++) {
        if (a.substr(i, n2) == b) {
            idx = i;
            break;
        }
    }

    return idx;
}

int main() {
    string a, b;
    cin >> a >> b;

    int ans = SubSequence(a, b);
    cout << ans << endl;
    return 0;
}