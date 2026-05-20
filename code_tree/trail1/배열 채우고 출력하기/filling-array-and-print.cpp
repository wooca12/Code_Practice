#include <iostream>
using namespace std;

int main() {
    char arr[10];

    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < 10; i++) {
        cout << arr[10 - i - 1];
    }
    return 0;
}