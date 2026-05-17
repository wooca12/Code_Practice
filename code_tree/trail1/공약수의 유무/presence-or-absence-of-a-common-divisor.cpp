#include <iostream>
using namespace std;

int main() {
    int a, b;
    bool satisfied = false;
    cin >> a >> b;
    for (int i = a; i <= b; i++) {
        if ((1920 % i == 0) && (2880 % i == 0)) {
            satisfied = true;
            break;
        }

    }
    cout << (satisfied ? 1 : 0) << endl;
    return 0;
}