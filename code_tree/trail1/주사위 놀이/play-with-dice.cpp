#include <iostream>
using namespace std;

int main() {
    int count[7] = {};

    for (int i = 0; i < 10; i++) {
        int n;
        cin >> n;

        count[n]++;
    }
    for (int i = 1; i < 7; i++) {
        cout << i << " - " << count[i] << endl;
    }
    return 0;
}