#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    int cnt = 0;

    for (int i = 0; i < a.length() - 1; i++) {
        if (a.substr(i, 2) == b)
            cnt++;
    }
    cout << cnt << endl;

    return 0;
}