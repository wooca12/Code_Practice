#include <iostream>
using namespace std;

#define MAX_K 100000

int n;

int checked[2 * MAX_K +1] = {};

int main() {
    cin >> n;

    int cur = MAX_K;

    for (int i = 0; i < n; i++) {
        int x;
        char d;
        cin >> x >> d;

        if (d == 'L') {
            // for (int j = cur - x + 1; j < cur + 1; j++) 
            //     checked[j] = 1;
            // cur -= x - 1;

            while (x--) {
                checked[cur] = 1;
                if (x) cur++;
            }
        }
        else {
            // for (int j = cur; j < cur + x; j++) 
            //     checked[j] = 2;
            // cur += x - 1;

            while(x--) {
                checked[cur] = 2;
                if(x) cur--;
            }
        }
    }

    int w = 0, b = 0;

    for (int i = 0; i < 2 * MAX_K + 1; i++) {
        if (checked[i] == 1)
            w++;
        else if (checked[i] == 2)
            b++;
    }

    cout << w << " " << b << endl;

    return 0;
}