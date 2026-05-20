#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int sum_val1 = 0;
    int sum_val2 = 0, cnt = 0;

    for (int i = 0; i < 10; i++) {
        cin >> arr[i];
        
        if ((i + 1) % 2 == 0)
            sum_val1 += arr[i];
        if ((i + 1) % 3 == 0) {
            sum_val2 += arr[i];
            cnt++;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << sum_val1 << " " << (double)sum_val2 / cnt << endl;
    return 0;
}