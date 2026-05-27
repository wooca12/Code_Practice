#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    string sum = to_string(a + b);

    int cnt = 0;

    for (int i = 0; i < sum.length(); i++) {
        if (sum[i] == '1')
            cnt++;
    }
    cout << cnt << endl;

    return 0;
}