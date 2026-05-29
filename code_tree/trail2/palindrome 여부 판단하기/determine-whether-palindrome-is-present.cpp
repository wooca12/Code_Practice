#include <iostream>
#include <string>

using namespace std;


bool IsPalindrome(string &s) {
    int len = s.length();
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1])
            return false;
    }
    return true;

}

int main() {
    string A;
    cin >> A;

    if (IsPalindrome(A)) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }

    return 0;
}