#include <iostream>
#include <string>
using namespace std;

int NumOfDays(int m, int d) {
    int days[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int total_days = 0;

    for (int i = 1; i < m; i++) 
        total_days += days[i];
    total_days += d;

    return total_days;
}
int main() {
    int m1, d1, m2, d2;
    string a;
    cin >> m1 >> d1 >> m2 >> d2;
    cin >> a;

    string week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

    int diff = NumOfDays(m2, d2) - NumOfDays(m1, d1);

    int cnt = 0;

    while(diff >= 0) {
        if (week[diff % 7] == a)
            cnt++;
        diff--;
    }
    cout << cnt << endl;

    return 0;
}