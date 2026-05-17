#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    bool flag = false;
    cin >> a >> b >> c;
    for (int i = a; i <= b; i++) {
        if (i % c == 0) {
            flag = true;
            break;
        }
    }
    if (flag)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}