#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    int n;
    cin >> n;

    string s = to_string(n);

    int sum = 0;

    for (int i = 0; i < s.length(); i++) {
        sum += int(s[i]) - int('0');
    }
    cout << sum;

    return 0;
}