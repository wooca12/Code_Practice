#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            for (int j = 0; j < n; j++) {
                cnt++;
                cout << cnt << " ";
            }
            cnt += n;
        }
        else {
            for (int j = 0; j < n; j++) {
                cout << cnt << " ";
                cnt--;
            }
            cnt += n;
        }
        cout << endl;
    }
    return 0;
}