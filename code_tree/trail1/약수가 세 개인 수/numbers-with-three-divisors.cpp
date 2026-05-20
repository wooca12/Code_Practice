#include <iostream>
using namespace std;

int main() {
    int start, end, cnt = 0;
    cin >> start >> end;

    for (int i = start; i <= end; i++) {
        int n_cnt = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0)
                n_cnt++;
        }
        if (n_cnt == 3)
            cnt++;
    }
    cout << cnt << endl;
    return 0;
}