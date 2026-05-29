#include <iostream>
using namespace std;
#define MAX_N 50

void AbsoluteValue(int n, int a[]) {
    for (int i = 0; i < n; i++) {
        if (a[i] < 0)
            a[i] = -a[i];
    }    
    return;
}

int main() {
    int n;
    int arr[MAX_N];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    AbsoluteValue(n, arr);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}