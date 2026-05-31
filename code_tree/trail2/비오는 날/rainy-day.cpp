#include <iostream>
#include <string>
#define MAX_N 100
using namespace std;

class DayInfo {
    public:
        string date;
        string week, weather;

        DayInfo(string date, string week, string weather) {
            this->date = date;
            this->week = week;
            this->weather = weather;
        }
        DayInfo() {}
};

int main() {
    int n;
    cin >> n;

    DayInfo days[MAX_N];

    for (int i = 0; i < n; i++) {
        string date, week, weather;
        cin >> date >> week >> weather;

        days[i] = DayInfo(date, week, weather);
    }

    int idx = 0;
    for (int i = 1; i < n; i++) {
        if (days[i].weather == "Rain") {
            if (days[idx].weather != "Rain") {
                idx = i;
            }
            else {
                if (days[idx].date > days[i].date) {
                    idx = i;
                }
            }
        }
    }
    cout << days[idx].date << " " << days[idx].week << " " << days[idx].weather << endl;

    return 0;
}