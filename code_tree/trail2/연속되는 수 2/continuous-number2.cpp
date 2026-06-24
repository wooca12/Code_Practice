#include <iostream>
using namespace std;
#define MAX_N 1001

int main() {
    int n;
    cin >> n;
    int arr[MAX_N] = {};

    int cnt = 0;
    int max_cnt = 0;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        if (i == 0 || arr[i] != arr[i - 1]) {
            if (max_cnt < cnt)
                max_cnt = cnt;
            cnt = 0;
        }
        cnt++;
    }
    if (max_cnt < cnt)
        max_cnt = cnt;

    cout << max_cnt << endl;

    return 0;
}