#include <iostream>
using namespace std;

#define OFFSET 100
#define MAX_N 201

int n;
int arr[MAX_N][MAX_N] = {};

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        x1 += OFFSET;
        x2 += OFFSET;
        y1 += OFFSET;
        y2 += OFFSET;

        
        for (int j = x1; j < x2; j++) {
            for (int k = y1; k < y2; k++) {
                if (i % 2 == 0) arr[j][k] = 1; // red
                else arr[j][k] = 2; // blue
            }
        }
    }
    int cnt_b = 0;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) {
            if (arr[i][j] == 2) cnt_b++;
        }
    }

    cout << cnt_b << endl;
    return 0;
}