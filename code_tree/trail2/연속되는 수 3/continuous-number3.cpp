#include <iostream>
#include <algorithm>
using namespace std;

#define MAX_N 1000

int n;
int arr[MAX_N];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int ans = 0, cnt = 0;
    int plus = 1;

    for (int i = 0; i < n; i++) {
        if (plus * arr[i] > 0)
            cnt++;
        else {
            cnt = 1;
            plus *= -1;
        }
        ans = max(ans, cnt);
    }

    cout << ans;

    return 0;
}