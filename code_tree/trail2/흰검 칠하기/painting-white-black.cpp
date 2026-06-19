#include <iostream>
using namespace std;

#define MAX_R 1000
#define MAX_N 200000
#define OFFSET 100000

int main() {
    int n;
    cin >> n;

    int cur = 0;  // 현재 위치

    // black, white 카운트
    int black_cnt[MAX_N] = {};
    int white_cnt[MAX_N] = {};

    // 덮어씌운 영역
    int block[MAX_N] = {};
    
    cur += OFFSET;

    for (int i = 0; i < n; i++) {
        int dist;
        char dir;
        cin >> dist >> dir;

        if (dir == 'L') { // left -> white
            for (int j = cur - dist + 1; j <= cur; j++) {
                block[j] = 1;
                white_cnt[j]++;
            }
            cur -= dist - 1;
        }
        else { // right -> black
            for (int j = cur; j < cur + dist; j++) {
                block[j] = 2;
                black_cnt[j]++;
            }
            cur += dist - 1;
        }
    }

    int w = 0, b = 0, g = 0;

    for (int i = 0; i < MAX_N; i++) {
        if (white_cnt[i] >= 2 && black_cnt[i] >= 2) {
            // cout << 'g';
            g++;
        }
        else if (block[i] == 1) {
            // cout << 'w';
            w++;
        }
        else if (block[i] == 2) {
            // cout << 'b';
            b++;
        }
    }
    
    cout << w << " " << b << " " << g << endl;
    return 0;
}