#include <iostream>
using namespace std;

int main() {
    int n, m, arr[100][100] = {};
    int cnt = 1;

    cin >> n >> m;


    for (int i = 0; i < n * m; i++) {
        // 숫자 다 채우면 멈춤
        if (cnt > n * m)
            break;
            
        for (int j = 0; j <= i; j++) {
            // 인덱스가 n, m 밖일 때: 채우지 않고 건너 뜀
            if (j >= n || (i - j) >= m) 
                continue;
            // 인덱스 n, m 안일 때: 숫자 채움
            arr[j][i - j] = cnt;
            cnt++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}