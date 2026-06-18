#include <iostream>

using namespace std;

int m1, m2, d1, d2;
string A;

int DayNums(int m1, int d1, int m2, int d2) {
    int days[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int total_days = 0;
    for (int i = m1; i < m2; i++) 
        total_days += days[i];
    return total_days - d1 + d2;
}

int Day(string a) {
    if (a == "Mon") return 0;
    else if (a == "Tue") return 1;
    else if (a == "Wed") return 2;
    else if (a == "Thu") return 3;
    else if (a == "Fri") return 4;
    else if (a == "Sat") return 5;
    else if (a == "Sun") return 6;
}

int main() {
    cin >> m1 >> d1 >> m2 >> d2;
    cin >> A;

    int diff = DayNums(m1, d1, m2, d2);

    int num = Day(A);
    int cnt = 0;


    for (int i = 0; i <= diff; i++) {
        if ((i % 7) == num)
            cnt++;
    }

    cout << cnt << endl;


    return 0;
}