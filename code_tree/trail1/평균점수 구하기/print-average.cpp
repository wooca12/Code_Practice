#include <iostream>
using namespace std;

int main() {
    double score[8];
    double sum = 0;
    int cnt = 0;

    for (int i = 0; i < 8; i++) {
        cin >> score[i];
        sum += score[i];
        cnt++;
    }
    double avg = sum / cnt;

    cout << fixed;
    cout.precision(1);
    cout << avg << endl;
    return 0;
}