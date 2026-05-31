#include <iostream>
using namespace std;

int LastDay(int m) {
    if (m == 2)
        return 28;
    if (m == 4 || m == 6 || m == 9 || m == 11)
        return 30;
    return 31;
}

int NumOfDays(int m, int d) {
    int total_days = 0;
    for (int i = 1; i < m; i++) {
        total_days += LastDay(i);
    }
    total_days += d;

    return total_days;
}

int main() {
    int m1, d1, m2, d2;
    cin >> m1 >> d1;
    cin >> m2 >> d2;

   
    cout << NumOfDays(m2, d2) - NumOfDays(m1, d1) + 1 << endl;

    return 0;
}