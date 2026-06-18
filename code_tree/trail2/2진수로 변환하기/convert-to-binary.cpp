#include <iostream>
using namespace std;
#define MAX_N 1000000

int main() {
    int n, cnt = 0;
    int arr[MAX_N] = {};
    cin >> n;

    while (true) {
        if (n < 2) {
            arr[cnt++] = n;
            break;
        }
        arr[cnt++] = n % 2;
        n /= 2;
    }

    for (int i = cnt - 1; i >= 0; i--) {
        cout << arr[i];
    }

    return 0;
}