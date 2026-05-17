#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    // n.  2 * n + 1   " "  "*"
    // 2.      5.        0.   5
    // 1.       3        2.   3
    // 0.        1       4.   1

    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < 2 * (n - 1 - i); j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}