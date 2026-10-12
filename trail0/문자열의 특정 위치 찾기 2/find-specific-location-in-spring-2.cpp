#include <iostream>
using namespace std;

int main() {
    string words[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char ch;
    int cnt = 0;

    cin >> ch;


    for (int i = 0; i < 5; i++) {
        if ((words[i][2] == ch) || (words[i][3] == ch)) {
            cout << words[i] << "\n";
            cnt++;
        }
    }
    cout << cnt << endl;

    return 0;
}