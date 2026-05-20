#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    double score[5];

    double sum = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        cin >> score[i];
        sum += score[i];
        cnt++;
        
    }
    double avg = sum / cnt;

    cout << fixed;
    cout.precision(1);
    cout << avg << endl;

    if (avg >= 4.0)
        cout << "Perfect" << endl;
    else if (avg >= 3.0)
        cout << "Good" << endl;
    else
        cout << "Poor" << endl;
    return 0;
}