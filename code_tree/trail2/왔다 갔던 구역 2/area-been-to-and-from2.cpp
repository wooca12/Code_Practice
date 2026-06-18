#include <iostream>
using namespace std;

#define OFFSET 1000
#define MAX_N 2000
#define MAX_R 100

int main() {
    int n;
    cin >> n;


    // 범위 기록
    int cur;
    int a[MAX_N], b[MAX_N];

    for (int i = 0; i < n; i++) {
        int x;
        char d;
        cin >> x >> d;

        if (d == 'R') {
            a[i] = cur;
            b[i] = cur + x;
            cur += x;
        }
        else {
            a[i] = cur - x;
            b[i] = cur;
            cur -= x;
        }
    }

    // 구간마다 지나가는 영역 체크
    int checked[MAX_N] = {};

    for (int i = 0; i < n; i++) {
        int start = a[i] + OFFSET;
        int end = b[i] + OFFSET;
        
        for (int j = start; j < end; j++) {
            checked[j]++;
        }
    }
    // 라인 2개 이상 지나가는 영역 카운트
    int cnt = 0;

    for (int i = 0; i < MAX_N; i++) {
        if (checked[i] >= 2)
            cnt++;
    }

    cout << cnt << endl;
    return 0;
}