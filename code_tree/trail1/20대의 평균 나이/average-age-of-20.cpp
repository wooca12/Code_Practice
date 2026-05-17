#include <iostream>
using namespace std;

int main() {
    int age, sum = 0, cnt = 0;
    while (1) {
        cin >> age;
        if (age < 20 || age > 29)
            break;
        sum += age;
        cnt++;
    }
    cout << fixed;
    cout.precision(2);
    cout << (double)sum / cnt << endl;
    return 0;
}