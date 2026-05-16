#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    double avg;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        sum += num;
    }
    avg = (double)sum / n;

    cout << fixed;
    cout.precision(1);

    cout << sum << " " << avg << endl;
    return 0;
}