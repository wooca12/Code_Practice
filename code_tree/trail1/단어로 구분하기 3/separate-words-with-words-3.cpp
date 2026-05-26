#include <iostream>
#include <string>
using namespace std;

int main() {
    int n = 10;
    string arr[10];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 1; i <= n; i++) {
        cout << arr[n - i] << endl;
    }
    return 0;
}