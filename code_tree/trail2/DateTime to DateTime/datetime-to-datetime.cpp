#include <iostream>
using namespace std;

int GetMinutes(int day, int hour, int minute) {
    return day * 24 * 60 + hour * 60 + minute;
}

int main() {
    int d = 11, h = 11, m = 11;
    int a, b, c;
    cin >> a >> b >> c;

    int total_minutes = GetMinutes(a, b, c) - GetMinutes(d, h, m);

    if (total_minutes < 0) {
        cout << -1 << endl;
    }
    else {
        cout << total_minutes << endl;
    }

    return 0;
}