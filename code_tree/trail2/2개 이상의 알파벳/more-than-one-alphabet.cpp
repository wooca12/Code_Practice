#include <iostream>
#include <string>

using namespace std;

bool Exist2Alphabet(string a) {
    string alphabets = "";
    int cnt = 0;

    for (int i = 0; i < a.length(); i++) {
        if (alphabets.find(a[i]) == string::npos) {
            cnt++;
            alphabets += a[i];
        }
    }
    return (cnt >= 2);
}

int main() {
    string A;
    cin >> A;

    if (Exist2Alphabet(A)) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }
    return 0;
}