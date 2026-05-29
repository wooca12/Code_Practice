#include <iostream>
using namespace std;

void Modify(int n, int a[]) {
    for (int i = 0; i < n; i++) {
        if (a[i] < 0)
            a[i] = -a[i];
    }    
}

int main() {
    int n;
    int arr[50];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Modify(n, arr);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}