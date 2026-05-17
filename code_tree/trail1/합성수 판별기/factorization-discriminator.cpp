#include <iostream>
using namespace std;

int main() {
    int n;
    bool satisfied = false;
    cin >> n;

    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            satisfied = true;
            break;
        }
    }
    cout << (satisfied ? 'C' : 'N') << endl;
    return 0;
}