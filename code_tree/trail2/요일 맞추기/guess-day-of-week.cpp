#include <iostream>
#include <string>
using namespace std;

int NumOfDay (int m, int d) {
    int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int total_days = 0;
    for (int i = 1; i < m; i++) {
        total_days += days[i];
    }
    total_days += d;
    
    return total_days;
}

int main() {
    string day_week[7] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

    int m1, d1, m2, d2;
    cin >> m1 >> d1 >> m2 >> d2;

    int eclapsed_days = NumOfDay(m2, d2) - NumOfDay(m1, d1);
    
    while (eclapsed_days < 0) {
        eclapsed_days += 7;
    }

    cout << day_week[eclapsed_days % 7];


    return 0;
}