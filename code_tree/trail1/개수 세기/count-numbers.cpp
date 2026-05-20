#include <iostream>
using namespace std;

int main() {
    int n, m, cnt = 0;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        int num; 
        cin >> num;

        if (m == num)
            cnt++;
    }
    cout << cnt << endl;
    return 0;
}