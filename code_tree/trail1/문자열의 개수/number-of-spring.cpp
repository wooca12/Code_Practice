#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    string arr[200] = {};

    int cnt = 0;
    int idx = 0;
    while (true) {
        cin >> str;

        if (str == "0")
            break;
        arr[idx] = str;
        cnt++;
        idx++;
    }
    
    cout << cnt << endl;

    for (int i = 0; i < cnt; i++) {
        if (i % 2 == 0)
            cout << arr[i] << endl;
    }
    return 0;
}