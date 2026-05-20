#include <iostream>
using namespace std;

int main() {
    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int n, cnt = 0;
        cin >> n;

        while (n != 1) {
            if (n % 2 == 0)
                n /= 2;
            else 
                n = n * 3 + 1;
            cnt++;
        }
        cout << cnt << endl;
    }

    return 0;
}