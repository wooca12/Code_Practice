#include <iostream>
using namespace std;

int days(int m) {
    if (m == 2)
        return 28;
    if (m == 4 || m == 6 || m == 9 || m == 11)
        return 30;
    return 31;
}
int main() {
    int m1, d1, m2, d2;
    cin >> m1 >> d1;
    cin >> m2 >> d2;

    int days1 = d1;
    for (int i = 1; i < m1; i++) {
        days1 += days(i);
    }

    int days2 = d2;
    for (int i = 1; i < m2; i++) {
        days2 += days(i);
    }

    cout << days2 - days1 + 1 << endl;

    return 0;
}