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

int NumOfDay(string s) {
    if (s == "Mon") return 0;
    else if (s == "Tue") return 1;
    else if (s == "Wed") return 2;
    else if (s == "Thu") return 3;
    else if (s == "Fri") return 4;
    else if (s == "Sat") return 5;
    return 6;
}

int main() {
    int m1, d1, m2, d2;
    string a;
    cin >> m1 >> d1 >> m2 >> d2;
    cin >> a;


    // ############ < MY SOLUTION > ################
    // string week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

    // int diff = NumOfDays(m2, d2) - NumOfDays(m1, d1);

    // int cnt = 0;

    // while(diff >= 0) {
    //     if (week[diff % 7] == a)
    //         cnt++;
    //     diff--;
    // }
    // cout << cnt << endl;

    int start_day = NumOfDays(m1, d1);
    int end_day = NumOfDays(m2, d2);
    int cur_day = NumOfDay("Mon");

    int cnt = 0;

    for (int i = start_day; i <= end_day; i++) {
        if(cur_day == NumOfDay(a))
            cnt++;
        cur_day++;
        cur_day %= 7;
    }

    cout << cnt << endl;

    return 0;
}