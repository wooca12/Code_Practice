#include <iostream>
using namespace std;
#define MAX_N 1001

int main() {
    int n, k;
    cin >> n >> k;

    int arr[MAX_N] = {};

    int a, b;

    for (int i = 0; i < k; i++) {
        cin >> a >> b;

        for (int j = a; j <= b; j++) {
            arr[j]++;
        }
    }

    int max = 0;

    for (int i = 0; i < MAX_N; i++) {
        if (max < arr[i])
            max = arr[i];
    }

    cout << max << endl;


    return 0;
}