#include <iostream>

#define MAX_N 201
#define OFFSET 100
using namespace std;

int N;
int x[100], y[100];
int arr[MAX_N][MAX_N] = {0, };

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x[i] >> y[i];
    }

    for (int i = 0; i < N; i++) {
        int a = x[i] + OFFSET;
        int b = y[i] + OFFSET;

        for (int j = a; j < a + 8; j++) {
            for (int k = b; k < b + 8; k++) {
                arr[j][k] = 1;
            }
        }
    }
    
    int cnt = 0;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) {
            if (arr[i][j] == 1)
                cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}