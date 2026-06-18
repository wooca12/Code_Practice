#include <iostream>
using namespace std;
#define OFFSET 100

int main() {
    int MAX_N = OFFSET * 2 + 1;

    int n; 
    cin >> n;

    int arr[MAX_N] = {};
    int x1, x2;

    for (int i = 0; i < n; i++) {
        cin >> x1 >> x2;
        x1 += OFFSET;
        x2 += OFFSET;

        for (int j = x1; j < x2; j++) {
            arr[j]++;
        }
    }

    int max_lines = 0;

    for (int i = 0; i < MAX_N; i++) {
        if (max_lines < arr[i])
            max_lines = arr[i];
    }
    cout << max_lines << endl;

    return 0;
}