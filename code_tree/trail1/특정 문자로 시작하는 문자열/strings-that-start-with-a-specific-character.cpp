#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    string arr[20];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    char c;
    cin >> c;

    int cnt = 0;
    int total_len = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i][0] == c) {
            total_len += arr[i].length();
            cnt++;
        }
    }

    cout << fixed;
    cout.precision(2);

    cout << cnt << " " << (double)total_len / cnt << endl;

    return 0;
}