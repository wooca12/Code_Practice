#include <iostream>
using namespace std;
#define MAX_N 101

int main() {
    int n;
    cin >> n;

    int arr[MAX_N] = {};

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;

        for (int j = a; j <= b; j++) {
            arr[j]++;
        }
    }

    int max_lines = 0;

    for (int i = 1; i < MAX_N; i++) {
        if (max_lines < arr[i])
            max_lines = arr[i];
    }

    cout << max_lines << endl;

    return 0;
}