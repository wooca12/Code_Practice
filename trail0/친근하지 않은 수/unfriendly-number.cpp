#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int i;
    int cnt = 0;
    for (i = 1; i <= n; i++) {
        if ((i % 2 != 0) && (i % 3 != 0) && (i % 5 != 0))
            cnt += 1;
    }
    cout << cnt << endl;
    return 0;
}