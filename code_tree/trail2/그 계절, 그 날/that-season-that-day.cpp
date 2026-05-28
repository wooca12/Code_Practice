#include <iostream>
using namespace std;

int LastDayFeb(int y, int m) {
    if (y % 4 != 0)
        return 28;

    if (y % 100 != 0)
        return 29;

    if (y % 400 == 0)
        return 29;

    return 28;
}

int LastDayNumber(int y, int m) {
    if (m == 2)
        return LastDayFeb(y, m);

    if (m == 4 || m == 6 || m == 9 || m == 11)
        return 30;

    return 31;
}

bool JudgeDay(int y, int m, int d) {
    if (m <= 12 && d <= LastDayNumber(y, m))
        return true;
    return false;
}


int main() {
    int y, m, d;
    cin >> y >> m >> d;


    if (JudgeDay(y, m, d)) {
        if (3 <= m && m <= 5)
            cout << "Spring" << endl;
        else if (6 <= m && m <= 8)
            cout << "Summer" << endl;
        else if (9 <= m && m <= 11)
            cout << "Fall" << endl;
        else 
            cout << "Winter" << endl;
    }
    else
        cout << -1 << endl;

    return 0;
}