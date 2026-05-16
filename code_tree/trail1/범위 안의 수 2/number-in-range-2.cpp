#include <iostream>
using namespace std;

int main() {
    int sum = 0, cnt = 0;
    double avg;

    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;
        if ((num >= 0) && (num <= 200)) {
            sum += num;
            cnt++;
        }
    }
    avg = (double)sum / cnt;
    cout << fixed;
    cout.precision(1);
    cout << sum << " " << avg << endl;
    return 0;
}