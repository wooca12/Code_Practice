#include <iostream>
using namespace std;

int main() {
    int n;
    bool satisfied = true;
    for (int i = 0; i < 5; i++) {
        cin >> n;
        if (n % 3 != 0)
            satisfied = false;
    }
    cout << (satisfied ? 1 : 0) << endl;
    return 0;
}