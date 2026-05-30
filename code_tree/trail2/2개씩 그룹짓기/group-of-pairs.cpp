#include <iostream>
#include <string>
#include <algorithm>
#define MAX_N 1000
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[2 * MAX_N];

    for (int i = 0; i < 2 * n; i++) {
        cin >> arr[i];
    }
    std::sort(arr, arr + 2 * n);

    int minmax = 0;

    for (int i = 0; i < n; i++) {
            int sum = arr[i] + arr[2 * n - i - 1];
        minmax = max(minmax, sum);
    }
    cout << minmax << endl;

    return 0;
}