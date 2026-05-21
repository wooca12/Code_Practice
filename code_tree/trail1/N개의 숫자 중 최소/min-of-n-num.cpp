#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, min = INT_MAX;
    cin >> n;

    int arr[100];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        if (min > arr[i])
            min = arr[i];
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (min == arr[i])
            cnt++;
    }
    cout << min <<  " " << cnt << endl;
    return 0;
}