#include <iostream>

using namespace std;

void FindLcm(int n, int m) {
    int gcd;
    for (int i = 1; i <= min(m, n); i++) {
        if (n % i == 0 && m % i == 0)
            gcd = i;
    }
    cout << (n * m) / gcd << endl;
}

int main() {
    int n, m;
    cin >> n >> m;

    FindLcm(n, m);

    return 0;
}