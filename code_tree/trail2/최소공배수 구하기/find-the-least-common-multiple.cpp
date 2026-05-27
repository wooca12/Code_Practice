#include <iostream>

using namespace std;

void FindGcd(int n, int m) {
    int ans;
    for (int i = 1; i < 100; i++) {
        ans = m * i;
        if (ans % n == 0 && ans % m == 0)
            break;
    }
    cout << ans << endl;
}

int main() {
    int n, m;
    cin >> n >> m;

    FindGcd(n, m);

    return 0;
}