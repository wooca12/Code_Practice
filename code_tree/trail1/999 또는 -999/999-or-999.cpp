#include <iostream>
#include <climits>
using namespace std;

int main() {
    int arr[100];
    int max_val = INT_MIN, min_val = INT_MAX;

    for (int i = 0; i < 100; i++) {
        cin >> arr[i];

        if (arr[i] == 999 || arr[i] == -999)
            break;

        if (max_val < arr[i])
            max_val = arr[i];
        if (min_val > arr[i])
            min_val = arr[i];
    }
    cout << max_val << " " << min_val << endl;
    return 0;
}