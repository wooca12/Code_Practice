#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 4 == 0) {
            if ((i % 100 != 0) || (i % 400 == 0))
                cnt++;
        } 
    }
    cout << cnt << endl;
    return 0;
}