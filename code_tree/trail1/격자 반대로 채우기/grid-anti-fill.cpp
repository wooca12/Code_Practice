#include <iostream>
using namespace std;

int main() {
    int n, num = 1;
    cin >> n;

    int arr[10][10] = {};

    for (int j = n - 1; j >= 0; j--) {
        for (int i = n - 1; i >= 0; i--) {
            if (((num - 1) / n) % 2 == 0)
                arr[i][j] = num;
            else 
                arr[n - i - 1][j] = num;
            num++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}