#include <iostream>
using namespace std;

#define OFFSET 100
#define MAX_K 201

int n;
int arr[MAX_K][MAX_K] = {};
int cnt = 0;

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
                arr[j][k] = 1;
            }
        }
    }

    for (int i = 0; i < MAX_K; i++) {
        for (int j = 0; j < MAX_K; j++) {
            if (arr[i][j] == 1)
                cnt++;
        }
    }

    cout << cnt << endl;
    
    return 0;
}