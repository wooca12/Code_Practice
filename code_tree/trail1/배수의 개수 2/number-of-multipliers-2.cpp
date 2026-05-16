#include <iostream>
using namespace std;

int main() {
    int cnt = 0;
    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;

        if (num % 2 == 1)
            cnt++;
    }
    cout << cnt << endl;
    return 0;
}