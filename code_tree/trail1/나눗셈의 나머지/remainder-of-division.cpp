#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int cnt[10] = {};

    while (a > 1) {
        cnt[a % b]++;
        a = a / b;
    }

    int sum = 0;

    for (int i = 0; i < 10; i++) {
        sum += cnt[i] * cnt[i];
    }
    cout << sum << endl;
    return 0;
}