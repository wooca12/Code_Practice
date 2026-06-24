#include <iostream>
#include <algorithm>
using namespace std;

#define MAX_N 1001

int main() {
    // int n;
    // cin >> n;
    // int arr[MAX_N] = {};

    // int cnt = 0;
    // int max_cnt = 0;

    // for (int i = 0; i < n; i++) {
    //     cin >> arr[i];

    //     if (i == 0 || arr[i] != arr[i - 1]) { // 값이 이전과 다를 때 다시 카운트 + 최대값 저장
    //         if (max_cnt < cnt)
    //             max_cnt = cnt;
    //         cnt = 0;
    //     }
    //     cnt++;
    // }

    // if (max_cnt < cnt) // 모두 동일한 숫자일 때 --> 다시 최대값 저장
    //     max_cnt = cnt;

    // cout << max_cnt << endl;

    int n;
    int arr[MAX_N] = {};

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int ans = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        if (i >= 1 && arr[i] == arr[i - 1])
            cnt++;
        else
            cnt = 1;

        ans = max(ans, cnt);
    }

    cout << ans << endl;

    return 0;
}