#include <iostream>
#include <string>
using namespace std;

int main() {
    int len[3] = {};

    for (int i = 0; i < 3; i++) {
        string str;
        cin >> str;
        len[i] = str.length();
    }
    int max = 0, min = 20;

    for (int i = 0; i < 3; i++) {
        if (max < len[i])
            max = len[i];
        if (min > len[i])
            min = len[i];
    }
    cout << max - min << endl;
    return 0;
}