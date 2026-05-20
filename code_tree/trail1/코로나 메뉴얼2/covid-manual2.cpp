#include <iostream>
using namespace std;

int main() {
    int cnt[4] = {};

    for (int i = 0; i < 3; i++) {
        char exist;
        int temp;
        cin >> exist >> temp;

        if (exist == 'Y') {
            if (temp >= 37)
                cnt[0]++;
            else
                cnt[2]++;
        }
        else if (exist == 'N')
            if (temp >= 37)
                cnt[1]++;
            else
                cnt[3]++;
    }
    for (int i = 0; i < 4; i++) {
        cout << cnt[i] << " ";
    }
    if (cnt[0] >= 2)
        cout << "E" << endl;
    return 0;
}