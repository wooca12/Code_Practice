#include <iostream>
using namespace std;
int n, m;
int answer[100][100] = {0};
int count = 1;

int main() {
    cin >> n >> m;

    
    for (int start_col = 0; start_col < m; start_col++) {
        int cur_col = start_col;
        int cur_row = 0;

        while (cur_col >= 0 && cur_row < n) {
            answer[cur_row][cur_col] = count;
            cur_col--;
            cur_row++;
            count++;
        }
    }
    for (int start_row = 1; start_row < n; start_row++) {
        int cur_row = start_row;
        int cur_col = m - 1;

        while (cur_col >= 0 && cur_row < n) {
            answer[cur_row][cur_col] = count;
            cur_row++;
            cur_col--;
            count++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << answer[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}