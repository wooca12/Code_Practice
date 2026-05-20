#include <iostream>
using namespace std;

int main() {
    int arr[10] = {};
    int sum_val = 0, cnt = 0;

    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
        if (arr[i] >= 250)
            break;
        sum_val += arr[i];
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << sum_val << " " << (double)sum_val / cnt << endl;
    return 0;
}