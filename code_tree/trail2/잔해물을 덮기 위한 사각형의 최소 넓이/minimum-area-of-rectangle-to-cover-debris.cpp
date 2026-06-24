#include <iostream>
using namespace std;

#define OFFSET 1000
#define MAX_N 2001

int arr[MAX_N][MAX_N] = {};

int main() {
    int x1, y1, x2, y2;


    cin >> x1 >> y1 >> x2 >> y2;

    x1 += OFFSET;
    y1 += OFFSET;
    x2 += OFFSET;
    y2 += OFFSET;

    for (int i = x1; i < x2; i++) {
        for (int j = y1; j < y2; j++) {
            arr[i][j] = 1;
        }
    }


    int a1, b1, a2, b2;
    cin >> a1 >> b1 >> a2 >> b2;

    a1 += OFFSET;
    b1 += OFFSET;
    a2 += OFFSET;
    b2 += OFFSET;

    for (int i = a1; i < a2; i++) {
        for (int j = b1; j < b2; j++) {
            arr[i][j] = 0;
        }
    }
    int min_x = MAX_N, min_y = MAX_N;
    int max_x = 0, max_y = 0;

    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) {
            if (arr[i][j] == 1) {
                if (min_x > i) min_x = i;
                if (min_y > j) min_y = j;
                if (max_x < i) max_x = i;
                if (max_y < j) max_y = j;
            }
        }
    }

    int size = (max_x - min_x + 1) * (max_y - min_y + 1);

    if (size >= 4000000)
        cout << 0 << endl;
    else 
        cout << size << endl;

    return 0;
}