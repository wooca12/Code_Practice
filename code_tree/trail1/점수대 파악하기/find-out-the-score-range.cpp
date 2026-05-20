#include <iostream>
using namespace std;

int main() {
    int score[100];
    int score_cnt[11] = {};

    for (int i = 0; i < 100; i++) {
        cin >> score[i];

        if (score[i] == 0)
            break;

        score_cnt[score[i] / 10]++;

    }

    for (int i = 10; i > 0; i--) {
        cout << 10 * i << " - " << score_cnt[i] << endl;
    }

    return 0;
}