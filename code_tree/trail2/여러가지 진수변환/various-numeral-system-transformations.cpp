#include <iostream>
using namespace std;
#define MAX_N 100000

int main() {
    int n, b;
    cin >> n >> b;
    
    int arr[MAX_N];
    int cnt = 0;

    while (true) {
        if (n < b) {
            arr[cnt++] = n;
            break;
        }
        arr[cnt++] = n % b;
        n /= b;
    }

    for (int i = cnt - 1; i >= 0; i--) {
        cout << arr[i];
    }
    return 0;
}