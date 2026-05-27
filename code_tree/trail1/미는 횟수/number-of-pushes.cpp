#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    int answer = 0;
    int len = a.length();

    while (a != b) {
        a = a.substr(len - 1, 1) + a.substr(0, len - 1);
        answer++;
        if (answer == len) {
            answer = -1;
            break;
        }
    }
    cout << answer << endl;

    return 0;
}