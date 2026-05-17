#include <iostream>
using namespace std;

int main() {
    int n;
    bool satisfied = true;
    cin >> n;

     for (int i = 2; i < n; i++) {
        if (n % i == 0)
            satisfied = false;
    }
    cout << (satisfied ? "P" : "C") << endl;
    return 0;
}