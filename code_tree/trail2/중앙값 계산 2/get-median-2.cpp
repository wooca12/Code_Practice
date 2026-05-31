#include <iostream>
#include <algorithm>
#define MAX_N 100

using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[MAX_N + 1] = {};


    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        if (i % 2 == 0) {
            sort(arr, arr + i + 1);
            cout << arr[i / 2] << " ";
        }
    }

    return 0;
}