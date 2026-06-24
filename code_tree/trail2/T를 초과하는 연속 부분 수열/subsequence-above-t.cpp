#include <iostream>
#include <algorithm>
#define MAX_N 1000
using namespace std;

int n, t;
int arr[MAX_N];

int main() {
    cin >> n >> t;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int ans = 0, cnt = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] > t) { // t보다 커야함
            cnt++;
        }
        else // t보다 작음
            cnt = 0;
        ans = max(ans, cnt);
    }
    cout << ans;

    return 0;
}