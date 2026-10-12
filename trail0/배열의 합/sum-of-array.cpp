#include <iostream>
using namespace std;

int main() {
    int n;

    for (int i = 0; i < 4; i++) {
        int total = 0;
        for (int j = 0; j <4; j++) {
            cin >> n;
            total += n;
        }
        cout << total << "\n";
    }
    return 0;
}