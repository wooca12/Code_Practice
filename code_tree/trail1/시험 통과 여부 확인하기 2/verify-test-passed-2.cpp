#include <iostream>
using namespace std;

int main() {
    int n, cnt = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int score[4];
        int sum = 0;

        for (int j = 0; j < 4; j++) {
            cin >> score[i];
            sum += score[i];
        }
        double avg = (double)sum / 4;
        
        if (avg >= 60) {
            cout << "pass" << endl;
            cnt++;
        }
        else
            cout << "fail" << endl;
    }
    cout << cnt << endl;
    return 0;
}